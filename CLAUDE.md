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
| `/gemify:sidebar` | 본 작업 중 떠오른 것을 material + thought 쌍으로 옆에 빼두기 |
| `/gemify:retro` | 이미 완료된 작업을 역방향으로 library에 기록 |
| `/gemify:wrapup` | 세션 마무리 (HITL 체크 → 리포트 생성) |
| `/gemify:improve-plugin [경로]` | 플러그인 개선 (add-dir 후 작업) |
| `/gemify:setup [path]` | Gemify 구조 초기화 (`--examples` 옵션 가능) |
| `/gemify:help` | 도움말 |
| `/gemify:howto` | 사용 가이드 |

## 디렉토리 구조

```
inbox/          → 원석 (thoughts/, materials/)
drafts/         → 다듬는 중 (status: cutting → set)
library/        → 완성된 지식 (Type별 분류)
  ├── principles/   근본 원칙
  ├── decisions/    의사결정 기록
  ├── insights/     학습/발견
  ├── how-tos/      절차/방법
  ├── specs/        스펙/정의
  └── workflows/    워크플로우/프로세스
views/          → 주제별 조합 (by-subject/, .history/)
sessions/       → 세션 리포트
```

## Library Type 분류

| Type | 설명 | 핵심 질문 |
|------|------|----------|
| principle | 근본 원칙 | 왜 이렇게 해야 하는가? |
| decision | 의사결정 기록 | 무엇을 선택했고 왜? |
| insight | 학습/발견 | 무엇을 알게 됐는가? |
| how-to | 절차/방법 | 어떻게 하는가? |
| spec | 스펙/정의 | 정확히 무엇인가? |
| workflow | 워크플로우 | 어떤 순서로 진행하는가? |

## Origin 분류

| Origin | 설명 |
|--------|------|
| original | 직접 생성한 지식 |
| digested | 외부 자료를 소화해서 재구성 |
| derived | 기존 문서에서 파생 |

## Frontmatter 필수 필드

**inbox/thoughts/**
```yaml
title: "{제목}"
date: YYYY-MM-DD
status: raw
```

**inbox/materials/**
```yaml
title: "{제목}"
date: YYYY-MM-DD
source: "(URL, 대화, 문서 등)"
type: article|document|conversation|snippet|other
status: raw
```

**drafts/**
```yaml
title: "{제목}"
status: cutting|set    # cutting: 진행 중, set: 완료
```

**library/**
```yaml
title: "{제목}"
type: {6가지 type 중 하나}
origin: original|digested|derived
```

**views/by-subject/**
```yaml
subject: {주제명}
artifact: {연결된 결과물 경로}
sources: [library 문서 목록]
```

## 파일명 규칙

- **thoughts/materials**: `YYYY-MM-DD-{slug}.md`
- **drafts**: `{slug}.md`
- **library**: `{slug}.md`
- **views**: `{subject}.md`
- **sessions**: `YYYY-MM-DD-{slug}.md`

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
