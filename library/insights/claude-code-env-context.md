---
title: Claude Code 환경 컨텍스트 활용
type: insight
origin: digested
views: [gemify]
---

# Claude Code 환경 컨텍스트 활용

## 핵심

Claude Code는 대화 시작 시 시스템 프롬프트에 `<env>` 블록을 자동 주입받는다. 사용자가 명시적으로 알려주지 않아도 작업 환경을 파악하고 있음.

## 주입되는 정보

| 항목 | 설명 |
|------|------|
| Working directory | 현재 작업 디렉토리 |
| Additional working directories | `--add-dir`로 추가한 경로들 |
| Is directory a git repo | git 저장소 여부 |
| Platform / OS Version | 운영체제 정보 |
| Today's date | 오늘 날짜 |

## 동적 경로 추가 방법

| 방식 | 사용법 | 범위 |
|------|--------|------|
| `/add-dir` | 세션 중 `/add-dir /path/to/dir` | 세션만 |
| `--add-dir` | CLI 시작 시 플래그 | 세션만 |
| `settings.json` | `additionalDirectories` 배열 | 영구 (재시작 필요) |

## Permission 규칙

- **Read/Grep/Glob** (읽기): permission 불필요
- **Write/Edit/Bash** (쓰기/실행): permission prompt

## 활용 패턴

skill이나 hook에서 사용자에게 경로를 요청하고 동적으로 접근:

1. 사용자로부터 경로 받기 (AskUserQuestion)
2. 이미 접근 가능하면 바로 작업
3. 아니면 `/add-dir <path>` 안내
4. 자주 쓰는 경로면 `settings.json`에 영구 등록 제안 (재시작 필요 안내)
