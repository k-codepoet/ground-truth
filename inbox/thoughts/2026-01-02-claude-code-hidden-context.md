---
title: Claude Code는 숨겨진 환경 컨텍스트를 안다
date: 2026-01-02
status: used
used_in: drafts/claude-code-hidden-context.md
references:
  - inbox/materials/2026-01-02-claude-code-env-injection.md
---

# Claude Code는 숨겨진 환경 컨텍스트를 안다

Claude Code는 사용자가 명시적으로 알려주지 않아도 작업 환경을 파악하고 있다.

- 어떤 디렉토리에서 작업 중인지
- 추가로 접근 가능한 디렉토리가 어딘지
- git repo인지 아닌지
- 오늘 날짜가 언제인지

이 정보들이 시스템 프롬프트에 자동 주입되기 때문.

**시사점**: Claude Code 확장 개발 시 이 env 정보를 활용할 수 있다. 예를 들어 hook이나 skill에서 현재 환경에 맞는 동작을 하도록 설계 가능.
