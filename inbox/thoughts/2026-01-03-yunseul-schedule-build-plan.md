---
title: 윤슬이시간표 앱 빌드/배포 환경 구축 계획
date: 2026-01-03
status: raw
used_in: null
deadline: 2026-01-31
references:
  - inbox/materials/2026-01-03-elementary-schedule-project.md
---

# 윤슬이시간표 앱 빌드/배포 환경 구축 계획

## 배경
- 초등학교 입학하는 딸아이 시간표 앱
- 맞벌이 가정의 오후 케어 스케줄링 문제 해결
- 현재 React+TailwindCSS 프로토타입 완성 상태

## 결정사항
- 제품별 독립 turborepo 구조로 진행
- GitOps 고려 (ArgoCD/Flux 친화적 구조)
- 통합 monorepo는 오버엔지니어링 → 나중에 공유 코드 생기면 그때 결정

## 사전 작업 필요
- 작업환경 셋업 플러그인 먼저 만들기
- 효율적 작업 도구들 마련 후 시작
- 플러그인 없이는 시작하지 않음

## 예상 구조
```
yunseul-schedule/
├── apps/web/          # React 앱
├── packages/ui/       # 공유 컴포넌트 (나중에)
├── infra/k8s/         # GitOps manifests
├── turbo.json
└── package.json
```
