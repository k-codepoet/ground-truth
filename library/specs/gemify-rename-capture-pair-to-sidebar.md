---
title: capture-pair를 sidebar로 리네임
type: spec
origin: derived
target_plugin: gemify
improvement_type: refactor
priority: high
problem: "capture-pair 이름이 직관적이지 않아 기능을 바로 이해하기 어려움"
solution: "capture-pair를 sidebar로 리네임 - 미국 문화권에서 '본론 아닌 걸 옆으로 빼둠'의 의미"
requirements:
  - commands/capture-pair.md → commands/sidebar.md 리네임
  - skills/capture-pair/ → skills/sidebar/ 폴더 리네임
  - SKILL.md 내용에서 capture-pair → sidebar 변경
  - command 내용에서 capture-pair → sidebar 변경
  - CLAUDE.md에서 capture-pair → sidebar 변경
  - CHANGELOG.md에 변경 사항 기록
references:
  - inbox/materials/2026-01-03-capture-pair-rename-discussion.md
  - inbox/thoughts/2026-01-03-sidebar-rename-insight.md
views: []
---

## Why

### 문제
- `capture-pair`라는 이름이 "쌍으로 캡처"라는 기술적 동작을 설명
- 실제 사용 맥락과 맞지 않음

### 실제 사용 맥락
- 원래 하던 일 진행 중
- 갑자기 문제/개선점/아이디어가 떠오름
- "이거 나중에 해야지" → 다음 작업함에 넣기

### 네이밍 원칙
- 브랜드(gemify): 메타포, 스토리 OK
- 기능(sidebar): 직관적 용어 사용

## What

`capture-pair` → `sidebar` 리네임

**sidebar의 의미**:
- 미국 직장 문화에서 "let's sidebar this" = 본론 아닌 걸 옆으로 빼둠
- "지금 다룰 건 아니니까 옆에 빼둬"라는 정확한 뉘앙스

## Scope

포함:
- `commands/capture-pair.md` → `commands/sidebar.md`
- `skills/capture-pair/SKILL.md` → `skills/sidebar/SKILL.md`
- 파일 내용에서 모든 `capture-pair` 텍스트를 `sidebar`로 변경
- description 업데이트: "본 작업 중 떠오른 것을 옆에 빼두기"
- CLAUDE.md 업데이트
- CHANGELOG.md 업데이트 (버전 bump)

제외:
- 기능 로직 변경 없음 (이름만 변경)
- 다른 스킬/커맨드 변경 없음
