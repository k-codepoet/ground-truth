# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(corpus)으로 변환합니다.

```
HEAD (암묵지) → /seed → /grow → /digest → CORPUS → EXPORTS
                inbox    growing   corpus
```

현재 Stage 0 (수동 검증 단계)입니다.

## Knowledge Flow

| 단계 | 폴더 | 설명 |
|------|------|------|
| 1. Seed | `inbox/` | Raw 지식 입력 (자유 형식) |
| 2. Grow | `growing/` | 대화로 확장 중인 생각 |
| 3. Digest | `corpus/` | 구조화된 지식 (frontmatter 필수) |
| 참고 | `docs/humans/knowledge-ops/brainstorm/` | 전략/개선안 문서 |

## 6대 Domain (corpus 분류 체계)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

## Available Commands

### /seed
씨앗 아이디어를 inbox에 빠르게 저장합니다.

```
/seed                     # 직전 대화 내용 저장
/seed 이런 생각이 들었어    # 입력 내용 저장
```

저장 후 `/grow`로 키울 수 있습니다.

### /grow
씨앗 아이디어를 대화로 확장합니다 (expand/brew/brainstorm 통합).

```
/grow                    # 목록 또는 새 시작
/grow "아이디어..."       # 새 씨앗으로 시작
/grow growing/파일.md    # 기존 이어가기
```

Claude가 대화 상대로서:
- 질문으로 도전 ("왜 필요해?", "반대로 생각하면?")
- 새 각도 제안 ("연결되는 건?", "극단적으로 밀면?")
- 익으면 `/digest` 전환 제안

### /digest
inbox 파일을 소크라테스식 질문으로 분석하여 corpus로 구조화합니다.

```
/digest                  # inbox 목록 보여주고 선택
/digest inbox/파일명.md  # 특정 파일 처리
```

질문 순서:
1. 목적: "이거 왜 남기려고 해?"
2. 필요성: "이게 없으면 나중에 뭐가 안 돼?"
3. 요약: "한 문장으로 요약하면?"
4. 압축: "이 중에 진짜 핵심만 남기면?"
5. 분류: "6개 domain 중 어디야?"
6. 연결: "기존 corpus에 연결되는 거 있어?"

완료 후: 원본 파일을 `inbox_archived/`로 이동

## Key Files

**스킬 정의**
- `skills/seed/SKILL.md` - /seed 스킬
- `skills/grow/SKILL.md` - /grow 스킬
- `skills/knowledge-digest/SKILL.md` - /digest 스킬

**커맨드 정의**
- `.claude/commands/seed.md` - /seed 커맨드
- `.claude/commands/grow.md` - /grow 커맨드
- `.claude/commands/digest.md` - /digest 커맨드

**템플릿**
- `inbox/_template.md` - inbox 문서 템플릿
- `growing/_template.md` - growing 문서 템플릿
- `corpus/_template.md` - corpus 문서 템플릿

**전략 문서**
- `docs/humans/knowledge-ops/brainstorm/00-summary-and-priorities.md` - 전략 요약

## Session Start Behavior

세션 시작 시:
1. **growing/** 폴더의 진행 중인 생각 확인 (status: growing)
2. **inbox/** 폴더의 미처리 파일 확인 (`_template.md` 제외)
3. 알림: "진행 중인 생각 N개, inbox에 M개 파일 있어요"
4. `/grow`로 이어가거나 `/digest`로 정리할 수 있다고 안내

## 핵심 규칙

- 질문은 **하나씩 순차적으로** (한꺼번에 던지지 않음)
- 사용자 **컨펌 없이 corpus에 저장하지 않음**
- 템플릿 파일 (`_template.md`)은 처리 대상에서 제외
- slug는 영문 kebab-case로 자동 생성

## Document Formats

### Inbox (inbox/{date}-{slug}.md)
```markdown
# {제목}

> 날짜: YYYY-MM-DD
> 출처: (대화/메모/링크)

---

{내용}
```

### Growing (growing/{slug}.md)
```markdown
---
title: "{제목}"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD HH:MM"
turns: 0
status: growing
---

## Seed
{최초 아이디어}

## Growth Log
<!-- 세션별: C: 질문, U: 답변, Insight: 통찰 -->

## Current State
{현재까지 종합}

## Open Questions
- [ ] 열린 질문들
```

### Corpus (corpus/{domain}/{slug}.md)
```markdown
---
title: {제목}
domain: {6개 중 하나}
---

## Context
{왜 이 지식이 필요한지}

## Content
{핵심 내용}
```
