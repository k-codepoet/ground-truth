정확해. Claude Code가 제대로 동작하려면 **CLAUDE.md + 폴더 구조 + 템플릿**이 먼저야.

## ground-truth 레포 초기 구조

```
ground-truth/
├── CLAUDE.md                     # ⭐ AI Agent 컨텍스트 (핵심)
├── README.md
├── .gitignore
│
├── inbox/                        # RAW 입력 (미처리)
│   └── _template.md
│
├── enhanced/                     # 구조화된 문서
│   ├── knowledge/
│   │   ├── product/
│   │   ├── engineering/
│   │   ├── operations/
│   │   ├── growth/
│   │   ├── business/
│   │   └── ai-automation/
│   ├── cases/
│   │   └── (동일 구조)
│   └── decisions/
│       └── 2025/
│
├── docs/                         # 규칙/정책 문서
│   ├── humans/                   # WHY - 사람이 결정
│   │   └── principles/
│   └── agents/                   # HOW - AI 실행 규칙
│       └── knowledge-agent/
│
└── scripts/                      # 자동화 스크립트
```

---

지금 바로 만들어줄까?

1. **CLAUDE.md** - Knowledge Agent가 참조할 컨텍스트
2. **템플릿들** - inbox, enhanced 템플릿
3. **예제 문서** - 실제 처리 예시 1개

이거 만들어서 파일로 줄게. 그러면 레포에 바로 push하면 돼.