---
target_plugin: forgeify
improvement_type: feature
priority: high
problem: "forgeify의 플러그인 작업 스킬(improve-plugin, validate, create, compose, update) 실행 후 해당 플러그인의 help/howto 문서가 자동으로 최신화되지 않아 문서와 실제 기능이 불일치"
solution: "Stop 이벤트에 prompt 타입 hook을 설정하여 세션 종료 시 help/howto 갱신 필요 여부를 자동 체크"
requirements:
  - forgeify에 .claude-plugin/hooks.json 파일 생성
  - Stop 이벤트에 prompt hook 설정
  - 플러그인 작업 수행 시 help/howto 갱신 체크
  - gemify의 기존 hooks.json 패턴 참고
references:
  - /home/choigawoon/k-codepoet/my-claude-plugins/plugins/gemify/.claude-plugin/hooks.json
domain: engineering
views: []
---

## Why

forgeify는 Claude Code 플러그인을 생성, 수정, 검증하는 도구입니다. 플러그인 작업 후 해당 플러그인의 `help`와 `howto` 문서가 최신 상태를 반영해야 하지만, 현재는 이 동기화가 수동으로 이루어져 누락되기 쉽습니다.

forgeify가 다른 모든 플러그인(gemify, namify 등)을 관리하므로, forgeify에서 이 문제를 해결하면 전체 플러그인 생태계의 문서 품질이 향상됩니다.

## What

### 1. hooks.json 파일 생성

`/home/choigawoon/k-codepoet/my-claude-plugins/plugins/forgeify/.claude-plugin/hooks.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "이 세션에서 forgeify 플러그인 작업(improve-plugin, validate, create, compose, update)을 진행했다면, help/howto 문서 최신화가 필요한지 확인하세요.\n\n**체크 항목:**\n1. 플러그인의 스킬/커맨드가 추가/수정/삭제되었는가?\n2. 변경 사항이 skills/help/SKILL.md에 반영되었는가?\n3. 변경 사항이 skills/howto/SKILL.md에 반영되었는가?\n\n**필요 시:**\n- help 스킬: 명령어 목록, 설명, 사용법 갱신\n- howto 스킬: 사용 가이드, 예시 갱신\n\n**주의:** forgeify 작업이 아니었다면 무시하세요."
          }
        ]
      }
    ]
  }
}
```

### 2. prompt 내용 상세

Stop hook이 발동되면 Claude가 다음을 체크:
- 세션에서 forgeify 관련 작업(improve-plugin, validate, create, compose, update)이 있었는지
- 있었다면 대상 플러그인의 스킬/커맨드 변경 여부 확인
- 변경이 있으면 help/howto 갱신 필요 여부 판단 및 실행

## Scope

포함:
- forgeify에 hooks.json 파일 추가
- Stop 이벤트에 prompt hook 설정
- help/howto 갱신 체크 로직

제외:
- 다른 플러그인의 hooks.json (forgeify가 플러그인 작업 시 대상 플러그인의 help/howto를 직접 갱신)
- forgeify 외 스킬 수정

## 참고

gemify의 hooks.json 패턴:
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "이 세션에서 gemify:draft 작업을 진행했다면..."
          }
        ]
      }
    ]
  }
}
```
