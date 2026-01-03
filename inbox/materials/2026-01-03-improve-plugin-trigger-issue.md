---
title: gemify:improve-plugin 트리거 조건 문제 분석
date: 2026-01-03
source: 대화 중 발견
type: conversation
status: raw
used_in: null
---

# 문제 상황

Go/No-Go 체크 원칙을 improve-plugin에 추가하려는 작업에서 `/gemify:improve-plugin` 스킬이 자동 활성화되지 않음.

## 대화 흐름

1. 사용자가 `/gemify:draft inbox/thoughts/...improve-plugin-yagni-check.md` 명시적 호출
2. `/gemify:draft` 워크플로우로 진행
3. 원칙 문서 생성 (`library/operations/go-no-go.md`)
4. 개선 요청 문서 누락 → 마지막에 수동 추가

## 현재 트리거 조건 (SKILL.md description)

```
"플러그인 개선 아이디어", "plugin 개선안", "개선 문서 작성" 등 요청 시 활성화
```

## 실제 사용자 요청

```
Gemify improve-plugin 기준점 제시
/gemify:draft inbox/thoughts/2026-01-03-improve-plugin-yagni-check.md 로 구체화
```

## 매칭 실패 원인

1. 명시적 `/gemify:draft` 호출로 다른 스킬 지정됨
2. "기준점 제시"는 트리거 키워드에 없음
3. inbox 파일 제목 "improve-plugin에 YAGNI 체크리스트 필요"도 매칭 안 됨
