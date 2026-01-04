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
drafts/         → 다듬는 중
library/        → 완성된 재료 (6대 domain별 분류)
views/          → 레시피 + 결과물 연결
sessions/       → 세션 리포트
```

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
