# Brainstorm 02: 입력/추출 파이프라인 개선

> **핵심 질문**: 머릿속 지식이 시스템에 들어오는 경로를 어떻게 최적화할 것인가?
> **날짜**: 2025-12-31

---

## 1. 현황 분석

### 문서에서 언급된 입력 채널

| 채널 | 문서 | 현재 상태 |
|------|------|----------|
| Claude Chat → inbox | mvp-workplan | **MVP 대상** |
| Slack 연동 | as-is.md §6.4 | 미구현 |
| Discord 연동 | as-is.md §6.4 | 미구현 |
| Web Chatbot | as-is.md §6.4 | 미구현 |
| Voice | mvp-workplan §1 | 언급만 |

### 핵심 병목: "추출" 단계

v3 workplan의 지식 흐름:
```
HEAD (암묵지)
    │ 추출 ← 여기가 문제
    ▼
INBOX (원시 캡처)
```

**문제**:
- "AI 대화, 자문자답, 강제 출력"이 방법론으로 언급됨
- 하지만 이를 **도구화**하는 구체적 설계 없음

---

## 2. 핵심 통찰: 입력 ≠ 추출

### 구분 필요

| 개념 | 정의 | 예시 |
|------|------|------|
| **입력(Input)** | 이미 명시화된 지식을 시스템에 넣기 | 메모 복붙, 링크 저장 |
| **추출(Extraction)** | 머릿속 암묵지를 명시지로 변환 | 대화로 개념 정리 |

**현재 문서들의 혼란**: 둘을 같은 "inbox"로 취급

### 제안: 경로 분리

```
경로 A: 입력 (이미 아는 것)
    파일 드롭 / 복붙 / 링크
        → inbox/_raw/
        → 분류만 하면 됨

경로 B: 추출 (아직 정리 안 된 것)
    "이런 생각이 있는데..."
        → AI 대화 (구조화된 질문)
        → inbox/_extracted/
        → 분류 + 구조화 필요
```

---

## 3. 실행 가능한 개선안

### 제안 1: Claude Skill 2개로 분리

**현재 (단일 Skill)**:
```markdown
# Knowledge-ops Agent
사용자가 말하는 내용을 지식 문서로 변환한다.
```

**제안 (분리)**:

```markdown
# Skill A: /capture - 빠른 입력
사용자가 이미 정리된 내용을 저장한다.
- 질문 없이 바로 저장
- 분류만 수행
- inbox/_raw/{date}-{slug}.md

# Skill B: /extract - 추출 대화
사용자의 흐릿한 생각을 구조화한다.
- 소크라테스식 질문
- 5가지 표준 질문 사용
- inbox/_extracted/{date}-{slug}.md
```

### 제안 2: 추출용 표준 질문 세트

```yaml
extraction_questions:
  - "이게 해결하려는 문제가 뭐야?"
  - "누가 이걸 필요로 해?"
  - "비슷한 기존 방법 대비 뭐가 다른데?"
  - "이게 안 되면 어떤 일이 생겨?"
  - "6개 domain 중 어디에 가까워?"
```

**사용 시나리오**:
```
사용자: "God PM이란 개념이 있는데..."
Claude: "이게 해결하려는 문제가 뭐야?"
사용자: "CEO 입력을 자동으로 처리하는 거"
Claude: "누가 이걸 필요로 해?"
...
Claude: [구조화된 문서 생성]
```

---

## 4. inbox 구조 재설계

### 현재 (flat)
```
inbox/
├── _template.md
├── Hashbrown.dev Overview.md
├── INFRA-SETUP.md
└── 최고의 개발자... .md
```

### 제안 (분류된)
```
inbox/
├── _raw/              ← 빠른 입력용
│   └── *.md
├── _extracted/        ← 추출 대화 결과
│   └── *.md
└── _processing/       ← 처리 중 (임시)
    └── *.md
```

**워크플로우**:
```
_raw/ 또는 _extracted/
    │
    │ [수동 또는 AI 분류]
    ▼
corpus/{domain}/
```

---

## 5. MVP vs 풀 버전

### MVP (지금 당장)

```
✅ Claude Chat만 지원
✅ /capture와 /extract 2개 Skill
✅ inbox/_raw/, inbox/_extracted/ 폴더
✅ 수동 분류 (AI 보조)
```

### 풀 버전 (나중에)

```
❌ Slack/Discord 연동
❌ Voice 입력
❌ 자동 분류
❌ 실시간 연결 그래프
```

---

## 6. 구현 우선순위

| # | 작업 | 복잡도 | 임팩트 |
|---|------|--------|--------|
| 1 | inbox 폴더 구조 변경 | LOW | HIGH |
| 2 | /capture Skill 작성 | LOW | HIGH |
| 3 | /extract Skill 작성 | MEDIUM | HIGH |
| 4 | 표준 질문 세트 정의 | LOW | MEDIUM |
| 5 | 분류 도우미 스크립트 | MEDIUM | MEDIUM |

**제안 순서**: 1 → 2 → 4 → 3 → 5

---

## 7. 열린 질문

1. **/capture vs /extract 구분이 사용자에게 부담인가?**
   - 대안: 단일 Skill이 자동 판단

2. **표준 질문 5개가 최적인가?**
   - 적으면 추출 부족, 많으면 피로

3. **_processing/ 폴더가 필요한가?**
   - inbox → corpus 직행이 더 단순?

---

## 8. 다음 단계와의 연결

### → 03-export-diversification.md
- 추출된 지식이 어떤 형태로 나가는지
- agent-docs, blog, book 등

### → 04-ai-automation-roadmap.md
- 추출/분류 자동화 단계
- Claude API 연동 시점

---

**작성**: Claude (brainstorm session)
**상태**: Draft - 논의 필요
