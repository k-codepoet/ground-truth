---
title: "Gemify 브랜딩 의사결정"
domain: growth
views: [gemify, namify]
---

## Context

Knowledge Pipeline 제품의 네이밍과 브랜딩을 결정하는 과정. 메타포 선택, 폴더 구조, 제품명, 태그라인을 확정함.

## Content

### 최종 결정

| 항목 | 결정 |
|------|------|
| 제품명 | **Gemify** |
| 태그라인 | Turn your thoughts into gems. |
| 메타포 | 광물/보석 (원석 → 다듬기 → 보석) |

### 메타포 선정 과정

```
❌ 식물: Seed → Grow → Digest (Digest에서 깨짐)
❌ 술: Gather → Ferment → Distill (연령/성별 편향)
✅ 광물: Rough → Refine → Gem (모든 연령 OK, 성별 중립)
```

### 폴더명 결정

메타포는 브랜딩에만, 구조는 직관적으로:

| 후보 | 결정 | 이유 |
|------|------|------|
| ore/flux/corpus | inbox/drafts/library | 5개 타겟 그룹 전부 즉시 이해 |

```
├── inbox/      # 원재료 (모두 이해)
├── drafts/     # 작업 중 (모두 이해)
└── library/    # 완성된 지식 (모두 이해)
```

### 제품명 선정

| 후보 | 결과 | 이유 |
|------|------|------|
| Gem | ❌ | Ruby Gem 혼동, 검색 어려움 |
| GemCraft | ❌ | 약간 길다 |
| MindGem | ❌ | 평범 |
| **Gemify** | ✅ | "-ify" 변환 패턴 (Shopify), 동사화, 검색 구별 |

### BFS/DFS 모드 네이밍

| 모드 | 이름 | 의미 |
|------|------|------|
| BFS | facet | 여러 면 탐색 |
| DFS | polish | 깊이 연마 |

### 타겟 사용자별 어필 포인트

| 그룹 | 메시지 |
|------|--------|
| 일반인 | "생각 정리" |
| 크리에이터 | "아이디어 관리" |
| 개발자 | "지식 파이프라인" |
| 연구자 | "체계적 문서화" |
| AI Agents | "시맨틱하게 명확한 구조" |

### 브랜딩 에셋

**영문**
```
Gemify - Turn your thoughts into gems.
From rough ideas to polished knowledge.
```

**한국어**
```
Gemify - 당신의 생각을 보석으로.
모든 아이디어는 원석입니다.
```

## Connections

- [Knowledge Pipeline 비전](../operations/knowledge-pipeline-vision.md) - 전체 시스템 구조
- [facet/polish 모드](../operations/draft-facet-polish-mode.md) - 대화 모드 상세
