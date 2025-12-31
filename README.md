# Gemify - Personal Knowledge Pipeline

> Turn your thoughts into gems.

원석(생각)을 다듬어 보석(지식)으로 변환하는 개인 지식 파이프라인.

---

## 핵심 개념

```
/gemify:inbox → /gemify:draft → /gemify:library
    inbox/         drafts/         library/
```

원석이 **탐색 → 연마 → 응축**되어 밀도 있는 지식이 됨.

---

## 구조

```
.
├── inbox/
│   ├── thoughts/       # 내 생각 (원석)
│   └── materials/      # 외부 재료 (기사, 문서, 대화 등)
├── drafts/             # 다듬는 중인 아이디어
├── library/            # 완성된 지식 (domain별 분류)
│   ├── product/        # 무엇을 만들 것인가?
│   ├── engineering/    # 어떻게 만들 것인가?
│   ├── operations/     # 어떻게 돌릴 것인가?
│   ├── growth/         # 어떻게 알릴 것인가?
│   ├── business/       # 어떻게 유지할 것인가?
│   └── ai-automation/  # 어떻게 위임할 것인가?
└── docs/               # 프로젝트 문서
```

---

## 명령어

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/gemify:inbox` | 내 생각 포착 | inbox/thoughts/ |
| `/gemify:draft` | 원석 다듬기 (대화로 확장) | drafts/ |
| `/gemify:library` | 보석 정리 (library로) | library/ |

---

## Stage 0 성공 기준

- [ ] 5개 이상 문서가 inbox → drafts → library 이동됨
- [ ] 2개 이상 domain에 분포
- [ ] frontmatter 형식 일관성 유지

---

## 로드맵

상세 계획: [docs/humans/knowledge-ops/brainstorm/](./docs/humans/knowledge-ops/brainstorm/)

| Stage | 목표 | 상태 |
|-------|------|------|
| 0 | 수동 검증 (5개 문서 파이프라인 통과) | 진행중 |
| 1 | AI 보조 (CLAUDE.md, Claude Code) | ✅ |
| 2 | 자동 분류 스크립트 | 예정 |
| 3 | Export 파이프라인 | 예정 |
