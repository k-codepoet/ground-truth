---
title: gemify improve-plugin 커맨드/스킬 위치 이동 및 forgeify 연동 계획
date: 2026-01-03
status: used
used_in: drafts/gemify-forgeify-unidirectional-flow.md
references: []
---

## 목적

의식의 흐름을 단방향으로 조정: ground-truth → 제품

## 핵심 아이디어

1. gemify에서 plugin 개선에 특화된 문서 작성 기능
2. forgeify가 그 문서를 참조해서 플러그인 개선
3. 관심사 분리: 원천은 Ground-truth, 실행은 forgeify

## 작업 흐름

1. gemify:inbox → draft → library까지 개선 계획 문서 작성
2. forgeify가 library 문서를 참조해서 작업하는 기능 추가
3. forgeify로 스스로를 개선 (재귀적 부트스트래핑)

## 재귀 해결 순서

1. 계획 문서를 모두 작성한다 (ground-truth에서)
2. forgeify 플러그인이 그런 기능을 할 수 있게 개선한다
3. 이후 forgeify plugin을 이용해 스스로를 개선하도록 시킨다

## 구체적 변경사항

- gemify:improve-plugin → plugin 개선 계획 문서 생성 전문화
- forgeify → ground-truth/library 참조 기능 추가
- 단방향 파이프라인: 지식(ground-truth) → 실행(forgeify)
