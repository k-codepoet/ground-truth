---
date: "2026-01-04"
topic: gemify:draft 히스토리 문제 해결
status: completed
---

## Summary

gemify:draft 대화 종료 시 히스토리가 남지 않는 문제를 분석하고 해결함.

- **문제**: pivot 시에만 스냅샷 생성 → 대부분의 대화가 기록 없이 끝남
- **해결책**: prompt 타입 hooks (Stop 이벤트)로 Claude가 컨텍스트 기반 판단
- **결과**: gemify 플러그인 v1.12.2에 반영 완료

## Outputs

### ground-truth (개선 문서)

| 파일 | 설명 |
|------|------|
| `inbox/thoughts/2026-01-04-gemify-draft-history-fix.md` | 초기 아이디어 (status: used) |
| `library/engineering/plugin-improvements/gemify-draft-history-hooks.md` | 개선 문서 |

### gemify 플러그인 (실제 수정)

| 파일 | 설명 |
|------|------|
| `.claude-plugin/hooks.json` | prompt 타입 Stop 훅 추가 |
| `.claude-plugin/plugin.json` | 버전 1.12.2 |
| `skills/draft/SKILL.md` | 히스토리 저장 기준 명시, polish → library 안내 |

## Stashed for Next

없음

## Next Actions

- [x] 완료됨
