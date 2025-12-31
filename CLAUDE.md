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

## /grow 대화 모드

대화 흐름에 따라 자동 전환:
- **expand**: 아이디어 확장 ("연결되는 건?", "더 큰 그림에서?")
- **brew**: 깊이 숙성 ("왜 이게 중요해?", "핵심이 뭐야?")
- **brainstorm**: 자유로운 발산 ("미친 아이디어라면?", "반대로 하면?")

**Digest 전환 조건** (제안만, 강요 안 함):
- turns >= 5
- Open Questions 대부분 해결
- 같은 포인트 반복

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

- **스킬**: `skills/{seed,grow,digest}/SKILL.md`
- **참조**: `skills/*/references/*.md` (파일 형식 상세)
- **커맨드**: `.claude/commands/{seed,grow,digest}.md`
- **템플릿**: `{seed,materials,growing,corpus}/_template.md`

## Status 상태 흐름

| 폴더 | 상태값 |
|------|--------|
| seed/, materials/ | `raw` → `used` |
| growing/ | `growing` → `digested` |

## Session Start Behavior

세션 시작 시 growing/(status: growing)과 seed/(raw) 확인 후 `/grow` 또는 `/digest` 안내.

## 핵심 규칙

- 질문은 **하나씩 순차적으로**
- 사용자 **컨펌 없이 corpus에 저장하지 않음**
- 템플릿 파일 (`_template.md`) 처리 대상 제외
- slug는 영문 kebab-case

## Source Tracking

seed/materials 사용 시:
- 해당 파일의 `status` → `used`, `used_in` → growing 경로
- growing 파일의 `sources` 배열에 추가
