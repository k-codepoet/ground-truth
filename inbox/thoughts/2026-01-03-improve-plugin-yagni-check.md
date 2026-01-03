---
title: improve-plugin에 YAGNI 체크리스트 필요
date: 2026-01-03
status: used
used_in: drafts/improve-plugin-yagni-check.md
references:
  - inbox/materials/2026-01-03-yagni-realization-conversation.md
---

# improve-plugin에 YAGNI 체크 추가 필요

## 문제

플러그인 개선 작업 시작 전에 "이게 지금 필요한가?" 점검이 없음.
오늘 플러그인 종속성 관리 체계 조사하다가 중단 → 미래 걱정이었음.

## 제안

improve-plugin 스킬 시작 시 체크리스트:

```
□ 실제 문제가 발생했는가? (미래 걱정 아닌지)
□ 현재 사용자가 나만인가?
□ 문제가 발생하면 그때 해도 늦지 않은가?
```

3개 모두 "아니오"면 → 진행
하나라도 "예"면 → 정말 지금 필요한지 재확인

## 적용 위치

- `gemify/skills/improve-plugin/SKILL.md`에 체크리스트 추가
- 또는 참조할 원칙을 `library/operations/`에 두고 링크

## 연관 원칙

- YAGNI (You Aren't Gonna Need It)
- 캡처 우선 원칙 (이미 있음)
- "실제 문제 기반 개선" 원칙 (새로 필요)
