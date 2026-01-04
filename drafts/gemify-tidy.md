---
title: "gemify:tidy 스킬 설계"
created: 2026-01-03
updated: 2026-01-03
turns: 6
revision: 1
status: cutting
sources:
  - inbox/thoughts/2026-01-03-gemify-tidy-command.md
  - inbox/thoughts/2026-01-02-inbox-triage-skill-idea.md
history: []
---

# gemify:tidy 스킬 설계

## 원석에서 가져온 아이디어

- 깨진 링크 탐지 (frontmatter sources, 본문 링크)
- outdated 문서 표시 (오래된 updated 날짜, 참조 플러그인 변경)
- 중복 view 정리 제안

## 추가로 발견된 문제

- `used` 마킹 누락: inbox 파일이 drafts/library에서 사용됐는데 status가 여전히 `raw`

## 결정된 사항

### 동작 방식: 리포트 → 컨펌 → 수정

1. 문제 발견 시 리포트 출력
2. 사용자가 수정할 항목 선택 (전체/개별)
3. 컨펌 후 수정 실행

### 검증 순서: 역순 (결과물 → 원천)

```
실제 결과물 (플러그인, 콘텐츠)
       ↑ 대조
views/library
       ↑ 추적
drafts
       ↑ 추적
inbox
```

- library/views는 **실제 결과물**과 대조 (내용이 맞는지)
- drafts는 library와 대조 (사용 여부)
- inbox는 drafts와 대조 (used 마킹)

### Source-of-Truth 판단

불일치 발견 시 → 사용자에게 "어느 쪽이 정답?" 확인
- 문서가 outdated → 결과물 기준으로 문서 수정
- 결과물이 outdated → 문서 기준으로 결과물 수정 (별도 작업)

## Open Questions

- [x] 어떤 순서로 체크할 것인가? → **역순 (결과물 → views/library → drafts → inbox)**
- [ ] 출력 포맷은?
- [x] 자동 수정 vs 리포트만? → **리포트 후 컨펌**
- [x] 어느 범위까지? → **전체, 단 역순으로**
- [ ] "실제 결과물"을 어떻게 식별할 것인가? → **스키마 정의 필요**

## 발견된 선행 작업

tidy가 제대로 동작하려면:

### 1. 스키마/프로토콜 정의 (먼저)
- library/views frontmatter에 `artifact` 필드 추가
- 결과물 경로 명시 (예: `artifact: plugins/forgeify/`)
- 컨벤션 규칙도 함께 정의

### 2. 기존 문서 마이그레이션 (그 다음)
- 본문에 있는 경로 → frontmatter로 추출
- 컨벤션 적용해서 누락된 연결 채우기

### 3. tidy 본체 (마지막)
- 정의된 스키마 기반으로 검증
- 불일치/누락 리포트

## 접근법: 점진적 tidy

**한 번에 하나씩, 여러 번 호출**

```
/gemify:tidy
→ 탐색: "스키마 정의가 안 된 문서 5개 발견"
→ 제안: "library/ai-automation/forgeify.md에 artifact 필드 추가할까요?"
→ 컨펌 → 수정
→ 종료

/gemify:tidy
→ 탐색: "깨진 링크 3개 발견"
→ 제안: "views/by-subject/ced.md → forgeify.md로 수정할까요?"
→ 컨펌 → 수정
→ 종료

(반복)
```

### 장점
- 한 번에 큰 변경 위험 없음
- 사용자가 컨트롤 유지
- 중간에 멈춰도 OK
- 각 단계 결과 확인 가능

### 탐색 우선순위

1. 스키마 누락 (artifact 필드 없음)
2. 깨진 링크 (존재하지 않는 파일 참조)
3. used 마킹 누락 (inbox status)
4. outdated 감지 (오래된 updated, 이름 변경된 참조)
5. 중복 view

## triage와의 관계

**발견**: tidy와 triage가 순환 의존

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

### 차이점
| | triage | tidy |
|---|---|---|
| 대상 | inbox (raw) | library/views/drafts (완성/진행 중) |
| 목적 | 다음 할 일 찾기 | 기존 것 검증/수정 |
| 방향 | 순방향 (생산) | 역방향 (유지보수) |

### 결론: 분리, 순서 있음

**깨진 유리창 이론** + **제텔카스텐** 관점:
- 기존 체계가 깨끗해야 새 것을 올바른 곳에 연결
- tidy로 먼저 정리 → triage로 새 inbox 연결

**실행 순서**:
```
1. 스키마/컨벤션 정의 (선행 - 둘 다 필요)
   ↓
2. /gemify:tidy (기존 문서 정리 - 깨진 유리창 수리)
   ↓
3. /gemify:triage (새 inbox를 정리된 체계에 연결)
```

**스킬 구조**:
- `/gemify:tidy` - library/views/drafts 정리 (역방향)
- `/gemify:triage` - inbox 정리 (순방향)
- 둘 다 스키마/컨벤션 공유
