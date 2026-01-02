---
title: "Inbox 트리아지 스킬/커맨드 아이디어"
date: 2026-01-02
status: raw
used_in: null
references:
  - inbox/materials/2026-01-02-inbox-priority-analysis-session.md
---

# Inbox 트리아지 스킬 아이디어

## 핵심 인사이트

**새 세션/새 사람이 작업 인계받을 때 inbox 현황 파악이 필수**

현재 SessionStart hook이 있지만:
- drafts의 cutting 상태만 체크
- inbox raw 파일 "있다" 정도만 알려줌
- 우선순위/클러스터링 없음

## 제안: `/gemify:triage` 스킬

### 기능
1. inbox의 raw 파일 수집
2. references 기반 연결 관계 분석
3. 주제별 클러스터링
4. 우선순위 자동 판단
5. 추천 다음 액션 제시

### 출력 예시
```
## Inbox 현황
- raw thoughts: 7개
- raw materials: 14개
- 진행 중 drafts: 없음

## 1순위: 플러그인 개선 클러스터
- plugin-validator-agent-idea (핵심)
- plugin-sync-automation-idea
- ced-improve-command-idea
→ 추천: /gemify:draft plugin-validator-agent-idea.md

## 2순위: 단독 발전 가능
- gemify-recursive-insight
- domain-criteria
...
```

### 구현 위치
```
gemify/
├── skills/
│   └── triage.md      # 스킬 정의
└── commands/
    └── triage.md      # 커맨드 (스킬 호출)
```

### 커맨드 vs 스킬
- **커맨드**: `/gemify:triage` - 사용자가 직접 호출
- **스킬**: 내부적으로 Glob, Grep, Read 조합

## 추가 아이디어

### 클러스터링 기준
1. `references` 필드 (명시적 연결)
2. 파일명 prefix 유사성 (날짜, 키워드)
3. title 키워드 매칭

### 우선순위 판단 기준
- 연결된 파일 수 (많을수록 높음)
- 최근 날짜 (최신일수록 높음)
- thought vs material (thought가 액션 대상)

## 다음 단계

1. gemify 플러그인에 skills/triage.md 작성
2. 테스트: 현재 inbox로 실행
3. SessionStart hook에서 자동 호출 옵션 추가
