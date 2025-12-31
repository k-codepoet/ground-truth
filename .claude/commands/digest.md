---
description: inbox 파일을 소화시켜 corpus로 분류/저장
arguments:
  - name: file
    description: inbox 파일 경로 (예: inbox/INFRA-SETUP.md)
    required: true
---

# /digest - 지식 소화 스킬

## 역할
inbox의 raw 지식을 대화를 통해 소화시키고, 구조화하여 corpus에 저장한다.

## 워크플로우

### Step 1: 파일 읽기
$ARGUMENTS 파일을 읽고 내용을 파악한다.

### Step 2: 소크라테스식 질문 (순차적으로)

**Phase 1: 목적**
```
Q1. "이거 왜 남기려고 해?"
Q2. "이게 없으면 나중에 뭐가 안 돼?"
```

**Phase 2: 압축**
```
Q3. "한 문장으로 요약하면?"
Q4. "이 중에 진짜 핵심만 남기면?"
```

**Phase 3: 분류**
```
Q5. "6개 domain 중 어디야?"
    - product: 뭘 만들지 고민?
    - engineering: 어떻게 만들지 고민?
    - operations: 어떻게 돌릴지 고민?
    - growth: 어떻게 알릴지 고민?
    - business: 어떻게 유지할지 고민?
    - ai-automation: 어떻게 위임할지 고민?
```

**Phase 4: 연결**
```
Q6. "기존 corpus에 연결되는 거 있어?"
```

### Step 3: 재조립 제안
대화 내용을 바탕으로 구조화된 문서 초안을 제시한다:

```markdown
---
title: {Q3 답변 기반}
domain: {Q5 답변}
---

## Context
{Q1, Q2 답변 기반 - 왜 필요한지}

## Content
{Q4 답변 기반 - 핵심만}

## Connections
{Q6 답변 기반 - 관련 문서}
```

### Step 4: 사용자 컨펌
"이렇게 저장할까?" 물어보고 승인받으면:

1. `corpus/{domain}/{slug}.md`로 저장
2. 원본 inbox 파일 삭제 여부 확인
3. 완료 보고

## 규칙
- 질문은 하나씩 순차적으로 (한꺼번에 던지지 않음)
- 답변이 모호하면 추가 질문
- 컨펌 없이 저장하지 않음
- slug는 영문 kebab-case로 자동 생성
