---
title: gemify-forgeify 단방향 흐름 설계 세션
date: 2026-01-03
source: 대화 세션
type: conversation
status: raw
used_in:
---

## 대화 맥락

gemify:improve-plugin 커맨드의 역할 재정의 논의.

### 문제 인식
- gemify 안에서 코드 수정까지 하고 있어 관심사 혼재
- ground-truth(지식) → 제품(실행) 단방향 흐름 필요

### 결정 과정
1. gemify: 개선 계획 문서 생성만 담당
2. forgeify: 문서 참조해서 실제 코드 수정
3. 개선 문서 스키마 설계 (frontmatter + body, Progressive Disclosure)
4. 저장 위치: library/engineering/plugin-improvements/

### 결과물
- 프로토콜 문서: gemify-forgeify-protocol.md
- forgeify 개선 문서: forgeify-improve-command.md
- gemify 개선 문서: gemify-improve-plugin-refactor.md

### 부트스트래핑 순서
1. forgeify에 /forgeify:improve 기능 추가 (먼저)
2. gemify improve-plugin 역할 변경 (이후)
3. forgeify로 스스로를 개선
