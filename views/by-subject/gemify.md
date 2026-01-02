---
title: "Gemify Plugin 종합 View"
subject: gemify
updated: 2026-01-02
sources:
  - library/growth/gemify-branding-decision.md
  - library/operations/knowledge-pipeline-vision.md
  - library/operations/draft-facet-polish-mode.md
  - library/operations/external-research-pipeline.md
  - library/ai-automation/gemify-1.5.0-workflow-extensions.md
  - library/ai-automation/improve-plugin-workflow.md
  - library/ai-automation/claude-code-env-context.md
  - library/ai-automation/execution-first-principle.md
---

# Gemify Plugin 종합 View

## 구조 (도식)

```
┌─────────────────────────────────────────────────────────────────┐
│                        Gemify Plugin                            │
│         "Turn your thoughts into gems"                          │
└─────────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │   inbox/    │ →  │   drafts/   │ →  │   library/  │
    │   (원석)    │    │  (다듬기)    │    │   (보석)    │
    └─────────────┘    └─────────────┘    └─────────────┘
         │                   │                   │
    ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
    │thoughts/│         │ facet   │         │ 6 domain│
    │materials│         │ polish  │         │ 분류    │
    └─────────┘         └─────────┘         └─────────┘

    확장 워크플로우:
    ┌─────────────────────────────────────────────────────────────┐
    │  /capture-pair    material + thought 동시 생성              │
    │  /retro           구현 완료 후 역방향 → library 직행        │
    │  /improve-plugin  add-dir로 세션 한정 플러그인 개선         │
    └─────────────────────────────────────────────────────────────┘
```

## 스토리 (왜 → 뭘 → 어디까지)

### 왜 만들었나

1인 AI Company를 위한 지식 관리 시스템이 필요했다. 머릿속 암묵지를 구조화된 지식으로 변환하는 파이프라인. **"말하는 대로 지식이 정리되는 시스템"**을 목표로 함.

### 무엇을 만들었나

**Gemify** - 보석 메타포를 채택한 지식 파이프라인 플러그인

| 결정 | 내용 |
|------|------|
| 제품명 | Gemify ("-ify" 변환 패턴, 동사화) |
| 메타포 | 광물/보석 (원석 → 다듬기 → 보석) |
| 태그라인 | Turn your thoughts into gems. |
| 폴더 구조 | inbox/drafts/library (직관적) |

**핵심 커맨드**:
- `/gemify:inbox` - 생각 포착
- `/gemify:import` - 외부 재료 가져오기 (Perplexity 등에서)
- `/gemify:draft` - facet(넓게)/polish(깊이) 모드로 다듬기
- `/gemify:library` - domain별 분류 저장

**v1.5.0 확장**:
- `/gemify:capture-pair` - material + thought 동시 생성
- `/gemify:retro` - 사후처리 (구현 완료 후 역방향 기록)
- `/gemify:improve-plugin` - 세션 한정 플러그인 개선

### 어디까지 왔나

```
Stage 0: 완전 수동      ✅ 완료
Stage 1: AI 보조        ← 현재 진행 중
Stage 2: AI 주도        (예정)
Stage 3: AI 자율        (예정)
```

## 핵심 원칙

1. **실행 우선**: 완벽보다 동작, 틀리면 나중에 고침
2. **역방향도 정당**: retro로 사후 기록 가능
3. **세션 한정 스코프**: add-dir로 필요할 때만 접근

## 관련 문서

### 브랜딩/비전
- [Gemify 브랜딩 의사결정](../../library/growth/gemify-branding-decision.md) - 네이밍, 메타포, 태그라인
- [Knowledge Pipeline 비전](../../library/operations/knowledge-pipeline-vision.md) - 전체 시스템 구조

### 기능/워크플로우
- [facet/polish 모드](../../library/operations/draft-facet-polish-mode.md) - draft 대화 모드
- [외부 리서치 파이프라인](../../library/operations/external-research-pipeline.md) - import 배경
- [1.5.0 워크플로우 확장](../../library/ai-automation/gemify-1.5.0-workflow-extensions.md) - capture-pair, retro

### 구현/기술
- [플러그인 개선 워크플로우](../../library/ai-automation/improve-plugin-workflow.md) - add-dir 패턴
- [Claude Code 환경 컨텍스트](../../library/ai-automation/claude-code-env-context.md) - env 정보 활용
- [실행 우선 원칙](../../library/ai-automation/execution-first-principle.md) - 개발 철학
