# Gemify - Personal Knowledge Pipeline

> Turn your thoughts into gems.

원석(생각)을 다듬어 보석(지식)으로 변환하는 개인 지식 파이프라인.

---

## 핵심 개념

```
/gemify:inbox → /gemify:draft → /gemify:library → /gemify:view
    inbox/         drafts/         library/          views/
```

원석이 **탐색 → 연마 → 응축 → 렌더링**되어 밀도 있는 지식이 됨.

---

## 구조

```
.
├── inbox/
│   ├── thoughts/       # 내 생각 (원석)
│   └── materials/      # 외부 재료 (기사, 문서, 대화 등)
├── drafts/             # 다듬는 중인 아이디어
├── library/            # 완성된 지식 (Type별 분류)
│   ├── principles/     # 근본 원칙
│   ├── decisions/      # 의사결정 기록
│   ├── insights/       # 학습/발견
│   ├── how-tos/        # 절차/방법
│   ├── specs/          # 스펙/정의
│   └── workflows/      # 워크플로우/프로세스
├── views/              # 서사가 있는 렌더링
│   ├── by-subject/     # 문제 → 해결책
│   ├── by-talk/        # 발표/강연
│   ├── by-curriculum/  # 교육/커리큘럼
│   ├── by-portfolio/   # 포트폴리오
│   └── by-essay/       # 에세이/수필
└── sessions/           # 세션 리포트
```

---

## 명령어

### 핵심 파이프라인

| 명령어 | 설명 | 저장 위치 |
|--------|------|----------|
| `/gemify:inbox` | 내 생각 포착 | inbox/thoughts/ |
| `/gemify:import` | 외부 재료 가져오기 | inbox/materials/ |
| `/gemify:draft` | 원석 다듬기 (대화로 확장) | drafts/ |
| `/gemify:library` | 보석 정리 (library로) | library/ |
| `/gemify:view` | library를 주제별로 조합 | views/ |

### 보조 명령어

| 명령어 | 설명 |
|--------|------|
| `/gemify:sidebar` | 본 작업 중 떠오른 것을 옆에 빼두기 |
| `/gemify:retro` | 이미 완료된 작업을 역방향으로 기록 |
| `/gemify:wrapup` | 세션 마무리 |
| `/gemify:help` | 도움말 |

---

## 로드맵

| Stage | 목표 | 상태 |
|-------|------|------|
| 0 | 수동 검증 | 진행중 |
| 1 | AI 보조 (CLAUDE.md, Claude Code) | ✅ |
| 2 | 자동 분류 스크립트 | 예정 |
| 3 | Export 파이프라인 | 예정 |
