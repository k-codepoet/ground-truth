---
title: "gemify에 자가 발전 subagent 필요"
date: 2026-01-04
status: raw
used_in: null
references:
  - inbox/materials/2026-01-04-self-improvement-agent-need.md
---

# gemify에 자가 발전 subagent 필요

## 핵심 인사이트

현재는 사용자가 모든 연쇄 업데이트를 지시해야 함. 이걸 자동화하는 subagent가 필요.

## 아이디어: consistency-checker 또는 ripple-detector

**역할:**
1. 변경 감지 → 영향 범위 분석
2. 연쇄 업데이트 필요한 문서 목록 제시
3. 사용자 컨펌 → 일괄 업데이트

**예시 흐름:**
```
[사용자] draft 완성
[subagent] "이 변경으로 다음 문서도 업데이트 필요해 보여요:
  - library/engineering/plugin-improvements/gemify-*.md
  - CLAUDE.md (frontmatter 스키마)
  - ground-truth-protocol.md
  업데이트할까요?"
[사용자] "응"
[subagent] 일괄 업데이트 실행
```

## 자가 발전의 의미

- 내가 놓쳐도 시스템이 찾아냄
- 제안은 하되 실행은 컨펌 후 (HITL)
- 시간이 지날수록 더 똑똑해짐 (패턴 학습)

## 다음 단계

- subagent 설계 (gemify plugin에 추가)
- tidy/triage 스킬과 연계 가능성 검토
