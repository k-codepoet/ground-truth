---
title: "Views Layer 아이디어 - 대화 기록"
date: 2026-01-02
source: "Claude 대화"
type: conversation
status: raw
used_in:
---

# Views Layer 아이디어 - 대화 기록

## 발단

library에 gemify-branding-decision.md를 저장한 후, 제품/주제별로 묶어서 보는 필요성 발견.

현재 구조의 한계:
- library는 domain별 분류 (product, engineering, growth...)
- 하지만 gemify, ced, gitops 등 제품/프로젝트별 묶음이 안 됨
- 관련 문서가 여러 domain에 흩어져 있음

## 의사결정 과정

두 가지 축 정의:

| 축 | 예시 | 용도 |
|-----|------|------|
| Domain (How) | product, engineering, growth | 역량별 정리 |
| Subject (What) | gemify, ced, gitops | 제품/프로젝트별 묶음 |

검토한 옵션:
- Option A: 태그 기반 - 구조 변경 없음, 뷰어 필요
- Option B: _index 폴더 - 수동 관리, 동기화 문제
- Option C: views 레이어 - 레이어 분리 명확, 확장성 좋음

## 최종 결정

Option C 채택:

```
ground-truth/
├── inbox/
├── drafts/
├── library/     # 원천 데이터 (domain별)
└── views/       # 조합 레이어
    └── by-subject/
        ├── gemify.md
        ├── ced.md
        └── gitops.md
```

핵심: library = 원천, views = 재구성
