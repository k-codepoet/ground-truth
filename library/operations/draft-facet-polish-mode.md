---
title: "/gemify:draft의 facet/polish 모드"
domain: operations
---

## Context

/gemify:draft 대화 시 탐색 방식을 명시적으로 구분하여 효율적인 지식 확장이 가능하도록 함. inbox(원석) → draft(facet/polish) → library(보석) 흐름과 일관된 보석 메타포 유지.

## Content

### 두 가지 모드

```
/gemify:draft
├── facet  - 여러 면 탐색, 넓게 (BFS)
└── polish - 깊이 연마, 광택 (DFS) → library 준비
```

| 모드 | 성격 | 질문 스타일 |
|------|------|------------|
| facet | 넓게 탐색 | "연결되는 건?", "다른 관점에서?" |
| polish | 깊이 연마 | "왜 중요해?", "핵심만 남기면?" |

### 전환 규칙

- **기본**: facet
- **polish 트리거**: "연마해봐", "좀 더 다듬자", "핵심이 뭐야"

### revision (스냅샷)

방향 전환(pivot) 시 자동 스냅샷:

```
revision 증가 조건:
├── facet → 다른 방향 facet
├── facet → polish 전환
└── polish → 다른 방향 polish
```

### 히스토리 구조

```
drafts/
├── {slug}.md              # 현재 상태 (압축)
└── .history/{slug}/
    └── {rev}-{mode}-{date}.md  # 스냅샷
```

- 메인 파일: frontmatter `history` 배열로 요약
- 스냅샷: 그 시점의 결정사항 + 다음 작업 (바로 작업 가능한 형태)
