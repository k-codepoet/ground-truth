---
description: 생각을 inbox에 빠르게 저장
arguments:
  - name: content
    description: 저장할 내용 (없으면 직전 대화 내용 사용)
    required: false
---

# /capture - 빠른 캡처

capture 스킬을 사용하여 생각을 inbox에 저장한다.

## 사용법

```
/capture                     # 직전 대화 내용 저장
/capture 이런 생각이 들었어   # 입력 내용 저장
```

## 동작

1. $ARGUMENTS가 있으면 해당 내용 저장
2. 없으면 직전 사용자 발화 내용 저장
3. 최소한의 정돈 후 inbox에 저장
