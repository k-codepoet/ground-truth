---
title: ground-truth 프로토콜
domain: operations
views: []
---

## Context

tidy와 triage 스킬을 설계하다 순환 의존성 발견:
- tidy 먼저? → 스키마 없으면 검증 불가
- triage 먼저? → library가 outdated면 잘못된 곳에 연결

→ 공통 프로토콜/스키마 정의가 선행 작업.

## Decision

### 계층 구조

```
library/ ─────────── 재료 (개념의 밀도)
   │                  - 재사용 가능
   │                  - artifact 없음
   │                  - 대기 상태 정상 (아직 안 쓰인 재료)
   ▼
views/ ──────────── 레시피 + 결과물 연결
   │                  - sources: library 참조
   │                  - artifact: 실제 경로
   │                  - story: 왜/뭘/어디까지
   ▼
artifact ─────────── 현실 결과물
                      - plugins/, infra/, docs/
```

### views frontmatter 스키마

```yaml
title: "Gemify Plugin 종합 View"
subject: gemify
created: 2026-01-04
updated: 2026-01-04
revision: 1
sources:
  - library/operations/knowledge-pipeline-vision.md
  - library/ai-automation/bootstrapping-principle.md
artifact: plugins/gemify/          # 실제 결과물 경로
artifact_type: plugin              # plugin | content | code | doc
history: []
```

### library frontmatter 스키마

```yaml
title: 문서 제목
domain: operations                 # 6대 domain 중 하나
views: []                          # 역참조 (이 재료를 쓴 view 목록)
```

### 6대 Domain

| Domain | 핵심 질문 |
|--------|----------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

### tidy 역할

views ↔ artifact 일치 검사:

1. **artifact 존재 확인** - views에 명시된 경로에 실제 파일 있나?
2. **수정 시점 비교** - 어느 쪽이 더 최신인가?
3. **HITL 판단 요청** - 불일치 발견 시 사람에게 확인
   - [A] artifact가 맞아 → views 업데이트 필요
   - [B] views가 맞아 → artifact 수정 필요
   - [C] 둘 다 반영할 부분 있음
   - [D] 나중에 볼게

library 현황 보고:
- 사용 중: views.sources에 연결된 재료
- 대기 중: 아직 안 쓰인 재료 (경고 아님, 현황)

### triage 역할

inbox → library/views 연결점 제안:

1. **클러스터링** - 비슷한 thoughts/materials 묶기
2. **연결점 찾기** - 기존 library/views 어디와 연결되는지
3. **HITL 확인** - "이건 gemify view에 추가될 재료 같아요" → 사람 판단

### source-of-truth 판단 원칙

```
의도적 변경: views가 먼저 (설계 → 구현)
급한 수정: artifact가 먼저 (hotfix → 나중에 문서화)

→ 수정 시점으로 추측 + HITL로 최종 판단
→ 방향은 사람이 정함
```

## Outcome

- tidy/triage가 이 프로토콜을 참조하여 동작
- library = 재료, views = 레시피 + 결과물 연결로 관심사 분리
- 불일치 시 HITL로 처리, 자동 판단 안 함

## References

- drafts/ground-truth-protocol.md
