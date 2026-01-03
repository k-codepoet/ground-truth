---
title: 세션 종료 시점 재확인 패턴
date: 2026-01-03
source: bootstrapping-principle draft 세션 마무리
type: conversation
status: raw
used_in:
---

## 상황

- task 진행 후 대화 마무리 시점
- 사용자가 "놓친 거 있니?" 질문
- 매번 세션 종료 시 비슷한 패턴 반복

## 반복되는 행동

1. 작업 완료 후 종료 전 재확인 요청
2. 놓친 것 없는지 체크
3. 최종 정리/리포트 필요

## 현재 방식

- 수동으로 질문 ("놓친 거 있니?")
- Claude가 정리해서 답변
- 별도 기록 없이 대화로만 끝남
