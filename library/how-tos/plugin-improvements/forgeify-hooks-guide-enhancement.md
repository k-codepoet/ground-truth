---
title: "forgeify hooks-guide 보강 및 validate 연동"
target_plugin: forgeify
improvement_type: bugfix
priority: high
problem: "Claude Code 플러그인 hooks가 동작하지 않음. hooks.json 포맷, 매처 규칙 등 구현 규칙이 명확하지 않아 실수하기 쉬움."
solution: "forgeify의 hooks-guide 문서를 보강하여 올바른 hooks 구현 규칙을 제공하고, validate 스킬에서 이를 검증하도록 연동"
requirements:
  - hooks-guide 문서에 올바른 hooks.json 포맷 명시
  - 매처 규칙 (tool name, 대소문자, glob 패턴) 상세 설명
  - 디버그 방법 (claude --debug) 안내
  - validate 스킬에서 hooks.json 검증 로직 추가
references:
  - inbox/materials/2026-01-04-claude-plugin-hooks-debug.md
  - inbox/thoughts/2026-01-04-plugin-hooks-not-working.md
type: how-to
origin: original
---

## Why

gemify, forgeify 등 플러그인에 구현한 hooks가 동작하지 않는 문제 발생. perplexity와 조사한 결과:

1. **포맷 문제**: 플러그인 `hooks/hooks.json` 구조가 요구사항과 다름
2. **매처 오류**: tool name, 대소문자, glob 패턴 불일치
3. **세션 이슈**: 훅 변경 후 Claude 세션 재시작 누락

현재 forgeify의 hooks-guide가 이 부분을 충분히 다루지 않아 같은 실수가 반복됨.

## What

### 1. hooks-guide 문서 보강

forgeify의 `SKILL.md` (hooks-guide)에 다음 내용 추가:

**올바른 hooks.json 포맷**
```json
{
  "hooks": [
    {
      "event": "PreToolUse",
      "matcher": "Bash",
      "command": ["./scripts/pre-bash.sh"]
    }
  ]
}
```

**주요 검증 포인트**
- `event`: PreToolUse, PostToolUse, Stop 등 정확한 이벤트명
- `matcher`: Tool 이름 대소문자 정확히 일치 (Bash, Read, Write 등)
- `command`: 배열 형태, 실행 권한 확인

**디버깅 방법**
```bash
claude --debug  # 훅 로딩/실행 로그 확인
/hooks          # 현재 로드된 훅 목록 확인
```

### 2. validate 스킬에서 hooks 검증

`/forgeify:validate` 실행 시 다음 검증 추가:

- [ ] hooks/hooks.json 존재 여부
- [ ] JSON 파싱 가능 여부
- [ ] event 필드가 유효한 값인지
- [ ] matcher가 실제 Tool 이름과 일치하는지
- [ ] command 배열의 스크립트 파일 존재 및 실행 권한

## Scope

**포함**:
- forgeify hooks-guide 문서 보강
- forgeify validate 스킬에 hooks 검증 로직 추가

**제외**:
- 다른 플러그인 수정 (검증 후 별도 적용)
- hooks 기능 자체 변경 (Claude Code 내부)

## 적용 순서

1. forgeify hooks-guide 보강
2. forgeify validate에 hooks 검증 추가
3. gemify 플러그인에서 hooks 수정 시도
4. `claude --debug`로 동작 검증
5. 성공 시 나머지 플러그인에 동일 패턴 적용
