# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(library)으로 변환합니다.

```
/gemify:inbox → /gemify:draft → /gemify:library → /gemify:view
    inbox/         drafts/         library/          views/
```

**태그라인**: Turn your thoughts into gems.

## Commands

### 핵심 파이프라인

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/gemify:inbox [내용]` | 내 생각 포착 | inbox/thoughts/ |
| `/gemify:import [내용]` | 외부 재료 가져오기 | inbox/materials/ |
| `/gemify:draft [파일/아이디어]` | 원석 다듬기 (대화로 확장) | drafts/ |
| `/gemify:library [파일]` | 보석 정리 (library로) | library/ |
| `/gemify:view [subject]` | library를 주제별로 조합 | views/by-subject/ |

### 보조 명령어

| 명령어 | 설명 |
|--------|------|
| `/gemify:capture-pair` | 대화에서 material + thought 쌍으로 동시 추출 |
| `/gemify:retro` | 이미 완료된 작업을 역방향으로 library에 기록 |
| `/gemify:improve-plugin [경로]` | 플러그인 개선 (add-dir 후 작업) |
| `/gemify:setup [path]` | Gemify 구조 초기화 (`--examples` 옵션 가능) |
| `/gemify:help` | 도움말 |
| `/gemify:howto` | 사용 가이드 |

## /gemify:draft 대화 모드

```
├── facet  - 여러 면 탐색, 넓게 (기본)
└── polish - 깊이 연마 → library 준비
```

**polish 트리거**: "연마해봐", "좀 더 다듬자", "핵심이 뭐야"

**File 전환 조건** (제안만, 강요 안 함):
- turns >= 5
- Open Questions 대부분 해결
- 같은 포인트 반복

## 데이터 흐름

### 디렉토리

| 경로 | 용도 |
|------|------|
| `inbox/thoughts/` | 내 생각 (원석) |
| `inbox/materials/` | 외부 재료 (기사, 문서, 대화 등) |
| `drafts/` | 다듬는 중인 아이디어 |
| `drafts/.history/{slug}/` | pivot 시 스냅샷 |
| `library/{domain}/` | 완성된 지식 (domain별 분류) |
| `views/by-subject/` | library를 주제별로 조합한 뷰 |

### Status 상태 흐름

| 폴더 | 상태값 |
|------|--------|
| inbox/ | `raw` → `used` |
| drafts/ | `cutting` → `set` |

### Source Tracking

inbox 파일 사용 시:
- 해당 파일의 `status` → `used`, `used_in` → drafts 경로
- drafts 파일의 `sources` 배열에 추가

## 6대 Domain (library 분류)

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

## Frontmatter 필드

| 폴더 | 필수 필드 |
|------|----------|
| inbox/thoughts/ | `title`, `date`, `status` (raw/used), `used_in`, `references` |
| inbox/materials/ | `title`, `date`, `source`, `type` (article\|document\|conversation\|snippet\|other), `status`, `used_in` |
| drafts/ | `title`, `created`, `updated`, `turns`, `revision`, `status` (cutting→set), `sources`, `history` |
| library/ | `title`, `domain`, `views` (해당 문서가 포함된 view 목록 - 역참조) |
| views/by-subject/ | `title`, `subject`, `updated`, `sources` (library 문서 경로 목록) |

## 파일 네이밍

- **inbox/thoughts/**: `YYYY-MM-DD-{slug}.md`
- **inbox/materials/**: `YYYY-MM-DD-{slug}.md`
- **drafts/**: `{slug}.md`
- **library/**: `{slug}.md` (domain 폴더 내)
- **views/by-subject/**: `{subject}.md`
- slug는 영문 kebab-case

## 핵심 규칙

- 질문은 **하나씩 순차적으로**
- 사용자 **컨펌 없이 library에 저장하지 않음**
- 템플릿 파일 (`_template.md`) 처리 대상 제외

## 세션 시작 시

SessionStart hook 자동 실행:
- `drafts/`에서 `status: cutting` 파일 확인
- `inbox/thoughts/`에서 `status: raw` 파일 확인
- 진행 중인 작업 있으면 `/gemify:draft`로 이어가기 안내
- `_template.md`는 제외
