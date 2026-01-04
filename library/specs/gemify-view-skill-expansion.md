---
title: gemify:view 스킬 5가지 타입 확장
type: spec
origin: derived
target_plugin: gemify
improvement_type: feature
priority: high
problem: "/gemify:view가 by-subject만 지원 → 발표, 교육, 포트폴리오, 에세이 등 다양한 렌더링 목적을 담지 못함"
solution: "5가지 view 타입별 생성 로직 추가, 타입별 고유 렌즈(판단 기준) 적용"
requirements:
  - /gemify:view 스킬에 타입 파라미터 추가
  - 각 타입별 frontmatter 템플릿 정의
  - 각 타입별 대화 흐름(렌즈 질문) 구현
  - views 폴더 구조 확장 (by-talk, by-curriculum, by-portfolio, by-essay)
references:
  - library/specs/gemify-views-type-system.md
  - inbox/thoughts/2026-01-04-views-expansion-need.md
views: [gemify]
---

## Why

### 핵심 인사이트

**library = 모델, views = 렌더링 레이어**

- library: 재사용 가능한 원자 단위 (지식의 재료)
- views: 서사(narrative)가 있는 스토리텔링

현재 `/gemify:view`는 by-subject만 지원:
- "문제 해결을 위한 결과물"만 다룸
- 발표, 교육, 포트폴리오, 에세이 등 다른 렌더링 목적 불가

### 확장 필요성

| View 타입 | 목적 | 서사의 핵심 질문 |
|-----------|------|-----------------|
| by-subject | 문제 → 해결책 | 어떤 문제를 어떻게 풀었는가? |
| by-talk | 메시지 전달 | 청중이 무엇을 깨닫고 가는가? |
| by-curriculum | 가르침 | 학습자가 무엇을 할 수 있게 되는가? |
| by-portfolio | 셀프 브랜딩 | 나는 어떤 사람인가? (증명과 함께) |
| by-essay | 자기 성찰 | 나는 무엇을 믿고/느끼는가? |

## What

### 1. /gemify:view 스킬 확장

**현재:**
```
/gemify:view {subject}
```

**확장:**
```
/gemify:view {type} {title}

# 예시
/gemify:view subject gemify
/gemify:view talk ai-knowledge-management
/gemify:view curriculum plugin-dev-101
/gemify:view portfolio developer
/gemify:view essay why-i-write
```

**기본값**: type 생략 시 `subject`로 동작 (하위 호환)

### 2. 타입별 대화 흐름 (렌즈 질문)

#### by-subject
1. 어떤 subject인가요?
2. artifact 경로는?
3. 어떤 domain들과 관련있나요? (복수 선택 가능)
   - product, engineering, operations, growth, business, ai-automation
4. 참조할 library 문서들은?

#### by-talk
1. 발표 제목은?
2. 청중은 누구인가요?
3. 청중이 얻어갈 것(takeaway)은?
4. 발표 시간은?
5. 참조할 library 문서들은?

#### by-curriculum
1. 커리큘럼 제목은?
2. 대상자는 누구인가요?
3. 대상자 수준은? (beginner/intermediate/advanced)
4. 학습 목표는?
5. 모듈 구성은?
6. 참조할 library 문서들은?

#### by-portfolio
1. 포트폴리오 제목은?
2. 어떤 역할로 셀링하나요?
3. 강조할 강점은?
4. 증명할 수 있는 evidence는?
5. 참조할 library 문서들은?

#### by-essay
1. 에세이 제목은?
2. 어떤 질문에 대한 답인가요?
3. 어떤 톤/감정인가요?
4. 참조할 library 문서들은?

### 3. 타입별 Frontmatter 템플릿

#### by-subject
```yaml
subject: {주제명}
artifact: {연결된 결과물 경로}
domains:
  - {domain1}
  - {domain2}
sources: [library 문서 목록]
```

#### by-talk
```yaml
title: "{발표 제목}"
audience: "{청중}"
takeaway: "{청중이 얻어갈 것}"
duration: {시간}
sources: [library 문서 목록]
```

#### by-curriculum
```yaml
title: "{커리큘럼 제목}"
audience: "{대상}"
level: beginner|intermediate|advanced
objective: "{학습 목표}"
modules:
  - title: "{모듈1 제목}"
    sources: [...]
  - title: "{모듈2 제목}"
    sources: [...]
sources: [library 문서 목록]
```

#### by-portfolio
```yaml
title: "{포트폴리오 제목}"
role: "{역할}"
strengths:
  - {강점1}
  - {강점2}
evidence:
  - {증명1}
  - {증명2}
sources: [library 문서 목록]
```

#### by-essay
```yaml
title: "{에세이 제목}"
question: "{다루는 질문}"
mood: "{톤/감정}"
sources: [library 문서 목록]
```

### 4. 폴더 구조

```
views/
├── by-subject/       # 기존
├── by-talk/          # 새로 추가
├── by-curriculum/    # 새로 추가
├── by-portfolio/     # 새로 추가
├── by-essay/         # 새로 추가
└── .history/         # 기존 유지
```

### 5. 파일명 규칙

- **by-subject**: `{subject}.md`
- **by-talk**: `{slug}.md`
- **by-curriculum**: `{slug}.md`
- **by-portfolio**: `{slug}.md`
- **by-essay**: `{slug}.md`

## Scope

**포함:**
- /gemify:view SKILL.md 수정
- view.md 커맨드 수정 (있다면)
- 타입별 대화 흐름 구현
- 타입별 frontmatter 템플릿 적용
- 폴더 자동 생성 로직

**제외:**
- 기존 by-subject 파일 마이그레이션 (호환성 유지)
- views .history 관련 수정 (기존 유지)
- library 관련 수정 (별도 spec으로 완료됨)

## 구현 순서

1. SKILL.md에 타입 파라미터 추가
2. 타입별 분기 로직 구현
3. 각 타입별 대화 흐름 구현
4. frontmatter 템플릿 적용
5. 폴더 자동 생성 로직 추가
