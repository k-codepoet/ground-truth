# Brainstorm 03: Export 다양화 전략 - 하나의 원천, 다양한 형태

> **핵심 질문**: 같은 corpus에서 어떤 형태의 output을 만들 수 있고, 무엇부터 해야 하는가?
> **날짜**: 2025-12-31

---

## 1. 현황 분석

### 문서들에서 언급된 Export 형태

| Export | 문서 위치 | 설명 | 현재 상태 |
|--------|----------|------|----------|
| agent-docs | v3 workplan | AI Agent용 선언적 문서 | **MVP 대상** |
| web/ interactive | as-is, v2 | 인터랙티브 마인드맵/데모 | 템플릿 미완 |
| blog | as-is, v3 | 스토리텔링 블로그 | 미구현 |
| docs (Docusaurus) | as-is | 정적 문서 사이트 | 미구현 |
| book | v3 workplan | 출판용 선형 구조 | 미구현 |
| resume | as-is | 성과 중심 이력서 | 미구현 |
| Notion | as-is | Notion 페이지 동기화 | 미구현 |

### 핵심 모순 발견

```
as-is.md: "웹앱 = React + TanStack Router + Framer Motion"
v3 workplan: "MVP는 agent-docs만"
v2 workplan: "Static HTML first"

→ 어느 것을 먼저 해야 하는지 불명확
```

---

## 2. Export 형태별 특성 분석

### 2.1 구조적 차이

| Export | 구조 | 대상 독자 | 복잡도 |
|--------|------|----------|--------|
| agent-docs | 선언적, 규칙 기반 | AI Agent | LOW |
| blog | 서사적, 독립 단편 | 일반 웹 사용자 | MEDIUM |
| book | 선형적, 챕터 구조 | 깊이 있는 학습자 | HIGH |
| web/interactive | 비선형, 탐색 가능 | 능동적 학습자 | HIGH |
| resume | 성과 중심, 압축 | 채용 담당자 | LOW |

### 2.2 변환 요구사항

```yaml
corpus → agent-docs:
  - frontmatter → YAML 헤더 유지
  - 명령형 → 선언형 어투
  - connections → 규칙 참조
  - 복잡도: LOW

corpus → blog:
  - 1 corpus file → 1 blog post
  - 기술 용어 → 친근한 설명
  - examples → 스토리
  - 복잡도: MEDIUM

corpus → book:
  - N corpus files → 1 chapter
  - tree.yaml → 목차 구조
  - 연결 → 챕터 간 흐름
  - 복잡도: HIGH
```

---

## 3. 핵심 제안: 단계적 확장

### Phase 1: agent-docs (MVP)

**왜 먼저인가**:
- AI Company 목표와 직결
- 변환 복잡도 가장 낮음
- corpus 구조 검증에 적합

**구현 방법**:
```python
# export-agent-docs.py (단순 버전)
for file in corpus/**/*.md:
    # 1. frontmatter 파싱
    # 2. 어투만 조정 (명령형 → 선언형)
    # 3. exports/agent-docs/{domain}/{file}.md로 복사
```

**예시 변환**:
```markdown
# corpus/ai-automation/god-pm.md (원본)
God PM은 CEO 입력을 받아서 적절한 agent에게 위임한다.

# exports/agent-docs/ai-automation/god-pm.md (변환)
## God PM
- 역할: CEO 입력 수신 및 agent 위임
- 규칙:
  1. 모든 CEO 입력은 God PM을 통과한다
  2. 적절한 agent를 선택하여 위임한다
```

### Phase 2: blog (MVP+1)

**왜 두 번째인가**:
- 외부 공유 가능 (Growth 기여)
- 작성 과정에서 corpus 품질 검증
- 독립 단편이라 병렬 작업 가능

**구현 방법**:
```python
# export-blog.py
for file in corpus/**/*.md:
    # 1. 블로그 템플릿 적용
    # 2. 제목, 요약, 태그 추출
    # 3. 친근한 어투로 변환 (LLM 활용 가능)
    # 4. exports/blog/{slug}.md로 저장
```

### Phase 3+: web, book (나중에)

