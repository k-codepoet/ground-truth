---
title: "DevOps 관련 용어 분석: 철학과 방법론의 경계"
date: 2026-01-03
source: "/home/choigawoon/k-codepoet/devops-terminology-analysis.md"
type: document
status: raw
used_in: null
references:
  - DevOps
  - GitOps
  - MLOps
  - AIOps
  - DevSecOps
---

# DevOps 관련 용어 분석: 철학과 방법론의 경계

## 발단

> "DevOps, GitOps, MLOps, AIOps, DevSecOps의 포함관계와 상관관계가 궁금하다"

단순 용어 정리가 아닌, 각 개념이 **어디까지 정의하고 어디부터 자유를 주는가**를 파악하려는 질문에서 시작됨.

---

## 의사결정 과정

### 1단계: 관계 파악

```
DevOps (기반 철학)
├── GitOps      → 하위집합 (구현 방법론)
├── DevSecOps   → 확장 (DevOps + Security)
├── MLOps       → 도메인 적용 (DevOps for ML)
└── AIOps       → 역방향 (AI for Ops) ← 방향이 다름
```

### 2단계: "철학"의 정의

Framework vs Library의 비유에서 핵심을 도출:

| 구분 | 정의하는 것 | 비유 |
|------|-------------|------|
| Library | 기능 | 내가 부르는 것 |
| Framework | 기능 + 제어 흐름 | 나를 부르는 것 (IoC) |
| Philosophy | 방향 + 원칙 | "왜"와 "어디로" |
| Methodology | 구체적 방법 | "어떻게" |

**핵심 인사이트:** Philosophy는 "왜"와 "어디로"를 정의하고, 구체적인 "어떻게"는 정의하지 않는다.

### 3단계: Why / What / How 프레임 적용

```
추상적 ◀───────────────────────────────▶ 구체적

        Why          What          How
         │            │             │
DevOps   ████████████████           ░░░░░░░░  (How 자유)
GitOps   ░░░░░░░░░░░░████████████████████████  (How 강제)
DevSecOps████████████████████████   ░░░░░░░░  (What 확장)
MLOps    ░░░░░░░░░░░░████████████████░░░░░░░  (What 재정의)
AIOps    ████████████████████████████░░░░░░░  (독자적 Why)
```

### 4단계: GitOps의 차별점

GitOps만 유일하게 **How를 강하게 정의**:

1. Git = Single Source of Truth
2. Declarative (선언적)
3. Pull-based (Agent가 당겨감)
4. Continuous Reconciliation (자동 복구)

→ 이 중 하나라도 빠지면 GitOps가 아님

### 5단계: 대안 검토

| 방식 | 특징 | 트레이드오프 |
|------|------|--------------|
| GitOps (Pull) | Agent가 Git 상태로 sync | 복잡도 ↑, 안정성 ↑ |
| Push-based CI | CI가 직접 배포 | 단순함, 드리프트 방지 없음 |
| ChatOps | Slack 등에서 명령 | 가시성 ↑, 재현성 ↓ |
| ClickOps | UI 클릭 | 쉬움, 감사추적 불가 |

---

## 핵심 결론

### 1. 철학 vs 방법론의 구분

```
"DevOps 한다" → 검증 불가 (문화/철학)
"GitOps 한다" → 검증 가능 (제약 체크리스트 존재)
```

### 2. 각 용어의 포지션

| 용어 | 성격 | 정의 범위 |
|------|------|-----------|
| **DevOps** | 철학 | Why + What |
| **GitOps** | Opinionated 방법론 | What + How (강제) |
| **DevSecOps** | 확장된 철학 | Why + What (보안 추가) |
| **MLOps** | 도메인 특화 | What (재정의) + How (느슨) |
| **AIOps** | 별개 영역 | Why + What (역방향) |

### 3. 선택의 기준

GitOps는 "정답"이 아니라 **트레이드오프**:
- 복잡도를 감수 → 감사추적, 재현성, 드리프트방지 획득
- 작은 팀/빠른 실험 → Push-based가 실용적일 수 있음

### 4. 비유로 정리

```
DevOps    = 요리하는 방법 (철학)
GitOps    = 레시피북으로 요리하기 (구체적 방법론)
DevSecOps = 위생관리하며 요리하기 (영역 확장)
MLOps     = AI 요리사 훈련시키기 (새 도메인)
AIOps     = AI가 주방 관리하기 (역방향)
```

---

## 다음 탐구 방향

각 엔지니어링 분야를 Why/What/How 레이어로 조망하는 프레임워크 확립:

- [ ] CI/CD 파이프라인 설계 철학
- [ ] Infrastructure as Code의 레이어
- [ ] Observability의 Why/What/How
- [ ] Security의 Shift Left 원칙

---

*작성일: 2025-01-03*
*맥락: DevOps 용어 분석 대화에서 도출*
