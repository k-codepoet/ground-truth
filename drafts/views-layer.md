---
title: "Views 레이어 설계"
created: "2026-01-02"
updated: "2026-01-02"
turns: 5
revision: 1
status: set
sources:
  - inbox/thoughts/2026-01-02-views-layer-need.md
  - inbox/materials/2026-01-02-views-layer-discussion.md
history: []
---

## Seed

library는 domain별 분류가 원칙이지만, 제품/프로젝트 관점에서 묶어보는 views 레이어가 필요하다.

---

## Sources

- inbox/thoughts/2026-01-02-views-layer-need.md (내 생각)
- inbox/materials/2026-01-02-views-layer-discussion.md (의사결정 과정)

---

## Current State

### 문제

- library는 domain별 분류 (product, engineering, growth...)
- gemify, ced, gitops 등 제품/프로젝트별 묶음이 안 됨
- 관련 문서가 여러 domain에 흩어져 있음

### Views = 창문 (Window into Knowledge)

지식을 분해하고 재조립해서 바라보는 창문.
사람은 스토리로 기억한다 → 도식 + 스토리 구조.

### 확정된 구조

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

### View 파일 형식 (확정)

```markdown
# {Subject} View

## 구조
(단순 ASCII 도식, 필요시 Mermaid)
[inbox] → [drafts] → [library]
   ↓         ↓          ↓
 포착       다듬기      정리

## 스토리
(왜 시작 → 뭘 결정 → 어디까지)
(링크는 스토리 안에 자연스럽게)

## 관련 문서
(views: [subject] 태그 기반 자동 수집)
```

### 명령어: `/gemify:view`

```
/gemify:view              # views 목록 또는 새로 만들기
/gemify:view gemify       # gemify view 초안 생성/업데이트
```

**생성 흐름:**
1. 대화로 "관련 문서가 뭐야?" 물어봄
2. 사용자가 알려주면 library 문서에 `views: [subject]` 추가
3. views/by-subject/{subject}.md 생성 (구조 + 스토리)
4. 다음부터는 views 태그 기반 자동 수집

### 양방향 연결

- library 문서 → `views: [gemify, ced]`
- views 파일 → 스토리 안에 library 링크

---

## Open Questions

- [x] views 파일의 형식? → 도식 + 스토리 + 링크
- [x] 자동 생성 vs 수동 관리? → 반자동 (/gemify:view)
- [x] by-subject 외에 다른 view 타입? → 일단 by-subject만, 필요시 추가
