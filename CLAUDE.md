# Knowledge Pipeline - AI Agent Context

## Overview

이 레포는 1인 AI Company의 Knowledge Management System입니다.
RAW 경험을 수집하고, AI가 분류/태깅/구조화하여, **인터랙티브 웹앱** 등 다양한 형태로 Export합니다.

## Core Flow

```
INPUT (inbox/) → AI PROCESSING → CORPUS (corpus/) → MULTI-OUTPUT (exports/)
```

## Folder Structure

### `inbox/` - RAW 입력 (미처리)
- 자유 형식의 raw 경험, 메모, 아이디어
- AI Agent가 분류/태깅 후 corpus/로 이동

### `corpus/` - 구조화된 지식 코퍼스 ⭐
대주제(Topic)별로 3계층 구조로 지식을 관리합니다.

```
corpus/
├── _meta/                    # 메타데이터 정의
│   ├── domains.yaml          # 도메인 정의
│   ├── content-types.yaml    # 컨텐츠 타입 정의
│   └── output-formats.yaml   # 출력 형식 정의
│
└── {topic}/                  # 대주제별 폴더
    ├── topic.yaml            # 토픽 메타데이터
    ├── structure/            # 지식 구조
    │   ├── layers.yaml       # 계층별 항목
    │   └── graph.json        # 개념 연결 그래프
    ├── content/              # MDX 컨텐츠
    │   ├── cases/            # Layer 1: 사례
    │   ├── fundamentals/     # Layer 2: 원리
    │   └── decisions/        # Layer 3: 결정
    ├── demos/                # 인터랙티브 데모 스펙
    └── i18n/                 # 다국어
```

### `fragments/` - 독립 지식 조각
- 특정 토픽에 속하지 않는 독립적인 지식
- `knowledge/`, `cases/`, `decisions/` 하위 폴더

### `docs/` - 규칙/정책 문서
- `humans/` - WHY: 사람이 결정한 원칙, 정책
- `agents/` - HOW: AI Agent 실행 규칙

### `exports/` - 자동 생성된 Output
- `web/` - 🆕 인터랙티브 웹앱 (마인드맵 + 데모)
- `docs/` - Docusaurus 문서 사이트
- `blog/` - 스토리텔링 블로그
- `resume/` - 성과 중심 이력서

### `scripts/` - 파이프라인 스크립트
- `inbox-to-corpus.py` - inbox → corpus 변환
- `build-web.py` - corpus → 웹앱 빌드
- `validate-corpus.py` - 코퍼스 검증

## 3-Layer Knowledge Structure

각 토픽은 3계층으로 구조화됩니다:

| Layer | Type | Purpose | Example |
|-------|------|---------|---------|
| **Layer 1** | Cases | 실제 사례 분석 | 스타크래프트 락스텝 구현 |
| **Layer 2** | Fundamentals | 불변의 원리 | 게임 루프, 네트워킹 기초 |
| **Layer 3** | Decisions | 트레이드오프 | P2P vs Client-Server |

계층 간 연결:
- Case → 관련 Fundamentals, Decisions 참조
- Decision → 적용 사례 (Case Studies) 포함
- Demo → 여러 계층의 개념을 시각화

## 6 Domains

| Domain | Emoji | Question |
|--------|-------|----------|
| Product | 🎯 | 무엇을 만들 것인가? |
| Engineering | 🛠️ | 어떻게 만들 것인가? |
| Operations | ⚙️ | 어떻게 돌릴 것인가? |
| Growth | 📣 | 어떻게 알릴 것인가? |
| Business | 💰 | 어떻게 유지할 것인가? |
| AI/Automation | 🤖 | 어떻게 위임할 것인가? |

## Agent Processing Rules

### 1. inbox → corpus 분류

inbox/ 문서를 읽고 다음을 결정합니다:

1. **Topic 결정**: 어느 대주제에 속하는가?
   - 기존 토픽 중 선택 또는 새 토픽 생성 제안

2. **Layer 결정**: 어느 계층인가?
   - `cases/` - 구체적인 사례, 특정 기술/제품 분석
   - `fundamentals/` - 추상화된 원리, 패턴
   - `decisions/` - 선택지와 트레이드오프

