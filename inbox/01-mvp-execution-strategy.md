# Brainstorm 01: MVP 실행 전략 - 지금 당장 만들 수 있는 것

> **핵심 질문**: 현재 문서들이 제시하는 비전과 실제 실행 가능한 MVP 사이의 갭은 무엇인가?
> **날짜**: 2025-12-31

---

## 1. 현황 진단

### As-Is에서 발견된 문제

| 문제 | 문서 위치 | 심각도 |
|------|----------|--------|
| AI Agent 연동 미완료 | as-is.md §6.1 | **CRITICAL** |
| 파이프라인 스크립트 구조만 존재 | as-is.md §4.1-4.2 | HIGH |
| 웹앱 템플릿 없음 | as-is.md §6.2 | MEDIUM |
| 입력 프론트엔드 미구현 | as-is.md §6.4 | LOW (MVP 제외) |

### 문서들 간의 모순

```
v2 workplan: "Static HTML first, React later"
v3 workplan: "agent-docs가 MVP export"
as-is.md: "React + TanStack Router 웹앱"
mvp-workplan: "Claude Skill (CLAUDE.md)로 시작"

→ 4개의 다른 방향이 공존
```

---

## 2. 핵심 제안: "Working Software First"

### 제안 1: 가장 작은 동작하는 단위 정의

**현재 상태**: 폴더 구조와 스키마는 과잉 설계, 실제 동작하는 코드는 부족

**제안**: 아래 순서로 **하나씩** 동작 확인

```
Step 1: inbox → corpus 수동 이동 (스크립트 없이)
    ↓ 검증: 5개 문서 수동 이동해보기
Step 2: CLAUDE.md 작성 + Claude Chat에서 테스트
    ↓ 검증: 말하면 파일 생성되는가?
Step 3: validate-corpus.py 실행
    ↓ 검증: 생성된 파일이 스키마 준수하는가?
```

**왜 이게 맞나**:
- 컴파일러 부트스트래핑에서 배운 교훈: "작동하는 v0.1 > 완벽한 설계"
- 현재 문서들은 Phase 4까지 설계되어 있지만 Phase 1도 미완료

### 제안 2: 스크립트 순서 재정립

```
현재 계획된 스크립트:
- inbox-to-corpus.py (TODO: AI 연동)
- build-web.py (TODO: 템플릿)
- validate-corpus.py (완성)

제안하는 순서:
1. validate-corpus.py (이미 완성 → 먼저 활용)
2. simple-classify.py (AI 없이 키워드 기반 분류)
3. manual-review.py (분류 결과 사람이 확인)
4. (나중에) AI 연동
```

---

## 3. 실행 가능한 48시간 계획

### Day 1: 구조 검증

| 시간 | 작업 | 산출물 |
|------|------|--------|
| 2h | 기존 inbox 파일 3개 수동으로 corpus로 이동 | corpus/{domain}/에 3개 파일 |
| 1h | validate-corpus.py 실행 | 검증 통과 확인 |
| 1h | 발견된 문제점 기록 | issues.md |

### Day 2: CLAUDE.md 테스트

| 시간 | 작업 | 산출물 |
|------|------|--------|
| 2h | CLAUDE.md 작성 (mvp-workplan 기반) | 동작하는 Skill |
| 2h | 3개 주제로 테스트 | inbox/ + corpus/ 각 3개 |
| 1h | 결과 분석 및 개선점 도출 | iteration-1.md |

---

## 4. 제거해야 할 것들

### 현재 문서에서 빼야 할 항목

| 항목 | 이유 | 대안 |
|------|------|------|
| i18n (ko, en) | MVP에 불필요한 복잡도 | 한국어 only |
| demos/ 폴더 | 인터랙티브 데모는 Phase 3 이후 | 삭제 |
| exports/web/ | 정적 HTML도 오버스펙 | agent-docs만 |
| graph.json | 연결은 나중에 | tree.yaml만 |
| library/ 공유 원자 | 미래 기능 | 삭제 |

### 스키마 단순화

```yaml
# 현재 (과잉)
---
id: ai-automation-20250102-god-pm-orchestrator
title: God PM - AI Company 오케스트레이터
created: 2025-01-02T...
domain: ai-automation
tags: [god-pm, orchestrator, multi-agent]
status: draft
connects_to: []
exportable:
  web: true
  blog: false
---

# 제안 (최소)
---
title: God PM - AI Company 오케스트레이터
domain: ai-automation
---
```

---

## 5. 성공 기준 재정의

### 현재 문서들의 성공 기준 (과잉)

- "knowledge-ops content 파일 수 5개 이상"
- "AI 자동화 비율 extraction 50% 이상"
- "Topic 수 3개 이상"

### 제안하는 MVP 성공 기준

```
[ ] Claude에게 말하면 파일이 생성된다
[ ] 생성된 파일이 corpus/{domain}/에 위치한다
[ ] validate-corpus.py가 통과한다

끝. 이 3개만 되면 MVP 성공.
```

---

## 6. 열린 질문

1. **CLAUDE.md vs Python 스크립트**: 둘 다 필요한가, 하나로 충분한가?
2. **domain 6개 vs 더 적게**: 처음부터 6개가 필요한가?
3. **inbox 필수 여부**: corpus로 바로 가면 안 되나?

---

## 7. 다음 단계

이 문서의 제안이 합의되면:

1. `02-input-pipeline-improvement.md` - 입력 흐름 개선
2. `03-export-diversification.md` - 출력 형태 다양화
3. `04-ai-automation-roadmap.md` - AI 자동화 로드맵

---

**작성**: Claude (brainstorm session)
**상태**: Draft - 논의 필요
