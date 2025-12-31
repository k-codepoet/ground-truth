# Ground Truth Knowledge Pipeline

> Stage 0: 수동 검증 단계

---

## 핵심 개념

```
seed/ + materials/ → /grow → /digest → CORPUS
 내 생각   외부재료     growing    corpus
```

seed와 materials가 grow에서 만나 **해체 → 재조립 → 응축**되어 밀도 있는 지식이 됨.

---

## 현재 구조

```
.
├── seed/               # 내 생각의 씨앗
├── materials/          # 외부 재료 (기사, 문서, 대화 등)
├── growing/            # seed + materials 확장 중
├── corpus/             # 구조화된 지식
│   ├── product/        # 무엇을 만들 것인가?
│   ├── engineering/    # 어떻게 만들 것인가?
│   ├── operations/     # 어떻게 돌릴 것인가?
│   ├── growth/         # 어떻게 알릴 것인가?
│   ├── business/       # 어떻게 유지할 것인가?
│   └── ai-automation/  # 어떻게 위임할 것인가?
└── skills/             # Claude Code 스킬
```

---

## 명령어

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/seed` | 내 생각의 씨앗 저장 | seed/ |
| `/grow` | seed + materials 대화로 확장 | growing/ |
| `/digest` | 구조화하여 corpus로 | corpus/ |
| `/import` | 외부 재료 저장 (예정) | materials/ |

---

## Stage 0 성공 기준

- [ ] 5개 이상 문서가 seed/materials → growing → corpus 이동됨
- [ ] 2개 이상 domain에 분포
- [ ] frontmatter 형식 일관성 유지

---

## 다음 단계

Stage 0 검증 완료 후:
- Stage 1: CLAUDE.md 추가 (AI 보조) ✅
- Stage 2: 자동 분류 스크립트
- Stage 3: Export 파이프라인
