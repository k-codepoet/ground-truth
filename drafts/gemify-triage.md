---
title: "gemify:triage 스킬 설계"
created: 2026-01-04
updated: 2026-01-04
turns: 6
revision: 1
status: set
sources:
  - inbox/thoughts/2026-01-02-inbox-triage-skill-idea.md
  - library/operations/ground-truth-protocol.md
  - library/ai-automation/gemify-tidy-skill.md
history: []
---

# gemify:triage 스킬 설계

## 원석에서 가져온 아이디어

- inbox raw 파일 수집
- references 기반 연결 관계 분석
- 주제별 클러스터링
- 우선순위 자동 판단
- 추천 다음 액션 제시

## 프로토콜에서 정의된 역할

```
inbox → library/views 연결점 제안:

1. 클러스터링 - 비슷한 thoughts/materials 묶기
2. 연결점 찾기 - 기존 library/views 어디와 연결되는지
3. HITL 확인 - "이건 gemify view에 추가될 재료 같아요" → 사람 판단
```

## tidy와의 관계

| | triage | tidy |
|---|---|---|
| 대상 | inbox (raw) | library/views/drafts |
| 목적 | 다음 할 일 찾기 | 기존 것 검증/수정 |
| 방향 | 순방향 (생산) | 역방향 (유지보수) |

실행 순서: tidy → triage (깨진 유리창 먼저 수리)

## Open Questions

- [x] 클러스터링 알고리즘은? → **triage 내부에서 map 로직 처리 (progressive disclosure)**
- [x] 출력 포맷 (리스트 vs 하나씩)? → **전체 리포트 후 선택 (Option B)**
- [x] 우선순위 가중치? → **Claude가 판단 후 양쪽 제안**
- [x] library/views 연결점 제안 방식? → **기존 편입 vs 새 클러스터 제안**

## 발견: 선행 스킬 필요

### 문제

inbox를 클러스터링하려면 **기준점**이 필요:
- 기존 지식 체계의 클러스터 구조
- 대주제 / 소주제 관계
- 어디에 편입 가능한지 판단 기준

현재 이 "클러스터 맵"이 없음.

### 해결: 선행 스킬

```
/gemify:triage 요청
    ↓
클러스터 맵 있나?
    ├─ 있음 → triage 본체 실행
    └─ 없음 → 클러스터 맵 생성 스킬 발동
                ↓
              library/views 분석
              대주제/소주제 추출
              클러스터 맵 저장
                ↓
              triage 본체 실행
```

### 클러스터 맵 내용

```yaml
# views/clusters.md 또는 library/operations/에 저장?

clusters:
  - name: "gemify 생태계"
    subjects: [gemify, forgeify]
    keywords: [지식, 플러그인, draft, library]

  - name: "-ify 트릴로지"
    subjects: [gemify, terrafy, craftify]
    keywords: [what, where, how]

  - name: "인프라"
    subjects: [terrafy]
    keywords: [docker, k8s, infra]
```

### 스킬 이름: `/gemify:map`

**선택 이유**:
- "map out" = 구조화하다 (미국 문화권에서 직관적)
- "knowledge map", "mental map" 익숙한 표현
- taxonomy는 학술적, cluster는 기술 용어 느낌

### Progressive Disclosure: triage 안에 map 포함

**별도 스킬 X** → triage가 map을 내부적으로 처리

```
/gemify:triage 요청
    ↓
meta/cluster/current.md 있나?
    ├─ 있음 → triage 본체 실행
    └─ 없음 → "클러스터 맵이 없습니다. 먼저 생성할까요? [Y/n]"
                ├─ Y → map 로직 실행 → 저장 → triage 이어가기
                └─ n → 종료
```

**장점**:
- 진입점 하나 (`/gemify:triage`)
- 필요할 때만 map 노출 (progressive disclosure)
- 사용자가 map만 업데이트하고 싶으면 `meta/cluster/current.md` 직접 수정

### 저장 위치: `meta/cluster/`

```
meta/
└── cluster/
    ├── current.md          # 최신 버전 (항상 이걸 참조)
    └── .history/
        ├── 2026-01-04-v1.md
        └── 2026-01-05-v2.md
```

**특징**:
- 모든 지식 체계에서 참조하는 메타 정보
- 변경 시 `.history/`에 스냅샷
- `current.md`는 항상 최신 유지

### map 동작 흐름: 자동 제안 → 커스텀 가능

```
/gemify:map

library/views 분석 중...

## 발견된 클러스터 (3개)

1. gemify 생태계
   - subjects: gemify, forgeify
   - views: 2개
   - library: 15개

2. -ify 트릴로지
   - subjects: gemify, terrafy, craftify
   - views: 3개
   - library: 8개

3. 인프라
   - subjects: terrafy
   - views: 1개
   - library: 3개

이대로 저장할까요?
[Y] 저장  [n] 취소  [c] 커스텀 수정
```

**커스텀 수정 시**:
```
> c

어떻게 수정할까요?
(예: "gemify, forgeify는 지식 생산 도구로 묶어줘")
(예: "인프라 클러스터에 devops 키워드 추가")

> namify는 gemify 생태계에 넣어줘

수정된 클러스터:
1. gemify 생태계
   - subjects: gemify, forgeify, namify  ← 추가됨
   ...

저장할까요? [Y/n/c]
```

## 결정된 사항

### 출력 포맷: 전체 리포트 후 선택

tidy와 다르게, triage는 **전체 현황**을 먼저 보여줌:

```
/gemify:triage

## Inbox 현황
- raw thoughts: 35개
- raw materials: 46개

## 클러스터 (4개)
1. gemify 개선 (3개) - 추천
2. 플러그인 개선 (5개)
3. 인프라 (2개)
4. 단독 (25개)

어느 클러스터부터? [1-4]
```

**이유**:
- triage는 "다음 뭐 할지" 결정 → 전체 그림 필요
- tidy는 "이거 맞아?" 검증 → 하나씩 집중

### 미분류 항목 처리

미분류 inbox 선택 시, Claude가 **양쪽 제안**:

```
/gemify:triage
> 3  (미분류 선택)

## 미분류 항목 분석 (24개)

### 기존 클러스터 편입 가능 (8개)
- domain-criteria.md
  → "operations" 클러스터에 가까움 (키워드: 분류, 기준)
  [1] 편입  [2] 새 클러스터  [3] 스킵

- personal-essay-publishing.md
  → "growth" 클러스터에 가까움 (키워드: 발행, 콘텐츠)
  [1] 편입  [2] 새 클러스터  [3] 스킵

### 새 클러스터 제안 (3개 묶음)
- elementary-schedule-project.md
- yunseul-schedule-build-plan.md
  → 새 클러스터 "개인 프로젝트" 생성?
  [Y] 생성  [n] 스킵  [c] 다른 이름

### 단독 처리 권장 (13개)
- random-thought-xyz.md
  → 기존 클러스터와 연결점 없음
  [1] /gemify:draft 시작  [2] 스킵
```

**원칙**:
- 기존 편입 가능하면 양쪽 제안 (편입 vs 새 클러스터)
- 얼토당토 안 맞으면 새 클러스터 제안만
- 완전 단독이면 draft 시작 제안
