---
date: "2026-01-04"
topic: gemify:draft 히스토리 문제 해결
status: completed
---

## Summary

gemify:draft 대화 종료 시 히스토리가 남지 않는 문제를 분석하고 개선 문서를 작성함.

- **문제**: pivot 시에만 스냅샷 생성 → 대부분의 대화가 기록 없이 끝남
- **해결책**: prompt 타입 hooks (Stop 이벤트)로 Claude가 컨텍스트 기반 판단

## Outputs

| 파일 | 설명 |
|------|------|
| `inbox/thoughts/2026-01-04-gemify-draft-history-fix.md` | 초기 아이디어 (status: used) |
| `library/engineering/plugin-improvements/gemify-draft-history-hooks.md` | 개선 문서 |

## Stashed for Next

없음

## Next Actions

- [ ] `/forgeify:improve-plugin`으로 실제 플러그인 코드 수정 (gemify)
  - hooks.json 생성 (prompt 타입 Stop 훅)
  - skills/draft/SKILL.md 수정 (polish → library 안내)
