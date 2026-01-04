---
title: "Claude Code 플러그인 hooks 디버깅 세션"
date: 2026-01-04
status: completed
---

## Summary

Claude Code 플러그인 hooks가 동작하지 않는 문제를 조사하고, forgeify의 hooks-guide 및 validate 스킬을 보강했다. 실제 적용 과정에서 Claude Code 자체 버그(`type: "prompt"` silently ignore)를 발견하여 나머지 작업은 보류했다.

## Outputs

### 생성된 파일
- `library/how-tos/plugin-improvements/forgeify-hooks-guide-enhancement.md` - 개선 요청 문서

### 수정된 파일 (다른 스레드에서)
- `forgeify/skills/hook-guide/SKILL.md` - 올바른 hooks.json 포맷, Known Issues 섹션 추가
- `forgeify/skills/validate/SKILL.md` - hooks.json 검증 로직 추가

## Stashed for Next

| 파일 | 내용 |
|------|------|
| `inbox/materials/2026-01-04-claude-plugin-hooks-debug.md` | perplexity와 조사한 hooks 검증 요약 |
| `inbox/thoughts/2026-01-04-plugin-hooks-not-working.md` | 원인 후보 정리 |
| `inbox/materials/2026-01-04-hooks-validation-need.md` | 발견된 이슈들 (Issue #13155 등) |
| `inbox/thoughts/2026-01-04-hooks-validation-plugin-idea.md` | hooks-validator 플러그인 아이디어 |

## Next Actions

- [ ] GitHub Issue #13155 해결 모니터링
- [ ] 해결 후 gemify/craftify 등 나머지 플러그인 hooks 적용
- [ ] hooks-validator 플러그인 생성 검토
