---
title: "Library 분류 체계 리팩토링 세션"
date: 2026-01-04
duration: ~1.5h
---

# Library 분류 체계 리팩토링 세션

## Summary

6대 domain 기반 library 분류를 Type 기반으로 전면 리팩토링.

**핵심 결정:**
- library = 재료의 본질(Type)로 분류
- 6대 domain = views의 lens로 역할 이동
- 관심사 분리: 재료(what) vs 관점(how to use)

**Type 분류 (6개):**
- principles, decisions, insights, how-tos, specs, workflows

**Origin 분류 (3개):**
- original, digested, derived

## Outputs

### 생성된 파일
| 파일 | 설명 |
|------|------|
| `drafts/domain-classification-rethink.md` | 분류 체계 결정 문서 (status: set) |
| `drafts/library-migration-plan.md` | 마이그레이션 계획 (status: set) |
| `library/engineering/plugin-improvements/gemify-library-type-classification.md` | gemify 개선 문서 |

### 수정된 파일
- gemify plugin: SKILL.md, library-format.md, assets 폴더 구조
- library: 38개 파일 마이그레이션 (폴더 이동 + frontmatter 수정)
- CLAUDE.md: library Type 분류 반영
- views: 6개 파일 경로 수정

## Stashed for Next

| inbox 파일 | 내용 | 다음 액션 |
|------------|------|----------|
| `2026-01-04-views-expansion-need.md` | views 확장 필요성 (발표/교육 등) | /gemify:draft |
| `2026-01-04-self-improvement-subagent-idea.md` | 자가 발전 subagent 아이디어 | /gemify:draft |

## Next Actions

1. **Views 확장 설계** (별도 draft)
   - by-subject 외 다른 view 타입 정의 (발표, 교육, 세미나)
   - 각 타입별 적합한 lens/기준 설계

2. **자가 발전 subagent 설계**
   - consistency-checker / ripple-detector
   - 변경 감지 → 영향 분석 → 역제안 → 컨펌 후 실행
