---
title: "Knowledge Pipeline 비전"
created: "2025-12-31"
updated: "2025-12-31 10:00"
turns: 1
revision: 1
status: set
sources:
  - inbox/thoughts/2025-12-31-knowledge-pipeline-vision.md
history:
  - rev: 1
    mode: polish
    date: 2025-12-31
    summary: "gemify 플러그인으로 구현 완료, library 정리"
    file: .history/knowledge-pipeline-vision/01-polish-2025-12-31.md
---

## Seed

1인 AI Company를 위한 Knowledge Management System. 머릿속 암묵지를 말로 꺼내면 AI가 자동으로 분류/구조화하고, 다양한 형태로 출력해주는 파이프라인.

---

## Sources

- inbox/thoughts/2025-12-31-knowledge-pipeline-vision.md

---

## Growth Log

### Session 1 (2025-12-31)

- 비전 문서 작성 → gemify 플러그인으로 구현
- inbox → drafts → library 파이프라인 확립
- /gemify:inbox, /gemify:draft, /gemify:library 명령어 완성

---

## Current State

**구현 완료된 것:**
- gemify 플러그인 (k-codepoet-plugins)
- 3단계 파이프라인: inbox → drafts → library
- facet/polish 모드
- 6대 domain 분류 체계

**핵심 흐름:**
```
/gemify:inbox → /gemify:draft → /gemify:library
    inbox/         drafts/         library/
```

---

## Open Questions

- [x] Stage 0 검증 완료
- [ ] Stage 1 (AI 보조) 고도화
