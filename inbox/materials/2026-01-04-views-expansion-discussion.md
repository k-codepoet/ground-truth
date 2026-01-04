---
title: "Views 확장 필요성 논의"
date: 2026-01-04
source: "gemify:draft 세션 - library 분류 체계 리팩토링"
type: conversation
status: raw
used_in: null
---

# Views 확장 필요성 논의

## 맥락

library 분류 체계 리팩토링 중 views에 대한 생각도 고도화됨.

## 현재 views 구조

```
views/by-subject/{subject}.md
```

- gemify, forgeify, namify 등 제품/솔루션/서비스
- 문제 → 해결책(제품/솔루션/서비스/프로세스/파이프라인/프레임워크)

## 문제 인식

by-subject는 "내가 만든 것"에 집중. 하지만 views는 더 확장될 수 있음:

1. **발표/메시지 전달** - 내 메시지를 다른 사람에게 전달
2. **교육/강의/세미나** - 주니어를 가르치기 위한 콘텐츠

## 기준 차이

| View 타입 | 적합한 기준 |
|-----------|------------|
| by-subject (제품/솔루션) | 6대 domain (product, engineering, operations...) |
| 발표/메시지 | ? (다른 기준 필요) |
| 교육/강의/세미나 | ? (다른 기준 필요) |

→ 각 view 타입별로 다른 판단/처리 기준이 필요
