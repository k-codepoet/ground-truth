---
title: "grow 스킬 모드 확장"
created: "2024-12-31"
updated: "2024-12-31 09:45"
turns: 3
revision: 3
status: set
sources:
  - inbox/thoughts/2024-12-31-grow-mode-expansion.md
  - inbox/materials/2024-12-31-claude-md-review.md
history:
  - rev: 1
    mode: facet
    date: 2024-12-31
    summary: "모드 구조 정리: BFS + DFS, progressive disclosure 히스토리"
    file: .history/grow-mode-expansion/01-facet-2024-12-31.md
  - rev: 2
    mode: facet
    date: 2024-12-31
    summary: "revision 기준 정의: pivot(방향 전환) 시 스냅샷"
    file: .history/grow-mode-expansion/02-facet-2024-12-31.md
  - rev: 3
    mode: facet
    date: 2024-12-31
    summary: "용어 확정: facet/polish (보석 메타포)"
    file: .history/grow-mode-expansion/03-facet-2024-12-31.md
---

## Current State

### 모드 (확정)

```
/gemify:draft
├── facet  - 여러 면 탐색, 넓게 (BFS)
└── polish - 깊이 연마, 광택 (DFS) → library 준비

기본: facet
트리거: "연마해봐", "좀 더 다듬자", "핵심이 뭐야" → polish
```

### 히스토리 구조 (확정)

```
drafts/
├── {slug}.md              # 현재 상태
└── .history/{slug}/
    └── {rev}-{mode}-{date}.md
```

### revision = pivot (확정)

방향 전환 시 스냅샷 생성

### 자동화 (확정)

Stop 훅 + prompt → pivot 감지 → revision++

---

## Open Questions

- [ ] 스킬 구현 착수?
