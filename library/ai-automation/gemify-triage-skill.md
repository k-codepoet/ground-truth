---
title: "gemify:triage 스킬 설계"
domain: ai-automation
views: []
---

## Context

inbox에 raw 파일이 쌓이면 다음 할 일 찾기가 어려움. 클러스터링과 우선순위 판단이 필요.

**참조 프로토콜**: [ground-truth-protocol](../operations/ground-truth-protocol.md)
**관련 스킬**: [gemify-tidy-skill](./gemify-tidy-skill.md) (역방향 유지보수)

## Content

### 핵심 개념

triage는 **순방향 정리** 도구:
- inbox → library/views 연결점 제안
- 클러스터링 + 우선순위 판단
- 전체 리포트 후 선택

### tidy vs triage

| | triage | tidy |
|---|---|---|
| 대상 | inbox (raw) | library/views/drafts |
| 목적 | 다음 할 일 찾기 | 기존 것 검증/수정 |
| 방향 | 순방향 (생산) | 역방향 (유지보수) |
| 출력 | 전체 리포트 → 선택 | 하나씩 집중 |

**실행 순서**: tidy → triage (깨진 유리창 먼저 수리)

### 동작 흐름

```
/gemify:triage 요청
    ↓
meta/cluster/current.md 있나?
    ├─ 있음 → triage 본체 실행
    └─ 없음 → "클러스터 맵이 없습니다. 먼저 생성할까요? [Y/n]"
                ├─ Y → map 로직 실행 → 저장 → triage 이어가기
                └─ n → 종료
```

### Progressive Disclosure: map 내장

별도 `/gemify:map` 스킬 없음. triage가 내부적으로 처리:
- 필요할 때만 map 노출
- 진입점 하나 유지

### 클러스터 맵 저장

```
meta/
└── cluster/
    ├── current.md          # 최신 버전
    └── .history/
        ├── 2026-01-04-v1.md
        └── ...
```

### 출력 포맷

**전체 리포트 후 선택**:

```
/gemify:triage

## Inbox 현황
- raw thoughts: 35개
- raw materials: 46개

## 클러스터 (4개)
1. gemify 개선 (3개) - 추천
2. 플러그인 개선 (5개)
3. 인프라 (2개)
4. 미분류 (25개)

어느 클러스터부터? [1-4]
```

### 미분류 항목 처리

Claude가 **양쪽 제안**:
- 기존 편입 가능 → [편입] [새 클러스터] [스킵]
- 얼토당토 안 맞음 → 새 클러스터 제안만
- 완전 단독 → draft 시작 제안

### map 동작 (triage 내부)

**자동 제안 → 커스텀 가능**:

```
library/views 분석 중...

## 발견된 클러스터 (3개)
1. gemify 생태계 (subjects: gemify, forgeify)
2. -ify 트릴로지 (subjects: gemify, terrafy, craftify)
3. 인프라 (subjects: terrafy)

이대로 저장할까요?
[Y] 저장  [n] 취소  [c] 커스텀 수정
```

## Connections

- [ground-truth-protocol](../operations/ground-truth-protocol.md) - 공통 프로토콜
- [gemify-tidy-skill](./gemify-tidy-skill.md) - 역방향 유지보수 (tidy 먼저 실행)
