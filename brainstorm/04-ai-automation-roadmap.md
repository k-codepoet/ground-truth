# Brainstorm 04: AI 자동화 로드맵 - 수동에서 자동으로

> **핵심 질문**: AI Company의 최종 목표인 "CEO 입력 → 배포된 URL" 자동화를 어떻게 단계적으로 달성할 것인가?
> **날짜**: 2025-12-31

---

## 1. 현황 분석

### 문서들에서 언급된 AI 자동화 범위

| 자동화 영역 | 문서 위치 | 현재 상태 |
|------------|----------|----------|
| 분류 (classify) | as-is §4.1 | TODO (AI 연동 필요) |
| 태깅 (tagging) | as-is §1.2 | 설계만 |
| 추출 (extraction) | v3 §4 | 방법론만 언급 |
| 구조화 (structuring) | v3 §4 | 스크립트 구조만 |
| Export 변환 | as-is §4.2 | 템플릿 적용 미완 |
| HITL 질문 생성 | as-is §4.1 | 설계만 |

### 의존성 체인 (v3 workplan 기반)

```
Layer 0: Knowledge-ops (메타 시스템) ← 지금 여기
    ↓
Layer 1: Domain Corpus (도메인 지식)
    ↓
Layer 2: Exports (다양한 형태)
    ↓
Layer 3: AI Company (자동화) ← 최종 목표
```

---

## 2. 자동화 단계 정의

### Stage 0: 완전 수동 (현재)

```
사람이 하는 것:
- inbox에 파일 생성
- corpus로 파일 이동
- frontmatter 작성
- domain 분류
- export 생성

AI가 하는 것:
- (없음)
```

### Stage 1: AI 보조 (MVP 목표)

```
사람이 하는 것:
- Claude Chat으로 대화
- 분류 결과 확인/수정
- export 트리거

AI가 하는 것:
- 대화 → 문서 변환
- domain 분류 제안
- frontmatter 자동 생성
```

### Stage 2: AI 주도 (중기 목표)

```
사람이 하는 것:
- 아이디어 말하기
- 최종 승인

AI가 하는 것:
- 추출 질문
- 분류 + 저장
- 연결 그래프 생성
- export 자동 생성
```

### Stage 3: AI 자율 (장기 목표)

```
사람이 하는 것:
- 고수준 지시 ("블로그 발행해")

AI가 하는 것:
- 전체 파이프라인 자동화
- 품질 검증
- 배포
```

---

## 3. Stage 1 구현 상세 (MVP)

### 3.1 CLAUDE.md Skill 활용

**현재 mvp-workplan의 Skill**:
```markdown
# Knowledge-ops Agent
## 워크플로우
1. 사용자 입력 받음
2. inbox/{date}-{slug}.md 로 raw 저장
3. 6개 domain 중 적절한 곳 선택
4. 구조화된 문서로 변환
5. corpus/{domain}/{slug}.md 로 저장
```

**개선 제안**:
```markdown
# Knowledge-ops Agent v2
## 워크플로우
1. 입력 유형 판단 (capture vs extract)
2. extract면: 표준 질문으로 구조화
3. inbox/{type}/{date}-{slug}.md 저장
4. domain 분류 (신뢰도 표시)
5. 신뢰도 낮으면: 사용자에게 질문
6. corpus/{domain}/{slug}.md 저장
7. 저장 완료 + 관련 문서 연결 제안
```

### 3.2 분류 신뢰도 시스템

```python
def classify_with_confidence(content: str) -> tuple[str, float]:
    """
    Returns: (domain, confidence)

    - confidence >= 0.8: 자동 분류
    - 0.5 <= confidence < 0.8: 사용자 확인 요청
    - confidence < 0.5: 사용자에게 직접 질문
    """
    # 키워드 기반 휴리스틱 (MVP)
    keywords = {
        "product": ["문제", "사용자", "기획", "PRD"],
        "engineering": ["코드", "아키텍처", "구현", "API"],
        "operations": ["배포", "인프라", "모니터링", "서버"],
        "growth": ["마케팅", "콘텐츠", "SEO", "사용자 획득"],
        "business": ["수익", "계약", "법률", "재무"],
        "ai-automation": ["Agent", "LLM", "자동화", "워크플로우"],
    }

    # 키워드 매칭 → 점수 계산
    scores = calculate_scores(content, keywords)
    best_domain = max(scores, key=scores.get)
    confidence = scores[best_domain] / sum(scores.values())

    return best_domain, confidence
```

### 3.3 HITL (Human-in-the-Loop) 흐름

