---
title: forgeify 커맨드-스킬 위임 리팩토링
type: spec
origin: derived
target_plugin: forgeify
improvement_type: refactor
priority: high
problem: "validate, create, compose, update 커맨드에 로직이 직접 구현되어 있어 AI agent가 자동 위임하기 어려움"
solution: "각 커맨드에 대응하는 스킬을 생성하고, 커맨드는 진입점 역할만 하도록 리팩토링"
requirements:
  - skills/validate/SKILL.md 생성 - 검증 로직 이동
  - skills/create/SKILL.md 생성 - 플러그인 생성 로직 이동
  - skills/compose/SKILL.md 생성 - 플러그인 조립 로직 이동
  - skills/update/SKILL.md 생성 - 업데이트 로직 이동
  - 각 command는 스킬 참조 형태로 간소화
references: []
views: []
---

## Why

forgeify 플러그인 검수 중 발견된 문제:

1. **command-guide에서 권장하는 "스킬 참조 패턴" 미적용**
   - command-guide/SKILL.md:79-109에 패턴이 명시되어 있으나, forgeify 자체는 이를 따르지 않음
   - "의사가 자기 처방은 안 따르는" 상황

2. **AI agent 자동 위임 불가**
   - 스킬은 Claude가 컨텍스트를 보고 자동 로드 가능
   - 커맨드는 사용자가 명시적으로 `/command` 호출 필요
   - 현재 로직이 커맨드에 있어서 AI가 적절한 시점에 자동 활성화 불가

3. **Progressive Disclosure 원칙 위반**
   - 커맨드 파일에 상세 워크플로우가 모두 포함
   - guide 스킬들과 내용 중복 발생

## What

### 점진적 적용 순서

**Phase 1: validate** (가장 명확한 케이스)
```
현재:
commands/validate.md (로직 직접 구현)

변경 후:
skills/validate/SKILL.md (검증 로직)
commands/validate.md (스킬 참조만)
```

**Phase 2: create**
```
현재:
commands/create.md (생성 로직 + 예시 직접 포함)

변경 후:
skills/create/SKILL.md (생성 로직, guide 스킬들 참조)
commands/create.md (스킬 참조만)
```

**Phase 3: update**
```
현재:
commands/update.md (업데이트 로직 직접 구현)

변경 후:
skills/update/SKILL.md (업데이트 로직)
commands/update.md (스킬 참조만)
```

**Phase 4: compose**
```
현재:
commands/compose.md (조립 로직 직접 구현)

변경 후:
skills/compose/SKILL.md (조립 로직)
commands/compose.md (스킬 참조만)
```

### 커맨드 간소화 예시

변경 전 (validate.md):
```markdown
---
description: 플러그인이 가이드라인을 준수하는지 검증...
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
---

# Plugin Validation & Refactoring

[60줄의 상세 로직...]
```

변경 후 (validate.md):
```markdown
---
description: 플러그인이 가이드라인을 준수하는지 검증...
---

# /forgeify:validate

validate 스킬을 사용하여 플러그인을 검증합니다.

## 사용법

/forgeify:validate                     # 현재 디렉토리
/forgeify:validate ./plugins/my-plugin # 특정 플러그인
```

### 스킬 작성 시 주의사항

- 기존 guide 스킬들(plugin-guide, command-guide 등)을 **참조**
- 검증 기준은 guide 스킬이 source of truth
- 스킬 description에 자동 활성화 트리거 명시
  - 예: "플러그인 검증", "validate", "규격 확인" 등

## Scope

포함:
- validate, create, update, compose 4개 커맨드
- 각각에 대응하는 스킬 생성
- 커맨드 파일 간소화

제외:
- help, howto 커맨드 (이미 적절한 구조)
- improve-plugin (이미 스킬 참조 패턴 적용됨)
- guide 스킬들 내용 수정 (별도 이슈)
