---
title: CED 플러그인 가이드 vs 공식 문서 비교 분석
date: 2026-01-02
source: Claude Code 공식 문서 웹검색 비교
type: document
status: used
used_in: ced 플러그인 개선 작업
---

# CED 플러그인 가이드 vs 공식 문서 비교

## 검증 대상
- skill-guide, plugin-guide, command-guide, agent-guide, hook-guide, marketplace-guide

## 토큰 규칙 (Progressive Disclosure)

| 레이어 | ced 가이드 | 공식 문서 | 일치 |
|--------|-----------|----------|------|
| Metadata | ~100 토큰 | ~100 토큰 (30-50/스킬) | ✅ |
| Instructions | <5000 토큰 | <5k 토큰 | ✅ |
| SKILL.md 전체 | - | <10,000 토큰 (~500 lines) | ℹ️ |

## 일치하는 가이드
- **Skill Guide**: Progressive Disclosure, 토큰 규칙 정확
- **Agent Guide**: frontmatter 필드, 내장 subagent 정확
- **Plugin Guide**: 구조, 필드 정확
- **Marketplace Guide**: 구조, 필드 정확

## 누락/차이 발견

### Command Guide 누락 필드
| 필드 | 설명 |
|------|------|
| `model` | 모델 지정 가능 (예: `claude-3-5-haiku-20241022`) |
| `disable-model-invocation` | 모델이 자동 호출 못하게 차단 |

### Hook Guide 누락 이벤트
| 이벤트 | 설명 |
|--------|------|
| `Stop` | 턴 종료 시 |
| `SubagentStop` | 서브에이전트 종료 시 |
| `PreCompact` | 컴팩트 전 |

### Hook Guide 검증 필요
- `PostToolUseFailure`: 공식 문서에서 별도 언급 없음
- Hook 타입 `agent`: 공식에서 `command`, `prompt`만 명시

## 참조 공식 문서
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/slash-commands
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/plugin-marketplaces
