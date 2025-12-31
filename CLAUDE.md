# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(corpus)으로 변환합니다.

```
seed/ + materials/ → /distill:grow → /distill:digest → CORPUS
 내 생각   외부재료        growing          corpus
```

**핵심**: seed와 materials가 grow에서 만나 해체 → 재조립 → 응축되어 밀도 있는 지식이 됨.

## Commands

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/distill:seed [내용]` | 내 생각의 씨앗 저장 | seed/ |
| `/distill:grow [파일/아이디어]` | seed + materials 대화로 확장 | growing/ |
| `/distill:digest [파일]` | 구조화하여 corpus로 | corpus/ |

```bash
/distill:seed                      # 직전 대화 내용 저장
/distill:seed 이런 생각이 들었어     # 입력 내용 저장
/distill:grow                      # growing 목록 또는 새 시작
/distill:grow "새로운 아이디어"      # 새 씨앗으로 시작
/distill:grow growing/my-idea.md   # 기존 이어가기
/distill:digest                    # growing 목록에서 선택
/distill:digest growing/my-idea.md # 특정 파일 처리
```

## /distill:grow 대화 모드

```
/distill:grow
├── branch - 가지치기, 넓게 뻗기 (기본)
└── ripen  - 익히기, 응축 → digest 준비
```

- **branch**: 넓게 탐색 ("연결되는 건?", "다른 관점에서?")
- **ripen**: 깊이 응축 ("왜 중요해?", "핵심만 남기면?")

**ripen 트리거**: "익혀봐", "좀 더 익히자", "핵심이 뭐야"

**Digest 전환 조건** (제안만, 강요 안 함):
- turns >= 5
- Open Questions 대부분 해결
- 같은 포인트 반복

## revision (스냅샷)

방향 전환(pivot) 시 자동 스냅샷:
- `.history/{slug}/` 폴더에 저장
- frontmatter `history` 배열에 기록

## 6대 Domain (corpus 분류)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

## 데이터 디렉토리

- `seed/` - 내 생각의 씨앗
- `materials/` - 외부 재료 (기사, 문서, 대화 등)
- `growing/` - 확장 중인 아이디어
- `corpus/` - 완성된 지식 (domain별 분류)

## Status 상태 흐름

| 폴더 | 상태값 |
|------|--------|
| seed/, materials/ | `raw` → `used` |
| growing/ | `growing` → `digested` |

## 핵심 규칙

- 질문은 **하나씩 순차적으로**
- 사용자 **컨펌 없이 corpus에 저장하지 않음**
- 템플릿 파일 (`_template.md`) 처리 대상 제외
- slug는 영문 kebab-case

## Source Tracking

seed/materials 사용 시:
- 해당 파일의 `status` → `used`, `used_in` → growing 경로
- growing 파일의 `sources` 배열에 추가
