---
name: seed
description: 사용자의 생각을 seed/에 빠르게 저장. "저장해", "메모해", "seed", "씨앗" 등 요청 시 활성화. raw 상태로 저장하여 /grow로 확장 가능.
license: MIT
compatibility: 이 프로젝트의 seed/, materials/, growing/, corpus/ 구조 필요
metadata:
  author: choigawoon
  version: "0.2"
allowed-tools: Read Write Edit
---

# Seed Skill

사용자의 생각을 **씨앗 상태로 빠르게 저장**합니다.

## 동작

1. 사용자가 말한 내용 파악
2. 최소한의 정돈 (마크다운)
3. `seed/{date}-{slug}.md`로 저장
4. "/grow로 키울 수 있어요" 안내

## 파일 형식

```markdown
# {제목}

> 날짜: YYYY-MM-DD
> 참조: (materials 경로, 없으면 생략)
> status: raw
> used_in: (growing 경로, 사용 후 기록)

---

{내용}
```

## seed vs materials

| 폴더 | 용도 | 명령어 |
|------|------|--------|
| seed/ | 내 생각의 씨앗 | /seed |
| materials/ | 외부 재료 | /import (예정) |

## 규칙

- **과하게 다듬지 않음** - raw 상태 유지
- 제목은 핵심 키워드 추출
- slug는 영문 kebab-case
- 저장 후 `/grow` 안내
