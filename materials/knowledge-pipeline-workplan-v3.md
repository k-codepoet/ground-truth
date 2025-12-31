# Knowledge Pipeline v3: Bootstrapping AI Company

> **핵심 통찰**: Knowledge-ops가 첫 번째 topic이다. 스스로를 문서화하면서 시스템을 증명한다.
> **목표**: AI Company가 지식을 자동으로 추출/구조화/출력할 수 있게 하는 기반 시스템
> **갱신일**: 2025-01-02

---

## 1. 의존성 체인

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 0: Knowledge-ops (메타 시스템) ← 지금 만들 것         │
│  "지식을 어떻게 추출/구조화/출력하는가"                        │
└─────────────────────────────────────────────────────────────┘
                          ↓ enables
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: Domain Corpus (도메인 지식들)                      │
│  game-development, devops, ai-engineering, ...              │
└─────────────────────────────────────────────────────────────┘
                          ↓ enables
┌─────────────────────────────────────────────────────────────┐
│  Layer 2: Exports (형태별 결과물)                            │
│  interactive-course, book, blog, agent-docs, ...            │
└─────────────────────────────────────────────────────────────┘
                          ↓ enables
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: AI Company (자동화)                                │
│  CEO 입력 → 배포된 URL                                       │
└─────────────────────────────────────────────────────────────┘
```

**이 문서는 Layer 0 구축에 집중한다.**

---

## 2. 지식 흐름

```
HEAD (암묵지)
    │ 추출 (AI 대화, 자문자답, 강제 출력)
    ▼
INBOX (원시 캡처)
    │ 분류 (어느 topic?)
    ▼
CORPUS/_DRAFTS (topic별 초안)
    │ 구조화 (layers, connections)
    ▼
CORPUS/CONTENT (구조화된 원자)
    │ 조립 (어떤 형태로?)
    ▼
EXPORTS (형태별 결과물)
```

---

## 3. 폴더 구조

```
ground-truth/
├── README.md
├── CLAUDE.md                       # AI Agent 컨텍스트
│
├── inbox/                          # 원시 캡처
│   └── *.md
│
├── corpus/                         # Topic 기반 지식
│   │
│   ├── knowledge-ops/              # 🥇 첫 번째 topic (메타)
│   │   ├── topic.yaml
│   │   ├── _drafts/                # 작업 중
│   │   ├── content/
│   │   │   ├── extraction/         # 머릿속에서 꺼내는 법
│   │   │   ├── structuring/        # 구조화하는 법
│   │   │   └── exporting/          # 다양한 형태로 내보내는 법
│   │   └── structure/
│   │       └── tree.yaml
│   │
│   ├── game-development/           # 🥈 두 번째 topic (검증용)
│   │   └── ...
│   │
│   └── {other-topics}/
│
├── library/                        # (미래) 공유 원자
│
├── exports/                        # 빌드 결과물
│   ├── web/                        # 인터랙티브 강의
│   ├── agent-docs/                 # AI Agent용 문서
│   ├── book/                       # 출판용
│   └── blog/                       # 블로그 포스트
│
└── scripts/
    ├── extract.py                  # HEAD → inbox (AI 대화 기반)
    ├── classify.py                 # inbox → corpus/_drafts
    ├── structure.py                # _drafts → content
    └── export.py                   # content → exports/*
```

---

## 4. 같은 원천, 다른 출력

하나의 `corpus/content/`에서 여러 형태로 변환:

| Export 형태 | 구조 특징 | 대상 독자 |
|-------------|----------|----------|
| `web/` (인터랙티브 강의) | 서사적, 점진적 공개 | 학습자 |
| `agent-docs/` (AI Agent용) | 선언적, 규칙 기반 | AI Agent |
| `book/` (출판) | 선형적, 챕터 구조 | 일반 독자 |
| `blog/` (블로그) | 독립적, 단편 | 웹 독자 |

**MVP는 하나만**: `agent-docs/` (AI Company 구축이 목표니까)

---

## 5. Bootstrapping 전략

### 원칙

> knowledge-ops로 knowledge-ops 자체를 문서화한다.
> 이게 되면 다른 모든 topic에 적용할 수 있다.

### 단계

```
Phase 1: 수동으로 knowledge-ops 만들기
    ↓
Phase 2: knowledge-ops로 knowledge-ops 문서화하기 (self-hosting)
    ↓
Phase 3: game-development에 적용 (검증)
    ↓
