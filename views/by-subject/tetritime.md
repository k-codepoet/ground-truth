---
title: "Tetritime View"
subject: tetritime
artifact: "/home/choigawoon/k-codepoet/my-domains/products/tetritime"
domains: [product]
created: "2026-01-04"
updated: "2026-01-04"
revision: 1
sources:
  - drafts/yunseul-schedule-build-plan.md
  - inbox/materials/2026-01-03-elementary-schedule-project.md
  - inbox/thoughts/2026-01-03-yunseul-schedule-build-plan.md
history:
  - rev: 1
    date: 2026-01-04
    summary: "초기 생성 - 프로젝트 시작점 정의"
---

# Tetritime View

> "시간표를 테트리스처럼 맞춰요"

## 문제

```
맞벌이 가정의 케어 공백
────────────────────────────

[학교 수업]     [   ?   ]     [부모 퇴근]
08:50          12:40~13:40    18:00+

              ↑ 이 빈 공간을 채워야 함
```

**핵심 문제**:
- 초등학교 1학년은 12:40~13:40에 하교
- 부모 퇴근은 18:00 이후
- **4~5시간의 케어 공백** 발생

**복잡성**:
- 방과후 프로그램 40개 (1학년 신청 가능)
- 요일별 하교 시간 상이 (월/금 vs 화/수/목)
- 프로그램별 시간대 상이
- **시간 충돌 감지** 필요

## 해결책

**Tetritime** = 방과후 시간표 테트리스

```
┌─────────────────────────────────────┐
│  주간 시간표 (테트리스 UI)           │
├─────────────────────────────────────┤
│  월    화    수    목    금         │
│ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐     │
│ │축구│ │   │ │로봇│ │   │ │미술│     │
│ └───┘ │바둑│ └───┘ │바둑│ └───┘     │
│       └───┘       └───┘           │
│ [충돌 감지] [카테고리 필터]         │
└─────────────────────────────────────┘
```

**핵심 기능**:
- 방과후 프로그램 클릭 선택
- **시간 충돌 자동 감지** (테트리스의 핵심!)
- 카테고리 필터 (예술, 체육, 언어...)
- 선택 프로그램 요약

## 여정

```
[Phase 0] ─────────────────────────────────
  프로토타입 완성 (Cursor AI 협업)
  - React + TailwindCSS
  - weekly-timetable-complete.jsx

[Phase 1] ───────────── (현재 위치) ──────
  환경 셋업 (Craftify 위임)
  - turborepo + ssr boilerplate
  - git init → Cloudflare Pages 연결

[Phase 2] ─────────────────────────────────
  프로토타입 마이그레이션
  - apps/web/src/ 이동
  - 빌드/배포 확인

[Phase 3] ─────────────────────────────────
  기능 확장
  - localStorage 저장
  - PDF/이미지 내보내기
  - 드래그 앤 드롭
  - 비용 계산기
```

## 현재 상태

| 항목 | 상태 |
|------|------|
| 프로토타입 | 완료 |
| 제품명 | Tetritime 확정 |
| 기술스택 | React + TailwindCSS + SSR |
| 배포 환경 | Cloudflare Pages |
| 다음 액션 | Craftify로 환경 셋업 위임 |

## 관련 문서

- `drafts/yunseul-schedule-build-plan.md` - Craftify 위임 작업 문서
- `inbox/materials/2026-01-03-elementary-schedule-project.md` - 프로토타입 요약
- `inbox/thoughts/2026-01-03-yunseul-schedule-build-plan.md` - 빌드 계획 원석
