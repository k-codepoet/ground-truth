---
title: "Knowledge-ops MVP Workplan"
date: 2025-01-02
source: "Claude 대화"
type: document
status: raw
used_in:
---

> **Goal**: 말하는 대로 지식이 정리되는 시스템
> **Status**: Ready to Execute

---

## 1. 지향점 (Vision)

```
┌─────────────────────────────────────────────────────────────────┐
│  최종 목표: AI Company Knowledge Infrastructure                  │
│                                                                 │
│  INPUT (다양한 채널)                                             │
│  ├── Slack / Discord / Web / Voice / Claude Chat               │
│  └── "이런 거 알게 됐어" → 자동으로 정리됨                        │
│                                                                 │
│  PROCESSING (Knowledge-ops)                                     │
│  ├── 분류 → 구조화 → 연결 → 저장                                │
│  └── AI Agent가 자동 처리                                       │
│                                                                 │
│  OUTPUT (다양한 형태)                                            │
│  ├── Blog / Resume / Agent-docs / Book / Graphiti              │
│  └── 같은 원천, 다른 출력                                        │
└─────────────────────────────────────────────────────────────────┘
```

### 핵심 원칙

| 원칙 | 설명 |
|------|------|
| **Git = Source of Truth** | 모든 지식은 Git repo의 markdown |
| **AI 자동화** | 분류, 태깅, 구조화는 AI가 수행 |
| **Bootstrapping** | 이 시스템으로 이 시스템을 문서화 |
| **점진적 구축** | 돌아가는 것 먼저, 개선은 나중 |

---

## 2. 현재 단계 (Phase 1: MVP)

### 2.1 범위 정의

```
NOW (MVP)                          LATER (확장)
─────────────────────────────────────────────────────
✅ Claude Chat → inbox             ❌ Slack/Discord 연동
✅ inbox → corpus 자동 분류        ❌ 다중 입력 채널
✅ 6개 domain 분류                 ❌ 세부 태깅 시스템
✅ 기본 템플릿                      ❌ 복잡한 메타데이터
✅ Claude Skill (CLAUDE.md)        ❌ Export 파이프라인
                                   ❌ Graphiti 연동
                                   ❌ Blog/Resume 생성
```

### 2.2 MVP 정의

**한 문장**: Claude에게 말하면 → inbox에 저장 → corpus로 분류/구조화

**성공 기준**:
- [ ] "God PM 개념"을 말하면 `corpus/ai-automation/`에 문서 생성됨
- [ ] 생성된 문서가 템플릿 형식을 따름
- [ ] 두 번째 문서도 같은 방식으로 동작함 (반복 가능)

---

## 3. 최소 구조

```
ground-truth/
├── CLAUDE.md                 ← Claude Skill 정의
├── inbox/                    ← raw input
└── corpus/                   ← 정리된 지식
    ├── product/              # 무엇을 만들 것인가
    ├── engineering/          # 어떻게 만들 것인가
    ├── operations/           # 어떻게 돌릴 것인가
    ├── growth/               # 어떻게 알릴 것인가
    ├── business/             # 어떻게 유지할 것인가
    └── ai-automation/        # 어떻게 위임할 것인가
```

**Total: 8개 폴더 + 1개 파일**

---

## 4. CLAUDE.md (Skill 정의)

```markdown
# Knowledge-ops Agent

## 역할
사용자가 말하는 내용을 지식 문서로 변환한다.

## 워크플로우
1. 사용자 입력 받음
2. inbox/{date}-{slug}.md 로 raw 저장
3. 6개 domain 중 적절한 곳 선택
4. 구조화된 문서로 변환
5. corpus/{domain}/{slug}.md 로 저장
6. 저장 완료 보고

## 6개 Domain
| Domain | 질문 | 예시 |
|--------|------|------|
| product | 무엇을 만들 것인가? | 기획, 문제정의, PRD |
| engineering | 어떻게 만들 것인가? | 코드, 아키텍처, 기술선택 |
| operations | 어떻게 돌릴 것인가? | 인프라, 배포, 모니터링 |
| growth | 어떻게 알릴 것인가? | 마케팅, 콘텐츠, 세일즈 |
| business | 어떻게 유지할 것인가? | 재무, 법무, 계약 |
| ai-automation | 어떻게 위임할 것인가? | Agent, Workflow, LLM |

## 문서 템플릿
---
id: {domain}-{YYYYMMDD}-{slug}
title: {제목}
created: {ISO8601}
domain: {domain}
tags: []
status: draft
---

## Context
(왜 이 지식이 필요한지, 배경)

## Content
(핵심 내용)

## Connections
(관련 문서 id 목록, 없으면 비워둠)

## 분류 기준
- product: 사용자 문제, 기능 정의, 제품 방향
- engineering: 구현 방법, 기술 스택, 코드 패턴
- operations: 서버, 배포, 모니터링, 장애대응
- growth: 사용자 획득, 콘텐츠, 브랜딩
- business: 수익, 비용, 계약, 법률
- ai-automation: AI Agent, 자동화, LLM 활용

## 작업 규칙
- 항상 inbox에 먼저 raw 저장 (유실 방지)
- domain 애매하면 사용자에게 질문
- 하나의 문서 = 하나의 개념 (atomic)
- 관련 문서가 있으면 Connections에 추가
```

