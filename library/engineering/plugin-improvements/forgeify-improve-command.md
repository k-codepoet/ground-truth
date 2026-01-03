---
target_plugin: forgeify
improvement_type: feature
priority: high
problem: "forgeify가 외부 개선 문서를 참조해서 플러그인을 개선하는 기능이 없음"
solution: "/forgeify:improve 명령어 추가 - 개선 문서 경로를 받아 해당 내용 기반으로 플러그인 수정"
requirements:
  - /forgeify:improve <문서경로> 명령어 추가
  - 문서의 frontmatter에서 target_plugin, requirements 파싱
  - body의 Why, What 섹션 읽어 맥락 이해
  - references/ 폴더 있으면 상세 내용 참조
references: []
domain: engineering
views:
  - views/by-subject/forgeify.md
---

## Why

ground-truth에서 생성한 개선 문서를 forgeify가 실행하는 단방향 흐름 구축. 지식 생산(gemify)과 실행(forgeify) 분리.

## What

- `commands/improve.md` 신규 생성
- 개선 문서 스키마 파싱 로직 (frontmatter + body)
- Progressive Disclosure 지원: references/ 있으면 추가 참조

## Scope

포함:
- /forgeify:improve 명령어
- 개선 문서 파싱

제외:
- 개선 문서 생성 (gemify 역할)
- 자동 실행 (사용자 확인 후 진행)
