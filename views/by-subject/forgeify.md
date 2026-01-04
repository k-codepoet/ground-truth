---
title: "Forgeify Plugin 종합 View"
subject: forgeify
created: 2026-01-03
updated: 2026-01-03
revision: 3
artifact: plugins/forgeify/
artifact_type: plugin
sources:
  - library/engineering/claude-code-extension-fundamentals.md
  - library/ai-automation/forgify-plugin-review.md
  - library/engineering/plugin-improvements/gemify-forgeify-protocol.md
  - library/engineering/plugin-improvements/forgeify-improve-command.md
  - library/ai-automation/bootstrapping-principle.md
history:
  - revision: 2
    date: 2026-01-03
    changes: v1.4.0 업데이트 (improve-plugin 추가)
---

# Forgeify Plugin 종합 View

## 구조 (도식)

```
┌─────────────────────────────────────────────────────────────────┐
│                       Forgeify Plugin                            │
│       "Forge your ideas into Claude extensions"                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
            ┌─────────────┐      ┌─────────────┐
            │   Skills    │      │  Commands   │
            │   (지식)    │      │   (도구)    │
            └─────────────┘      └─────────────┘
                    │                   │
         ┌──────────┼──────────┐        │
         ▼          ▼          ▼        ▼
    ┌─────────┐┌─────────┐┌─────────┐┌──────────┐
    │ plugin  ││  skill  ││  agent  ││ create   │
    │ -guide  ││ -guide  ││ -guide  ││ validate │
    └─────────┘└─────────┘└─────────┘│ update   │
    ┌─────────┐┌─────────┐┌─────────┐│ compose  │
    │ command ││  hook   ││workflow ││ howto    │
    │ -guide  ││ -guide  ││ -guide  ││ help     │
    └─────────┘└─────────┘└─────────┘│ improve- │
    ┌─────────┐                      │ plugin   │
    │improve- │                      └──────────┘
    │ plugin  │
    └─────────┘

    v1.4.0 핵심: gemify ↔ forgeify 분리
    ┌─────────────────────────────────────────────────────────────┐
    │  gemify (지식 생산)        forgeify (실행)                  │
    │      │                         │                            │
    │      └── 개선 문서 생성 ──────▶ 개선 문서 실행              │
    │          (library/...)         (/forgeify:improve-plugin)   │
    └─────────────────────────────────────────────────────────────┘

    메타 구조:
    ┌─────────────────────────────────────────────────────────────┐
    │  Forgeify = 다른 플러그인을 만들기 위한 플러그인 (메타 레벨) │
    │  Gemify, Terrafy, Craftify, Namify → 사용자 문제 해결       │
    │  Forgeify → 위 플러그인들을 만드는 데 도움                  │
    └─────────────────────────────────────────────────────────────┘
```

## 스토리 (왜 → 뭘 → 어디까지)

### 왜 만들었나

-fy 플러그인들(Gemify, Terrafy, Craftify, Namify)을 만들 때 반복되는 질문들:
- 어떻게 skill 파일을 작성하는지
- agent는 어떤 구조인지
- hook은 언제 쓰는지
- plugin.json은 어떤 필드가 필요한지

이런 질문에 바로 답해주는 **한국어 가이드 도구**가 필요했음.

### 무엇을 만들었나

**Forgeify** - Claude Code 플러그인 개발의 메타 도구

| 구분 | 내용 |
|------|------|
| 버전 | **v1.4.0** |
| 정체성 | 다른 플러그인을 만들기 위한 플러그인 |
| 구성 | 8 Skills (지식) + 7 Commands (도구) |
| 철학 | Progressive Disclosure + 지식/실행 분리 |

**8개 Skills (자동 활성화 지식)**

| 스킬 | 주제 |
|------|------|
| plugin-guide | 플러그인 구조, plugin.json |
| skill-guide | SKILL.md 작성법, Agent Skills 표준 |
| agent-guide | 서브에이전트 정의, frontmatter |
| command-guide | 슬래시 커맨드 작성 |
| hook-guide | Hook 이벤트, hooks.json |
| marketplace-guide | 마켓플레이스 배포 |
| workflow-guide | 전체 개발 워크플로우 |
| **improve-plugin** | **개선 문서 기반 플러그인 수정 (v1.4.0 신규)** |

**7개 Commands (명시적 도구)**

