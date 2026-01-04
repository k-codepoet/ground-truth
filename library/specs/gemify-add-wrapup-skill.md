---
title: gemify:wrapup 스킬 추가
type: spec
origin: derived
target_plugin: gemify
improvement_type: feature
priority: high
problem: "세션 종료 시 매번 수동으로 '놓친 거 있니?' 질문 필요. 일관성 없고 기록도 안 남음."
solution: "/gemify:wrapup 스킬 추가 - HITL 체크 후 세션 리포트 생성"
requirements:
  - wrapup 스킬 커맨드 추가
  - sessions/ 디렉토리에 리포트 저장
  - 리포트 템플릿 적용 (Summary, Outputs, Stashed for Next, Next Actions)
  - 세션 범위 확인 로직 (기본값: 대화 전체)
references:
  - library/specs/gemify-wrapup-skill.md
views: []
---

## Why

세션 종료는 반복되는 패턴. 부트스트래핑 원칙의 "신뢰 기반 위임" 적용 - 반복 패턴을 스킬로 위임하여 일관된 품질 보장.

현재 문제:
- 수동 질문 → Claude 답변 → 기록 없이 끝남
- 일관성 없음, 누락 가능성

## What

### 1. 스킬 커맨드 추가

`/gemify:wrapup` - 세션 마무리 스킬

### 2. 동작 흐름

```
1. 놓친 것 체크 (interactive, HITL)
   ├─ 다룬 파일, 상태, 열린 질문 확인
   ├─ 누락 있으면 사용자가 추가 지시
   └─ "이 정도면 됐다" 승인
        ↓
2. 리포트 생성 (sessions/에 저장)
   ├─ Summary (이번 세션에서 한 일)
   ├─ Outputs (생성/수정된 파일)
   ├─ Stashed for Next (inbox에 챙겨둔 것)
   └─ Next Actions (파생 TODO, 우선순위)
```

### 3. 저장 위치

```
sessions/
└── YYYY-MM-DD-NNN.md
```

gemify 파이프라인 바깥의 **운영 계층**.

### 4. 리포트 템플릿

```markdown
---
title: Session Wrapup
date: YYYY-MM-DD
session: NNN
---

## Summary
(이번 세션에서 한 일 요약)

## Outputs
(생성/수정된 파일 목록)

## Stashed for Next
(inbox에 의도적으로 저장해둔 것들)

## Next Actions
(파생된 TODO, 우선순위 제안)
```

### 5. 세션 범위

- **기본값**: 대화 전체 (Claude Code 세션)
- **사용자 지정**: 리포팅 요청 시 "어디서부터 어디까지?" 확인

### 6. 핵심 구분

inbox 항목 = "미완료"가 아니라 **"의도적으로 챙겨둔 것"**
- Stashed for Next 섹션에서 이 의도를 명확히 표현

## Scope

포함:
- wrapup 스킬 커맨드 (skills/wrapup/SKILL.md)
- sessions/ 디렉토리 구조
- 리포트 템플릿
- CLAUDE.md 업데이트

제외:
- 기존 스킬 수정
- exports/ 계층 (별도 작업)
