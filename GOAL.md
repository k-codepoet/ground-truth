# Knowledge Pipeline 구축 작업 계획서

> **프로젝트**: 1인 AI Company Knowledge Management System
> 

> **목표**: RAW 경험 → 다중 Output 자동화 파이프라인 구축
> 

> **작성일**: 2025-01-02
> 

---

## 1. 프로젝트 개요

### 1.1 한 문장 정의

**"내가 뭔가 쓰면 → AI가 분류/태깅/구조화 → Git Repo에 저장 → 필요시 다양한 형태로 Export"**

### 1.2 핵심 원칙

| 원칙 | 설명 |
| --- | --- |
| **Git = Source of Truth** | 모든 지식은 Git Repo의 mdx/markdown으로 관리 |
| **AI 자동화** | 분류, 태깅, 메타데이터 생성은 AI가 수행 |
| **HITL** | 모자란 정보는 사용자에게 질문 |
| **Multi-Output** | 하나의 RAW에서 여러 형태의 Export 생성 |
| **점진적 구축** | 기존 Notion은 그대로 두고 새 구조로 하나씩 이전 |

### 1.3 6개 도메인

```
🎯 Product        - 무엇을 만들 것인가? (문제 정의, 기획)
🛠️ Engineering    - 어떻게 만들 것인가? (코드, 아키텍처)
⚙️ Operations     - 어떻게 돌릴 것인가? (인프라, 배포, 모니터링)
📣 Growth         - 어떻게 알릴 것인가? (마케팅, 세일즈, 콘텐츠)
💰 Business       - 어떻게 유지할 것인가? (재무, 법무, 계약)
🤖 AI/Automation  - 어떻게 위임할 것인가? (Agent, Workflow, LLM)
```

### 1.4 5가지 Output 타입

| Output | 성격 | 독자 |
| --- | --- | --- |
| **Knowledge** | 추상화된 원칙, 패턴 | 미래의 나, AI Agent |
| **Cases** | 구체적 사례, 재현 가능 | 나, 동료 |
| **Decisions** | 트레이드오프, 선택 이유 | 미래의 나 |
| **Blog** | 스토리텔링, 공유 가치 | 외부 독자 |
| **Resume** | 성과, 임팩트, 수치 | 채용자, 클라이언트 |

---

## 2. 시스템 아키텍처

### 2.1 전체 흐름

