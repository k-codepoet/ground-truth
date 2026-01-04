---
title: "gemify:draft 히스토리 문제 해결 아이디어"
date: "2026-01-04"
status: used
used_in: library/engineering/plugin-improvements/gemify-draft-history-hooks.md
references: []
---

## 문제

1. **draft 대화 종료 시 히스토리가 안 남음** - pivot할 때만 남기게 되어있어서, 대부분의 대화가 기록 없이 끝남
2. **polish 모드와 gemify:library 명령어 혼동** - 스킬에서 "polish" 용어 쓰면서 실제 동작은 gemify:library로 해야함
3. **대화 종료 시점 자동 체크 없음** - hooks가 없어서 히스토리 저장 기준 체크를 못함

## 해결책

1. **hooks.json에 NotificationStop 이벤트 추가** - 대화 종료 시 히스토리 저장 기준 체크
2. **히스토리 저장 기준 명확화**:
   - turns >= 3 (의미있는 대화량)
   - Current State에 변경 있음
   - 마지막 스냅샷 이후 내용 변화
3. **draft 스킬에 "polish → library 전환은 /gemify:library 명령어로" 명시**
4. **대화 종료 시 자동 히스토리 저장 제안** (강제 아님, HITL 유지)