Phase 4: AI Agent가 이 과정을 자동화
```

---

## 6. Phase 1: 수동으로 knowledge-ops 만들기 (Day 1-2)

### 목표

- 폴더 구조 생성
- 지금까지의 대화를 첫 번째 콘텐츠로 변환
- 최소한의 export (agent-docs)

### 작업 목록

| # | 작업 | 시간 | 결과물 |
|---|------|------|--------|
| 1.1 | Repo 생성 & 폴더 구조 | 30분 | `ground-truth/` 전체 구조 |
| 1.2 | 이 대화를 inbox에 덤프 | 15분 | `inbox/2025-01-02-knowledge-ops-discussion.md` |
| 1.3 | topic.yaml 작성 | 15분 | `corpus/knowledge-ops/topic.yaml` |
| 1.4 | _drafts로 이동 & 정리 | 1시간 | `corpus/knowledge-ops/_drafts/*.md` |
| 1.5 | content로 승격 (구조화) | 2시간 | `corpus/knowledge-ops/content/**/*.mdx` |
| 1.6 | tree.yaml 작성 | 30분 | `corpus/knowledge-ops/structure/tree.yaml` |
| 1.7 | CLAUDE.md 작성 | 30분 | AI Agent 컨텍스트 |
| 1.8 | agent-docs export 스크립트 | 2시간 | `scripts/export-agent-docs.py` |
| 1.9 | 첫 번째 export 생성 | 30분 | `exports/agent-docs/knowledge-ops/` |

**총 예상 시간: ~8시간 (1.5일)**

### 성공 기준

- [ ] `exports/agent-docs/knowledge-ops/`가 존재한다
- [ ] 이 문서를 읽고 새 topic을 만드는 방법을 알 수 있다
- [ ] AI Agent가 이 문서를 참조할 수 있다

---

## 7. Phase 2: Self-hosting 검증 (Day 3)

### 목표

knowledge-ops 시스템을 사용해서 knowledge-ops를 개선한다.

### 작업 목록

| # | 작업 | 시간 | 결과물 |
|---|------|------|--------|
| 2.1 | Phase 1 과정을 inbox에 기록 | 30분 | 회고 문서 |
| 2.2 | extraction 문서 보강 | 1시간 | "머릿속에서 꺼내는 법" 상세화 |
| 2.3 | structuring 문서 보강 | 1시간 | "구조화하는 법" 상세화 |
| 2.4 | exporting 문서 보강 | 1시간 | "내보내는 법" 상세화 |
| 2.5 | agent-docs 재생성 | 30분 | 개선된 버전 |

### 성공 기준

- [ ] "이 시스템으로 이 시스템을 만들었다"가 증명됨
- [ ] 문서만 보고 다른 사람(또는 AI)이 따라할 수 있음

---

## 8. Phase 3: game-development 적용 (Day 4-5)

### 목표

두 번째 topic으로 시스템 검증

### 작업 목록

| # | 작업 | 시간 | 결과물 |
|---|------|------|--------|
| 3.1 | game-dev 관련 기존 자료 inbox에 수집 | 1시간 | `inbox/game-*.md` |
| 3.2 | knowledge-ops 절차대로 _drafts 생성 | 2시간 | `corpus/game-development/_drafts/` |
| 3.3 | content로 구조화 | 3시간 | `corpus/game-development/content/` |
| 3.4 | agent-docs export | 1시간 | `exports/agent-docs/game-development/` |
| 3.5 | 절차 문제점 기록 | 30분 | knowledge-ops 피드백 |

### 성공 기준

- [ ] game-development topic이 완성됨
- [ ] knowledge-ops 문서를 참조하며 만들 수 있었음
- [ ] 발견된 문제점이 knowledge-ops에 반영됨

---

## 9. Phase 4: AI 자동화 (Week 2+)

### 목표

AI Agent가 extraction/classification/structuring을 도울 수 있게

### 예상 작업

| 자동화 영역 | 설명 | 우선순위 |
|------------|------|----------|
| Extraction | 대화를 통해 암묵지 → inbox | HIGH |
| Classification | inbox → 적절한 corpus/_drafts | MEDIUM |
| Structuring | _drafts → content 변환 제안 | MEDIUM |
| Export | content → 다양한 형태 자동 생성 | LOW (스크립트로 충분) |

**Phase 4는 Phase 3 완료 후 상세 계획**

---

## 10. 핵심 스키마

### topic.yaml

```yaml
id: knowledge-ops
title: Knowledge Operations
description: 지식을 추출, 구조화, 출력하는 메타 시스템

