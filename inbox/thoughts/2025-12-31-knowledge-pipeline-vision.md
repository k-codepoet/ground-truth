---
title: "Knowledge Pipeline 비전 총정리"
date: 2025-12-31
references: []
status: used
used_in: drafts/knowledge-pipeline-vision.md
---

## Part 1: 무엇을 만들려는가 (What)

### 한 문장 정의

**"말하는 대로 지식이 정리되는 시스템"**

1인 AI Company를 위한 Knowledge Management System. 머릿속 암묵지를 말로 꺼내면 AI가 자동으로 분류/구조화하고, 다양한 형태로 출력해주는 파이프라인.

### 핵심 문제

| 문제 | 현재 상태 |
|------|----------|
| 지식이 흩어져 있음 | Notion, 메모, 대화 로그, 머릿속 |
| 정리하는 데 시간이 많이 듦 | 수동 분류, 수동 태깅, 수동 연결 |
| 같은 지식을 여러 형태로 재사용 못함 | 블로그 따로, 문서 따로, 이력서 따로 |
| AI Agent에게 맥락을 전달하기 어려움 | 매번 설명해야 함 |

### 최종 목표 (Layer 3: AI Company)

```
CEO 입력 ("블로그 발행해")
    ↓
God PM (오케스트레이터)
    ↓
자동으로 corpus에서 지식 조합
    ↓
배포된 URL
```

### 지식 흐름

```
HEAD (암묵지)
    ↓ 추출 (AI 대화)
INBOX (원시 캡처)
    ↓ 분류 (6개 domain)
CORPUS (구조화된 지식)
    ↓ 조립 (형태별 변환)
EXPORTS (다양한 출력)
    ├── agent-docs (AI Agent용)
    ├── blog (웹 독자용)
    ├── book (출판용)
    └── web (인터랙티브)
```

### 6개 Domain

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

---

## Part 2: 어떻게 만들겠는가 (How)

### 핵심 전략: Bootstrapping

> "knowledge-ops로 knowledge-ops 자체를 문서화한다"

컴파일러가 자기 자신을 컴파일하는 것처럼, 지식 관리 시스템으로 지식 관리 시스템을 만든다.

### 단계별 접근 (Stage 0 → 3)

**Stage 0: 완전 수동 (현재)**
- 사람이 inbox에 파일 생성
- 사람이 corpus로 분류/이동
- 사람이 frontmatter 작성
- **목적**: 구조 검증, 워크플로우 검증

**Stage 1: AI 보조 (MVP)**
- Claude Skill로 대화형 분류
- 소크라테스식 질문으로 생각 정리
- 사람이 최종 컨펌
- **목적**: 피드백 루프 검증

**Stage 2: AI 주도 (중기)**
- 자동 분류 + 연결 그래프
- Export 자동 생성
- 사람은 승인만
- **목적**: 자동화 검증

**Stage 3: AI 자율 (장기)**
- CEO 입력 → 배포까지 자동
- 품질 자동 검증
- **목적**: AI Company 완성

### 현재 구현된 것

```
skills/knowledge-digest/SKILL.md   # Claude 자동 활성화
.claude/commands/digest.md         # /digest 명시적 호출
.claude/settings.json              # SessionStart hook
```

**동작 흐름**:
1. repo에서 Claude Code 실행
2. hook이 inbox 파일 감지 → 알림
3. /digest 또는 "정리해줘"
4. 소크라테스식 질문 (Q1~Q6)
5. 컨펌 → corpus 저장

### 소크라테스식 질문 프레임워크

```
Phase 1 (목적): 왜 남기려고 해? 없으면 뭐가 안 돼?
Phase 2 (압축): 한 문장으로? 핵심만 남기면?
Phase 3 (분류): 6개 domain 중 어디?
Phase 4 (연결): 기존 corpus에 연결되는 거?
```

### 핵심 원칙

| 원칙 | 설명 |
|------|------|
| Git = Source of Truth | 모든 지식은 Git repo의 markdown |
| Working Software First | 설계보다 동작하는 것 먼저 |
| 점진적 자동화 | 수동 → AI 보조 → AI 주도 → AI 자율 |
| 스키마 최소화 | title, domain만 필수 |

### 성공 기준

**Stage 0 완료**:
- [ ] 5개 문서가 inbox → corpus 이동됨
- [ ] 2개 이상 domain에 분포
- [ ] 소크라테스 질문으로 밀도 높아짐

**Stage 1 완료**:
- [ ] /digest로 자동 분류 동작
- [ ] 분류 정확도 80% 이상
- [ ] 문서 10개 이상 축적

---

## 요약

**What**: 말하면 정리되는 1인 AI Company Knowledge System
**How**: Bootstrapping + 단계적 자동화 (수동 → AI 보조 → AI 주도 → AI 자율)
