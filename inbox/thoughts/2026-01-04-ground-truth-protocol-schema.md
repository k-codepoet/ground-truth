---
title: "ground-truth 공통 프로토콜/스키마 정의 필요"
date: 2026-01-04
status: raw
used_in: null
references:
  - inbox/materials/2026-01-04-tidy-triage-protocol-need.md
---

# ground-truth 공통 프로토콜/스키마 정의

## 핵심 인사이트

tidy와 triage 모두 **공통 프로토콜**이 있어야 제대로 동작.
gemify:improve-plugin ↔ forgeify:improve-plugin 처럼 프로토콜로 상호작용.

## 정의해야 할 것

### 1. artifact 스키마

library/views frontmatter에 추가:

```yaml
artifact: plugins/forgeify/  # 실제 결과물 경로
artifact_type: plugin | content | code | doc
```

### 2. 컨벤션 규칙

- 네이밍: kebab-case, 일관된 prefix
- 경로: 상대경로 기준
- 참조: sources 배열에 명시

### 3. source-of-truth 판단

불일치 발견 시:
- 문서 outdated → 결과물 기준으로 문서 수정
- 결과물 outdated → 문서 기준으로 결과물 수정 (별도 작업)
- 판단 불가 → 사용자에게 확인

## 구현 방향

**Option A**: 별도 스킬 `/gemify:schema`
**Option B**: tidy에 포함 (첫 실행 시 정의)
**Option C**: library 문서로 (`library/operations/ground-truth-schema.md`)

→ **C 추천**: 스키마도 지식이니까 library에 넣고 스킬들이 참조

## 다음 단계

1. `library/operations/ground-truth-schema.md` 작성
2. tidy/triage가 이 문서 참조하도록 설계
3. 기존 문서 마이그레이션 (artifact 필드 추가)