structure: layered

layers:
  - id: extraction
    title: 추출
    description: 머릿속 암묵지를 명시지로
    
  - id: structuring
    title: 구조화
    description: 원시 지식을 연결된 구조로
    
  - id: exporting
    title: 출력
    description: 구조화된 지식을 다양한 형태로

exports:
  agent-docs: true    # MVP
  web: false          # later
  book: false         # later
  blog: false         # later

status: bootstrapping
```

### Content 파일 (MDX)

```yaml
---
id: ai-conversation-extraction
title: AI 대화를 통한 지식 추출
layer: extraction
summary: Claude와의 대화로 머릿속 지식을 꺼내는 방법

connects_to:
  - inbox-capture
  - draft-organization
---

# 내용...
```

### tree.yaml

```yaml
root:
  - id: overview
    title: 개요
    
  - id: extraction
    title: 추출
    children:
      - id: ai-conversation-extraction
      - id: self-questioning
      - id: forced-output
      
  - id: structuring
    title: 구조화
    children:
      - id: topic-definition
      - id: layer-separation
      - id: connection-mapping
      
  - id: exporting
    title: 출력
    children:
      - id: agent-docs-format
      - id: web-interactive-format
      - id: book-format
```

---

## 11. 성공 지표

### Phase 1 완료 시

| 지표 | 목표 |
|------|------|
| knowledge-ops content 파일 수 | 5개 이상 |
| agent-docs export 생성 | 완료 |
| 소요 시간 | 2일 이내 |

### Phase 3 완료 시

| 지표 | 목표 |
|------|------|
| Topic 수 | 2개 (knowledge-ops, game-dev) |
| knowledge-ops 참조 횟수 | game-dev 작업 중 3회 이상 |
| 시스템 자체 수정 횟수 | 2회 이상 (self-hosting 증명) |

### 1개월 후

| 지표 | 목표 |
|------|------|
| Topic 수 | 3개 이상 |
| Export 형태 | 2개 이상 (agent-docs + 1) |
| AI 자동화 비율 | extraction 50% 이상 |

---

## 12. 리스크 & 대응

| 리스크 | 영향 | 대응 |
|--------|------|------|
| 메타 작업에 빠져서 실제 콘텐츠 못 만듦 | 시스템만 있고 내용 없음 | Phase 3에서 강제로 실제 topic 적용 |
| 스키마 과잉 설계 | 작성 부담 | 필드 최소화, 필요할 때 추가 |
| Self-hosting 순환 참조 | 끝없는 개선 | Phase 2는 1일로 제한 |

---

## 13. 시작 명령

```bash
# 1. Repo 생성
cd /Volumes/mac-ext-storage/ai-company
mkdir -p ground-truth && cd ground-truth
git init

# 2. 폴더 구조 생성
mkdir -p inbox
mkdir -p corpus/knowledge-ops/{_drafts,content/{extraction,structuring,exporting},structure}
mkdir -p corpus/game-development/{_drafts,content/{cases,fundamentals,decisions},structure}
mkdir -p exports/{web,agent-docs,book,blog}
mkdir -p scripts

# 3. 첫 번째 파일들
touch corpus/knowledge-ops/topic.yaml
touch corpus/knowledge-ops/structure/tree.yaml
touch CLAUDE.md
touch README.md

# 4. 이 대화 내용 저장
# inbox/2025-01-02-knowledge-ops-discussion.md 로 복사
```

---

## 14. 다음 액션 (오늘)

1. ☐ 위 시작 명령 실행
2. ☐ 이 대화 전체를 `inbox/2025-01-02-knowledge-ops-discussion.md`에 저장
3. ☐ `corpus/knowledge-ops/topic.yaml` 작성
4. ☐ 대화 내용을 `_drafts/`로 분류하며 정리 시작

---

## Appendix: 기존 문서와의 관계

| 기존 | 새 위치 | 상태 |
|------|---------|------|
| knowledge-pipeline-workplan.md | 대체됨 | 이 문서로 대체 |
| knowledge-pipeline-workplan-v2.md | 대체됨 | 이 문서로 대체 |
| how-to-make-a-game | corpus/game-development의 export 결과물 | Phase 3 이후 마이그레이션 검토 |

---

**작성**: Claude (with Choi)
**상태**: Ready for Execution
