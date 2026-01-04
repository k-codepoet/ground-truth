---
title: "6대 Domain은 library가 아니라 views 기준일 수 있다"
date: 2026-01-04
status: raw
used_in: null
references:
  - inbox/materials/2026-01-04-six-domain-mismatch.md
---

# 6대 Domain은 library가 아니라 views 기준일 수 있다

## 핵심 인사이트

library는 "재료"인데, 재료를 domain으로 분류하는 게 맞나?

재료는 여러 맥락에서 재사용됨:
- `bootstrapping-principle.md`가 product에도, engineering에도 쓰일 수 있음
- domain은 "이 재료를 어떤 관점에서 보느냐"의 문제

→ **domain은 views의 관점 (lens)이지, library의 분류 기준이 아닐 수 있다**

## 가설

```
library/ → 평평하게 (flat) 또는 다른 기준으로 분류
views/ → domain 관점에서 library 재료 조합
```

## 다음 단계

- 이 가설 검증 필요
- 기존 library 구조 어떻게 마이그레이션할지 고민
