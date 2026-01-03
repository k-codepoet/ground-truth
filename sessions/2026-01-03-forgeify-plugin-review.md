---
title: Forgeify 플러그인 검수
date: 2026-01-03
type: session-report
---

# Forgeify 플러그인 검수

## Summary

Forgeify 플러그인이 대원칙(progressive disclosure, single source of truth, command→skill 위임)을 따르는지 6가지 포인트로 검수.

주요 발견:
- Command→Skill 위임 패턴이 validate, create, compose, update에 미적용
- gemify→forgeify 단방향 흐름 원칙을 Claude가 자연스럽게 따르지 않는 문제 인식

## Outputs

### inbox/thoughts/
- `2026-01-03-gemify-forgeify-flow-enforcement.md`
  - Claude가 플러그인을 직접 수정하려는 패턴 반복
  - gemify→forgeify 흐름 강제 필요성

### library/engineering/plugin-improvements/
- `forgeify-command-skill-delegation.md`
  - Command→Skill 위임 패턴 적용 리팩토링
  - Phase 1~4: validate → create → update → compose 순서
  - priority: high

## Stashed for Next

- 중복 내용 정리 (Skills vs Commands 비교표, CLAUDE_PLUGIN_ROOT 설명) - 사소해서 보류

## Next Actions

1. `/forgeify:improve-plugin` 으로 `forgeify-command-skill-delegation.md` 실행
2. `gemify-forgeify-flow-enforcement` 원석을 draft로 발전시켜 원칙 문서화 검토
