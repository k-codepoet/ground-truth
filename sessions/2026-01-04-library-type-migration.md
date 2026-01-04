---
title: "Library Type 기반 마이그레이션 및 AI Company 정리"
date: 2026-01-04
duration: ~2h
---

# 세션 리포트: Library Type 기반 마이그레이션

## Summary

Library 구조를 6개 domain 기반에서 6개 Type 기반으로 전면 재구성. docs/humans 폴더를 library로 통합하고, AI Company 비전 문서를 정리하여 view로 구성.

## 주요 작업

### 1. Library 마이그레이션 (38개 파일)

**Before**: `library/{domain}/` (ai-automation, engineering, operations, growth, business, product)

**After**: `library/{type}/` (principles, decisions, insights, how-tos, specs, workflows)

| Type | 파일 수 | 설명 |
|------|---------|------|
| principles | 3 | 근본 원칙 |
| decisions | 4 | 의사결정 기록 |
| insights | 3 | 학습/발견 |
| how-tos | 4 | 절차/방법 |
| specs | 23 | 스펙/정의 |
| workflows | 3 | 워크플로우 |

**Frontmatter 변경**: `domain: X` → `type: X` + `origin: Y`

### 2. docs/humans 통합 및 삭제

- claude-code 가이드 8개 → `library/how-tos/claude-code-ecosystem-guide.md`로 통합
- brainstorm 문서 5개 → 구 기획문서라 삭제
- principles 중복 → 삭제
- **docs 폴더 전체 삭제**

### 3. AI Company 비전 정리

- `library/specs/ai-company-automation-roadmap.md` 생성 (Stage 0→3 로드맵)
- `views/by-subject/ai-company.md` 생성

## Outputs

### 신규 생성
- `library/principles/` 3개
- `library/decisions/` 4개
- `library/insights/` 3개
- `library/how-tos/` 4개 (+1 claude-code-ecosystem-guide)
- `library/specs/` 23개 (+1 ai-company-automation-roadmap)
- `library/workflows/` 3개
- `views/by-subject/ai-company.md`

### 수정
- `views/by-subject/*.md` 6개 (sources 경로)
- `CLAUDE.md` (Type 분류 설명)
- `drafts/library-migration-plan.md` (status: set)

### 삭제
- `library_legacy/` 전체
- `docs/` 전체

## Next Actions

- [ ] Namify 플러그인 구현
- [ ] Craftify 플러그인 구현
- [ ] Terrafy 플러그인 구현
- [ ] Stage 2 전환 준비 (API 연동)
