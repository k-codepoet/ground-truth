---
title: "Views 타입 시스템 설계"
date: 2026-01-04
type: session-report
---

# Views 타입 시스템 설계

## Summary

library → views 파이프라인에서 views의 역할을 확장. "library = 모델, views = 렌더링 레이어" 개념을 정립하고, 5가지 view 타입(subject, talk, curriculum, portfolio, essay)을 설계함.

## Outputs

### 생성된 파일

| 파일 | 설명 |
|------|------|
| `library/specs/gemify-views-type-system.md` | views 타입 시스템 spec |
| `library/specs/gemify-view-skill-expansion.md` | /gemify:view 스킬 확장 개선 문서 |
| `views/by-subject/_template.md` | by-subject 템플릿 |
| `views/by-talk/_template.md` | by-talk 템플릿 |
| `views/by-curriculum/_template.md` | by-curriculum 템플릿 |
| `views/by-portfolio/_template.md` | by-portfolio 템플릿 |
| `views/by-essay/_template.md` | by-essay 템플릿 |

### 수정된 파일

| 파일 | 변경 내용 |
|------|----------|
| `CLAUDE.md` | Views 타입 시스템 섹션 추가, 5가지 타입별 frontmatter 정의 |
| `inbox/thoughts/2026-01-04-views-expansion-need.md` | status: processed, used_in 연결 |
| `inbox/materials/2026-01-04-views-expansion-discussion.md` | status: processed, used_in 연결 |

### 외부 반영 (다른 스레드)

| 파일 | 설명 |
|------|------|
| `plugins/gemify/skills/view/SKILL.md` | 5가지 타입 지원으로 확장 |

## Key Decisions

1. **library = 모델, views = 렌더링**: 지식의 원자 단위(library)와 서사가 있는 스토리텔링(views) 분리
2. **5가지 view 타입**: subject, talk, curriculum, portfolio, essay
3. **타입별 렌즈**: 각 타입마다 고유한 판단 기준(렌즈) 적용
4. **6대 domain은 by-subject 전용**: library 분류에서 제거, views/by-subject의 렌즈로 이동

## Stashed for Next

(없음)

## Next Actions

- [ ] 실제 view 생성 테스트 (`/gemify:view talk {title}` 등)
- [ ] gemify assets 폴더에도 새 타입 템플릿 반영