| 커맨드 | 역할 |
|--------|------|
| help | 도움말 |
| howto | 가이드 주제 조회 |
| create | 경로 기반 플러그인 생성 |
| compose | 여러 플러그인 조립 |
| validate | 가이드라인 준수 검증 |
| update | 최신 가이드라인 갱신 |
| **improve-plugin** | **개선 문서 실행 (v1.4.0 신규)** |

### 어디까지 왔나

**강점 (현재)**
1. 체계적 학습 경로: Plugin → Skill → Agent → Command → Hook → Marketplace → Workflow
2. Progressive Disclosure: Skills는 자동, Commands는 명시적 호출로 분리
3. 개발 사이클 커버: create → compose → validate → update
4. 실수 방지: agents 필드 형식(디렉토리 불가) 검증

**개선 필요 (다음)**

| 우선순위 | 항목 | 핵심 |
|----------|------|------|
| High | 문서 동기화 | 공식 스펙 변경 시 outdated 방지 (WebFetch + diff) |
| Medium | 검증 자동화 | Hook 기반 실시간 피드백 |
| Medium | 테스트 가이드 | 로컬 설치, 디버그 모드 안내 |
| Low | 예시 보강 | references/ 폴더에 실제 예시 |

## 핵심 원칙

1. **메타 레벨**: 플러그인을 만드는 플러그인
2. **Progressive Disclosure**: 필요한 것만 필요할 때
3. **한국어 가이드**: 진입 장벽 낮추기
4. **지식/실행 분리 (v1.4.0)**: gemify가 개선 문서 생성, forgeify가 실행

## gemify ↔ forgeify 프로토콜

v1.4.0의 핵심: 지식 생산과 실행의 분리

```
ground-truth (gemify)              마켓플레이스 (forgeify)
─────────────────────              ──────────────────────
/gemify:improve-plugin             /forgeify:improve-plugin <문서>
     ↓                                   ↓
개선 문서 생성                      문서 참조 → 코드 수정
library/engineering/
  plugin-improvements/
```

**개선 문서 스키마 (Progressive Disclosure)**:

| Layer | 내용 | 용도 |
|-------|------|------|
| frontmatter | problem, solution, requirements | 빠른 판단 |
| body | Why, What, Scope | 이해 |
| references/ | 구현 힌트, 상세 스펙 | 실행 시 필요시만 |

## 계단식 부트스트래핑

```
gemify (지식 생산)          forgeify (코드 실행)
    │                            │
    ├─ improve-plugin 문서 ──────→ 코드 수정
    │                            │
    ←── 플러그인 검수/버그픽스 ────┘
```

- gemify로 조사, 계획, 의사결정
- forgeify로 코드 수정, 검수, 버그픽스
- 둘이 서로를 점진적으로 개선
- 사람(HITL)이 방향성과 중심을 잡음

## 계보 (Lineage)

```
engineering (시초)
  └─ claude-code-extension-fundamentals.md
        ↓ AI에게 위임
ai-automation (현재)
  └─ forgify-plugin-review.md
        ↓ 프로토콜 확립
engineering/plugin-improvements (v1.4.0)
  ├─ gemify-forgeify-protocol.md
  └─ forgeify-improve-command.md
```

## 관련 문서

### 기초/시초
- [Claude Code 확장 개발 기초](../../library/engineering/claude-code-extension-fundamentals.md) - 플러그인 개발 기본 구조

### 검토/개선
- [Forgify 플러그인 검수 및 개선 가능성](../../library/ai-automation/forgify-plugin-review.md) - 강점과 개선점 분석

### v1.4.0 프로토콜
- [gemify-forgeify 개선 문서 프로토콜](../../library/engineering/plugin-improvements/gemify-forgeify-protocol.md) - 단방향 흐름 설계
- [forgeify-improve-command 개선 문서](../../library/engineering/plugin-improvements/forgeify-improve-command.md) - improve-plugin 구현 스펙

### 원칙
- [계단식 부트스트래핑 원칙](../../library/ai-automation/bootstrapping-principle.md) - gemify ↔ forgeify 순환 구조

### 연관 패턴
- [improve-plugin-workflow](../../library/ai-automation/improve-plugin-workflow.md) - 플러그인 개선 워크플로우
- [ced-plugin-agents-marketplace-fix](../../library/engineering/ced-plugin-agents-marketplace-fix.md) - agents 검증 자동화
