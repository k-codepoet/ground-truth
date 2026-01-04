---
title: "외부 리서치 → 작업 환경 연결 파이프라인"
type: workflow
origin: original
created: 2026-01-02
created_via: retro
views: [gemify]
sources:
  - inbox/thoughts/2025-12-31-import-command-needed.md
---

# 외부 리서치 → 작업 환경 연결 파이프라인

## 배경

문제 상황 리서치와 자료 수집에는 검색 기능이 필수. Perplexity가 검색 퀄리티가 좋아서 거기서 작업 후 Claude Code로 가져오는 패턴이 생김.

## 해결: /gemify:import

외부에서 다듬은 재료를 `inbox/materials/`로 가져오는 커맨드.

### inbox vs import 분리 이유

| 커맨드 | 시작점 | 상황 |
|--------|--------|------|
| `/gemify:inbox` | 즉흥적 | 생각나는 거 바로, 준비된 재료 있을 때 |
| `/gemify:import` | 외부 작업물 | 다른 공간에서 작업해온 것 가져올 때 |

## 교훈

1. **작업 환경 일원화가 목표** - 당분간은 익숙한 도구로 우회하되, 궁극적으로는 하나로
2. **단계적 축적이 필요** - 학습 → 숙달 → 하위 레이어 → 상위 레이어 실행
3. **선언형은 기반이 있어야** - 밑에 여러 시스템이 쌓여야 위에서 선언적으로 동작 가능
4. **일단 실행해야 문제를 발견** - 모든 상황을 예견하려다 멈추는 건 BFS/DFS 동시 탐색하며 한 발짝도 못 나가는 것과 같음
