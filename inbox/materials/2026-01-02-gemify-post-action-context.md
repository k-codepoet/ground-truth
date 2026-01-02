---
title: gemify 사후처리 기능 - 맥락과 배경
date: 2026-01-02
source: 대화에서 추출
type: conversation
status: used
used_in: library/ai-automation/gemify-1.5.0-workflow-extensions.md
---

## 발단

플러그인 개선 아이디어(`/gemify:improve-plugin`)를 논의하다가, gemify 흐름(inbox → drafts → library)을 거치지 않고 바로 플러그인을 만들어버림.

## 문제 인식

원래 흐름:
```
inbox/thoughts에 아이디어 저장
    ↓
drafts에서 다듬기
    ↓
library로 정리
    ↓
실제 구현
```

실제로 일어난 일:
```
아이디어 논의 → 바로 구현 → 사후에 library 기록
```

## 필요한 기능

"역방향 기록" 또는 "사후처리" 기능:
- 이미 액션이 일어난 경우
- 의사결정 과정을 역으로 library에 기록
- 또는 drafts를 건너뛰고 바로 library로 가는 단축 경로

## 관련 파일

- thoughts: `inbox/thoughts/2026-01-02-gemify-post-action-feature.md`
- 이번에 만든 library: `library/ai-automation/improve-plugin-workflow.md`
- 이번에 만든 스킬: `gemify/commands/improve-plugin.md`, `gemify/skills/improve-plugin/SKILL.md`

## 작업 시 참고

1. gemify 플러그인에 역방향 흐름 지원 검토
2. `/gemify:library`에 drafts 없이 바로 저장하는 옵션?
3. 또는 `/gemify:retroactive` 같은 별도 명령어?
