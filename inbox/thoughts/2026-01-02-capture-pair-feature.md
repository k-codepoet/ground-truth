---
title: "material + thought 쌍으로 캡처하는 기능"
date: 2026-01-02
status: raw
used_in:
references:
---

# material + thought 쌍으로 캡처하는 기능

대화 맥락에서 material(외부 기록)과 thought(내 생각)를 쌍으로 한번에 생성해주는 기능이 있으면 좋겠다.

지금은 `/gemify:import`와 `/gemify:inbox`를 따로 써야 하는데, `/gemify:capture-pair` 같은 걸로 한번에 처리하면 편할듯.

- 대화 기록 → material로
- 거기서 뽑은 내 핵심 생각 → thought로

## 예상 사용법

```
/gemify:capture-pair
```

자동으로:
1. 직전 대화 맥락에서 의사결정 과정/외부 정보 추출 → `inbox/materials/`
2. 핵심 인사이트/내 생각 추출 → `inbox/thoughts/`
3. thought에 material을 references로 연결
