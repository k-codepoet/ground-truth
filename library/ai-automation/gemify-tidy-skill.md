---
title: "gemify:tidy 스킬 설계"
domain: ai-automation
views: []
---

## Context

ground-truth의 views, library 문서들이 시간이 지나면서 outdated되거나 깨진 링크가 발생. 점진적으로 정리하는 도구가 필요.

**참조 프로토콜**: [ground-truth-protocol](../operations/ground-truth-protocol.md)

## Content

### 핵심 개념

tidy는 **역방향 검증** 도구:
- views ↔ artifact 일치 검사
- library 현황 보고 (사용 중/대기 중)
- 점진적 실행 (한 번에 하나씩)

### 동작 방식

```
리포트 → 컨펌 → 수정
```

1. 문제 발견 시 **하나만** 리포트
2. 사용자가 판단 (HITL)
3. 컨펌 후 수정 실행

### 검증 순서 (역순)

```
artifact (실제 결과물)
   ↑ 대조
views
   ↑ 추적
library
   ↑ 추적
drafts
   ↑ 추적
inbox
```

### 탐색 우선순위

1. artifact 필드 누락 (views에 없음)
2. 깨진 링크 (존재하지 않는 파일 참조)
3. used 마킹 누락 (inbox status)
4. outdated 감지 (오래된 updated, 이름 변경된 참조)
5. 중복 view

### 출력 포맷

**하나씩 집중 방식**:

```
/gemify:tidy

views/by-subject/forgeify.md ↔ plugins/forgeify/ 불일치 발견

artifact가 더 최신입니다 (1시간 전 수정)
view는 2일 전 업데이트

[A] artifact 기준으로 view 업데이트
[B] view 기준으로 artifact 수정 (별도 작업)
[C] 둘 다 반영할 부분 있음 (수동)
[D] 나중에 볼게
```

### source-of-truth 판단

```
의도적 변경: views가 먼저 (설계 → 구현)
급한 수정: artifact가 먼저 (hotfix → 나중에 문서화)

→ 수정 시점으로 추측 + HITL로 최종 판단
```

### triage와의 관계

| | triage | tidy |
|---|---|---|
| 대상 | inbox (raw) | library/views/drafts |
| 목적 | 다음 할 일 찾기 | 기존 것 검증/수정 |
| 방향 | 순방향 (생산) | 역방향 (유지보수) |

**실행 순서**:
1. 프로토콜 정의 (완료)
2. `/gemify:tidy` (깨진 유리창 수리)
3. `/gemify:triage` (새 inbox 연결)

## Connections

- [ground-truth-protocol](../operations/ground-truth-protocol.md) - 공통 프로토콜
- gemify:triage - 순방향 정리 (inbox → library)
