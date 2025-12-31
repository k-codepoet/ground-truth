---
title: "domain 선택 시 판단 어려움 발견"
date: 2025-12-31
source: "Claude 대화"
type: conversation
status: raw
used_in:
---

## 맥락

grow-mode-expansion을 digest 하는 과정에서 domain 선택 질문:

> **이 지식의 domain은?**
> - engineering (어떻게 만들 것인가?)
> - operations (어떻게 돌릴 것인가?)

사용자 답변: "operations. 어떻게 만들지 정리는 됐고 이대로 하기만 하면되니까."

## 발견

- domain 선택 시 **"만드는 것"과 "돌리는 것"의 경계**가 모호할 수 있음
- 현재는 핵심 질문만 있고, 구체적인 판단 기준이 없음
- digest 시점에 domain 분류가 빠르게 되려면 명확한 기준 필요

## 도출된 아이디어

→ 6대 domain별 구체적인 판단 기준/예시 문서화 필요
