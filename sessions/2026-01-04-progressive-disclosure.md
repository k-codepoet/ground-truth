---
title: CLAUDE.md progressive disclosure 적용
date: 2026-01-04
slug: "progressive-disclosure"
---

## Summary

CLAUDE.md에서 상세 규칙들을 제거하고 스킬로 위임했다. 스킬이 호출되지 않고 Claude가 직접 동작하는 문제를 해결. 작업 중 6대 domain이 library 분류 기준으로 맞지 않을 수 있다는 문제 발견하여 sidebar로 빼둠.

## Outputs

| 파일 | 설명 |
|------|------|
| `CLAUDE.md` | progressive disclosure 적용 (상세 제거) |
| `library/engineering/claude-md-progressive-disclosure.md` | retro로 의사결정 기록 |
| `inbox/materials/2026-01-04-six-domain-mismatch.md` | 6대 domain 문제 맥락 |
| `inbox/thoughts/2026-01-04-domain-belongs-to-views.md` | domain은 views 기준 가설 |

## Stashed for Next

- `inbox/thoughts/2026-01-04-domain-belongs-to-views.md` - 6대 domain이 library가 아니라 views 기준일 수 있다는 가설. 검증 및 마이그레이션 방향 고민 필요.

## Next Actions

1. 6대 domain 역할 재정의 (`/gemify:draft`로 이어가기)
2. library 분류 기준 재검토
