---
title: gemify:draft 히스토리 자동 저장 훅
type: spec
origin: derived
target_plugin: gemify
improvement_type: feature
priority: high
problem: "draft 대화 종료 시 히스토리가 남지 않고, polish 용어와 gemify:library 명령어가 혼동됨"
solution: "hooks.json에 Stop 이벤트 추가하여 대화 종료 시 히스토리 저장 기준 체크"
requirements:
  - hooks.json 파일 추가 (Stop 이벤트 핸들러)
  - 히스토리 저장 기준 명확화 (turns >= 3, 내용 변경 있음)
  - draft 스킬에 polish → gemify:library 전환 안내 명시
  - 대화 종료 시 자동 히스토리 저장 제안 (HITL 유지)
references:
  - inbox/thoughts/2026-01-04-gemify-draft-history-fix.md
views: []
---

## Why

현재 gemify:draft는 pivot(방향 전환) 시에만 히스토리를 남기도록 설계되어 있다. 그러나 실제 사용에서는:

1. **대부분의 대화가 pivot 없이 진행됨** - 한 방향으로 계속 다듬다가 끝나는 경우가 많음
2. **히스토리가 안 남으면 과정이 소실됨** - 어떤 논의를 거쳐 결론에 도달했는지 추적 불가
3. **polish 용어 혼동** - 스킬에서 "polish" 모드라고 하지만, 실제 library 전환은 `/gemify:library` 명령어로 해야 함

## What

### 1. hooks.json 추가 (prompt 타입)

`.claude-plugin/hooks.json` 파일을 추가. **prompt 타입**을 사용하여 Claude가 컨텍스트를 보고 직접 판단:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "이 세션에서 gemify:draft 작업을 진행했다면, 히스토리 저장이 필요한지 확인하세요.\n\n**히스토리 저장 기준:**\n- turns >= 3 (의미있는 대화량)\n- Current State에 실질적 변경이 있음\n- 마지막 스냅샷 이후 새로운 결정사항이 있음\n\n**기준 충족 시:**\n1. drafts/.history/{slug}/ 폴더에 스냅샷 저장\n2. drafts/{slug}.md의 history 배열에 기록 추가\n3. revision 증가\n\n**기준 미충족 시:** 아무 작업도 하지 않음\n\n**주의:** 이 체크는 gemify:draft 작업이 있었을 때만 적용됩니다. 다른 작업 중이었다면 무시하세요."
          }
        ]
      }
    ]
  }
}
```

> **왜 prompt 타입인가?** 셸 스크립트로는 "현재 세션에서 draft를 수정했는지", "turns가 몇인지" 같은 대화 컨텍스트를 판단할 수 없음. prompt 타입은 Stop 이벤트에서 지원되며, Claude가 전체 컨텍스트를 보고 지능적으로 판단 가능.

### 2. draft 스킬 수정

`skills/draft/SKILL.md`에 다음 내용 추가:
- polish 모드 설명에 "library 전환은 `/gemify:library` 명령어로" 명시
- 세션 종료 시 히스토리 저장 안내 추가

### 3. 히스토리 저장 기준

| 조건 | 설명 |
|------|------|
| turns >= 3 | 의미있는 대화량 |
| Current State 변경 | 마지막 스냅샷 대비 내용 변화 |
| 명시적 요청 | 사용자가 직접 저장 요청 |

위 조건 중 하나라도 충족하면 히스토리 저장 제안.

## Scope

**포함:**
- hooks.json 파일 생성 (prompt 타입 Stop 훅)
- skills/draft/SKILL.md 수정 (polish → library 안내 명시)
- plugin.json 버전 업데이트

**제외:**
- 기존 draft 파일 마이그레이션
- 다른 스킬/명령어 수정
- UI/UX 변경
