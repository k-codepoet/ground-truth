---
title: "Namify - 제품 네이밍 가이드"
subject: namify
updated: 2026-01-03
artifact: plugins/namify/
artifact_type: plugin
sources:
  - library/specs/namify-plugin-spec.md
  - library/decisions/gemify-branding-decision.md
---

# Namify - 제품 네이밍 가이드

> "Name it right"

## 구조

```
┌─────────────────────────────────────────────────────────────────┐
│  Namify: 이름 만드는 과정                                        │
│                                                                 │
│  1. 핵심 가치 추출                                               │
│     "이 제품이 하는 일은?"                                       │
│         ↓                                                       │
│  2. 메타포 탐색                                                  │
│     광물? 식물? 요리? 건축?                                      │
│         ↓                                                       │
│  3. 이름 생성                                                    │
│     패턴 적용 (-ify, Craft, Lab...)                             │
│         ↓                                                       │
│  4. 검증                                                        │
│     발음, 기존 의미, 문화적 적합성                               │
│         ↓                                                       │
│  5. 선택 + 태그라인                                              │
└─────────────────────────────────────────────────────────────────┘
```

## 스토리

### 왜 (Why)

좋은 이름은:
- 기억에 남는다
- 제품이 뭘 하는지 암시한다
- 시리즈로 확장 가능하다

### 뭘 (What)

**Namify 플러그인**:
```
/name [제품 설명]                    # 기본 이름 생성
/name [제품 설명] --pattern "-ify"   # 특정 패턴 적용
/name [제품 설명] --series "Gemify"  # 시리즈 일관성
```

**핵심 원칙**:
- 브랜드 레이어 vs UX 레이어 분리
- 사용자 맞춤 패턴 (일관성)
- 문화적 검증

### 어디까지 (Scope)

**MVP**:
- `/name` 스킬 하나에 집중
- 메타포 → 후보 → 검증 → 추천

**Future**:
- 태그라인 생성
- 도메인/상표 체크
- 브랜딩 가이드 출력

## 사례: -ify Trilogy

```
┌─────────────────────────────────────────────────────────────────┐
│  패턴: -ify (변환을 의미)                                        │
│                                                                 │
│  Gemify   💎  "Turn your thoughts into gems"                   │
│           └── WHAT: 뭘 만들지 (생각 → 지식)                     │
│                                                                 │
│  Terrafy  🏗️  "Lay the groundwork for your digital city"       │
│           └── WHERE: 어디서 돌릴지 (서버 → 인프라)              │
│                                                                 │
│  Craftify 🔨  "Craft your products with AI"                    │
│           └── HOW: 어떻게 만들지 (설계도 → 코드)                │
└─────────────────────────────────────────────────────────────────┘
```

**선택 이유**:
- 일관성: 같은 패턴으로 시리즈 형성
- 직관성: 이름에서 역할 파악
- 행동 유도: 동사형 (-ify = ~로 만들다)

## 안티패턴

| 피해야 할 것 | 이유 |
|-------------|------|
| 메타포 혼재 | 이미지 혼란 (Capture + Cultivate) |
| UX에 강한 메타포 | 학습 곡선 상승 (ore/ flux/) |
| 설명이 필요한 이름 | 첫인상 실패 (Corpus) |
| 문화적 맹점 | 타겟 이탈 (술 메타포 → 미성년자 제외) |

## 관련 문서

- [Namify Plugin 스펙](../../library/specs/namify-plugin-spec.md) - 상세 스펙
- [Gemify 브랜딩 의사결정](../../library/decisions/gemify-branding-decision.md) - 실제 사례
- [제품 네이밍 프레임워크](../../inbox/materials/product-naming-branding-framework.md) - 원본 프레임워크
