# Ground Truth - Knowledge Pipeline

> 1인 AI Company Knowledge Management System
> 
> RAW 경험 → 구조화된 코퍼스 → 인터랙티브 웹앱/블로그/문서

## Overview

RAW 경험을 수집하고, AI가 분류/태깅/구조화하여, **인터랙티브 웹앱**, 블로그, 문서 등 다양한 형태로 Export하는 지식 관리 시스템입니다.

```
INPUT (Write) → AI PROCESSING → CORPUS (Source of Truth) → MULTI-OUTPUT
                                                            ├── 🌐 Web App (Interactive)
                                                            ├── 📖 Docs (Docusaurus)
                                                            ├── ✍️ Blog
                                                            └── 📋 Resume
```

## 핵심 개념: 3계층 지식 구조

대주제(Topic)별로 지식을 3계층으로 구조화합니다:

| Layer | 이름 | 설명 | 예시 |
|-------|------|------|------|
| **Layer 1** | Cases | 실제 사례 분석 | 스타크래프트의 락스텝 구현 |
| **Layer 2** | Fundamentals | 불변의 원리 | 게임 루프, 네트워크 기초 |
| **Layer 3** | Decisions | 설계 트레이드오프 | P2P vs Client-Server |

## Quick Start

### 1. RAW 문서 작성
`inbox/` 폴더에 자유 형식으로 경험/메모 작성

### 2. AI 처리
```bash
python scripts/inbox-to-corpus.py
```
Knowledge Agent가 분류/태깅/구조화하여 `corpus/`에 저장

### 3. 웹앱 빌드
```bash
python scripts/build-web.py --topic game-development
```
`exports/web/game-development/`에 인터랙티브 웹앱 생성

### 4. 검증
```bash
python scripts/validate-corpus.py --all
```
코퍼스 무결성 검증

## Folder Structure

```
ground-truth/
├── CLAUDE.md              # AI Agent 컨텍스트
├── README.md              # 이 파일
│
├── inbox/                 # 📥 RAW 입력 (미처리)
│   └── _template.md
│
├── corpus/                # 📚 구조화된 지식 코퍼스
│   ├── _meta/             # 메타데이터 정의
│   │   ├── domains.yaml   # 도메인 정의
│   │   ├── content-types.yaml  # 컨텐츠 타입 정의
│   │   └── output-formats.yaml # 출력 형식 정의
│   │
│   ├── game-development/  # 📂 Topic: 게임 개발
│   │   ├── topic.yaml     # 토픽 메타데이터
│   │   ├── structure/     # 지식 구조 정의
│   │   │   ├── layers.yaml
│   │   │   └── graph.json
│   │   ├── content/       # 실제 컨텐츠
│   │   │   ├── cases/
│   │   │   ├── fundamentals/
│   │   │   └── decisions/
│   │   ├── demos/         # 인터랙티브 데모 스펙
│   │   └── i18n/          # 다국어 지원
│   │
│   └── {other-topics}/    # 다른 대주제들
│
├── fragments/             # 🧩 독립 지식 조각 (레거시)
│   ├── knowledge/
│   ├── cases/
│   └── decisions/
│
├── docs/                  # 📋 규칙/정책 문서
│   ├── humans/            # WHY - 사람이 결정
│   └── agents/            # HOW - AI 실행 규칙
│
├── exports/               # 📤 자동 생성된 Output
│   ├── web/               # 🆕 인터랙티브 웹앱
│   ├── docs/              # 정적 문서 사이트
│   ├── blog/              # 블로그 포스트
│   └── resume/            # 이력서
│
└── scripts/               # 🔧 파이프라인 스크립트
    ├── inbox-to-corpus.py # inbox → corpus 변환
    ├── build-web.py       # corpus → 웹앱 빌드
    └── validate-corpus.py # 코퍼스 검증
```

## Topic Structure

각 토픽은 다음 구조를 가집니다:

```
corpus/{topic}/
├── topic.yaml           # 토픽 메타데이터 (필수)
│
├── structure/           # 지식 구조 정의
│   ├── layers.yaml      # 계층별 항목 정의
│   ├── graph.json       # 개념 간 연결 관계
│   └── tree.yaml        # (선택) 트리 구조
│
├── content/             # MDX 컨텐츠
│   ├── cases/           # Layer 1: 사례
│   │   ├── _schema.yaml
│   │   └── *.mdx
│   ├── fundamentals/    # Layer 2: 원리
│   │   ├── _schema.yaml
│   │   └── *.mdx
│   └── decisions/       # Layer 3: 결정
│       ├── _schema.yaml
│       └── *.mdx
│
├── demos/               # 인터랙티브 데모
│   └── {demo-name}/
│       ├── spec.yaml    # 데모 스펙
│       └── README.md
│
└── i18n/                # 다국어
    ├── ko.json          # 한국어 (primary)
    ├── en.json
    └── ja.json
```

## Domains

지식이 속할 수 있는 도메인:

| Domain | Emoji | Description |
|--------|-------|-------------|
| Product | 🎯 | 무엇을 만들 것인가? |
| Engineering | 🛠️ | 어떻게 만들 것인가? |
| Operations | ⚙️ | 어떻게 돌릴 것인가? |
| Growth | 📣 | 어떻게 알릴 것인가? |
| Business | 💰 | 어떻게 유지할 것인가? |
| AI/Automation | 🤖 | 어떻게 위임할 것인가? |

## Output Formats

| Format | Emoji | Description |
|--------|-------|-------------|
| Web Interactive | 🌐 | 인터랙티브 마인드맵/데모 웹앱 |
| Docs | 📖 | Docusaurus 문서 사이트 |
| Blog | ✍️ | 스토리텔링 블로그 포스트 |
| Resume | 📋 | 성과 중심 이력서 |
| Notion | 📝 | Notion 페이지 동기화 |

## Tech Stack

| Layer | Tech |
|-------|------|
| Storage | Git (GitHub) |
| Format | MDX/Markdown + YAML |
| Processing | Claude Code / Claude API |
| Export - Web | React + TanStack Router |
| Export - Docs | Docusaurus |
| Export - Blog | Remix |
| Hosting | Cloudflare Pages |

## Pipeline Scripts

### `inbox-to-corpus.py`
RAW 입력을 AI가 분류/구조화하여 corpus로 변환

```bash
python scripts/inbox-to-corpus.py --file "my-note.md"
python scripts/inbox-to-corpus.py --dry-run  # 테스트
```

### `build-web.py`
corpus에서 인터랙티브 웹앱 생성

```bash
python scripts/build-web.py --topic game-development
python scripts/build-web.py --all
```

### `validate-corpus.py`
코퍼스 무결성 검증

```bash
python scripts/validate-corpus.py --all
python scripts/validate-corpus.py --topic game-development
```

## Example: Game Development Topic

`corpus/game-development/`에 게임 개발 지식이 구조화되어 있습니다:

- **Cases**: 스타크래프트, 오버워치, LoL 등 실제 게임 분석
- **Fundamentals**: 게임 루프, 네트워킹, 물리 연산 등 핵심 원리
- **Decisions**: 동기화 전략, 틱레이트, 아키텍처 선택 등 트레이드오프
- **Demos**: 락스텝 동기화, 마리오 점프 물리 등 인터랙티브 데모

빌드 결과물은 `how-to-make-a-game` 같은 인터랙티브 교육 웹앱이 됩니다.

## Related Documents

- [GOAL.md](./GOAL.md) - 상세 작업 계획서
- [corpus/_meta/](./corpus/_meta/) - 메타데이터 정의
