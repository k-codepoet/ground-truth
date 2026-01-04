---
title: "Library 분류 체계 리팩토링"
status: set
sources:
  - inbox/thoughts/2026-01-03-domain-classification-problem.md
  - inbox/thoughts/2026-01-04-domain-belongs-to-views.md
history: []
---

# Library 분류 체계 리팩토링

## 문제의식

현재 library에 저장할 때 6대 domain으로 분류하는데, 이게 맞는 기준인가?

### 느끼는 문제들

1. **경계가 겹침**: engineering과 ai-automation이 자주 겹침
2. **단일 선택 강제**: 복수 domain 해당 시 하나만 골라야 함
3. **기준 불명확**: "핵심 질문"만으로는 판단 어려움

### 핵심 인사이트

library는 "재료"인데, 재료를 domain으로 분류하는 게 맞나?

재료는 여러 맥락에서 재사용됨:
- `bootstrapping-principle.md`가 product에도, engineering에도 쓰일 수 있음
- domain은 "이 재료를 어떤 관점에서 보느냐"의 문제

→ **domain은 views의 관점(lens)이지, library의 분류 기준이 아니다**

---

## 결정: 관심사 분리

### library = 재료의 pillar (본질적 속성)

**1차 분류: Type (지식의 형태)** - 폴더 구조
```
library/
├── principles/    # 근본 원칙, 철학
├── decisions/     # 의사결정 기록 (ADR)
├── insights/      # 발견, 깨달음
├── how-tos/       # 방법론, 절차
└── specs/         # 명세, 스펙
```

**메타데이터: Origin (출처)** - frontmatter
```yaml
title: "Bootstrapping 원칙"
type: principle
origin: original    # original | digested | derived
```

- **original**: 내 생각에서 나온 것
- **digested**: 외부 콘텐츠를 소화해서 내 방식으로 재구성
- **derived**: 산출물(artifact)에서 역추출한 것

### views = subject별 조합 + 6대 domain 관점

```
views/by-subject/{subject}.md
  → library 재료들을 조합
  → 6대 domain은 "이 재료를 어떤 관점에서 쓰는가"의 lens
```

**6대 Domain (views의 lens)**

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

---

## 효과

- **library**: 재료의 본질(Type)로 분류 → 재사용성 극대화
- **views**: subject별 조합 시 domain 관점 적용 → 밀도 높은 콘텐츠 생산
- **관심사 분리**: 재료(what) vs 관점(how to use) 명확히 구분

---

## 다음 단계

1. **마이그레이션** (별도 세션)
   - 기존 37개 library 파일을 Type 폴더로 재분류
   - frontmatter에 type, origin 추가
   - CLAUDE.md, ground-truth-protocol.md 업데이트

2. **Views 확장 설계** (별도 draft)
   - by-subject 외 다른 view 타입 정의 (발표, 교육 등)
   - 각 타입별 적합한 lens/기준 설계
