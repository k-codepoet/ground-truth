---
title: "tidy/triage 공통 프로토콜 필요성 발견"
date: 2026-01-04
source: gemify:draft session
type: conversation
status: used
used_in: drafts/ground-truth-protocol.md
---

# tidy/triage 공통 프로토콜 필요성 발견

## 맥락

gemify:tidy 스킬 설계 중 triage와의 순환 의존성 발견.

## 핵심 논의

### 순환 구조

```
triage (inbox 클러스터링/우선순위)
   ↓
draft → library (생산)
   ↓
tidy (검증/정리)
   ↓ outdated 발견 → 새 thought?
inbox
   ↓
triage...
```

### 공통점

- 둘 다 "현황 파악 → 제안 → 컨펌 → 실행"
- 둘 다 스키마/컨벤션 기반 동작
- 점진적 실행 (한 번에 하나씩)

### 선행 작업 발견

tidy가 먼저냐 triage가 먼저냐 → 둘 다 막혀있음

```
tidy 먼저? → 스키마 없으면 검증 불가
triage 먼저? → library가 outdated면 잘못된 곳에 연결
```

→ **공통 프로토콜/스키마 정의가 진짜 선행 작업**

### 참조 패턴

gemify:improve-plugin과 forgeify:improve-plugin이 프로토콜로 상호작용하듯,
tidy와 triage도 공통 프로토콜을 참조해야 함.

## 필요한 정의

1. **artifact 필드 스키마** - library/views가 실제 결과물과 연결
2. **컨벤션 규칙** - 네이밍, 경로, 참조 방식
3. **source-of-truth 판단 기준** - 불일치 시 어느 쪽 기준으로 수정할지

## 깨진 유리창 + 제텔카스텐 관점

- 기존 체계가 깨끗해야 새 것을 올바른 곳에 연결
- tidy로 먼저 정리 → triage로 새 inbox 연결
- 하지만 둘 다 프로토콜이 있어야 동작
