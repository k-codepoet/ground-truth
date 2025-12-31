---
title: "grow 스킬 모드 확장"
created: "2024-12-31"
updated: "2024-12-31 09:45"
turns: 3
revision: 3
status: digested
sources:
  - seed/2024-12-31-grow-mode-expansion.md
  - materials/2024-12-31-claude-md-review.md
history:
  - rev: 1
    mode: branch
    date: 2024-12-31
    summary: "모드 구조 정리: BFS + DFS, progressive disclosure 히스토리"
    file: .history/grow-mode-expansion/01-expand-2024-12-31.md
  - rev: 2
    mode: branch
    date: 2024-12-31
    summary: "revision 기준 정의: pivot(방향 전환) 시 스냅샷"
    file: .history/grow-mode-expansion/02-expand-2024-12-31.md
  - rev: 3
    mode: branch
    date: 2024-12-31
    summary: "용어 확정: branch/ripen (식물 메타포)"
    file: .history/grow-mode-expansion/03-expand-2024-12-31.md
---

## Current State

### 모드 (확정)

```
/grow
├── branch - 가지치기, 넓게 뻗기 (BFS)
└── ripen  - 익히기, 응축 (DFS) → digest 준비

기본: branch
트리거: "익혀봐", "좀 더 익히자" → ripen
```

### 히스토리 구조 (확정)

```
growing/
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