---

## 5. 실행 계획

### Day 1 (오늘)

| # | Task | Time | Output |
|---|------|------|--------|
| 1 | repo 생성 | 5분 | `ground-truth/` |
| 2 | 폴더 구조 생성 | 5분 | inbox/, corpus/6개 |
| 3 | CLAUDE.md 작성 | 15분 | Claude Skill 정의 |
| 4 | 첫 번째 테스트 | 15분 | God PM 문서 생성 |
| 5 | 두 번째 테스트 | 15분 | 3-stage 전략 문서 |
| 6 | 문제점 기록 | 10분 | 개선점 목록 |

**Total: ~1시간**

### 시작 명령어

```bash
# 1. Repo 생성
cd /Volumes/mac-ext-storage/ai-company
mkdir -p ground-truth && cd ground-truth
git init

# 2. 폴더 구조
mkdir -p inbox
mkdir -p corpus/{product,engineering,operations,growth,business,ai-automation}

# 3. CLAUDE.md 생성
touch CLAUDE.md
# (위 Skill 정의 내용 붙여넣기)

# 4. 초기 커밋
git add -A
git commit -m "Initial structure: inbox, corpus, CLAUDE.md"
```

---

## 6. 첫 번째 테스트 시나리오

### Input (Claude에게 말하기)
```
God PM은 AI Company의 핵심 오케스트레이터야.
- 모든 CEO 입력을 받아서 적절한 agent에게 위임
- 3단계 개발 전략 (PoC → MVP → Scale)을 기억
- 각 stage에 맞는 agent 구성을 선택
- 프로젝트 전체 맥락을 유지
```

### Expected Output

**inbox/2025-01-02-god-pm-concept.md** (raw)
```markdown
God PM은 AI Company의 핵심 오케스트레이터야.
- 모든 CEO 입력을 받아서 적절한 agent에게 위임
...
```

**corpus/ai-automation/god-pm-orchestrator.md** (structured)
```markdown
---
id: ai-automation-20250102-god-pm-orchestrator
title: God PM - AI Company 오케스트레이터
created: 2025-01-02T...
domain: ai-automation
tags: [god-pm, orchestrator, multi-agent]
status: draft
---

## Context
AI Company에서 CEO 입력을 받아 자동으로 개발 작업을 수행하기 위한 
중앙 조율 시스템이 필요함.

## Content
God PM의 핵심 역할:
1. CEO 입력 수신 (Slack, Discord, Web 등)
2. 적절한 agent에게 작업 위임
3. 3단계 개발 전략 관리 (PoC → MVP → Scale)
4. 프로젝트 맥락 유지

## Connections
- (관련 문서 생기면 추가)
```

---

## 7. 성공 지표

### MVP 완료 기준
- [ ] 3개 이상 문서가 corpus/에 생성됨
- [ ] 2개 이상 domain에 문서 분포
- [ ] 템플릿 형식 일관성 유지
- [ ] inbox raw와 corpus 구조화 문서 둘 다 존재

### 다음 단계 트리거
MVP 성공 후:
- Export 파이프라인 추가 (blog, agent-docs)
- 태깅 시스템 강화
- 검색/연결 기능

---

## 8. 예상 문제 & 대응

| 문제 | 대응 |
|------|------|
| Domain 분류 애매함 | 사용자에게 질문, primary/secondary 허용 |
| 템플릿 너무 복잡 | 필드 줄이기 (id, title, domain만 필수) |
| 문서 너무 길어짐 | 쪼개기 (1문서 = 1개념) |
| 중복 문서 | id로 dedup, Connections로 연결 |

---

## 9. 이 문서 자체가 첫 번째 테스트

이 workplan 문서를 Knowledge-ops로 저장하면:
- Domain: `ai-automation`
- File: `corpus/ai-automation/knowledge-ops-mvp-workplan.md`

**Bootstrapping 시작.**

---

**Author**: Claude (with Choi)
**Next Action**: 시작 명령어 실행 → 첫 번째 테스트
