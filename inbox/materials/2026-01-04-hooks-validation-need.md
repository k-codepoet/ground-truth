---
title: Claude Code hooks 동작 검증 필요성
type: material
status: raw
created: 2026-01-04
source: gemify hooks 구현 세션
tags: [claude-code, hooks, plugin, validation, testing]
---

## 배경

gemify/forgeify 플러그인에 Stop 훅을 추가하는 과정에서 다수의 문제 발견.

## 발견된 이슈들

### 1. `type: "prompt"` 훅이 플러그인에서 작동 안 함
- GitHub Issue: #13155
- 플러그인 hooks.json에서 silently ignore됨
- `type: "command"`만 지원

### 2. hooks.json 위치 혼란
- 문서: `hooks/hooks.json`
- 초기 시도: `.claude-plugin/hooks.json` → 로드 안 됨
- plugin.json에 hooks 필드 필요 여부도 불명확 (자동 로드됨)

### 3. `-p` 모드에서 Stop 훅 미실행
- `claude -p "테스트"`에서는 Stop 훅이 트리거되지 않음
- 대화형 모드에서만 동작

### 4. JSON 출력 포맷
- 단순 echo는 동작 안 함
- `{"continue": true, "systemMessage": "..."}` 형식 필요
- 문서에서 명확히 설명되지 않은 부분들 있음

### 5. 디버그 로그 해석 어려움
- `Registered N hooks` vs `Matched N hooks` 구분
- 훅 실행 여부 확인하려면 로그 심층 분석 필요

## 검증이 필요한 항목

- [ ] 모든 이벤트 타입별 동작 여부 (PreToolUse, PostToolUse, Stop, SessionStart 등)
- [ ] `type: "command"` vs `type: "prompt"` 지원 범위
- [ ] matcher 패턴 동작
- [ ] JSON 출력 필드별 효과
- [ ] 종료 코드별 동작 (exit 0, 2, 기타)
- [ ] 플러그인 훅 vs 사용자 설정 훅 차이