- web: 인터랙티브 컴포넌트 필요 → React 개발 비용
- book: 전체 구조 완성 후 가능 → corpus 충분해야 함

---

## 4. MVP Export 파이프라인 설계

### 최소 구현

```
corpus/{domain}/*.md
    │
    │ [export-agent-docs.py]
    ▼
exports/agent-docs/{domain}/*.md
```

### export-agent-docs.py 핵심 로직

```python
#!/usr/bin/env python3
"""
MVP: corpus → agent-docs 변환
"""
import yaml
import re
from pathlib import Path

def transform_to_declarative(content: str) -> str:
    """서술형 → 선언형 변환 (간단한 규칙 기반)"""
    # "~한다" → "~해야 한다" 형태로
    # 향후 LLM으로 대체 가능
    return content

def export_agent_docs(corpus_path: Path, export_path: Path):
    for md_file in corpus_path.rglob("*.md"):
        # 1. frontmatter 분리
        with open(md_file) as f:
            raw = f.read()

        # 2. frontmatter + content 파싱
        if raw.startswith("---"):
            _, fm, content = raw.split("---", 2)
            meta = yaml.safe_load(fm)
        else:
            meta = {}
            content = raw

        # 3. 변환
        transformed = transform_to_declarative(content)

        # 4. 저장
        rel_path = md_file.relative_to(corpus_path)
        out_file = export_path / rel_path
        out_file.parent.mkdir(parents=True, exist_ok=True)

        with open(out_file, 'w') as f:
            f.write(f"---\n{yaml.dump(meta)}---\n{transformed}")
```

---

## 5. Export 우선순위 매트릭스

| Export | 비용 | 가치 | 우선순위 |
|--------|------|------|----------|
| agent-docs | LOW | HIGH (AI Company 목표) | **1** |
| blog | MEDIUM | HIGH (외부 공유) | **2** |
| resume | LOW | MEDIUM (개인 브랜딩) | 3 |
| web | HIGH | HIGH | 4 |
| book | HIGH | MEDIUM | 5 |
| Notion | MEDIUM | LOW | 6 |

---

## 6. 스키마 통일 제안

### 현재 문제
- corpus 파일과 export 파일의 frontmatter가 다름
- 변환 시 매핑 로직 필요

### 제안: Export 힌트 필드

```yaml
# corpus 파일 frontmatter
---
title: God PM 오케스트레이터
domain: ai-automation
export:
  agent-docs: true
  blog: false  # 아직 블로그용으로 다듬지 않음
  book: chapter-3  # 책의 3장에 포함
---
```

**이점**:
- 파일별로 어느 export에 포함될지 명시
- 점진적 확장 가능

---

## 7. 열린 질문

1. **agent-docs 어투 변환을 자동화할 것인가?**
   - 규칙 기반 vs LLM 기반

2. **blog 발행 플랫폼은?**
   - 자체 호스팅 vs Medium vs 개인 도메인

3. **export 버전 관리는?**
   - corpus 변경 시 export 재생성?
   - 캐시/증분 빌드?

---

## 8. 48시간 실행 계획

### Day 1: agent-docs 파이프라인

| 시간 | 작업 | 산출물 |
|------|------|--------|
| 2h | export-agent-docs.py 작성 | 동작하는 스크립트 |
| 1h | corpus 3개 파일로 테스트 | exports/agent-docs/ |
| 1h | 결과 검토 및 개선 | 버전 2 |

### Day 2: 블로그 준비

| 시간 | 작업 | 산출물 |
|------|------|--------|
| 2h | blog 템플릿 설계 | template.md |
| 2h | 1개 문서 수동 변환 | 블로그 포스트 1개 |
| 1h | 자동화 가능성 검토 | export-blog.py 초안 |

---

## 9. 다음 단계와의 연결

### → 04-ai-automation-roadmap.md
- Export 변환에 LLM 활용
- 자동 발행 파이프라인

### → 01-mvp-execution-strategy.md
- Export 성공 기준 통합

---

**작성**: Claude (brainstorm session)
**상태**: Draft - 논의 필요
