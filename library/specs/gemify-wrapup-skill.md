---
title: gemify wrapup 스킬 설계
type: spec
origin: derived
views: []
---

## 핵심

세션 종료를 스킬로 위임하여 일관된 품질의 마무리 보장.

## 스킬: `/gemify:wrapup`

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

- gemify 지식 파이프라인 바깥의 **운영 계층**
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

### 세션 범위

- **기본값**: 대화 전체 (Claude Code 세션)
- **사용자 지정**: 리포팅 요청 시 구간 확인 후 진행

## 핵심 구분

inbox 항목 = "미완료"가 아니라 **"의도적으로 챙겨둔 것"**
