# Ground Truth - Project Index

> **Last Updated**: 2025-12-31
> **Status**: Stage 0 (Manual Verification Phase)

---

## Overview

Ground Truth는 개인 지식 파이프라인 시스템입니다. 머릿속 암묵지를 구조화된 지식(corpus)으로 변환하고, 다양한 형태(agent-docs, blog, book 등)로 내보내는 것을 목표로 합니다.

### Core Philosophy

```
HEAD (암묵지) → INBOX (raw 캡처) → CORPUS (구조화) → EXPORTS (다양한 형태)
```

### 6대 Domain

| Domain | 핵심 질문 | 용도 |
|--------|----------|------|
| `product` | 무엇을 만들 것인가? | 제품 기획, PRD, 사용자 문제 |
| `engineering` | 어떻게 만들 것인가? | 코드, 아키텍처, 구현 |
| `operations` | 어떻게 돌릴 것인가? | 배포, 인프라, 모니터링 |
| `growth` | 어떻게 알릴 것인가? | 마케팅, 콘텐츠, SEO |
| `business` | 어떻게 유지할 것인가? | 수익, 계약, 법률 |
| `ai-automation` | 어떻게 위임할 것인가? | Agent, LLM, 워크플로우 |

---

## Directory Structure

```
ground-truth/
├── README.md                           # 프로젝트 소개 및 Stage 0 워크플로우
│
├── inbox/                              # Raw 입력 (자유 형식)
│   ├── _template.md                    # inbox 문서 템플릿
│   ├── INFRA-SETUP.md                  # 홈랩 인프라 설정
│   ├── Hashbrown.dev Overview.md       # 생성형 UI 프레임워크 연구
│   └── *.md                            # 기타 미처리 문서
│
├── corpus/                             # 구조화된 지식 저장소
│   ├── _template.md                    # corpus 문서 템플릿
│   ├── product/                        # 제품 기획 관련
│   ├── engineering/                    # 기술 구현 관련
│   ├── operations/                     # 운영/인프라 관련
│   ├── growth/                         # 마케팅/성장 관련
│   ├── business/                       # 비즈니스 관련
│   └── ai-automation/                  # AI 자동화 관련
│
├── brainstorm/                         # 개선안 및 전략 문서
│   ├── 00-summary-and-priorities.md    # 전체 요약 및 우선순위
│   ├── 01-mvp-execution-strategy.md    # MVP 실행 전략
│   ├── 02-input-pipeline-improvement.md # 입력 파이프라인 개선
│   ├── 03-export-diversification.md    # Export 다양화 전략
│   └── 04-ai-automation-roadmap.md     # AI 자동화 로드맵
│
├── skills/                             # Claude Code Skills
│   └── knowledge-digest/               # 지식 소화 스킬
│       └── SKILL.md                    # 소크라테스식 질문 기반 지식 정리
│
├── .claude/                            # Claude Code 설정
│   └── commands/                       # 슬래시 커맨드
│       └── digest.md                   # /digest 커맨드 정의
│
├── docs/                               # 문서화
│   ├── humans/                         # 사람을 위한 문서
│   │   ├── claude-code/                # Claude Code 생태계 가이드
│   │   │   ├── README.md               # 개요
│   │   │   ├── skills.md               # 스킬 가이드
│   │   │   ├── commands.md             # 커맨드 가이드
│   │   │   ├── agents.md               # 에이전트 가이드
│   │   │   ├── hooks.md                # 훅 가이드
│   │   │   ├── plugin.md               # 플러그인 가이드
│   │   │   ├── marketplace.md          # 마켓플레이스 가이드
│   │   │   ├── workflows.md            # 워크플로우 가이드
│   │   │   └── references.md           # 참고 자료
│   │   ├── decisions/                  # 의사결정 기록
│   │   │   └── _template.md
│   │   ├── principles/                 # 원칙
│   │   │   └── _template.md
│   │   └── policies/                   # 정책
│   │       └── _template.md
│   └── PROJECT-INDEX.md                # 이 문서
│
├── .vscode/                            # VSCode 설정
│   ├── settings.json
│   └── extensions.json
│
└── LICENSE                             # MIT 라이선스
```

---

## Key Components

### 1. Knowledge Pipeline (지식 파이프라인)

