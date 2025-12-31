# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(library)으로 변환합니다.

```
inbox/ → /gemify:develop → /gemify:file → LIBRARY
 원석        drafts           library
```

**핵심**: 원석을 다듬어 보석으로. 생각을 포착하고, 다듬고, 정리합니다.

**태그라인**: Turn your thoughts into gems.

## Commands

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/gemify:capture [내용]` | 내 생각 포착 | inbox/thoughts/ |
| `/gemify:develop [파일/아이디어]` | 원석 다듬기 (대화로 확장) | drafts/ |
| `/gemify:file [파일]` | 보석 정리 (library로) | library/ |

```bash
/gemify:capture                      # 직전 대화 내용 저장
/gemify:capture 이런 생각이 들었어     # 입력 내용 저장
/gemify:develop                      # drafts 목록 또는 새 시작
/gemify:develop "새로운 아이디어"      # 새 원석으로 시작
/gemify:develop drafts/my-idea.md    # 기존 이어가기
/gemify:file                         # drafts 목록에서 선택
/gemify:file drafts/my-idea.md       # 특정 파일 처리
```

## /gemify:develop 대화 모드

```
/gemify:develop
├── facet  - 여러 면 탐색, 넓게 (기본)
└── polish - 깊이 연마 → file 준비
```

- **facet**: 넓게 탐색 ("다른 면에서 보면?", "연결되는 건?")
- **polish**: 깊이 연마 ("왜 중요해?", "핵심만 남기면?")

**polish 트리거**: "연마해봐", "좀 더 다듬자", "핵심이 뭐야"

**File 전환 조건** (제안만, 강요 안 함):
- turns >= 5
- Open Questions 대부분 해결
- 같은 포인트 반복

## revision (스냅샷)

방향 전환(pivot) 시 자동 스냅샷:
- `.history/{slug}/` 폴더에 저장
- frontmatter `history` 배열에 기록

## 6대 Domain (library 분류)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

## 데이터 디렉토리

- `inbox/thoughts/` - 내 생각 (원석)
- `inbox/materials/` - 외부 재료 (기사, 문서, 대화 등)
- `drafts/` - 다듬는 중인 아이디어
- `library/` - 완성된 지식 (domain별 분류)

## Status 상태 흐름

| 폴더 | 상태값 |
|------|--------|
| inbox/ | `raw` → `used` |
| drafts/ | `developing` → `filed` |

## 핵심 규칙

- 질문은 **하나씩 순차적으로**
- 사용자 **컨펌 없이 library에 저장하지 않음**
- 템플릿 파일 (`_template.md`) 처리 대상 제외
- slug는 영문 kebab-case

## Source Tracking

inbox 파일 사용 시:
- 해당 파일의 `status` → `used`, `used_in` → drafts 경로
- drafts 파일의 `sources` 배열에 추가

## Frontmatter 필드

| 폴더 | 필수 필드 |
|------|----------|
| inbox/thoughts/ | `title`, `date`, `status` (raw/used), `used_in` |
| inbox/materials/ | `title`, `date`, `source`, `type`, `status` |
| drafts/ | `title`, `created`, `updated`, `turns`, `status`, `sources` |
| library/ | `title`, `domain` |

## 세션 시작 시

세션 시작 시 자동으로:
- `drafts/`에서 `status: developing` 파일 확인
- `inbox/thoughts/`에서 `status: raw` 파일 확인
- 진행 중인 작업이 있으면 안내
