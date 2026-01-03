---
title: "실행 전 YAGNI 체크 원칙"
created: "2026-01-03"
updated: "2026-01-03 15:00"
turns: 4
revision: 2
status: set
sources:
  - inbox/thoughts/2026-01-03-improve-plugin-yagni-check.md
  - inbox/materials/2026-01-03-yagni-realization-conversation.md
history:
  - rev1-facet.md
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

### Turn 1-4 (2026-01-03) - facet 모드

**시작점**: 플러그인 버전/종속성 관리 조사 중 멈춤. "지금 문제 된 적 있나?" → 없음.

**탐색 결과**:
1. 적용 위치 → library/operations/에 원칙 문서로 분리, SKILL.md에서 참조 (progressive disclosure)
2. "예" 시 액션 → 즉시 중단 권고 (정말 중요한 일에 시간을 써야 함)
3. 캡처 원칙과 연결 → "기록은 자유롭게, 실행은 신중하게"
4. 트리거 조건 → 금방 될 일은 그냥 진행, 깊어질 것 같으면 체크

---

## Current State

### 핵심 원칙

**기록은 자유롭게, 실행은 신중하게**

### YAGNI 체크리스트

시간이 많이 들 것 같은 작업 시작 전:

```
□ 실제 문제가 발생했는가? (미래 걱정 아닌지)
□ 현재 사용자가 나만인가?
□ 문제가 발생하면 그때 해도 늦지 않은가?
```

### 판정

- 3개 모두 "아니오" → 진행
- 하나라도 "예" → **즉시 중단**, 우선순위 재점검

### 적용 범위

- 금방 될 일 (5분 내) → 체크 불필요, 그냥 진행
- 깊어질 것 같은 작업 → 체크 필요
  - 조사/설계가 필요한 작업
  - 여러 파일을 건드리는 작업
  - "체계를 잡아두자" 류의 작업

### 구현 방식

1. `library/operations/go-no-go.md`에 원칙 문서 저장
2. 각 스킬의 SKILL.md에서 필요시 참조 (progressive disclosure)

---

## Open Questions

- [x] 체크리스트를 SKILL.md에 직접 넣을까, 별도 원칙 문서로 분리할까? → 분리
- [x] "예"가 나오면 정확히 어떤 액션을 취할까? → 즉시 중단
- [x] 기존 "캡처 우선 원칙"과 어떻게 연결할까? → "기록은 자유롭게, 실행은 신중하게"
