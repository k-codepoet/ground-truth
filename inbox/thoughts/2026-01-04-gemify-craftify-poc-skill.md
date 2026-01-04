---
title: Gemify → Craftify 위임 스킬 아이디어
date: 2026-01-04
status: raw
references:
  - inbox/materials/2026-01-04-gemify-craftify-delegation-workflow.md
---

# Gemify → Craftify 위임 스킬 아이디어

## 핵심 인사이트

`/gemify:improve-plugin`이 forgeify에게 작업문서를 만들어주듯이,
**제품 개발을 시작할 때 craftify에게 작업문서를 만들어주는 스킬**이 필요하다.

## 제안 스킬

### `/gemify:poc` 또는 `/gemify:kickoff`

```
/gemify:poc "초등학교 시간표 앱"
```

**자동 수행**:
1. triage로 관련 inbox 자료 수집
2. 대화로 요구사항 구체화
3. namify:name 호출 (제품명)
4. 프로젝트 경로 결정
5. WORK.md 생성 + git init
6. view subject 생성
7. library/specs에 저장

**결과물**:
- `{project-path}/WORK.md` - Craftify 작업 지시서
- `views/by-subject/{product}.md` - 서사 구조
- `library/specs/{product}-work-spec.md` - 영구 스펙

## 구현 고려사항

1. **기존 inbox 자료 활용**: triage로 연결
2. **대화형 구체화**: draft처럼 facet 모드
3. **일관된 출력 구조**: WORK.md 템플릿
4. **Git 초기화**: 바로 작업 시작 가능

## improve-plugin과의 유사성

| 항목 | improve-plugin | poc (제안) |
|------|----------------|------------|
| 목적 | 플러그인 개선 문서 | 제품 시작 문서 |
| 결과물 | improvement.md | WORK.md |
| 위임 대상 | forgeify | craftify |
| 패턴 | 지식 생산 → 실행 위임 | 동일 |
