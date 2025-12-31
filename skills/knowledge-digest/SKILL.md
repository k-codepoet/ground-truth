---
name: knowledge-digest
description: inbox의 raw 지식을 소화시켜 corpus로 분류/저장하는 워크플로우. inbox 폴더의 파일을 다룰 때, 지식 정리/분류 작업 시, 또는 사용자가 생각을 구조화하고 싶을 때 자동 활성화.
license: MIT
compatibility: 이 프로젝트의 inbox/, corpus/ 구조 필요
metadata:
  author: choigawoon
  version: "0.1"
allowed-tools: Read Write Edit
---

# Knowledge Digest Skill

## Overview

inbox의 raw 지식을 **소크라테스식 질문**을 통해 소화시키고, 구조화하여 corpus에 저장합니다.

## 프로젝트 구조

```
inbox/              # raw 입력 (자유 형식)
corpus/             # 구조화된 지식
├── product/        # 무엇을 만들 것인가?
├── engineering/    # 어떻게 만들 것인가?
├── operations/     # 어떻게 돌릴 것인가?
├── growth/         # 어떻게 알릴 것인가?
├── business/       # 어떻게 유지할 것인가?
└── ai-automation/  # 어떻게 위임할 것인가?
```

## Digest 워크플로우

### Step 1: 파일 확인
inbox 폴더의 파일을 읽고 내용 파악.

### Step 2: 소크라테스식 질문 (순차적으로, 하나씩)

**Phase 1: 목적**
- Q1: "이거 왜 남기려고 해?"
- Q2: "이게 없으면 나중에 뭐가 안 돼?"

**Phase 2: 압축**
- Q3: "한 문장으로 요약하면?"
- Q4: "이 중에 진짜 핵심만 남기면?"

**Phase 3: 분류**
- Q5: "6개 domain 중 어디야?"
  - product: 뭘 만들지 고민?
  - engineering: 어떻게 만들지 고민?
  - operations: 어떻게 돌릴지 고민?
  - growth: 어떻게 알릴지 고민?
  - business: 어떻게 유지할지 고민?
  - ai-automation: 어떻게 위임할지 고민?

**Phase 4: 연결**
- Q6: "기존 corpus에 연결되는 거 있어?"

### Step 3: 재조립 제안

대화 결과를 바탕으로 구조화된 문서 초안 제시:

```markdown
---
title: {Q3 답변 기반}
domain: {Q5 답변}
---

## Context
{Q1, Q2 답변 - 왜 필요한지}

## Content
{Q4 답변 - 핵심만}

## Connections
{Q6 답변 - 관련 문서}
```

### Step 4: 저장

사용자 컨펌 후:
1. `corpus/{domain}/{slug}.md`로 저장
2. 원본 inbox 파일을 `inbox_archived/`로 이동
3. 완료 보고

## 규칙

- 질문은 **하나씩 순차적으로** (한꺼번에 던지지 않음)
- 답변이 모호하면 추가 질문으로 명확화
- **컨펌 없이 저장하지 않음**
- slug는 영문 kebab-case로 자동 생성
- 템플릿 파일 (`_template.md`)은 처리하지 않음

## 자동 활성화 조건

- `inbox/` 폴더의 파일을 언급하거나 열 때
- "정리해줘", "분류해줘", "소화시켜" 등의 요청
- 지식 관리 관련 대화
