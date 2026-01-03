---
title: gemify:improve-plugin 트리거 조건 개선 필요
date: 2026-01-03
status: raw
used_in: null
references:
  - inbox/materials/2026-01-03-improve-plugin-trigger-issue.md
---

# improve-plugin 스킬 트리거 개선

## 핵심 인사이트

플러그인 개선 관련 inbox 파일을 draft로 시작할 때, `gemify:improve-plugin`이 자동으로 활성화되어야 함.
그래야 최종 결과물이 `library/engineering/plugin-improvements/`에 개선 문서로 저장됨.

## 개선 제안

description에 추가할 트리거 키워드:
- "improve-plugin" 파일/주제 언급 시
- inbox에서 플러그인 개선 관련 thought 다룰 때
- "스킬에 ~ 추가", "SKILL.md 수정" 관련 요청
- "기준점", "체크리스트", "원칙 추가" 등

## 또는 다른 접근

inbox 파일 제목에 "plugin-improvement" 같은 태그가 있으면 자동 감지?
→ 이건 너무 복잡할 수 있음. description 트리거 확장이 더 현실적.
