# Knowledge Pipeline - AI Agent Context

## Overview
이 레포는 1인 AI Company의 Knowledge Management System입니다.
RAW 경험을 수집하고, AI가 분류/태깅/구조화하여, 다양한 형태로 Export합니다.

## Core Flow
```
INPUT → AI PROCESSING → GIT STORAGE → MULTI-OUTPUT
```

## Folder Structure

### `inbox/` - RAW 입력 (미처리)
- 자유 형식의 raw 경험, 메모, 아이디어
- `status: raw` 상태
- AI Agent가 분류/태깅 후 enhanced/로 이동

### `enhanced/` - 구조화된 문서
- `knowledge/` - 추상화된 원칙, 패턴 (미래의 나, AI Agent용)
- `cases/` - 구체적 사례, 재현 가능 (나, 동료용)
- `decisions/` - 트레이드오프, 선택 이유 (ADR)

### `docs/` - 규칙/정책 문서
- `humans/` - WHY: 사람이 결정한 원칙, 정책
- `agents/` - HOW: AI Agent 실행 규칙

### `exports/` - 자동 생성된 Output
- `blog/` - 스토리텔링, 공유 가치
- `resume/` - 성과, 임팩트, 수치
- `notion/` - 읽기용 뷰

### `scripts/` - 자동화 스크립트

## 6 Domains
| Domain | 질문 |
|--------|------|
| Product | 무엇을 만들 것인가? (문제 정의, 기획) |
| Engineering | 어떻게 만들 것인가? (코드, 아키텍처) |
| Operations | 어떻게 돌릴 것인가? (인프라, 배포, 모니터링) |
| Growth | 어떻게 알릴 것인가? (마케팅, 세일즈, 콘텐츠) |
| Business | 어떻게 유지할 것인가? (재무, 법무, 계약) |
| AI/Automation | 어떻게 위임할 것인가? (Agent, Workflow, LLM) |

## Agent Processing Rules

### 1. 분류 (Domain Decision)
inbox/ 문서를 읽고 적절한 domain 결정

### 2. 태깅 (Tech/Concepts)
- `tech`: 사용된 기술 스택 추출
- `concepts`: 핵심 개념, 패턴 추출

### 3. 검증 (HITL)
부족한 정보가 있으면 사용자에게 질문

### 4. 구조화 (Template Based)
enhanced/ 템플릿에 맞춰 문서 생성

## Core Principles
1. **Git = Source of Truth**: 모든 지식은 Git의 mdx/markdown으로 관리
2. **AI 자동화**: 분류, 태깅, 메타데이터 생성은 AI가 수행
3. **HITL**: 모자란 정보는 사용자에게 질문
4. **Multi-Output**: 하나의 RAW에서 여러 형태의 Export 생성
5. **점진적 구축**: 새 구조로 하나씩 이전
