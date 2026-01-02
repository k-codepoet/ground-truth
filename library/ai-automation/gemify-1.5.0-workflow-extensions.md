---
title: Gemify 1.5.0 워크플로우 확장 - capture-pair, retro
domain: ai-automation
created_via: retro
---

## Context

Gemify의 기본 흐름(inbox → drafts → library)이 실제 사용에서 불편한 점들이 발견됨:
1. import + inbox를 따로 실행해야 함 → 대화에서 material과 thought를 한번에 뽑고 싶음
2. 바로 구현 후 사후 기록 불가 → drafts 없이 library로 가는 경로 필요
3. 파일명 규칙(YYYY-MM-DD-slug.md)이 자주 누락됨

## Decision

### 1. capture-pair: material + thought 동시 생성

```
/gemify:capture-pair
    ↓
inbox/materials/YYYY-MM-DD-{slug}.md  (대화 맥락)
inbox/thoughts/YYYY-MM-DD-{slug}.md   (핵심 인사이트)
    + thought.references → material 연결
```

핵심: 한 번의 대화에서 외부 기록과 내 생각을 분리 저장

### 2. retro: 사후처리 (역방향 기록)

```
[일반]  inbox → drafts → library → 구현
[retro] 아이디어 → 구현(완료) → /gemify:retro → library
```

- drafts를 건너뛰는 단축 경로
- `created_via: retro` 필드로 사후 기록 표시
- 소크라테스식 질문으로 핵심 결정 추출

### 3. 파일명 규칙 강조

inbox/import 스킬 규칙 섹션에 명시적 추가:
```
**파일명은 반드시 `YYYY-MM-DD-{slug}.md` 형식**
```

## Outcome

- gemify v1.5.0 릴리즈
- 새 스킬: capture-pair, retro
- CHANGELOG.md 관리 시작

## Lessons

- 실제 사용하면서 발견되는 패턴을 기능으로 흡수
- "역방향 흐름"도 정당한 워크플로우로 인정
- 규칙이 잘 안 지켜지면 문서에서 더 강조 (반복/볼드)
