---
title: "Workflow 타입 발견 - library 분류 체계 논의 중"
date: 2026-01-04
source: "gemify:draft 세션 - library 분류 체계 리팩토링"
type: conversation
status: raw
used_in: null
---

# Workflow 타입 발견

## 맥락

library 분류 체계를 Type 기반(principles, decisions, insights, how-tos, specs)으로 변경하는 작업 중 새로운 타입 필요성 발견.

## 논의 내용

library에 저장되는 것 중 "작업 흐름/파이프라인"이 있음:
- input → output 패턴이 명확한 것
- 반복하다가 패턴을 발견해서 정형화된 것

### 현재 존재하는 workflow 예시

**improve-plugin workflow:**
```
gemify:improve-plugin → 개선 문서 생성
       ↓
forgeify:improve-plugin → 개선 문서 실행
```

### 앞으로 만들 workflow 예시

**poc-development workflow:**
```
gemify → 아이디어 정리
   ↓
craftify → POC 개발
```

## 관찰

- 처음엔 inbox → draft → library 일반 흐름으로 처리
- 여러 번 하다가 패턴 발견 → workflow로 정형화
- workflow는 플러그인 간 연계를 명확하게 함
