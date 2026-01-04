---
title: views 타입 시스템 설계
type: spec
origin: original
target_plugin: gemify
improvement_type: feature
priority: high
problem: "views/by-subject만 존재 → 지식 렌더링의 다양한 목적을 담지 못함"
solution: "5가지 view 타입 도입, 각 타입별 고유 렌즈(판단 기준) 정의"
requirements:
  - views 폴더 구조 확장
  - 각 view 타입별 frontmatter 스키마 정의
  - /gemify:view 스킬 확장
references:
  - inbox/thoughts/2026-01-04-views-expansion-need.md
  - inbox/materials/2026-01-04-views-expansion-discussion.md
  - library/specs/gemify-library-type-classification.md
views: [gemify]
---

## Why

### 핵심 인사이트

**library = 모델, views = 렌더링 레이어**

- library: 내 지식의 원자 단위, 재사용 가능한 재료
- views: 서사(narrative)가 있는 것, library를 조합해 스토리텔링

현재 views/by-subject만 있음 → "문제 해결을 위한 결과물"만 다룸.
하지만 지식을 렌더링하는 목적은 더 다양함.

### 문제

1. 발표/강연 콘텐츠를 담을 곳이 없음
2. 교육/커리큘럼을 구조화할 곳이 없음
3. 포트폴리오/이력서 형태의 셀프 브랜딩 공간 없음
4. 개인 에세이/수필을 담을 곳이 없음

## What

### 1. 5가지 View 타입

| View 타입 | 목적 | 서사의 핵심 질문 |
|-----------|------|-----------------|
| **by-subject** | 문제 → 해결책 | 어떤 문제를 어떻게 풀었는가? |
| **by-talk** | 메시지 전달 | 청중이 무엇을 깨닫고 가는가? |
| **by-curriculum** | 가르침 | 학습자가 무엇을 할 수 있게 되는가? |
| **by-portfolio** | 셀프 브랜딩 | 나는 어떤 사람인가? (증명과 함께) |
| **by-essay** | 자기 성찰 | 나는 무엇을 믿고/느끼는가? |

### 2. 각 타입별 렌즈(판단 기준)

#### by-subject
- **6대 domain**: product, engineering, operations, growth, business, ai-automation
- 결과물 형태: 서비스, workflow, plugin, framework, pipeline 등

#### by-talk
- **audience**: 누가 듣는가?
- **takeaway**: 청중이 무엇을 얻어가는가?
- **duration**: 발표 길이 (5분, 20분, 1시간 등)

#### by-curriculum
- **audience**: 누가 배우는가?
- **level**: 대상자 수준 (beginner, intermediate, advanced)
- **objective**: 무엇을 할 수 있게 되는가?

#### by-portfolio
- **role**: 어떤 역할로 셀링하는가? (developer, architect, leader 등)
- **strengths**: 어떤 강점을 보여주는가?
- **evidence**: 증명할 수 있는 결과물/경험

#### by-essay
- **question**: 어떤 질문에 대한 답인가?
- **mood**: 어떤 감정/톤인가?

### 3. 폴더 구조 확장

```
views/
├── by-subject/       # 문제 해결 결과물
│   ├── gemify.md
│   ├── forgeify.md
│   └── ...
├── by-talk/          # 발표/강연
│   └── {talk-title}.md
├── by-curriculum/    # 교육/커리큘럼
│   └── {curriculum-title}.md
├── by-portfolio/     # 포트폴리오
│   └── {role-or-theme}.md
├── by-essay/         # 에세이/수필
│   └── {essay-title}.md
└── .history/         # 버전 히스토리 (기존 유지)
```

### 4. Frontmatter 스키마

#### by-subject (기존 + 확장)
```yaml
subject: gemify
artifact: ~/my-claude-plugins/plugins/gemify
domains:              # 복수 가능
  - product
  - ai-automation
sources: [library 문서 목록]
```

#### by-talk
```yaml
title: "AI 시대의 개인 지식 관리"
audience: "개발자, 지식 근로자"
takeaway: "암묵지를 구조화하는 파이프라인 구축 방법"
duration: 20min
sources: [library 문서 목록]
```

#### by-curriculum
```yaml
title: "Claude Code 플러그인 개발 입문"
audience: "주니어 개발자"
level: beginner
objective: "간단한 skill 기반 플러그인을 만들 수 있다"
modules:              # 커리큘럼 구조
  - title: "기본 구조 이해"
    sources: [...]
  - title: "첫 스킬 만들기"
    sources: [...]
sources: [library 문서 목록]
```

#### by-portfolio
```yaml
title: "AI-Native Developer"
role: developer
strengths:
  - "AI 도구 활용 극대화"
  - "지식 시스템 설계"
evidence:
  - gemify 플러그인 개발
  - forgeify 프레임워크 구축
sources: [library 문서 목록]
```

#### by-essay
```yaml
title: "왜 나는 메모하는가"
question: "기록의 의미는 무엇인가?"
mood: reflective
sources: [library 문서 목록]
```

### 5. /gemify:view 스킬 확장

현재:
```
/gemify:view {subject}
```

확장:
```
/gemify:view {type} {title}
# 예시
/gemify:view subject gemify
/gemify:view talk ai-knowledge-management
/gemify:view curriculum plugin-dev-101
/gemify:view portfolio developer
/gemify:view essay why-i-write
```

또는 타입별 별도 스킬:
```
/gemify:view:subject {subject}
/gemify:view:talk {title}
/gemify:view:curriculum {title}
/gemify:view:portfolio {role}
/gemify:view:essay {title}
```

## Scope

**포함:**
- views 폴더 구조 확장
- 각 타입별 frontmatter 스키마 정의
- /gemify:view 스킬 확장
- CLAUDE.md 업데이트

**제외:**
- 기존 by-subject 파일 마이그레이션 (호환성 유지)
- 각 view 타입별 생성 워크플로우 상세화 (별도 spec)

## Migration

기존 views/by-subject/ 파일은 그대로 유지.
frontmatter에 domains 필드만 추가하면 됨.
