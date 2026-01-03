---
title: "gemify 자동 캡처 제안 에이전트 아이디어"
date: 2026-01-03
status: raw
used_in: null
references:
  - inbox/materials/2026-01-03-gemify-capture-pair-manual-trigger-pattern.md
---

## 핵심 원칙

**각 task는 독립적으로 마무리되어야 한다.**

작업 중 별개 이슈가 발생하면:
1. 현재 task는 그대로 진행
2. 별개 이슈는 capture-pair로 inbox에 기록
3. 나중에 별도 task로 처리

→ task 간 오염 방지, 일감 누락 방지

## 에이전트 역할

### 이름: `issue-tracker` 또는 `side-issue-catcher`

### 동작 방식

**자동 감지 모드**:
- 작업 중 변경점/사이드 이슈 발생 감지
- "이건 현재 task와 별개 이슈네요. 기록해둘까요?" 제안
- 승인 시 capture-pair 실행

**명시적 호출 모드**:
- 사용자: "지금 하려던 것과 별개 이슈 발생했어. 기록 남겨줘"
- 에이전트: 즉시 capture-pair 실행

### 감지 패턴

| 패턴 | 예시 |
|------|------|
| 별개 이슈 발견 | "이것도 고쳐야겠네", "이건 나중에" |
| 반복 문제 | "매번 이런다", "또 이 오류" |
| 개선 아이디어 | "이렇게 하면 좋겠다" |
| 의존성 발견 | "이거 먼저 해야겠네" |

## 워크플로우 예시

```
[terrafy 플러그인 개발 중]
    │
    ├─ agents 경로 오류 발생 (별개 이슈!)
    │   │
    │   └─ issue-tracker 감지
    │       "현재 task(terrafy)와 별개 이슈입니다. 기록할까요?"
    │       │
    │       └─ capture-pair 실행
    │           - material: 오류 상황
    │           - thought: 개선 방안
    │
    └─ terrafy 작업 계속 진행 (오염 없음)
```

## 구현 고려사항

- 현재 task 컨텍스트 파악 필요 (무엇이 "별개"인지 판단)
- 제안 빈도 조절 (너무 자주 X)
- 명시적 호출은 항상 즉시 실행

## 우선순위

높음 - task 독립성 유지와 일감 누락 방지는 핵심 원칙
