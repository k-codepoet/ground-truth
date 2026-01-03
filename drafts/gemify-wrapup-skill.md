---
title: gemify wrapup 스킬 설계
created: 2026-01-03
updated: 2026-01-03
turns: 5
revision: 1
status: set
sources:
  - inbox/thoughts/2026-01-03-session-wrapup-skill-idea.md
  - inbox/materials/2026-01-03-session-wrapup-pattern.md
history: []
---

## Core Insight

세션 종료는 반복되는 패턴. 매번 "놓친 거 있니?"라고 물어보는 대신, 스킬로 위임하면 일관된 품질의 마무리 보장.

## 설계 확정

### 스킬 이름

`/gemify:wrapup`
- "wrap up" = 미국 비즈니스 문화에서 "깔끔하게 정리하며 마무리"
- 회의, 프로젝트 종료 시 자연스럽게 쓰이는 표현

### 동작 흐름

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

### 저장 위치

```
sessions/
└── YYYY-MM-DD-NNN.md
```

- gemify 지식 파이프라인(inbox→drafts→library→views) 바깥
- **운영 계층** - 작업 메타데이터, 세션 기록
- `exports/`와 구분: exports는 library 지식을 가공해서 내보내는 출력 계층

### 리포트 템플릿

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

## 중요한 구분

- inbox 항목 = "미완료"가 아니라 **"의도적으로 챙겨둔 것"**
- Stashed for Next 섹션에서 이 의도를 명확히 표현

## 세션 범위

- **기본값**: 대화 전체 (Claude Code 세션 시작~종료)
- **사용자 지정**: 리포팅 요청 시 "어디서부터 어디까지?" 확인 후 진행

## Raw Material

### thought에서
- 부트스트래핑 원칙의 "신뢰 기반 위임" 적용
- 반복되는 패턴 → 규칙화 → 스킬로 위임

### material에서
- 현재: 수동 질문 → Claude 답변 → 기록 없이 끝남
- 문제: 일관성 없음, 누락 가능성
