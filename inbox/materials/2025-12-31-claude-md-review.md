---
title: "CLAUDE.md 리뷰 및 개선점"
date: 2025-12-31
source: "직접 리뷰"
type: document
status: used
used_in: drafts/grow-mode-expansion.md
---

# CLAUDE.md 리뷰 결과

## 현재 상태

CLAUDE.md가 핵심 개념과 워크플로우를 잘 담고 있음.

## 발견된 개선점

### 1. /grow 대화 모드 미구현

현재 CLAUDE.md에 설명된 3가지 모드:
- **expand**: 아이디어 확장 ("연결되는 건?", "더 큰 그림에서?")
- **brew**: 깊이 숙성 ("왜 이게 중요해?", "핵심이 뭐야?")
- **brainstorm**: 자유로운 발산 ("미친 아이디어라면?", "반대로 하면?")

실제 `skills/grow/SKILL.md`에는 이 모드가 구현되어 있지 않음. 도전/확장/구체화 역할만 정의됨.

### 2. 추가 권장 사항

- 커맨드 사용 예시 추가
- Frontmatter 필드 요약 테이블
- docs/humans/ 폴더 참조 언급

## 관련 파일

- `skills/grow/SKILL.md`
- `.claude/commands/grow.md`
