---
name: capture
description: 사용자의 생각을 inbox에 빠르게 캡처. "이거 저장해", "메모해", "inbox에 넣어" 등의 요청 시 자동 활성화.
license: MIT
metadata:
  author: choigawoon
  version: "0.1"
allowed-tools: Write
---

# Capture Skill

## Overview

사용자가 말하는 생각을 **즉시 inbox에 저장**한다.
정돈은 하되, 과하게 다듬지 않는다.

## 자동 활성화 조건

- "이거 저장해", "메모해", "inbox에 넣어"
- "기록해", "남겨", "캡처해"
- 생각을 쏟아내는 대화

## 동작

1. 사용자가 말한 내용을 파악
2. 최소한의 정돈 (마크다운 형식)
3. `inbox/{date}-{slug}.md`로 저장
4. 저장 완료 알림

## 파일 형식

```markdown
# {제목 - 내용에서 추출}

> 날짜: YYYY-MM-DD
> 출처: 대화

---

{사용자가 말한 내용 - 최소한의 정돈}
```

## 규칙

- **과하게 다듬지 않는다** - raw 상태 유지
- 제목은 내용에서 핵심 키워드 추출
- slug는 영문 kebab-case
- 저장 후 바로 알림
