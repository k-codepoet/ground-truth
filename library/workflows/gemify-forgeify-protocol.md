---
title: gemify-forgeify 개선 문서 프로토콜
type: workflow
origin: original
views:
  - views/by-subject/forgeify.md
---

## 개요

ground-truth에서 생성한 플러그인 개선 문서를 forgeify가 참조해서 실행하는 단방향 프로토콜.

```
ground-truth (gemify)              마켓플레이스 (forgeify)
─────────────────────              ──────────────────────
/gemify:improve-plugin             /forgeify:improve <문서>
     ↓                                   ↓
개선 문서 생성                      문서 참조 → 코드 수정
library/specs/
```

## 개선 문서 스키마

```markdown
---
target_plugin: <플러그인명>
improvement_type: feature | fix | refactor
priority: high | medium | low
problem: "한 줄 문제 정의"
solution: "한 줄 해결 방향"
requirements:
  - 핵심 요구사항 (방향)
  - 핵심 요구사항 (방향)
references:
  - ./details/<상세문서>.md  # 필요시만
---

## Why

2-3문장 배경과 필요성

## What

- 변경 포인트

## Scope

포함: ...
제외: ...
```

## Progressive Disclosure

| Layer | 내용 | 용도 |
|-------|------|------|
| frontmatter | problem, solution, requirements | 빠른 판단 |
| body | Why, What, Scope | 이해 |
| references/ | 구현 힌트, 상세 스펙 | 실행 시 필요시만 |

## 관련 명령어

| 명령어 | 위치 | 역할 |
|--------|------|------|
| `/gemify:improve-plugin` | ground-truth | 개선 문서 생성 |
| `/forgeify:improve` | 마켓플레이스 | 문서 참조해서 실행 |
