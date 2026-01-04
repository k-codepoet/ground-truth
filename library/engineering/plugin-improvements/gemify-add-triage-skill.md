---
target_plugin: gemify
improvement_type: feature
priority: high
problem: "inbox에 raw 파일이 쌓이면 다음 할 일 찾기가 어려움. 클러스터링과 우선순위 판단이 없음."
solution: "gemify:triage 스킬 추가 - 순방향 정리 도구로 inbox 클러스터링 + 우선순위 판단"
requirements:
  - 전체 리포트 후 선택 방식
  - map 로직 내장 (progressive disclosure)
  - meta/cluster/ 저장 구조
  - 미분류 항목 양쪽 제안 (편입 vs 새 클러스터)
references:
  - library/ai-automation/gemify-triage-skill.md
  - library/ai-automation/gemify-tidy-skill.md
  - library/operations/ground-truth-protocol.md
domain: engineering
views: []
---

## Why

inbox에 raw thoughts/materials가 쌓이면:
- 어디서부터 시작할지 모름
- 연관된 것끼리 묶여있지 않음
- 기존 library/views와 어떻게 연결되는지 불명확

tidy가 역방향(유지보수)이라면, triage는 순방향(생산) 정리 도구.

## What

### 스킬 파일

`skills/triage.md` 생성:

```yaml
---
name: triage
description: "inbox 클러스터링 + 우선순위 판단 + 다음 액션 제안"
triggers:
  - "triage"
  - "정리"
  - "inbox"
  - "다음 뭐 해"
---
```

### 핵심 동작

1. **클러스터 맵 확인**: `meta/cluster/current.md` 있나?
   - 없음 → "클러스터 맵이 없습니다. 먼저 생성할까요? [Y/n]"
   - Y → map 로직 실행 → 저장 → 이어가기

2. **전체 리포트**:
   ```
   ## Inbox 현황
   - raw thoughts: N개
   - raw materials: M개

   ## 클러스터 (K개)
   1. gemify 개선 (3개) - 추천
   2. 플러그인 개선 (5개)
   ...

   어느 클러스터부터? [1-K]
   ```

3. **미분류 처리**:
   - 기존 편입 가능 → [편입] [새 클러스터] [스킵]
   - 얼토당토 안 맞음 → 새 클러스터 제안만
   - 완전 단독 → draft 시작 제안

### map 로직 (내장)

```
library/views 분석 중...

## 발견된 클러스터 (3개)
1. gemify 생태계 (subjects: gemify, forgeify)
2. -ify 트릴로지 (subjects: gemify, terrafy, craftify)
...

이대로 저장할까요?
[Y] 저장  [n] 취소  [c] 커스텀 수정
```

### 클러스터 맵 저장

```
meta/
└── cluster/
    ├── current.md          # 최신 버전
    └── .history/
        ├── 2026-01-04-v1.md
        └── ...
```

### 커맨드 파일

`commands/triage.md` 생성:

```yaml
---
name: triage
description: "inbox 정리 + 다음 할 일 찾기"
---

triage 스킬을 호출하여 inbox 정리 시작
```

## Scope

### 포함
- skills/triage.md 생성
- commands/triage.md 생성
- map 로직 내장 (별도 스킬 X)
- meta/cluster/ 구조 지원

### 제외
- tidy 스킬 (별도 개선 문서)
- 자동 클러스터링 (사용자 컨펌 필수)
