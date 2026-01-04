---
target_plugin: gemify
improvement_type: refactor
priority: high
problem: "library 분류 시 6대 domain 사용 → 경계 모호, 복수 domain 해당 시 선택 강제"
solution: "library는 Type 기반 분류로 변경, 6대 domain은 views의 lens로 이동"
requirements:
  - /gemify:library 스킬에서 domain 대신 type 선택하도록 변경
  - library frontmatter 스키마 변경 (domain → type + origin)
  - 관련 SKILL.md, 커맨드 문서 업데이트
references:
  - drafts/domain-classification-rethink.md
domain: engineering
views: [gemify]
---

## Why

현재 `/gemify:library`는 6대 domain(product, engineering, operations, growth, business, ai-automation)으로 분류함.

문제:
1. **경계가 겹침**: engineering과 ai-automation이 자주 겹침
2. **단일 선택 강제**: 복수 domain 해당 시 하나만 골라야 함
3. **기준 불명확**: "핵심 질문"만으로는 판단 어려움

핵심 인사이트:
- library는 "재료" → 재료를 domain으로 분류하는 건 맞지 않음
- domain은 "이 재료를 어떤 관점에서 보느냐"의 문제
- **domain은 views의 관점(lens)이지, library의 분류 기준이 아니다**

## What

### 1. library 폴더 구조 변경

```
# Before (6대 domain)
library/
├── product/
├── engineering/
├── operations/
├── growth/
├── business/
└── ai-automation/

# After (Type 기반)
library/
├── principles/    # 근본 원칙, 철학
├── decisions/     # 의사결정 기록 (ADR)
├── insights/      # 발견, 깨달음
├── how-tos/       # 방법론, 절차
└── specs/         # 명세, 스펙
```

### 2. frontmatter 스키마 변경

```yaml
# Before
title: "Bootstrapping 원칙"
domain: ai-automation
views: []

# After
title: "Bootstrapping 원칙"
type: principle       # principle | decision | insight | how-to | spec
origin: original      # original | digested | derived
views: []
```

**Origin 정의:**
- **original**: 내 생각에서 나온 것
- **digested**: 외부 콘텐츠를 소화해서 내 방식으로 재구성
- **derived**: 산출물(artifact)에서 역추출한 것

### 3. /gemify:library 스킬 수정

- domain 선택 질문 → type 선택 질문으로 변경
- origin 선택 질문 추가
- 저장 경로: `library/{type}s/{slug}.md`

### 4. 6대 Domain 역할 변경

6대 domain은 views에서 사용:
- views/by-subject 조합 시 "어떤 관점에서 이 재료를 쓰는가"의 lens
- library frontmatter에서 제거

## Scope

**포함:**
- /gemify:library SKILL.md 수정
- library.md 커맨드 수정 (있다면)
- CLAUDE.md 업데이트 (library frontmatter 스키마)
- ground-truth-protocol.md 업데이트

**제외:**
- 기존 library 파일 마이그레이션 (별도 작업)
- views 관련 스킬 수정 (별도 draft 후 진행)
