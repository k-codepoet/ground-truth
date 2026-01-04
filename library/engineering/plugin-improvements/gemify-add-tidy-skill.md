---
target_plugin: gemify
improvement_type: feature
priority: high
problem: "ground-truth의 views/library 문서가 시간이 지나면서 outdated되거나 깨진 링크 발생. 점진적으로 정리하는 도구가 없음."
solution: "gemify:tidy 스킬 추가 - 역방향 검증 도구로 views ↔ artifact 일치 검사, 점진적 실행"
requirements:
  - views ↔ artifact 일치 검사
  - 하나씩 집중 출력 포맷 (HITL)
  - 점진적 실행 (한 번에 하나씩)
  - ground-truth-protocol.md 참조
references:
  - library/ai-automation/gemify-tidy-skill.md
  - library/operations/ground-truth-protocol.md
domain: engineering
views: []
---

## Why

ground-truth 문서들이 시간이 지나면서:
- **outdated**: 플러그인 리네임(ced → forgeify) 후 문서가 과거 버전 참조
- **깨진 링크**: sources, 관련 문서 경로가 실제로 없는 파일 가리킴
- **used 마킹 누락**: inbox가 사용됐는데 status가 raw

깨진 유리창 이론 + 제텔카스텐 관점:
- 기존 체계가 깨끗해야 새 것을 올바른 곳에 연결
- tidy로 먼저 정리 → triage로 새 inbox 연결

## What

### 스킬 파일

`skills/tidy.md` 생성:

```yaml
---
name: tidy
description: "ground-truth 문서 정리 - views ↔ artifact 일치 검사, 역방향 검증"
triggers:
  - "정리"
  - "tidy"
  - "검증"
  - "outdated"
---
```

### 핵심 동작

1. **탐색**: views의 artifact 필드와 실제 파일 비교
2. **리포트**: 불일치 하나만 보여줌 (하나씩 집중)
3. **HITL 판단 요청**:
   - [A] artifact 기준으로 view 업데이트
   - [B] view 기준으로 artifact 수정 (별도 작업)
   - [C] 둘 다 반영할 부분 있음 (수동)
   - [D] 나중에 볼게
4. **수정**: 사용자 컨펌 후 실행
5. **종료**: 다음 tidy 호출 대기

### 탐색 우선순위

1. artifact 필드 누락 (views에 없음)
2. 깨진 링크 (존재하지 않는 파일 참조)
3. used 마킹 누락 (inbox status)
4. outdated 감지 (오래된 updated, 이름 변경된 참조)
5. 중복 view

### 출력 포맷 예시

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

### 커맨드 파일

`commands/tidy.md` 생성:

```yaml
---
name: tidy
description: "ground-truth 문서 점진적 정리"
---

tidy 스킬을 호출하여 문서 정리 시작
```

## Scope

### 포함
- skills/tidy.md 생성
- commands/tidy.md 생성
- ground-truth-protocol.md 참조 로직

### 제외
- triage 스킬 (별도 개선 문서로)
- views 자동 생성 (수동 workflow 유지)
