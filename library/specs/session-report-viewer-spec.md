---
title: Session Report Viewer - PoC 스펙
type: spec
origin: original
created: 2026-01-04
status: polished
origin_file: inbox/thoughts/2026-01-04-session-report-viewer-idea.md
tags: [gemify, sessions, web-app, PoC, craftify]
views: []
---

## 개요

gemify:wrapup으로 생성된 세션 리포트(`sessions/`)를 웹에서 볼 수 있는 뷰어 앱.

Git repo URL을 입력하면 해당 repo의 세션 리포트들을 타임라인으로 조회.

## 핵심 기능

### 1. 인덱싱 플로우

```
사용자가 {host}/{user}/{repo} 접근
    ↓
인덱싱 됨? ─No→ "이 repo를 인덱싱하시겠습니까?" 페이지
    │              └→ GitHub repo URL 입력 → 인덱싱 시작
    ↓ Yes
세션 리포트 뷰어 표시
```

### 2. 뷰어 UI

- **리스트 뷰**: 최신순 타임라인, 10개씩 lazy load
- **클릭 시**: 마스터-디테일 레이아웃으로 전환
  - 왼쪽: 리스트 (사이드바화)
  - 오른쪽: 본문 (마크다운 렌더링)
- **본문 닫기**: 다시 리스트 전체화면

### 3. Reindex

- 이미 인덱싱된 repo에 Reindex 버튼 제공
- 최신 세션 리포트 반영

## 기술 요구사항

### SSR 필수

- `raw.githubusercontent.com`은 CORS 차단
- 브라우저에서 직접 fetch 불가
- 서버에서 GitHub API 호출 필요

### URL 구조

```
{host}/{user}/{repo}
```

예: `session-viewer.app/choigawoon/ground-truth`

### 입력 방식

- 랜딩 페이지에서 GitHub repo URL 입력 폼
- 입력 시 `/{user}/{repo}` 라우팅으로 이동

## 에러 처리

| 상황 | 처리 |
|------|------|
| sessions/ 폴더 없음 | 에러 메시지 표시 ("이 repo에는 sessions/ 폴더가 없습니다") |
| sessions/ 폴더는 있지만 마크다운 없음 | 에러 메시지 표시 ("세션 리포트가 없습니다") |
| repo 접근 불가 (private, 404) | 에러 메시지 표시 |

## 지원 범위

- Public repo만 지원 (v1)
- Private repo는 향후 확장 고려

## 세션 리포트 구조 (참고)

```yaml
---
title: "세션 제목"
date: YYYY-MM-DD
duration: ~2h  # optional
---

## Summary
## Outputs
## Stashed for Next
## Key Decisions  # optional
## Next Actions
```

## 결정 사항 (craftify 위임)

- 기술 스택 선택 (Next.js, Nuxt, SvelteKit 등)
- 호스팅/배포 플랫폼 (Vercel, Netlify 등)
- 캐싱 전략 (인덱싱 결과 저장 방식)

## 참고

- DeepWiki 패턴: URL 변환 방식 (`github.com` → `deepwiki.com`)
- 인덱싱 안 된 repo 접근 시 요청 페이지로 유도
