---
title: CLAUDE.md progressive disclosure 원칙
type: how-to
origin: original
created_via: retro
views: []
---

## Context

CLAUDE.md에 스킬 동작 상세가 모두 적혀있어서, 스킬이 호출되지 않고도 Claude가 직접 동작을 수행하는 문제 발생.

## Decision

**CLAUDE.md는 "무엇이 있는지"만, "어떻게 동작하는지"는 스킬이 처리**

### 제거한 것 (스킬로 위임)
- `/gemify:draft` 대화 모드 상세 (facet/polish)
- Status 상태 흐름 (raw→used, cutting→set)
- Source Tracking 규칙
- 6대 Domain 상세 설명
- Frontmatter 필드 상세
- 파일 네이밍 규칙

### 남긴 것 (CLAUDE.md 역할)
- 프로젝트 개요
- 명령어 목록 (무엇이 있는지만)
- 디렉토리 구조 (간략히)
- 핵심 규칙 (HITL 원칙)

## Outcome

- 스킬이 호출될 때 스킬 프롬프트에서 상세 동작 처리
- 관심사 분리: CLAUDE.md = 개요, 스킬 = 상세

## References

- library/how-tos/craftify-progressive-disclosure.md
