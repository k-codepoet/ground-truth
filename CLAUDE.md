# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(corpus)으로 변환합니다.

```
HEAD (암묵지) → INBOX (raw 캡처) → CORPUS (구조화) → EXPORTS (다양한 형태)
```

현재 Stage 0 (수동 검증 단계)입니다.

## Architecture

### Knowledge Flow

1. **inbox/** - Raw 지식 입력 (자유 형식 마크다운)
2. **corpus/** - 구조화된 지식 저장 (frontmatter 필수)
3. **brainstorm/** - 전략/개선안 문서

### 6대 Domain (corpus 분류 체계)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

### Corpus Document Format

```markdown
---
title: {제목}
domain: {위 6개 중 하나}
---

## Context
{왜 이 지식이 필요한지}

## Content
{핵심 내용}
```

## Available Commands

### /digest
inbox 파일을 소크라테스식 질문으로 분석하여 corpus로 구조화합니다.

```
/digest inbox/파일명.md
```

질문 순서:
1. 목적: "이거 왜 남기려고 해?"
2. 필요성: "이게 없으면 나중에 뭐가 안 돼?"
3. 요약: "한 문장으로 요약하면?"
4. 압축: "이 중에 진짜 핵심만 남기면?"
5. 분류: "6개 domain 중 어디야?"
6. 연결: "기존 corpus에 연결되는 거 있어?"

## Key Files

- `skills/knowledge-digest/SKILL.md` - /digest 스킬 정의
- `inbox/_template.md` - inbox 문서 템플릿
- `corpus/_template.md` - corpus 문서 템플릿
- `brainstorm/00-summary-and-priorities.md` - 전략 우선순위 요약

## Session Start Behavior

세션 시작 시 inbox/ 폴더의 미처리 파일을 확인하고 알려줍니다.
