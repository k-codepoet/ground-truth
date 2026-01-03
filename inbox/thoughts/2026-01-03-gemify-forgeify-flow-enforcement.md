---
title: gemify→forgeify 단방향 흐름 강제 필요성
date: 2026-01-03
status: raw
used_in: null
references: []
---

forgeify 검수 중 발견: Claude가 플러그인을 직접 수정하려는 패턴이 반복됨.

gemify(지식 생산) → forgeify(실행) 단방향 흐름 원칙을 지키도록 유도해야 함.

**올바른 흐름:**
1. 문제 발견
2. `/gemify:improve-plugin`으로 개선 문서 생성
3. `/forgeify:improve-plugin`으로 실행

이 흐름이 자연스럽게 나오도록 가이드나 훅이 필요할 수 있음.

현재 검수 과정에서도 "수정 진행할까요?"라고 바로 물어보는 패턴이 나타남 - 이건 원칙 위반.
