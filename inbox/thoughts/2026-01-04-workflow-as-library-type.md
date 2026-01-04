---
title: "Workflow를 library type으로 추가해야 한다"
date: 2026-01-04
status: raw
used_in: null
references:
  - inbox/materials/2026-01-04-workflow-type-discovery.md
---

# Workflow를 library type으로 추가해야 한다

## 핵심 인사이트

library의 Type에 **workflow**가 필요함.

```
library/
├── principles/    # 근본 원칙, 철학
├── decisions/     # 의사결정 기록 (ADR)
├── insights/      # 발견, 깨달음
├── how-tos/       # 방법론, 절차
├── specs/         # 명세, 스펙
└── workflows/     # input→output 패턴이 명확한 작업 흐름 ← NEW
```

## Workflow의 특징

- input → output 패턴이 명확
- 반복하다가 패턴을 발견해서 정형화됨
- 플러그인 간 연계를 정의함

## 현재 workflow 예시

1. **improve-plugin**: gemify → forgeify
2. **poc-development** (예정): gemify → craftify

## how-to와의 차이

- **how-to**: 단일 작업의 방법론/절차
- **workflow**: 여러 단계/도구를 연결한 파이프라인

## 다음 단계

- library Type에 workflows/ 추가
- gemify-library-type-classification.md 개선 문서 업데이트
