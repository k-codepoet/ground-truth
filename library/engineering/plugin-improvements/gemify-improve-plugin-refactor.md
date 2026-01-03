---
target_plugin: gemify
improvement_type: refactor
priority: high
problem: "gemify:improve-plugin이 직접 코드 수정까지 하고 있어 관심사가 혼재됨"
solution: "개선 계획 문서 생성만 담당하도록 역할 축소, 실행은 forgeify로 위임"
requirements:
  - improve-plugin 스킬을 문서 생성 전용으로 변경
  - 출력 위치를 library/engineering/plugin-improvements/로 고정
  - 개선 문서 스키마(frontmatter + body) 템플릿 사용
references: []
domain: engineering
views: []
---

## Why

단방향 흐름 구축: ground-truth(지식) → forgeify(실행). gemify는 지식 생산에만 집중.

## What

- improve-plugin 스킬 역할 변경: 코드 수정 → 문서 생성
- 프로토콜 스키마 적용 (target_plugin, improvement_type, problem, solution, requirements)
- library/engineering/plugin-improvements/에 저장

## Scope

포함:
- improve-plugin 스킬 수정
- 개선 문서 템플릿

제외:
- 실제 플러그인 코드 수정 (forgeify로 이관)
