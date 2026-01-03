---
title: gemify follow-up/sync-up 기능 필요
date: 2026-01-03
status: raw
used_in: null
references:
  - inbox/materials/2026-01-03-session-followup-context.md
---

# gemify follow-up/sync-up 기능 아이디어

## 핵심 인사이트

오랜만에 작업에 복귀하면 **"어디까지 했지?"** 파악이 필요하다.
현재는 수동으로 sessions/, drafts/, inbox/를 뒤져야 한다.

## 필요한 기능

`/gemify:followup` 또는 `/gemify:sync`:
- sessions/ 최근 세션 요약
- drafts/에서 status: cutting 찾기
- inbox/thoughts/에서 status: raw 개수
- 각 세션의 Next Actions 모아보기

## SessionStart hook과의 차이

현재 SessionStart hook은 drafts/와 inbox/만 체크.
→ **sessions/의 Next Actions는 보여주지 않음**

follow-up은:
- sessions/까지 포함한 **전체 맥락 복원**
- "이전 세션에서 하기로 한 것" 상기

## 구현 방향

1. SessionStart hook 확장? 또는
2. `/gemify:followup` 별도 스킬?