```
Claude: "이 내용은 'ai-automation' domain인 것 같아요 (신뢰도 65%). 맞나요?"

사용자 선택:
  [1] 맞아요 → corpus/ai-automation/에 저장
  [2] 아니요, engineering이에요 → corpus/engineering/에 저장
  [3] 둘 다 관련 → primary: ai-automation, secondary: engineering
```

---

## 4. Stage 2 로드맵 (중기)

### 4.1 추출 자동화

```yaml
trigger: 사용자가 "이런 생각이 있는데..." 형태로 시작

flow:
  1. 표준 질문 5개 순차 진행
  2. 답변 기반 구조화된 문서 생성
  3. 사용자 확인 후 저장

implementation:
  - Claude API 사용
  - 대화 기록 → 문서 변환 프롬프트
```

### 4.2 연결 그래프 자동 생성

```python
def suggest_connections(new_doc: str, corpus: list[str]) -> list[str]:
    """
    새 문서와 기존 corpus 문서들의 유사도 계산
    상위 3개 연결 제안
    """
    embeddings = get_embeddings([new_doc] + corpus)
    similarities = cosine_similarity(embeddings[0], embeddings[1:])
    top_3 = sorted(enumerate(similarities), key=lambda x: -x[1])[:3]
    return [corpus[i] for i, _ in top_3]
```

### 4.3 Export 자동 생성

```yaml
trigger: corpus/{domain}/ 파일 변경 감지

flow:
  1. 변경된 파일의 export 플래그 확인
  2. agent-docs: true면 → exports/agent-docs/ 재생성
  3. blog: true면 → exports/blog/ 재생성
  4. Git commit + push

implementation:
  - GitHub Actions 또는 local watcher
```

---

## 5. 기술 스택 결정

### MVP (Stage 1)

| 컴포넌트 | 선택 | 이유 |
|----------|------|------|
| AI 연동 | Claude Code (CLAUDE.md) | 설정 없이 바로 사용 |
| 분류 | 키워드 휴리스틱 | 단순, 디버깅 쉬움 |
| 저장 | 직접 파일 쓰기 | 의존성 없음 |
| 검증 | validate-corpus.py | 이미 완성됨 |

### Stage 2

| 컴포넌트 | 선택 | 이유 |
|----------|------|------|
| AI 연동 | Claude API (Python) | 프로그래밍 가능 |
| 분류 | Embedding + Similarity | 더 정확 |
| 연결 | Vector DB (Qdrant?) | 스케일러블 |
| 자동화 | GitHub Actions | CI/CD 통합 |

---

## 6. MVP 구현 체크리스트

### Week 1: 기본 동작

```
[ ] CLAUDE.md v2 작성 (신뢰도 시스템 포함)
[ ] classify_with_confidence() 휴리스틱 구현
[ ] 3개 문서로 테스트
[ ] 실패 케이스 기록
```

### Week 2: 안정화

```
[ ] HITL 흐름 개선
[ ] 분류 정확도 측정
[ ] edge case 처리
[ ] export-agent-docs.py 연동
```

---

## 7. 리스크 및 대응

| 리스크 | 영향 | 대응 |
|--------|------|------|
| 분류 정확도 낮음 | 잘못된 위치에 저장 | HITL 강화, 확인 스텝 추가 |
| Claude API 비용 | 예산 초과 | Stage 1은 Claude Code로 무료 |
| 과잉 자동화 | 품질 저하 | 단계별 검증, 수동 승인 유지 |
| 복잡한 프롬프트 | 유지보수 어려움 | 프롬프트 버전 관리 |

---

## 8. 성공 지표

### Stage 1 완료 기준

| 지표 | 목표 |
|------|------|
| 분류 정확도 | 80% 이상 (수동 검증) |
| HITL 개입 비율 | 30% 이하 |
| 문서 생성 시간 | 대화 시작 → 저장 완료 5분 이내 |

### Stage 2 완료 기준

| 지표 | 목표 |
|------|------|
| 자동 연결 정확도 | 70% 이상 |
| Export 자동화율 | 100% |
| 사람 개입 | 최종 승인만 |

---

## 9. 열린 질문

1. **Claude Code vs Claude API 시점**
   - 언제 API로 전환해야 하나?
   - 비용 대비 효과는?

2. **Vector DB 필요 시점**
   - corpus 몇 개부터 필요?
   - Qdrant vs Pinecone vs Chroma?

3. **자동화 vs 통제**
   - 어디까지 자동화하고 어디서 사람이 개입해야 하나?

---

## 10. 다음 단계

이 로드맵이 합의되면:

1. **즉시**: CLAUDE.md v2 작성 및 테스트
2. **Week 1**: Stage 1 완료
3. **Week 2+**: Stage 2 시작 여부 결정

---

**작성**: Claude (brainstorm session)
**상태**: Draft - 논의 필요
