---
title: "AI Company 자동화 로드맵"
type: spec
origin: original
views: [gemify, ai-company]
---

## Context

1인 AI Company의 핵심 목표: **"말하면 제품이 만들어지고, 개선되고, 확장된다"**

-ify Trilogy (Gemify, Terrafy, Craftify)가 이 비전을 실현하는 도구이며, 자동화 수준을 단계적으로 높여가는 로드맵.

## Content

### 자동화 단계 (Stage 0 → 3)

| Stage | 이름 | 설명 | AI 역할 | 사람 역할 |
|-------|------|------|---------|----------|
| 0 | 완전 수동 | 모든 작업을 직접 수행 | 없음 | 100% |
| 1 | AI 보조 | Claude Code + HITL | 초안/제안 | 검토/승인 |
| 2 | AI 주도 | API 연동, 자동 트리거 | 실행 주도 | 예외 처리 |
| 3 | AI 자율 | 자체 판단으로 개선/확장 | 자율 운영 | 방향 설정 |

### 현재 위치

```
Stage 0: 완전 수동      ✅ 완료
Stage 1: AI 보조        ← 현재 (Claude Code + Plugins)
Stage 2: AI 주도        예정
Stage 3: AI 자율        예정
```

### Stage 1 상세 (현재)

**핵심 도구**: Claude Code + -ify Plugins

```
[사람]              [Claude Code]           [결과물]
  │                      │                      │
  말한다 ───────────────→ 이해/실행 ───────────→ 코드/문서
  │                      │                      │
  검토한다 ←──────────── 제안한다               │
  │                      │                      │
  승인한다 ───────────────────────────────────→ 완료
```

**분류 신뢰도 시스템** (HITL 판단 기준):
- 높음 (80%+): 자동 진행
- 중간 (50-80%): 확인 요청
- 낮음 (<50%): 수동 분류

**Stage 1 성공 기준**:
- 분류 정확도 80% 이상
- HITL 개입 비율 30% 이하
- 말 → 동작하는 결과물 흐름 확립

### Stage 2 전환 조건

- Claude API 직접 연동 (Code → API)
- 이벤트 기반 자동 트리거
- 모니터링 + 알림 시스템
- 사람은 예외 처리만

### Stage 3 비전

- AI가 스스로 개선점 발견
- 새 기능/제품 제안
- 자동 배포 및 운영
- 사람은 방향만 설정

### -ify Trilogy의 역할

| Stage | Gemify | Terrafy | Craftify |
|-------|--------|---------|----------|
| 1 | 지식 정리 보조 | 인프라 설정 가이드 | 코드 생성 보조 |
| 2 | 자동 지식 분류 | 자동 인프라 프로비저닝 | 자동 코드 생성/배포 |
| 3 | 지식 자율 확장 | 인프라 자율 최적화 | 제품 자율 개선 |

## Connections

- [Knowledge Pipeline 비전](./knowledge-pipeline-vision.md) - Gemify 파이프라인 상세
- [-ify Trilogy 전략](../decisions/ify-trilogy-strategy.md) - WHAT/WHERE/HOW 역할 분담
- [Bootstrapping 원칙](../principles/bootstrapping-principle.md) - 단계적 발전 철학
