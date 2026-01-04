---
title: "Session Report Viewer 종합 View"
subject: session-report-viewer
created: 2026-01-04
updated: 2026-01-04
artifact: null
artifact_type: webapp
sources:
  - library/product/session-report-viewer-spec.md
---

# Session Report Viewer 종합 View

## 구조 (도식)

```
┌─────────────────────────────────────────────────────────────────┐
│                   Session Report Viewer                          │
│      "gemify:wrapup 세션 리포트를 웹으로 조회"                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
           ┌──────────────┐    ┌──────────────┐
           │   입력 폼    │    │   뷰어 UI    │
           │ GitHub URL   │    │  타임라인    │
           └──────────────┘    └──────────────┘
                    │                   │
                    ▼                   ▼
           ┌──────────────┐    ┌──────────────┐
           │   인덱싱     │    │ 마스터-디테일 │
           │ sessions/    │    │   레이아웃   │
           └──────────────┘    └──────────────┘
```

## 플로우

```
[사용자 접근]
{host}/{user}/{repo}
       │
       ▼
┌──────────────────┐
│ 인덱싱 됨?       │
└──────────────────┘
       │
   No ─┼─ Yes
       │    │
       ▼    ▼
  ┌────────┐ ┌────────────────┐
  │인덱싱  │ │ 세션 리포트    │
  │요청    │ │ 타임라인 표시  │
  │페이지  │ │ (최신순)       │
  └────────┘ └────────────────┘
                    │
                    ▼ 클릭
           ┌────────────────┐
           │ 마스터-디테일  │
           │ 리스트 | 본문  │
           └────────────────┘
```

## 스토리 (왜 → 뭘 → 어디까지)

### 왜 만드나

gemify:wrapup으로 생성된 세션 리포트(`sessions/`)가 마크다운으로 쌓이는데, 이를 편하게 조회할 방법이 없음. GitHub repo URL만 주면 바로 볼 수 있는 웹 뷰어가 필요.

### 무엇을 만드나

**Session Report Viewer** - GitHub repo의 sessions/ 폴더를 웹으로 조회하는 앱

| 항목 | 내용 |
|------|------|
| 입력 | GitHub public repo URL |
| 출력 | sessions/*.md 타임라인 뷰 |
| UI | 리스트 → 클릭 시 마스터-디테일 전환 |
| 아키텍처 | SSR 필수 (CORS 우회) |
| 구현 | craftify로 PoC 생성 예정 |

**핵심 기능:**
- 인덱싱 플로우 (DeepWiki 패턴 참고)
- 최신순 타임라인, 10개씩 lazy load
- Reindex 기능
- 에러 처리 (sessions/ 없음, 마크다운 없음)

### 어디까지 왔나

```
[x] 아이디어 포착          ✅ 완료
[x] 스펙 구체화           ✅ 완료
[x] library 저장          ✅ 완료
[ ] craftify로 PoC 생성   ← 다음 작업
[ ] 배포 및 테스트
```

## 기술 결정사항

| 항목 | 결정 | 이유 |
|------|------|------|
| SSR | 필수 | raw.githubusercontent.com CORS 차단 |
| 스택 | craftify 선택 | PoC로 위임 |
| 배포 | craftify 선택 | PoC로 위임 |
| 지원 범위 | Public repo만 (v1) | 단순화 |

## 관련 문서

### 스펙
- [Session Report Viewer 스펙](../../library/product/session-report-viewer-spec.md) - 상세 스펙

### 구현 도구
- [Craftify Plugin View](./craftify.md) - 이 앱을 만들 도구
