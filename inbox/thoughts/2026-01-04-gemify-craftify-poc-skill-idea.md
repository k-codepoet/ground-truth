---
created: 2026-01-04
status: raw
tags: [gemify, craftify, skill-design, delegation]
references:
  - inbox/materials/2026-01-04-gemify-craftify-delegation-context.md
---

# gemify:craftify-poc 스킬 아이디어

## 핵심 생각

gemify:improve-plugin처럼 **craftify에게 위임할 문서를 만드는 스킬**이 필요하다.

## 왜 필요한가

- session report viewer 같은 PoC 앱 아이디어가 생길 때마다 craftify에 전달해야 함
- 매번 수동으로 스펙 문서를 작성하는 건 비효율적
- gemify 파이프라인에서 자연스럽게 craftify로 흘러가는 구조가 필요

## 선행 작업

1. **gemify ↔ craftify 스키마/프로토콜** 정의
   - craftify가 이해할 수 있는 문서 구조
   - 필수 필드, 옵션 필드

2. **gemify:craftify-poc 스킬** 구현
   - 대화에서 PoC 스펙 추출
   - craftify 전달용 문서 생성

## 패턴

```
gemify:improve-plugin → forgeify (플러그인 수정)
gemify:craftify-poc   → craftify (PoC 앱 생성)
```

둘 다 "지식을 문서화 → 실행 도구에 위임" 패턴
