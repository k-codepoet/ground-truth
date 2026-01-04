---
title: 플러그인 개선 워크플로우 - 세션 한정 스코프
type: workflow
origin: original
views: [gemify]
---

## Context

플러그인 개선 작업 시 해당 플러그인 코드에 접근해야 한다.
하지만 항상 모든 플러그인을 워크스페이스에 두면 스코프가 커진다.
필요할 때만 추가하고, 세션 종료 시 자동으로 해제되는 패턴이 필요했다.

## Content

**핵심 결정**: `/add-dir`로 세션 한정 스코프 추가

워크플로우:
```
inbox에 플러그인 개선 아이디어
    ↓
/add-dir {플러그인 경로}  ← 사용자 승인 필요
    ↓
개선 작업 수행
    ↓
세션 종료 → 자동 스코프 해제
```

왜 이 방식인가:
- `remove-dir` 기능이 없음 → 세션 종료로 대체
- 명시적 승인 필요 → 의도치 않은 스코프 확장 방지
- 세션 단위 운영 → 깔끔한 컨텍스트 관리

구현: `/gemify:improve-plugin` 스킬 (gemify v1.3.0)

## Connections

- inbox/materials/agent-summary-out-of-scope-with-add-dir/ - add-dir 논의 원본
