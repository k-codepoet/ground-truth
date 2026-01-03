---
title: Forgify 플러그인 검수 및 개선 가능성
domain: ai-automation
views: []
---

## Context

Forgify는 Claude Code 플러그인 개발을 AI에게 위임하는 도구다. 원래 engineering 영역(직접 만드는 것)이었던 작업을 자동화했다. 이 문서는 forgify의 현재 상태를 검수하고 개선 가능성을 정리한다.

**시초 문서**: [claude-code-extension-fundamentals](../engineering/claude-code-extension-fundamentals.md)

## Content

### 플러그인 정체성

**Forgify** = "Forge your ideas into Claude extensions"
- **버전**: 1.3.0
- **구성**: 7 Skills (지식) + 6 Commands (도구)
- **목적**: Claude Code 확장 개발 가이드 (한국어)

### 구조

**Skills (자동 활성화 지식)**
| 스킬 | 역할 |
|------|------|
| plugin-guide | 플러그인 구조, plugin.json |
| command-guide | 슬래시 커맨드 작성법 |
| agent-guide | 서브에이전트 작성법 |
| skill-guide | SKILL.md, Agent Skills 표준 |
| hook-guide | 훅 이벤트, hooks.json |
| marketplace-guide | 마켓플레이스 구축 |
| workflow-guide | 실전 워크플로우 |

**Commands (명시적 도구)**
| 커맨드 | 역할 |
|--------|------|
| help | 도움말 |
| howto | 가이드 주제 조회 |
| create | 경로 기반 플러그인 생성 |
| compose | 여러 플러그인 조립 |
| validate | 가이드라인 준수 검증 |
| update | 최신 가이드라인 갱신 |

### 강점

1. **체계적 학습 경로**: Plugin → Skill → Agent → Command → Hook → Marketplace → Workflow
2. **Progressive Disclosure**: Skills는 자동, Commands는 명시적 호출로 분리
3. **개발 사이클 커버**: create → compose → validate → update
4. **실수 방지**: agents 필드 형식(디렉토리 불가) 검증

### 개선 필요 사항

| 우선순위 | 항목 | 현황 | 개선안 |
|----------|------|------|--------|
| **High** | 공식 문서 동기화 | 특정 시점 고정 | WebFetch로 최신 내용 확인 |
| **Medium** | 검증 자동화 | 수동 호출만 | Hook 기반 실시간 피드백 |
| **Medium** | 테스트 가이드 | 없음 | 로컬 설치, 디버그 모드 안내 |
| **Low** | 예시 보강 | 개념만 있음 | references/ 폴더에 실제 예시 |
| **Low** | 네이밍 통일 | 디렉토리≠plugin name | 디렉토리명도 forgeify로 |

### 핵심 인사이트

> Forgify는 **플러그인 개발의 진입 장벽을 낮추는 좋은 도구**다. 특히 한국어 사용자에게 유용하다. 다만 **지속 가능한 유지보수**를 위해 공식 문서 동기화, 자동 검증이 필요하다.

### 계보 (Lineage)

```
engineering (시초)
  └─ claude-code-extension-fundamentals.md
        ↓ AI에게 위임
ai-automation (현재)
  └─ forgify-plugin-review.md (이 문서)
```

## Connections

- [claude-code-extension-fundamentals](../engineering/claude-code-extension-fundamentals.md) - 시초: 플러그인 개발 기초
- [improve-plugin-workflow](./improve-plugin-workflow.md) - 플러그인 개선 워크플로우
- [ced-plugin-agents-marketplace-fix](../engineering/ced-plugin-agents-marketplace-fix.md) - agents 검증 자동화
