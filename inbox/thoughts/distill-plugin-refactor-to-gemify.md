---
title: distill 플러그인을 Gemify로 리팩토링
created: 2025-12-31
status: raw
tags:
  - refactoring
  - plugin
  - branding
source: materials/gemify-branding-decision.md
---

# distill 플러그인을 Gemify로 리팩토링

## 핵심 아이디어

materials/gemify-branding-decision.md 내용을 토대로 distill 플러그인을 리팩토링하고 싶다.

**변경 포인트:**
- 플러그인 이름: `distill` → `gemify`
- 메타포: 술/증류 → 광물/보석
- 폴더 구조: seed/growing/corpus → inbox/drafts/library
- 명령어: /distill:seed, /distill:grow, /distill:digest → /capture, /develop, /file

## 참조 문서

gemify-branding-decision.md의 최종 결정:

```
브랜드명: Gemify
태그라인: Turn your thoughts into gems.

폴더 구조:
├── inbox/      # Capture (포착)
├── drafts/     # Develop (발전)
│   ├── facet   # BFS - 넓게 탐색
│   └── polish  # DFS - 깊이 연마
├── library/    # File (정리)
└── exports/    # 출력물

명령어:
/capture    → inbox/
/develop    → drafts/
/file       → library/
```

## 고려 사항

1. 기존 distill 사용자 마이그레이션?
2. ground-truth repo의 폴더 구조도 함께 변경?
3. plugin.json, skills, commands 전체 리팩토링 범위
