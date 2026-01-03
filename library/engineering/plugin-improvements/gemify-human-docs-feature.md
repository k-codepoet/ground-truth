---
target_plugin: gemify
improvement_type: feature
priority: high
problem: "library에 안착된 지식을 인간 작업 기준 문서(principles, decisions, policies)로 발전시키는 기능이 없음"
solution: "human-principle, human-decision, human-policy 명령어 추가"
requirements:
  - 세 가지 타입 지원 (principle, decision, policy)
  - library 안착 여부 확인 후 미안착 시 library로 먼저 유도
  - 대화 맥락에서 인사이트 추출하여 각 타입별 템플릿에 맞게 문서 생성
  - 저장 위치는 docs/humans/{principles|decisions|policies}/
references:
  - docs/humans/principles/_template.md
  - docs/humans/decisions/_template.md
  - docs/humans/policies/_template.md
  - docs/humans/principles/bootstrapping-principle.md
domain: engineering
views: []
---

## Why

gemify 파이프라인은 현재 `inbox/ → drafts/ → library/`까지만 지원한다.
하지만 실제 작업 중에는 **인간 작업자를 위한 기준 문서**가 필요한 순간이 있다:

- **Principle**: 작업의 근본 원칙 (예: 계단식 부트스트래핑 원칙)
- **Decision**: 특정 상황에서의 의사결정 기록 (ADR 스타일)
- **Policy**: 반복적으로 적용할 정책/규칙

이런 문서들은 `library/`의 일반 지식과 성격이 다르다:
- library: 도메인별 지식 (what I know)
- docs/humans: 행동 지침 (how I should act)

현재는 수동으로 `docs/humans/`에 작성하고 있으나 (예: bootstrapping-principle.md),
gemify 파이프라인에 통합하면 **대화 맥락에서 인사이트를 추출**하여 구조화된 문서로 만들 수 있다.

## What

### 1. 새 명령어 3개

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/gemify:human-principle` | 작업 원칙 문서 생성 | `docs/humans/principles/` |
| `/gemify:human-decision` | 의사결정 기록 생성 | `docs/humans/decisions/` |
| `/gemify:human-policy` | 정책 문서 생성 | `docs/humans/policies/` |

### 2. 흐름

```
사용자: "이거 원칙으로 정리해줘" (또는 human-principle 호출)
           │
           ▼
    ┌─────────────────┐
    │ library 안착 확인 │
    └────────┬────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
 안착됨            미안착
    │                 │
    ▼                 ▼
human-* 진행    "/gemify:library 먼저
                 실행하시겠어요?"
```

### 3. 각 타입별 템플릿 연동

**principle** (`docs/humans/principles/_template.md` 기반):
```yaml
---
id: principle-{seq}-{slug}
created: {ISO8601}
status: active
---

## Principle
{원칙 이름}

## Why
{이 원칙이 중요한 이유}

## How
{이 원칙을 적용하는 방법}

## Examples
{구체적 적용 사례}
```

**decision** (`docs/humans/decisions/_template.md` 기반):
```yaml
---
id: decision-{seq}-{slug}
created: {ISO8601}
status: {proposed|accepted|deprecated|superseded}
superseded_by: null
---

## Title
{결정 제목}

## Context
{결정이 필요한 상황, 배경}

## Options Considered
1. **Option A**: ...
2. **Option B**: ...

## Decision
{선택한 옵션과 이유}

## Consequences
{예상되는 결과, 영향}
```

**policy** (`docs/humans/policies/_template.md` 기반):
```yaml
---
id: policy-{seq}-{slug}
created: {ISO8601}
updated: {ISO8601}
status: {active|deprecated}
---

## Policy
{정책 이름}

## Scope
{적용 범위}

## Rules
1. {규칙 1}
2. {규칙 2}

## Exceptions
{예외 사항}

## Review Date
{검토 예정일}
```

### 4. 소크라테스식 질문

각 타입별로 다른 질문:

**principle**:
- "이 원칙의 핵심이 뭐야?"
- "왜 이게 원칙이어야 해?"
- "어떻게 적용해?"
- "구체적인 사례가 있어?"

**decision**:
- "무슨 결정을 해야 해?"
- "어떤 옵션들이 있어?"
- "왜 이걸 선택했어?"
- "결과가 어떻게 될 것 같아?"

**policy**:
- "이 정책이 적용되는 범위는?"
- "구체적인 규칙들은?"
- "예외 사항이 있어?"

### 5. seq 자동 부여

기존 파일에서 가장 높은 seq를 찾아 +1:
```bash
# 예: principle-001, principle-002 → 다음은 principle-003
```

## Scope

**포함**:
- `/gemify:human-principle` 명령어 및 스킬
- `/gemify:human-decision` 명령어 및 스킬
- `/gemify:human-policy` 명령어 및 스킬
- library 안착 여부 확인 로직
- 각 타입별 소크라테스식 질문
- seq 자동 부여 로직
- `docs/humans/` 디렉토리 자동 생성 (없을 경우)

**제외**:
- 기존 `/gemify:library` 수정 (별도 명령어로 분리)
- `docs/humans/` 템플릿 파일 수정
- setup 명령어에 docs/humans 구조 추가 (별도 개선 사항)
