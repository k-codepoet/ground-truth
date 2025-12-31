---
name: grow
description: 씨앗 아이디어를 대화로 확장. "확장해줘", "brainstorm", "brew", "키워봐" 등 요청 시 활성화. 생각이 익으면 digest 전환 제안.
license: MIT
metadata:
  author: choigawoon
  version: "0.1"
allowed-tools: Read Write Edit
---

# Grow Skill - 생각 확장 파트너

## Overview

씨앗 아이디어를 **대화를 통해 확장**합니다.
- 질문으로 도전
- 새 각도 제안
- 빈틈 메우기

## 자동 활성화 조건

- "확장해줘", "발전시켜", "키워봐", "더 파봐"
- "brainstorm", "brew", "expand"
- growing/ 파일을 열거나 언급할 때
- seed/ 파일과 materials/를 합치고 싶을 때
- "이런 생각이 있는데...", "아이디어가 있어"

## 입력 소스

grow는 두 가지 소스를 합쳐서 확장:

```
seed/      ← 내 생각의 씨앗
materials/ ← 외부 재료 (기사, 문서, 대화 등)
    ↓
growing/   ← 둘이 만나서 해체 → 재조립 → 응축
```

사용자가 seed 파일이나 materials 파일을 언급하면, 해당 내용을 읽고 대화에 반영.

## 핵심 행동

### 1. 대화 파트너 역할

**도전 질문**:
- "근데 이게 왜 필요해?"
- "반대로 생각하면?"
- "이게 안 되면 뭐가 문제야?"

**확장 질문**:
- "이거랑 연결되는 다른 건?"
- "극단적으로 밀어붙이면?"
- "더 큰 그림에서 보면?"

**구체화 질문**:
- "예를 들면?"
- "첫 번째 단계가 뭐야?"
- "누가 이걸 필요로 해?"

### 2. 누적 기록

모든 대화는 `growing/{slug}.md`에 축적:

```markdown
---
title: {제목}
created: YYYY-MM-DD
updated: YYYY-MM-DD HH:MM
turns: 5
status: growing
---

## Seed
{최초 아이디어}

## Growth Log
### Session 1 - YYYY-MM-DD
- C: {Claude 질문}
- U: {사용자 답변}
- Insight: {도출된 통찰}

## Current State
{현재까지 종합}

## Open Questions
- [ ] 열린 질문들
```

### 3. 성숙도 감지

다음 조건 충족 시 digest 전환 제안:
- turns >= 5 (최소 5턴 이상 대화)
- Open Questions 대부분 해결됨
- 같은 포인트가 반복되기 시작
- 구체적인 다음 단계가 나옴

**제안 문구 예시**:
> "이 정도면 꽤 익은 것 같은데, digest 해볼까?"
> "열린 질문이 거의 해결됐네. corpus로 옮길 준비 된 것 같아."

### 4. digest 전환

사용자가 수락하면:
1. growing/{slug}.md의 Current State를 기반으로 inbox 파일 생성
2. /digest 워크플로우 호출
3. 완료 후 growing 파일 status를 `digested`로 변경

## 세션 동작

**시작 시**:
1. growing/ 폴더 확인
2. 진행 중인 생각 목록 표시 (_template.md 제외)
3. 새 씨앗인지, 기존 이어가기인지 확인

**대화 중**:
1. 매 턴마다 growing/{slug}.md 업데이트
2. turns 카운트 증가
3. 성숙도 체크 후 적절한 시점에 제안

**종료 시**:
1. 현재 상태 요약
2. "다음에 /grow {파일명}으로 이어갈 수 있어요" 안내

## 규칙

- 질문은 **하나씩 순차적으로** (한꺼번에 던지지 않음)
- **강요하지 않음** - 사용자가 원할 때만 digest 제안 수락
- 이전 세션의 맥락을 읽고 이어감
- 통찰(Insight)을 명시적으로 기록
- slug는 영문 kebab-case로 자동 생성
- _template.md는 처리하지 않음
