---
title: "Library 마이그레이션 작업 계획"
status: set
sources:
  - drafts/domain-classification-rethink.md
history:
  - date: 2026-01-04
    changes: 마이그레이션 완료 - 38개 파일을 Type 기반 구조로 재구성
---

# Library 마이그레이션 작업 계획

## 목표

기존 6대 domain 기반 library 구조를 Type 기반으로 마이그레이션.

## 변경 사항

### 폴더 구조
```
# Before
library/{domain}/{file}.md

# After
library/{type}s/{file}.md
```

### frontmatter
```yaml
# Before
domain: ai-automation
views: []

# After
type: principle|decision|insight|how-to|spec|workflow
origin: original|digested|derived
views: []
```

---

## 마이그레이션 대상 (38개)

### ai-automation/ (9개)
| 파일 | → Type | Origin |
|------|--------|--------|
| bootstrapping-principle.md | principles | original |
| execution-first-principle.md | principles | original |
| claude-code-env-context.md | insights | digested |
| forgify-plugin-review.md | insights | derived |
| gemify-1.5.0-workflow-extensions.md | specs | derived |
| gemify-tidy-skill.md | specs | derived |
| gemify-triage-skill.md | specs | derived |
| gemify-wrapup-skill.md | specs | derived |
| improve-plugin-workflow.md | workflows | original |

### engineering/ (5개)
| 파일 | → Type | Origin |
|------|--------|--------|
| ced-plugin-agents-marketplace-fix.md | specs | derived |
| claude-code-extension-fundamentals.md | insights | digested |
| claude-md-progressive-disclosure.md | how-tos | original |
| craftify-progressive-disclosure.md | how-tos | derived |
| external-standard-sync-strategy.md | decisions | original |

### engineering/plugin-improvements/ (13개)
| 파일 | → Type | Origin |
|------|--------|--------|
| forgeify-auto-sync-help-howto.md | specs | derived |
| forgeify-command-skill-delegation.md | specs | derived |
| forgeify-improve-command.md | specs | derived |
| gemify-add-tidy-skill.md | specs | derived |
| gemify-add-triage-skill.md | specs | derived |
| gemify-add-wrapup-skill.md | specs | derived |
| gemify-draft-history-hooks.md | specs | derived |
| gemify-forgeify-protocol.md | workflows | original |
| gemify-human-docs-feature.md | specs | derived |
| gemify-improve-plugin-go-no-go.md | decisions | original |
| gemify-improve-plugin-refactor.md | specs | derived |
| gemify-library-type-classification.md | specs | derived |
| gemify-rename-capture-pair-to-sidebar.md | specs | derived |

### operations/ (5개)
| 파일 | → Type | Origin |
|------|--------|--------|
| draft-facet-polish-mode.md | how-tos | original |
| external-research-pipeline.md | workflows | original |
| go-no-go.md | principles | original |
| ground-truth-protocol.md | specs | original |
| knowledge-pipeline-vision.md | specs | original |

### growth/ (1개)
| 파일 | → Type | Origin |
|------|--------|--------|
| gemify-branding-decision.md | decisions | original |

### product/ (5개)
| 파일 | → Type | Origin |
|------|--------|--------|
| craftify-plugin-design.md | specs | original |
| ify-trilogy-strategy.md | decisions | original |
| namify-plugin-spec.md | specs | original |
| session-report-viewer-spec.md | specs | original |
| terrafy-plugin-spec.md | specs | original |

---

## 작업 순서

1. [x] 새 폴더 생성 (`principles/`, `decisions/`, `insights/`, `how-tos/`, `specs/`, `workflows/`)
2. [x] 파일별 마이그레이션 (위 테이블 순서대로)
   - 파일 이동
   - frontmatter 수정 (domain → type + origin)
3. [x] 기존 domain 폴더 삭제
4. [x] CLAUDE.md 업데이트
5. [x] views 경로 수정 (6개 view 파일)

---

## 주의사항

- views 필드는 유지 (기존 연결 보존)
- plugin-improvements/ 하위 폴더 → specs/ 또는 workflows/로 flat하게 이동
- 마이그레이션 중 type/origin 판단이 애매하면 메모 남기고 나중에 재검토