```
┌─────────────────────────────────────────────────────────────────────┐
│  INPUT (다중 프론트엔드)                                            │
│  Slack / Discord / Web Chatbot / SMS / Voice                       │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PROCESSING (원격 컴퓨터 - Knowledge Agent)                         │
│                                                                     │
│  1. 분류 (domain 결정)                                              │
│  2. 태깅 (tech, concepts 추출)                                      │
│  3. 검증 (부족한 정보 질문)                                         │
│  4. 구조화 (Enhanced RAW 템플릿에 맞춰 저장)                        │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STORAGE (Git Repo - ground-truth/)                                 │
│                                                                     │
│  inbox/        → RAW (임시, 미처리)                                 │
│  enhanced/     → Enhanced RAW (구조화, 메타데이터 완비)             │
│  exports/      → 자동 생성된 Output들                               │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  EXPORT (on-demand)                                                 │
│                                                                     │
│  → Knowledge Base (Docusaurus)                                      │
│  → Blog (개인 블로그)                                               │
│  → Resume (포트폴리오)                                              │
│  → Notion (읽기용 뷰)                                               │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 폴더 구조

```
ground-truth/
├── [README.md](http://README.md)
├── [CLAUDE.md](http://CLAUDE.md)                     # AI Agent 컨텍스트
│
├── docs/
│   ├── humans/                   # WHY - 사람이 결정한 것
│   │   ├── principles/           # 불변 원칙
│   │   │   └── _[template.md](http://template.md)
│   │   ├── policies/             # 운영 정책
│   │   │   └── _[template.md](http://template.md)
│   │   └── decisions/            # ADR (의사결정 기록)
│   │       └── _[template.md](http://template.md)
│   │
│   └── agents/                   # HOW - AI 실행 규칙
│       ├── pm/
│       ├── dev/
│       ├── research/
│       └── ops/
│
├── inbox/                        # RAW 수집 (미처리)
│   └── _[template.md](http://template.md)
│
├── enhanced/                     # Enhanced RAW (구조화됨)
│   ├── knowledge/                # 추상화된 지식
│   │   ├── product/
│   │   ├── engineering/
│   │   ├── operations/
│   │   ├── growth/
│   │   ├── business/
│   │   └── ai-automation/
│   │
│   ├── cases/                    # 실제 사례
│   │   ├── product/
│   │   ├── engineering/
│   │   ├── operations/
│   │   ├── growth/
│   │   ├── business/
│   │   └── ai-automation/
│   │
│   └── decisions/                # 의사결정 기록
│       ├── 2024/
│       └── 2025/
│
├── exports/                      # 자동 생성 (gitignore 가능)
│   ├── blog/
│   ├── resume/
│   └── notion/
│
└── scripts/                      # 자동화 스크립트
    ├── [classify.py](http://classify.py)               # 분류 로직
    ├── [enhance.py](http://enhance.py)                # RAW → Enhanced 변환
    └── [export.py](http://export.py)                 # Export 생성
```

---

## 3. 템플릿 정의

### 3.1 inbox/ RAW 템플릿

```yaml
---
id: raw-{timestamp}
created: {ISO8601}
source: {slack|discord|web|sms|voice|manual}
status: raw
---

{자유 형식 내용}
```

### 3.2 enhanced/ Enhanced RAW 템플릿

```yaml
---
# === 자동 생성 ===
id: {type}-{domain}-{date}-{seq}
created: {ISO8601}
updated: {ISO8601}
source: {원본 source}
source_id: {원본 raw id}

# === 분류 ===
domain: {product|engineering|operations|growth|business|ai-automation}
type: {knowledge|case|decision}
status: enhanced

# === 태그 ===
tech: []           # 기술 스택
concepts: []       # 개념, 패턴
related: []        # 관련 문서 id

# === Export 설정 ===
exportable:
  knowledge: {true|false}
  blog: {true|false}
  resume: {true|false}
  
# === 성과 지표 (resume용, optional) ===
impact:
  problem: ""
  solution: ""
  result: ""
  metrics: []      # 수치화된 성과
---

## Context
(왜 이 작업을 했는지, 배경)

## Problem
(구체적 문제 상황)

## Solution
(해결 과정, 단계별)

## Learnings
(배운 점, 추상화된 인사이트)

## References
(참고 자료, 링크)
```

### 3.3 decisions/ ADR 템플릿

```yaml
---
id: adr-{seq}-{slug}
created: {ISO8601}
status: {proposed|accepted|deprecated|superseded}
superseded_by: null
domain: {domain}
---

## Title
{결정 제목}

## Context
(결정이 필요한 상황, 배경)

## Options Considered
1. **Option A**: {설명}
   - Pros: 
   - Cons: 
2. **Option B**: {설명}
   - Pros: 
   - Cons: 

## Decision
(선택한 옵션과 이유)

## Consequences
(예상되는 결과, 영향)
```

---

## 4. 작업 목록

### Phase 1: 기반 구조 구축 (Day 1)

| # | 작업 | 예상 시간 | 의존성 | 완료 기준 |
| --- | --- | --- | --- | --- |
| 1.1 | ground-truth 레포 생성 | 15분 | - | GitHub에 빈 레포 생성됨 |
| 1.2 | 폴더 구조 생성 | 15분 | 1.1 | 위 구조대로 폴더 생성됨 |
| 1.3 | 템플릿 파일 생성 | 30분 | 1.2 | 각 폴더에 _[template.md](http://template.md) 존재 |
| 1.4 | [CLAUDE.md](http://CLAUDE.md) 작성 | 30분 | 1.3 | AI Agent 컨텍스트 문서 완성 |
| 1.5 | [README.md](http://README.md) 작성 | 15분 | 1.4 | 프로젝트 설명 문서 완성 |

### Phase 2: 첫 번째 문서 파이프라인 테스트 (Day 1-2)

| # | 작업 | 예상 시간 | 의존성 | 완료 기준 |
| --- | --- | --- | --- | --- |
| 2.1 | 테스트용 RAW 문서 작성 | 15분 | 1.5 | inbox/에 RAW 문서 1개 |
| 2.2 | 수동으로 Enhanced 변환 | 30분 | 2.1 | enhanced/에 구조화된 문서 |
| 2.3 | 템플릿 문제점 파악 및 수정 | 30분 | 2.2 | 템플릿 v2 확정 |
| 2.4 | 두 번째 문서로 검증 | 30분 | 2.3 | 파이프라인 동작 확인 |

### Phase 3: Knowledge Agent 프롬프트 (Day 2-3)

| # | 작업 | 예상 시간 | 의존성 | 완료 기준 |
| --- | --- | --- | --- | --- |
| 3.1 | 분류 프롬프트 작성 | 1시간 | 2.4 | domain 자동 분류 동작 |
| 3.2 | 태깅 프롬프트 작성 | 1시간 | 3.1 | tech, concepts 자동 추출 |
| 3.3 | 질문 생성 프롬프트 | 1시간 | 3.2 | 부족한 정보 질문 생성 |
| 3.4 | 구조화 프롬프트 작성 | 1시간 | 3.3 | Enhanced 템플릿 자동 생성 |
| 3.5 | 통합 테스트 | 1시간 | 3.4 | RAW → Enhanced 자동화 |

### Phase 4: Export 파이프라인 (Day 3-4)

| # | 작업 | 예상 시간 | 의존성 | 완료 기준 |
| --- | --- | --- | --- | --- |
| 4.1 | Knowledge Export 스크립트 | 2시간 | 3.5 | knowledge/ 자동 생성 |
| 4.2 | Blog Export 스크립트 | 2시간 | 4.1 | blog/ 자동 생성 |
| 4.3 | Resume Export 스크립트 | 2시간 | 4.2 | resume/ 자동 생성 |
| 4.4 | Export 명령어 통합 | 1시간 | 4.3 | 단일 명령으로 전체 Export |

### Phase 5: 입력 프론트엔드 연결 (Day 5+)

| # | 작업 | 예상 시간 | 의존성 | 완료 기준 |
| --- | --- | --- | --- | --- |
| 5.1 | Slack 입력 연동 | 4시간 | 4.4 | Slack → inbox 자동 저장 |
| 5.2 | Web Chatbot 연동 | 4시간 | 5.1 | Web → inbox 자동 저장 |
| 5.3 | Discord 연동 | 4시간 | 5.2 | Discord → inbox 자동 저장 |

---

## 5. 우선순위 및 마일스톤

### MVP (최소 동작 버전)

**목표**: RAW → Enhanced → Export 수동 파이프라인 동작

- [ ]  Phase 1: 기반 구조
- [ ]  Phase 2: 첫 번째 문서 테스트

**완료 기준**:

- 수동으로 RAW 작성 → Enhanced 변환 → Blog 형태로 Export 가능

### v1.0 (자동화 버전)

**목표**: AI가 분류/태깅/구조화 자동 수행

- [ ]  Phase 3: Knowledge Agent
- [ ]  Phase 4: Export 파이프라인

**완료 기준**:

- Claude Code에서 `/knowledge-add` 명령으로 자동 처리

### v2.0 (다중 입력)

**목표**: 어떤 채널에서든 입력 가능

- [ ]  Phase 5: 입력 프론트엔드

**완료 기준**:

- Slack/Discord/Web에서 입력 → 자동으로 ground-truth에 저장

---

## 6. 기술 스택

| 레이어 | 기술 | 이유 |
| --- | --- | --- |
| Storage | Git (GitHub) | 버전 관리, AI 친화적 |
| Format | MDX/Markdown | 구조화 + 렌더링 유연성 |
| Processing | Claude Code | AI Agent 실행 환경 |
| Export - Web | Docusaurus | MDX 네이티브 지원 |
| Export - Blog | 개인 블로그 (Remix) | 기존 스택 활용 |
| Input | Slack/Discord Bot | 기존 인프라 활용 |
| Hosting | Cloudflare Pages | 기존 인프라 활용 |

---

## 7. 시작 명령

### Phase 1 시작

```bash
# 1.1 레포 생성
cd /Volumes/mac-ext-storage/ai-company
mkdir ground-truth && cd ground-truth
git init

# 1.2 폴더 구조 생성
mkdir -p docs/humans/{principles,policies,decisions}
mkdir -p docs/agents/{pm,dev,research,ops}
mkdir -p inbox
mkdir -p enhanced/{knowledge,cases,decisions}/{product,engineering,operations,growth,business,ai-automation}
mkdir -p enhanced/decisions/{2024,2025}
mkdir -p exports/{blog,resume,notion}
mkdir -p scripts

# 1.3 템플릿 생성
# (각 폴더에 _[template.md](http://template.md) 생성)

# 1.4 [CLAUDE.md](http://CLAUDE.md) 작성
# 1.5 [README.md](http://README.md) 작성
```

---

## 8. 첫 번째 테스트 문서 후보

| 후보 | 장점 | 단점 |
| --- | --- | --- |
| **홈서버 GPU 설정** | 최근 경험, 기술적 깊이 | 아직 정리 안됨 |
| **AI Company 설계 과정** | 메타적, 문서화 자체가 콘텐츠 | 추상적 |
| **Notion 재구성 논의** | 지금 하고 있는 것 | 아직 진행 중 |

**추천**: 홈서버 GPU 설정

- 구체적 문제/해결 있음
- 5가지 Output 모두 추출 가능
- Blog/Resume 가치 높음

---

## 9. 리스크 및 대응

| 리스크 | 영향 | 대응 |
| --- | --- | --- |
| 템플릿 과잉 설계 | 작성 부담 → 안 씀 | MVP에서 최소 필드만, 점진적 확장 |
| 분류 모호함 | 어느 도메인? | 복수 도메인 허용, primary/secondary |
| Export 품질 | 자동 생성 ≠ 좋은 글 | 수동 다듬기 단계 추가 |

---

## 10. 성공 지표

| 지표 | 목표 (1개월) |
| --- | --- |
| Enhanced 문서 수 | 10개 이상 |
| 도메인 커버리지 | 4개 이상 |
| Export 생성 | Blog 3개, Resume 1개 |
| 자동화 비율 | 분류/태깅 80% 자동 |

---

## Appendix: 관련 문서

- org-tinysolver README - AI Company 전체 구조
- Notion 재구성 다이어그램 - AS-IS/TO-BE
- Claude Code 심층 분석 - 서브에이전트, Hooks 등

---

**작성자**: Claude (with Human)

**최종 수정**: 2025-01-02

**상태**: Ready for Execution