3. **연결 추출**: 관련 개념은?
   - 다른 cases, fundamentals, decisions와의 연결
   - 관련 데모가 있으면 연결

### 2. 태깅 (Metadata)

- `domain`: 6개 도메인 중 선택
- `tags`: 기술 스택, 개념, 키워드
- `fundamentals`: 관련 기본 원리 ID 목록
- `decisions`: 관련 설계 결정 ID 목록
- `demos`: 관련 데모 ID 목록

### 3. 검증 (HITL)

부족한 정보가 있으면 사용자에게 질문:
- 어느 토픽에 속하는지 모호한 경우
- 메타데이터가 불완전한 경우
- 연결 관계가 불명확한 경우

### 4. 구조화 (Template Based)

`content/{layer}/_schema.yaml`에 정의된 템플릿에 맞춰 문서 생성:
- frontmatter 필수 필드 포함
- ID와 파일명 일치
- 연결 관계 명시

## Content File Format

### Case Study (cases/*.mdx)

```yaml
---
id: starcraft           # 파일명과 동일
title: 스타크래프트
description: RTS, 락스텝과 완벽한 동기화

genre: RTS
year: 1998
keyFeatures:
  - 완벽한 동기화
  - 락스텝 네트워킹

fundamentals: [modeling-simulation, networking]
decisions: [sync-strategy, tickrate]
demos: [lockstep]
---

# 스타크래프트

{본문}
```

### Fundamental (fundamentals/*.mdx)

```yaml
---
id: game-loop
title: 게임 루프
description: 게임의 심장박동

concepts:
  - 입력 처리
  - 업데이트
  - 렌더링

usedIn: [모든 게임]
---

# 게임 루프

{본문}
```

### Decision (decisions/*.mdx)

```yaml
---
id: sync-strategy
title: 동기화 전략
description: 낙관적 vs 비관적, 롤백

considerations:
  - 게임 템포
  - 허용 가능한 지연시간

options:
  - id: lockstep
    name: 락스텝
    pros: [완벽한 동기화]
    cons: [입력 지연]
    useCases: [RTS]

demos: [lockstep]
---

# 동기화 전략

{본문}
```

## Demo Spec Format

```yaml
# demos/{demo}/spec.yaml
id: lockstep
title: 락스텝 동기화 데모
description: 스타크래프트 스타일 동기화 체험

related:
  cases: [starcraft, lol]
  fundamentals: [networking]
  decisions: [sync-strategy]

type: simulation

interface:
  inputs:
    - name: latency
      type: slider
      range: [0, 500]
  outputs:
    - name: sync_status
      type: indicator

implementation:
  framework: react
  libraries: [framer-motion]
```

## Graph Connection Rules

`structure/graph.json`에서 노드 간 연결:

```json
{
  "nodes": [
    {
      "id": "starcraft",
      "layer": "cases",
      "fundamentals": ["networking"],
      "decisions": ["sync-strategy"],
      "demos": ["lockstep"]
    }
  ]
}
```

## Output Generation

### Web Interactive (`exports/web/`)

- `build-web.py` 스크립트로 생성
- corpus의 structure + content + demos + i18n 조합
- React + TanStack Router 기반 마인드맵 네비게이션

### Blog (`exports/blog/`)

- 스토리텔링 형식으로 변환
- SEO 최적화 메타데이터 추가

## Core Principles

1. **corpus = Source of Truth**: 모든 지식은 corpus/의 MDX/YAML로 관리
2. **3-Layer Structure**: Cases → Fundamentals → Decisions 계층화
3. **Topic-Based Organization**: 대주제별로 관련 지식을 묶음
4. **Graph Connections**: 개념 간 연결 관계 명시
5. **Multi-Output**: 하나의 corpus에서 여러 형태로 Export
6. **AI 자동화 + HITL**: 분류/태깅은 AI, 검증은 사람

## Pipeline Commands

```bash
# inbox → corpus
python scripts/inbox-to-corpus.py

# corpus 검증
python scripts/validate-corpus.py --all

# 웹앱 빌드
python scripts/build-web.py --topic game-development
```
