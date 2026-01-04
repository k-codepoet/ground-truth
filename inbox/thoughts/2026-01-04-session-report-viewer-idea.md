---
created: 2026-01-04
status: raw
tags: [gemify, sessions, web-app, PoC]
---

# Session Report Viewer 웹앱 아이디어

## 핵심 아이디어

gemify:wrapup을 하면 작업 디렉토리의 `sessions/` 경로에 마크다운 형식의 리포트 파일이 생성됨.

Git repo에 `sessions/` 경로가 있는 경우, **git repo URL만 주면 해당 세션 리포트들을 바로 볼 수 있는 웹사이트**를 만들고 싶음.

## 의도

- craftify에 PoC 앱을 만들게 시킬 예정
- 작업 문서를 구체화해서 전달해야 함

## 다음 단계

- craftify에 전달할 상세 스펙 문서 작성 필요
- 입력: git repo URL
- 출력: sessions/ 폴더의 마크다운 리포트를 읽기 좋은 UI로 렌더링
