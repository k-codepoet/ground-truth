# Brainstorm Summary: 개선안 요약 및 우선순위

> **목적**: 4개의 brainstorm 문서를 종합하여 실행 우선순위 제시
> **날짜**: 2025-12-31

---

## 1. 핵심 발견 사항

### 현재 상태 진단

| 영역 | 상태 | 문제 |
|------|------|------|
| 폴더 구조 | 과잉 설계 | 실제 파일 거의 없음 |
| 스키마 | 과잉 설계 | 필수 아닌 필드 다수 |
| 스크립트 | 골격만 존재 | AI 연동 미완 |
| Export | 계획만 존재 | 동작하는 것 없음 |
| 입력 채널 | 언급만 | 구현 없음 |

### 문서들 간 모순

```
as-is.md: React + TanStack + Framer Motion (복잡)
v2 workplan: Static HTML first (단순)
v3 workplan: agent-docs만 MVP (더 단순)
mvp-workplan: Claude Skill만 (가장 단순)

→ 가장 단순한 것부터 시작해야 함
```

---

## 2. 4개 브레인스토밍 문서 요약

### 01-mvp-execution-strategy.md

**핵심 메시지**: "Working Software First"
- 48시간 안에 동작하는 것 만들기
- 스키마 단순화 (title, domain만 필수)
- 성공 기준 3개만: 파일 생성, 올바른 위치, 검증 통과

### 02-input-pipeline-improvement.md

**핵심 메시지**: "입력 ≠ 추출" 분리
- /capture (빠른 입력)과 /extract (대화형 추출) 2개 Skill
- inbox를 _raw/, _extracted/로 분리
- 표준 질문 5개로 추출 구조화

### 03-export-diversification.md

**핵심 메시지**: "agent-docs 먼저"
- 변환 복잡도 가장 낮음
- AI Company 목표와 직결
- blog는 두 번째, web/book은 나중에

### 04-ai-automation-roadmap.md

**핵심 메시지**: "Stage 0 → 1 → 2 → 3 단계적 자동화"
- Stage 1: AI 보조 (Claude Code, HITL)
- 분류 신뢰도 시스템으로 자동/수동 결정
- API 전환은 Stage 2에서

---

## 3. 통합 실행 우선순위

### 즉시 실행 (Day 1-2)

| # | 작업 | 문서 | 산출물 |
|---|------|------|--------|
| 1 | 기존 inbox 파일 3개 수동으로 corpus 이동 | 01 | 검증된 구조 |
| 2 | validate-corpus.py 실행 및 확인 | 01 | 통과 로그 |
| 3 | CLAUDE.md v2 작성 (신뢰도 포함) | 04 | Skill 파일 |
| 4 | /capture, /extract 분리 구현 | 02 | 동작하는 입력 |

### 단기 실행 (Week 1)

| # | 작업 | 문서 | 산출물 |
|---|------|------|--------|
| 5 | export-agent-docs.py 작성 | 03 | Export 파이프라인 |
| 6 | 분류 휴리스틱 구현 | 04 | classify.py |
| 7 | 5개 문서로 전체 플로우 테스트 | 01 | 검증 보고서 |

### 중기 실행 (Week 2+)

| # | 작업 | 문서 | 산출물 |
|---|------|------|--------|
| 8 | blog export 템플릿 | 03 | export-blog.py |
| 9 | 연결 그래프 생성 | 04 | graph.json |
| 10 | Claude API 전환 검토 | 04 | 결정 문서 |

---

## 4. 제거 목록 (Scope Out)

| 항목 | 이유 | 재도입 시점 |
|------|------|------------|
| i18n (다국어) | MVP 복잡도 증가 | corpus 20개 이후 |
| demos/ 폴더 | 인터랙티브 불필요 | web export 시작 시 |
| library/ 공유 원자 | 미래 기능 | topic 5개 이후 |
| Notion 연동 | 낮은 우선순위 | 수동 동기화로 충분 |
| Slack/Discord | 입력 채널 다양화는 나중 | Stage 2 이후 |

---

## 5. 성공 기준 통합

### MVP 완료 (48시간)

```
[ ] Claude에게 말하면 파일이 생성된다
[ ] 생성된 파일이 corpus/{domain}/에 위치한다
[ ] validate-corpus.py가 통과한다
[ ] export-agent-docs.py가 동작한다
```

### Stage 1 완료 (Week 1)

```
[ ] 분류 정확도 80% 이상
[ ] HITL 개입 비율 30% 이하
[ ] 문서 10개 이상 corpus에 축적
```

---

## 6. 열린 질문 통합

| 질문 | 관련 문서 | 결정 필요 시점 |
|------|----------|--------------|
| 6개 domain vs 더 적게? | 01 | Day 1 |
| /capture vs /extract 분리 필수? | 02 | Day 1 |
| agent-docs 어투 변환 자동화? | 03 | Week 1 |
| Claude API 전환 시점? | 04 | Week 2 |
| Vector DB 필요 시점? | 04 | corpus 50개 이후 |

---

## 7. 다음 액션

### 오늘 (Day 0)

1. 이 문서 리뷰 및 우선순위 확정
2. 열린 질문 중 Day 1 결정 필요 항목 논의
3. 폴더 구조 정리 (불필요 항목 제거)

### 내일 (Day 1)

1. 작업 #1-4 시작
2. 저녁까지 MVP 동작 확인

---

## 8. 파일 구조 제안

### 현재 brainstorm/ 폴더

```
brainstorm/
├── 00-summary-and-priorities.md  ← 이 문서
├── 01-mvp-execution-strategy.md
├── 02-input-pipeline-improvement.md
├── 03-export-diversification.md
└── 04-ai-automation-roadmap.md
```

### 권장 사용법

1. 의사결정 필요 시 해당 문서 참조
2. 결정된 사항은 이 summary에 기록
3. 실행 완료된 항목은 체크

---

**작성**: Claude (brainstorm session)
**상태**: Ready for Review
**다음**: 사용자와 우선순위 확정 논의
