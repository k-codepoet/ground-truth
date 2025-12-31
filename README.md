# Ground Truth Knowledge Pipeline

> Stage 0: 수동 검증 단계

---

## 현재 구조

```
.
├── inbox/              # raw 입력 (자유 형식)
├── corpus/             # 구조화된 지식
│   ├── product/        # 무엇을 만들 것인가?
│   ├── engineering/    # 어떻게 만들 것인가?
│   ├── operations/     # 어떻게 돌릴 것인가?
│   ├── growth/         # 어떻게 알릴 것인가?
│   ├── business/       # 어떻게 유지할 것인가?
│   └── ai-automation/  # 어떻게 위임할 것인가?
└── brainstorm/         # 개선안 문서
```

---

## Stage 0 워크플로우

### 1. 입력 (inbox)

```bash
# 새 지식 캡처
vim inbox/YYYY-MM-DD-{slug}.md
```

템플릿: `inbox/_template.md`

### 2. 분류 (수동)

6개 domain 중 선택:

| Domain | 질문 |
|--------|------|
| product | 무엇을 만들 것인가? |
| engineering | 어떻게 만들 것인가? |
| operations | 어떻게 돌릴 것인가? |
| growth | 어떻게 알릴 것인가? |
| business | 어떻게 유지할 것인가? |
| ai-automation | 어떻게 위임할 것인가? |

### 3. 구조화 (corpus)

```bash
# inbox에서 corpus로 이동하며 구조화
mv inbox/YYYY-MM-DD-{slug}.md corpus/{domain}/{slug}.md
vim corpus/{domain}/{slug}.md  # frontmatter 추가
```

템플릿: `corpus/_template.md`

---

## Stage 0 성공 기준

- [ ] 5개 이상 문서가 inbox → corpus 이동됨
- [ ] 2개 이상 domain에 분포
- [ ] frontmatter 형식 일관성 유지

---

## 다음 단계

Stage 0 검증 완료 후:
- Stage 1: CLAUDE.md 추가 (AI 보조)
- Stage 2: 자동 분류 스크립트
- Stage 3: Export 파이프라인