#### Input Layer
- **inbox/** - Raw 지식 캡처 저장소
  - 자유 형식 문서
  - 템플릿: `_template.md`
  - 처리 후 corpus로 이동

#### Storage Layer
- **corpus/** - 구조화된 지식 저장소
  - 6개 domain 기반 분류
  - Frontmatter 필수 (title, domain)
  - 템플릿: `_template.md`

#### Export Layer (계획됨)
- agent-docs: AI Agent용 선언적 문서
- blog: 스토리텔링 블로그 포스트
- book: 선형 챕터 구조
- web: 인터랙티브 마인드맵

### 2. Claude Code Integration

#### /digest Command
```
.claude/commands/digest.md
```
inbox 파일을 corpus로 소화시키는 슬래시 커맨드

#### knowledge-digest Skill
```
skills/knowledge-digest/SKILL.md
```
소크라테스식 질문을 통한 지식 구조화:
1. **목적 파악**: 왜 남기려고 해? 없으면 뭐가 안 돼?
2. **압축**: 한 문장 요약, 핵심만 남기기
3. **분류**: 6개 domain 중 선택
4. **연결**: 기존 corpus와 연결점 찾기

### 3. Brainstorm Documents (전략 문서)

| 문서 | 핵심 메시지 | 우선순위 |
|------|------------|----------|
| 00-summary | 전체 통합 요약 | 참조용 |
| 01-mvp | Working Software First | **즉시** |
| 02-input | 입력 ≠ 추출 분리 | 단기 |
| 03-export | agent-docs 먼저 | 단기 |
| 04-ai-automation | Stage 0→1→2→3 단계적 | 중기 |

---

## Current Status (Stage 0)

### What's Working
- [x] 폴더 구조 정립 (inbox, corpus, brainstorm)
- [x] /digest 커맨드 정의
- [x] knowledge-digest 스킬 정의
- [x] 6개 domain 분류 체계
- [x] Claude Code 생태계 문서화

### What's Pending
- [ ] inbox → corpus 수동 이동 5개 이상
- [ ] 2개 이상 domain에 문서 분포
- [ ] frontmatter 형식 일관성 검증
- [ ] validate-corpus.py 스크립트
- [ ] export-agent-docs.py 스크립트

### Inbox Status

| 파일 | 내용 | 잠재적 Domain |
|------|------|--------------|
| INFRA-SETUP.md | 홈랩 인프라 설정 | operations |
| Hashbrown.dev Overview.md | 생성형 UI 프레임워크 | engineering |
| 최고의 개발자... | 업계 전문가 리서치 | growth |

---

## Automation Roadmap

### Stage 0: 완전 수동 (현재)
- 사람이 모든 것 수행
- AI는 없음

### Stage 1: AI 보조 (MVP 목표)
- Claude Chat으로 대화
- AI가 분류 제안 (신뢰도 표시)
- HITL (Human-in-the-Loop)

### Stage 2: AI 주도 (중기)
- 아이디어만 말하면 구조화
- 자동 연결 그래프
- 자동 export

### Stage 3: AI 자율 (장기)
- 고수준 지시만
- 전체 파이프라인 자동화

---

## Templates

### inbox/_template.md
```markdown
# {제목}

> 날짜: YYYY-MM-DD
> 출처: (대화/메모/링크/etc)

---

{내용을 자유롭게 작성}
```

### corpus/_template.md
```markdown
---
title: {제목}
domain: {product|engineering|operations|growth|business|ai-automation}
---

## Context

{왜 이 지식이 필요한지}

## Content

{핵심 내용}
```

---

## Quick Start

### 1. 새 지식 캡처
```bash
vim inbox/YYYY-MM-DD-{slug}.md
```

### 2. 분류 (수동)
6개 domain 중 선택

### 3. 구조화 (corpus)
```bash
mv inbox/YYYY-MM-DD-{slug}.md corpus/{domain}/{slug}.md
vim corpus/{domain}/{slug}.md  # frontmatter 추가
```

### 4. 또는 /digest 사용
```
/digest inbox/INFRA-SETUP.md
```
소크라테스식 질문을 통해 대화형으로 정리

---

## Cross-References

### Related Projects
- k-codepoet (상위 프로젝트)

### Key Files Quick Access
| 용도 | 파일 |
|------|------|
| 프로젝트 개요 | [README.md](../README.md) |
| 우선순위 요약 | [brainstorm/00-summary-and-priorities.md](../brainstorm/00-summary-and-priorities.md) |
| MVP 전략 | [brainstorm/01-mvp-execution-strategy.md](../brainstorm/01-mvp-execution-strategy.md) |
| /digest 커맨드 | [.claude/commands/digest.md](../.claude/commands/digest.md) |
| 지식 소화 스킬 | [skills/knowledge-digest/SKILL.md](../skills/knowledge-digest/SKILL.md) |
| Claude Code 가이드 | [docs/humans/claude-code/README.md](./humans/claude-code/README.md) |

---

## Metadata

- **Version**: 0.1.0
- **Last Modified**: 2025-12-31
- **Maintainer**: choigawoon
- **License**: MIT
