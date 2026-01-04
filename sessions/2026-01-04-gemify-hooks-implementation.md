---
title: gemify/forgeify Stop 훅 구현
date: 2026-01-04
type: session-report
status: completed
tags: [gemify, forgeify, hooks, claude-code, plugin]
---

## Summary

gemify와 forgeify 플러그인에 Stop 훅을 추가하여 세션 종료 시 안내 메시지를 표시하도록 구현. `type: "prompt"` 버그를 발견하고 `type: "command"` workaround로 해결.

## 주요 성과

### 1. 버그 발견 및 문서화
- Claude Code 플러그인에서 `type: "prompt"` 훅이 silently ignore됨
- GitHub Issue #13155 참조
- forgeify hook-guide에 Known Issues로 문서화

### 2. Workaround 적용
- `type: "command"` + 셸 스크립트 방식으로 대체
- JSON 출력 (`{"continue": true, "systemMessage": "..."}`)으로 메시지 전달
- 대화형 모드에서 정상 동작 확인

### 3. 플러그인 업데이트
- gemify `1.16.7`: Stop 훅 + scripts/stop-hook.sh
- forgeify `1.7.2`: Stop 훅 + scripts/stop-hook.sh + hook-guide 업데이트

## Outputs

### my-claude-plugins (vk/4eb1-gemify-hooks)
| 파일 | 변경 |
|------|------|
| `plugins/gemify/hooks/hooks.json` | command 타입으로 변경 |
| `plugins/gemify/scripts/stop-hook.sh` | 신규 생성 |
| `plugins/gemify/.claude-plugin/plugin.json` | 1.16.7 |
| `plugins/forgeify/hooks/hooks.json` | command 타입으로 변경 |
| `plugins/forgeify/scripts/stop-hook.sh` | 신규 생성 |
| `plugins/forgeify/skills/hook-guide/SKILL.md` | Stop 훅 가이드 + Known Issues |
| `plugins/forgeify/.claude-plugin/plugin.json` | 1.7.2 |

### ground-truth (stage0)
| 파일 | 변경 |
|------|------|
| `library/specs/gemify-draft-history-hooks.md` | SUCCESS (with workaround) 상태 |
| `inbox/materials/2026-01-04-hooks-validation-need.md` | 신규 |
| `inbox/thoughts/2026-01-04-hooks-validation-plugin-idea.md` | 신규 |

## Stashed for Next

| 위치 | 내용 |
|------|------|
| `inbox/thoughts/2026-01-04-hooks-validation-plugin-idea.md` | hooks-validator 플러그인 아이디어 |
| `inbox/materials/2026-01-04-hooks-validation-need.md` | 검증 필요 항목 정리 |

## Next Actions

- [ ] hooks-validator 플러그인 생성 (모든 이벤트 타입 동작 검증)
- [ ] `-p` 모드에서 Stop 훅 미실행 이슈 조사
- [ ] `type: "prompt"` 버그 수정 시 플러그인 업데이트

## 학습된 내용

1. 플러그인 hooks.json은 `hooks/hooks.json` 위치에 자동 로드됨
2. `type: "prompt"`는 플러그인에서 미지원 (v2.0.76 기준)
3. Stop 훅은 대화형 모드에서만 동작 (`-p` 모드 불가)
4. JSON 출력의 `systemMessage` 필드가 사용자에게 표시됨
