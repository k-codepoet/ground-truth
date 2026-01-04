---
title: "ground-truth 공통 프로토콜/스키마"
created: 2026-01-04
updated: 2026-01-04
turns: 1
revision: 1
status: set
sources:
  - inbox/thoughts/2026-01-04-ground-truth-protocol-schema.md
  - inbox/materials/2026-01-04-tidy-triage-protocol-need.md
history: []
---

# ground-truth 공통 프로토콜/스키마

## 문제

tidy와 triage를 설계하다 보니 순환 의존성 발견:
- tidy 먼저? → 스키마 없으면 검증 불가
- triage 먼저? → library가 outdated면 잘못된 곳에 연결

→ **공통 프로토콜/스키마 정의가 진짜 선행 작업**

## 공통 패턴

tidy/triage 모두:
- "현황 파악 → 제안 → 컨펌 → 실행"
- 스키마/컨벤션 기반 동작
- 점진적 실행 (한 번에 하나씩)

## 정의해야 할 것 (초안)

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
불일치 시:
- 문서 outdated → 결과물 기준으로 문서 수정
- 결과물 outdated → 문서 기준으로 결과물 수정
- 판단 불가 → 사용자에게 확인

---

## Open Questions

- [ ] artifact 필드가 모든 library 문서에 필요할까?
- [ ] tidy/triage가 이 프로토콜을 어떻게 참조할까?
- [ ] views layer와 artifact의 관계는?

## Session Notes

(대화하며 추가)
