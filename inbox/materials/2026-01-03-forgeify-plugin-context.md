---
title: "Forgeify 플러그인 맥락 (병렬 작업용)"
date: 2026-01-03
source: "/home/choigawoon/k-codepoet/my-claude-plugins/plugins/forgeify/"
type: document
status: raw
used_in:
---

## 플러그인 기본 정보

| 항목 | 값 |
|------|-----|
| 이름 | forgeify |
| 버전 | 1.3.0 |
| 태그라인 | "Forge your ideas into Claude extensions" |
| 역할 | Claude Code 플러그인 개발 가이드 |

## -fy 제품군에서의 위치

```
┌─────────────────────────────────────────────────────────┐
│  -fy 제품군                                              │
├─────────────────────────────────────────────────────────┤
│  [사용자 문제 해결]                                       │
│  Gemify   💎  지식 관리 (WHAT)                          │
│  Terrafy  🏗️  인프라 관리 (WHERE)                       │
│  Craftify 🔨  개발 자동화 (HOW)                         │
│  Namify   🏷️  제품 네이밍                               │
├─────────────────────────────────────────────────────────┤
│  [메타 레벨 - 플러그인 개발 도구]                         │
│  Forgeify 🔥  위 플러그인들을 만드는 도구                 │
└─────────────────────────────────────────────────────────┘
```

## 7개 Skills (가이드)

| 스킬 | 파일 | 설명 |
|------|------|------|
| plugin-guide | skills/plugin-guide/ | 플러그인 구조, plugin.json 스키마 |
| skill-guide | skills/skill-guide/ | SKILL.md 작성법, Agent Skills 표준 |
| agent-guide | skills/agent-guide/ | 서브에이전트 정의, frontmatter 필드 |
| command-guide | skills/command-guide/ | 슬래시 커맨드 YAML frontmatter |
| hook-guide | skills/hook-guide/ | Hook 이벤트, hooks.json 작성 |
| marketplace-guide | skills/marketplace-guide/ | 마켓플레이스 배포 방법 |
| workflow-guide | skills/workflow-guide/ | 전체 개발 워크플로우 예시 |

## 6개 Commands

| 커맨드 | 설명 |
|--------|------|
| `/forgeify:help` | 도움말 표시 |
| `/forgeify:howto` | 가능한 가이드 주제 목록 |
| `/forgeify:howto <topic>` | 특정 주제 가이드 표시 |
| `/forgeify:create <path>` | 경로 기반 플러그인 생성 |
| `/forgeify:compose <plugins>` | 여러 플러그인 조립 |
| `/forgeify:validate [path]` | 가이드라인 준수 검증 |
| `/forgeify:update [path]` | 최신 가이드라인으로 갱신 |

## 사용 패턴

**명시적 호출**:
```bash
/forgeify:howto plugin    # 플러그인 구조
/forgeify:howto agent     # 에이전트 작성
/forgeify:howto skill     # 스킬 작성
```

**자동 활성화**:
```
"플러그인 만드는 방법 알려줘"
"agent 파일 어떻게 작성해?"
"hook 이벤트 종류가 뭐야?"
```

## 강점 (검수 결과)

1. **체계적 학습 경로**: 7개 주제가 Plugin 개발 사이클 전체 커버
2. **Progressive Disclosure**: 필요할 때 관련 가이드 자동 활성화
3. **한국어 문서화**: 공식 문서가 영어인 점을 보완

## 개선 가능성 (검수 결과)

| 우선순위 | 항목 | 설명 |
|---------|------|------|
| High | 공식 문서 동기화 | Claude Code 업데이트 시 자동 반영 메커니즘 |
| Medium | 검증 자동화 | `/forgeify:validate` 강화 |
| Medium | 테스트 가이드 | 플러그인 테스트 방법 추가 |

## 참고 자료

- [Agent Skills 표준](https://agentskills.io)
- [Claude Code Plugins Reference](https://code.claude.com/docs/en/plugins-reference)
- [Claude Code Hooks Guide](https://code.claude.com/docs/en/hooks-guide)

## 병렬 작업자 안내

이 파일을 읽고 다음 단계 진행:
1. `inbox/thoughts/2026-01-03-forgeify-plugin-purpose.md` 함께 참고
2. 기존 `library/ai-automation/forgify-plugin-review.md` 참고
3. `/gemify:draft` 실행하여 drafts 생성
4. facet 모드로 가이드 구조, 학습 경로 탐색
5. polish 모드로 핵심 정리
6. `/gemify:library`로 library 저장 (domain: ai-automation 또는 product)
7. `/gemify:view`로 forgeify.md 생성

## 참고 경로

플러그인 소스: `/home/choigawoon/k-codepoet/my-claude-plugins/plugins/forgeify/`
