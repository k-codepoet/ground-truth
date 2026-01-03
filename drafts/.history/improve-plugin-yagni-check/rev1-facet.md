---
title: "improve-plugin에 YAGNI 체크리스트 추가"
created: "2026-01-03"
updated: "2026-01-03 14:30"
turns: 0
revision: 1
status: cutting
sources:
  - inbox/thoughts/2026-01-03-improve-plugin-yagni-check.md
  - inbox/materials/2026-01-03-yagni-realization-conversation.md
history: []
---

## Seed

플러그인 개선(improve-plugin) 시작 전에 "이게 지금 필요한가?" 점검이 없다.
오늘 종속성 관리 체계 조사하다 중단 → 실제 문제가 아닌 미래 걱정이었음.

---

## Sources

- `inbox/thoughts/2026-01-03-improve-plugin-yagni-check.md` - 원석
- `inbox/materials/2026-01-03-yagni-realization-conversation.md` - 깨달음의 맥락

---

## Growth Log

### Turn 1 (2026-01-03)

**시작점**: 플러그인 버전/종속성 관리 조사 중 멈춤. "지금 문제 된 적 있나?" → 없음.

---

## Current State

### 문제

improve-plugin 워크플로우에 "정말 지금 필요한가?" 검증 단계가 없음.
결과: 미래 대비용 작업에 시간 소모.

### 제안된 체크리스트

```
□ 실제 문제가 발생했는가? (미래 걱정 아닌지)
□ 현재 사용자가 나만인가?
□ 문제가 발생하면 그때 해도 늦지 않은가?
```

- 3개 모두 "아니오" → 진행
- 하나라도 "예" → 재확인 필요

### 적용 위치 후보

1. `gemify/skills/improve-plugin/SKILL.md`에 체크리스트 추가
2. `library/operations/`에 원칙 문서로 두고 참조

---

## Open Questions

- [ ] 체크리스트를 SKILL.md에 직접 넣을까, 별도 원칙 문서로 분리할까?
- [ ] "예"가 나오면 정확히 어떤 액션을 취할까? (중단? 재확인 질문?)
- [ ] 기존 "캡처 우선 원칙"과 어떻게 연결할까?
