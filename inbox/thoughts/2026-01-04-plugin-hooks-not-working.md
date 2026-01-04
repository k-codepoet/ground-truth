---
title: "Claude Code 플러그인 hooks 미동작 문제"
date: 2026-01-04
status: raw
references:
  - inbox/materials/2026-01-04-claude-plugin-hooks-debug.md
---

# 플러그인 hooks가 동작하지 않는 문제

gemify, forgeify 등 각 플러그인에 구현한 hooks가 실행되지 않음.

## 핵심 인사이트

perplexity와 함께 조사한 결과, 원인 후보:
1. **hooks.json 포맷 문제** - 플러그인 내부 hooks/hooks.json 구조가 요구사항과 다를 수 있음
2. **매처 오류** - tool name, 대소문자, glob 패턴 불일치
3. **세션 재시작 누락** - 훅 변경 후 Claude 세션 재시작 필요

## 다음 액션

디버깅을 위해 `claude --debug` 모드로 로그 확인 필요:
- 훅이 로드되는지
- 이벤트 트리거가 발생하는지
- 매처가 일치하는지
- 커맨드가 실제 실행되는지

실제 플러그인 hooks/hooks.json 내용을 확인하고 공식 문서와 대조해봐야 함.
