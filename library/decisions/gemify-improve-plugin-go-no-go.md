---
title: improve-plugin Go/No-Go 체크 도입
type: decision
origin: original
target_plugin: gemify
improvement_type: feature
priority: high
problem: "improve-plugin 시작 시 '이게 지금 필요한가?' 점검이 없어 미래 대비용 작업에 시간 낭비"
solution: "Go/No-Go 체크리스트를 improve-plugin 스킬에 추가하여 작업 시작 전 검증"
requirements:
  - improve-plugin SKILL.md에 Go/No-Go 체크 섹션 추가
  - 깊어질 것 같은 작업 시작 전 체크리스트 실행
  - "예" 판정 시 즉시 중단 권고
  - library/principles/go-no-go.md 참조 (progressive disclosure)
references:
  - library/principles/go-no-go.md
  - docs/humans/principles/go-no-go.md
views: []
---

## Why

플러그인 개선 작업 중 "미래 대비" 성격의 작업에 시간을 낭비하는 경우가 발생.
예: 플러그인 버전/종속성 관리 체계 조사 → 실제 문제가 아닌 미래 걱정이었음.

핵심 원칙: **기록은 자유롭게, 실행은 신중하게**

## What

improve-plugin 스킬 시작 시 Go/No-Go 체크 추가:

```
□ 실제 문제가 발생했는가? (미래 걱정 아닌지)
□ 현재 사용자가 나만인가?
□ 문제가 발생하면 그때 해도 늦지 않은가?
```

판정:
- 3개 모두 "아니오" → Go (진행)
- 하나라도 "예" → No-Go (즉시 중단, 우선순위 재점검)

적용 조건:
- 금방 될 일 (5분 내) → 체크 불필요
- 깊어질 것 같은 작업 → 체크 필요

## Scope

포함:
- gemify/skills/improve-plugin/SKILL.md 수정
- Go/No-Go 체크 섹션 추가
- library/principles/go-no-go.md 참조 링크

제외:
- 다른 스킬에 적용 (필요시 별도 개선 문서)
- 체크리스트 자동화 (수동 판단으로 충분)
