---
title: "gemify:tidy 명령어 필요성"
date: 2026-01-03
status: used
used_in: drafts/gemify-tidy.md
references: []
---

# gemify:tidy 명령어 필요성

ground-truth의 views, library 문서들이 시간이 지나면서:
- **outdated**: 플러그인 리네임(ced → forgeify) 후 문서가 과거 버전 참조
- **깨진 링크**: sources, 관련 문서 경로가 실제로 없는 파일 가리킴
- **중복/불필요**: 같은 subject의 view가 여러 개, 더 이상 의미 없는 문서

## 아이디어

`/gemify:tidy` 커맨드 추가:
- 깨진 링크 탐지 (frontmatter sources, 본문 링크)
- outdated 문서 표시 (오래된 updated 날짜, 참조 플러그인 변경)
- 중복 view 정리 제안
- 사용자가 생각날 때마다 실행해서 점진적으로 정리

## 트리거

ced.md → forgeify.md 작업하면서 이런 정리 도구가 필요함을 느낌.
