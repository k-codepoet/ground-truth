---
title: "AI Company Trilogy 네이밍 의사결정"
date: 2026-01-03
source: "Claude 대화 - AI Company 구축"
type: document
status: raw
used_in:
---

# AI Company Trilogy 네이밍 의사결정 기록

> **Date**: 2025-01-03
> **Context**: AI Company 구축을 위한 3대 핵심 시스템 정의 및 네이밍
> **Status**: Decision Made
> **Final Decision**: Gemify, Terrafy, Craftify

---

## 1. 발단 (Origin)

AI Company를 구축하면서 세 가지 핵심 시스템이 필요함을 인식:

```
AI Company = CEO 입력 → 배포된 URL

이를 위해 필요한 것:
1. 뭘 만들지? (설계도, 지식)        → Gemify (이미 존재)
2. 어디서 돌릴지? (인프라)          → ???? (필요)
3. 어떻게 만들지? (개발, 코딩)      → ???? (필요)
```

**문제**: 2번과 3번 시스템의 역할 정의 및 네이밍 필요

---

## 2. 의사결정 과정

### Phase 1: 역할 혼동 정리

**초기 혼동**:
- 3번을 "배포/DevOps"로 생각함
- 실제로는 "개발/코딩"이 빠져있었음

**정리 후**:

| # | 질문 | 역할 | 범위 |
|---|------|------|------|
| 1 | WHAT | 설계 | 생각 → 설계도/스펙 |
| 2 | WHERE | 인프라 | 서버 → 클러스터 |
| 3 | HOW | 개발 | 스펙 → 코드 |

### Phase 2: 메타포 탐색

**도시 건설 비유** 채택:

```
┌─────────────────────────────────────────────────────────────────┐
│  도시 = AI Company                                              │
│                                                                 │
│  마스터플랜 (Gemify)                                            │
│      ↓                                                          │
│  인프라 공사 - 도로, 전기, 수도, 통신 (Terrafy)                  │
│      ↓                                                          │
│  건물 시공 - 주거지, 상업지, 공장 (Craftify)                     │
│      ↓                                                          │
│  🌆 살아있는 도시 (Live Services)                               │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 3: 네이밍 전략

**기존 Gemify 브랜딩 원칙 적용**:
- 일관성: 같은 패턴 (-ify)
- 직관성: 이름에서 역할 파악 가능
- 행동 유도: 동사형

---

## 3. 최종 결정

### The -ify Trilogy

```
┌─────────────────────────────────────────────────────────────────┐
│  AI Company: The -ify Trilogy                                   │
│                                                                 │
│  Gemify   💎  "Turn your thoughts into gems"                   │
│           └── WHAT: 뭘 만들지 (지식 → 설계도)                   │
│                                                                 │
│  Terrafy  🏗️  "Lay the groundwork for your digital city"       │
│           └── WHERE: 어디서 돌릴지 (서버 → 인프라)              │
│                                                                 │
│  Craftify 🔨  "Craft your products with AI"                    │
│           └── HOW: 어떻게 만들지 (설계도 → 코드)                │
└─────────────────────────────────────────────────────────────────┘
```

### 상세 스펙

#### Gemify 💎 (이미 존재)

```yaml
Name: Gemify
Tagline: "Turn your thoughts into gems"
Role: WHAT - 뭘 만들지

Core Functions:
  - 생각 추출 및 구조화
  - 설계도/스펙 생성
  - 지식 문서화
  - agent-docs 출력

Input → Output:
  - Raw thoughts → Structured specs, PRD, agent-docs
```

#### Terrafy 🏗️

```yaml
Name: Terrafy
Tagline: "Lay the groundwork for your digital city"
Alternative: "Turn your servers into solid ground"
Role: WHERE - 어디서 돌릴지

Core Functions:
  - SSH 연결 및 초기 설정
  - Docker/k3s 클러스터 구축
  - ArgoCD/Portainer 설치
  - 네트워크/DNS 설정
  - 보안 hardening
  - 모니터링 설정

Input → Output:
  - Raw server IP → Ready-to-deploy cluster
  - "SSH 접속 가능" → "kubectl 동작, ArgoCD 접속 가능"
```

#### Craftify 🔨

```yaml
Name: Craftify
Tagline: "Craft your products with AI"
Alternative: "From specs to working code"
Role: HOW - 어떻게 만들지

Core Functions:
  - Gemify output(specs) → 코드 구현
  - Claude Code 기반 개발
  - 프로토타입/MVP 생성
  - 테스트 코드 작성
  - 코드 리뷰 & 리팩토링

Input → Output:
  - PRD/Specs → Working prototype
  - "사용자 인증 기능 필요" → "auth.py + tests + API"
```

---

## 4. 전체 흐름

```
CEO: "사용자 인증 서비스 만들어줘"
        │
        ▼
┌─── Gemify 💎 ───┐
│ 요구사항 분석    │
│ 설계도/스펙 생성 │
└────────┬────────┘
         │ specs, PRD, agent-docs
         ▼
┌─── Craftify 🔨 ──┐
│ 코드 구현        │
│ 테스트 작성      │
└────────┬─────────┘
         │ working code (git repo)
         ▼
┌─── Terrafy 🏗️ ──┐
│ 인프라 확인      │
│ 배포 실행        │
└────────┬─────────┘
         │
         ▼
CEO에게: "배포 완료: https://auth.example.com"
```

---

## 5. 도시 메타포 상세

```
┌─────────────────────────────────────────────────────────────────┐
│  Terrafy = 도시 인프라 (Infrastructure)                          │
│                                                                 │
│  도로      → Network, Load Balancer                             │
│  전기      → Computing resources (CPU, Memory)                  │
│  수도      → Storage (PV, S3)                                   │
│  통신      → DNS, SSL, Ingress                                  │
│  하수도    → Logging, Monitoring                                │
│                                                                 │
│  "건물 짓기 전에 땅이 준비되어야 한다"                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  그 위에 올라가는 건물들 = Craftify가 만든 서비스들               │
│                                                                 │
│  🏠 주거지   → 웹앱, 대시보드, 프론트엔드                        │
│  🏪 상업지   → API 서버, SaaS, 백엔드                           │
│  🏭 공장     → 배치 처리, ETL 파이프라인, Worker                 │
│  🏛️ 공공시설 → 인증 서비스, 로깅, 모니터링 대시보드              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. 선택 이유 요약

| 기준 | 결정 | 이유 |
|------|------|------|
| 패턴 | -ify 삼형제 | 브랜드 일관성, Gemify와 연결 |
| Terrafy | Terra + ify | "땅/기반" 의미, Terraform 연상 |
| Craftify | Craft + ify | 장인정신, 개발 문화와 연결 |
| 메타포 | 도시 건설 | 인프라→서비스 관계 직관적 설명 |

---

## 7. 기각된 대안들

| 대안 | 기각 이유 |
|------|----------|
| Buildify (인프라) | Craftify와 이미지 겹침 |
| Foundry (인프라) | -ify 패턴 깨짐 |
| Codeify (개발) | 너무 평범, 차별화 부족 |
| Shipify (개발) | 배포에 초점, 개발 의미 약함 |
