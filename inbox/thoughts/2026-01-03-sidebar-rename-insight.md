---
title: "capture-pair → sidebar 리네임"
date: 2026-01-03
references:
  - inbox/materials/2026-01-03-capture-pair-rename-discussion.md
status: used
used_in:
  - library/engineering/plugin-improvements/gemify-rename-capture-pair-to-sidebar.md
---

gemify:capture-pair를 gemify:sidebar로 리네임.

## 핵심 인사이트

1. **브랜드 vs 기능 네이밍 분리**
   - 브랜드(gemify): 메타포, 스토리 OK
   - 기능(sidebar): 직관적 용어 사용

2. **기능의 본질 재정의**
   - AS-IS: "material + thought를 쌍으로 캡처"
   - TO-BE: "본 작업 중 떠오른 것을 옆에 빼두기"

3. **sidebar의 적합성**
   - 미국 직장 문화에서 "let's sidebar this" = 본론 아닌 걸 옆으로 빼둠
   - "지금 다룰 건 아니니까 옆에 빼둬"라는 정확한 뉘앙스

## 수정 대상

- `commands/capture-pair.md` → `commands/sidebar.md`
- `skills/capture-pair/` → `skills/sidebar/`
- SKILL.md 내용 업데이트
- CLAUDE.md 업데이트
- CHANGELOG.md 업데이트
