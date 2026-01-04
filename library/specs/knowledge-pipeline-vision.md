---
title: "Knowledge Pipeline 비전과 구조"
type: spec
origin: original
views: [gemify]
---

## Context

1인 AI Company를 위한 지식 관리 시스템. 머릿속 암묵지를 구조화된 지식으로 변환하는 파이프라인이 필요했고, gemify로 구현됨.

## Content

### 한 문장 정의

**"말하는 대로 지식이 정리되는 시스템"**

### 핵심 파이프라인

```
/gemify:inbox → /gemify:draft → /gemify:library
    inbox/         drafts/         library/
   (원석)         (다듬기)          (보석)
```

### 3단계 흐름

| 단계 | 폴더 | 명령어 | 설명 |
|------|------|--------|------|
| 1 | inbox/ | /gemify:inbox | 생각 포착, 외부 재료 수집 |
| 2 | drafts/ | /gemify:draft | facet/polish로 다듬기 |
| 3 | library/ | /gemify:library | type별 분류 저장 |

### 자동화 단계

```
Stage 0: 완전 수동      ← 현재 완료
Stage 1: AI 보조        ← 현재 진행 중
Stage 2: AI 주도        (예정)
Stage 3: AI 자율        (예정)
```

## Connections

- [facet/polish 모드](../how-tos/draft-facet-polish-mode.md) - /gemify:draft 대화 모드
- [실행 우선 원칙](../principles/execution-first-principle.md) - 완벽보다 동작
