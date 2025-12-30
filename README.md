# Ground Truth - Knowledge Pipeline

> 1인 AI Company Knowledge Management System

## Overview

RAW 경험을 수집하고, AI가 분류/태깅/구조화하여, 다양한 형태로 Export하는 지식 관리 시스템입니다.

```
INPUT (Write) → AI PROCESSING → GIT STORAGE (Source of Truth) → MULTI-OUTPUT
```

## Quick Start

### 1. RAW 문서 작성
`inbox/` 폴더에 자유 형식으로 경험/메모 작성

### 2. AI 처리
Knowledge Agent가 분류/태깅/구조화

### 3. 구조화된 문서
`enhanced/` 폴더에 템플릿 기반 문서 생성

### 4. Export
`exports/` 폴더에 블로그, 이력서 등 다양한 형태로 출력

## Folder Structure

```
ground-truth/
├── CLAUDE.md          # AI Agent 컨텍스트
├── README.md          # 이 파일
│
├── inbox/             # RAW 입력 (미처리)
├── enhanced/          # 구조화된 문서
│   ├── knowledge/     # 추상화된 지식
│   ├── cases/         # 실제 사례
│   └── decisions/     # 의사결정 기록 (ADR)
│
├── docs/              # 규칙/정책 문서
│   ├── humans/        # WHY - 사람이 결정
│   └── agents/        # HOW - AI 실행 규칙
│
├── exports/           # 자동 생성된 Output
│   ├── blog/
│   ├── resume/
│   └── notion/
│
└── scripts/           # 자동화 스크립트
```

## Domains

| Domain | Description |
|--------|-------------|
| Product | 무엇을 만들 것인가? |
| Engineering | 어떻게 만들 것인가? |
| Operations | 어떻게 돌릴 것인가? |
| Growth | 어떻게 알릴 것인가? |
| Business | 어떻게 유지할 것인가? |
| AI/Automation | 어떻게 위임할 것인가? |

## Tech Stack

| Layer | Tech |
|-------|------|
| Storage | Git (GitHub) |
| Format | MDX/Markdown |
| Processing | Claude Code |
| Export - Web | Docusaurus |
| Export - Blog | Remix |
| Hosting | Cloudflare Pages |

## Related Documents

- [GOAL.md](./GOAL.md) - 상세 작업 계획서
- [PRD.md](./PRD.md) - 초기 구조 설계
