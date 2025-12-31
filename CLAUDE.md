# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(corpus)으로 변환합니다.

```
seed/ + materials/ → /grow → /digest → CORPUS
 내 생각   외부재료     growing    corpus
```

**핵심**: seed와 materials가 grow에서 만나 해체 → 재조립 → 응축되어 밀도 있는 지식이 됨.

## Commands

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/seed` | 내 생각의 씨앗 저장 | seed/ |
| `/grow` | seed + materials 대화로 확장 | growing/ |
| `/digest` | 구조화하여 corpus로 | corpus/ |

## 6대 Domain (corpus 분류)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

## Key Files

**스킬** (자동 활성화되는 워크플로우)
- `skills/seed/SKILL.md`
- `skills/grow/SKILL.md` + `references/growing-format.md`
- `skills/digest/SKILL.md` + `references/corpus-format.md`

**커맨드** (사용자가 `/`로 호출)
- `.claude/commands/seed.md`
- `.claude/commands/grow.md`
- `.claude/commands/digest.md`

**템플릿** (문서 형식 참조)
- `seed/_template.md`, `materials/_template.md`, `growing/_template.md`, `corpus/_template.md`

## Session Start Behavior

세션 시작 시:
1. growing/ 폴더의 진행 중인 생각 확인 (status: growing)
2. seed/ 폴더의 미처리 씨앗 확인 (`_template.md` 제외)
3. 알림 후 `/grow` 또는 `/digest` 안내

## 핵심 규칙

- 질문은 **하나씩 순차적으로**
- 사용자 **컨펌 없이 corpus에 저장하지 않음**
- 템플릿 파일 (`_template.md`) 처리 대상 제외
- slug는 영문 kebab-case

## Source Tracking

seed/materials 사용 시:
- 해당 파일의 `status` → `used`
- 해당 파일의 `used_in` → growing 파일 경로 기록
