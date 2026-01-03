---
title: gemify:draft 자동 스냅샷 개선 아이디어
date: 2026-01-03
status: raw
used_in:
references:
  - inbox/materials/2026-01-03-draft-auto-snapshot-need.md
---

## 개선 아이디어

gemify:draft 스킬에서 **자동 스냅샷 트리거**를 추가해야 함:

1. **모드 전환 시**: facet → polish 전환할 때 자동 스냅샷
2. **일정 turns 이상**: 예) 5턴마다 자동 스냅샷
3. **명시적 pivot 감지**: "방향 바꿔보자", "다른 관점에서" 등 키워드

## 구현 방향

- draft 스킬의 워크플로우에 스냅샷 로직 추가
- `.history/{slug}/` 폴더에 자동 저장
- frontmatter의 `history` 배열 자동 업데이트

## 이게 부트스트래핑 원칙에 부합하는 이유

- gemify가 gemify를 개선하는 사례
- 직접 사용하면서 불편함 발견 → 개선
- HITL → 기준 추출 → 위임 가능 형태로 발전
