---
title: "gemify:poc 스킬 스펙"
status: cutting
sources:
  - inbox/thoughts/2026-01-04-gemify-craftify-poc-skill-idea.md
  - inbox/thoughts/2026-01-04-gemify-craftify-poc-skill.md
  - inbox/materials/2026-01-04-gemify-craftify-delegation-workflow.md
  - inbox/materials/2026-01-04-gemify-craftify-delegation-context.md
---

# gemify:poc 스킬 스펙

## 핵심 목적

**Gemify에서 Craftify로 작업을 위임하기 위한 문서를 생성하는 스킬**

`/gemify:improve-plugin`이 forgeify에게 플러그인 개선 문서를 만들어주듯이,
`/gemify:poc`은 craftify에게 PoC 앱 개발 문서를 만들어준다.

## 패턴

```
gemify:improve-plugin → forgeify (플러그인 수정)
gemify:poc            → craftify (PoC 앱 생성)
```

둘 다 **"지식 생산 → 실행 위임"** 패턴

## 워크플로우 (6단계)

Tetritime 프로젝트에서 검증된 워크플로우:

1. **triage** - 관련 inbox 자료 수집
2. **draft** - facet 모드로 요구사항 구체화
3. **namify:name** - 제품명 결정
4. **view subject** - 서사 구조 생성
5. **프로젝트 폴더 셋업** - WORK.md + git init
6. **library** - specs에 영구 저장

## 결과물

| 파일 | 역할 |
|------|------|
| `{project-path}/WORK.md` | Craftify 작업 지시서 |
| `views/by-subject/{product}.md` | 프로젝트 서사/컨텍스트 |
| `library/specs/{product}-work-spec.md` | 영구 보관용 스펙 |

## 사용법 (초안)

```
/gemify:poc "초등학교 시간표 앱"
/gemify:poc inbox/thoughts/session-report-viewer-idea.md
```

## 구현 고려사항

1. **기존 inbox 자료 활용**: triage 연동
2. **대화형 구체화**: draft의 facet 모드 활용
3. **일관된 출력 구조**: WORK.md 템플릿
4. **Git 초기화**: 바로 작업 시작 가능

## 프로젝트 경로 결정

**방식**: 사용자에게 물어봄 (예시 제공)

```
프로젝트를 어디에 생성할까요?
예: /home/choigawoon/k-codepoet/my-domains/products/{product-name}
```

- 기본값 없음, 매번 확인
- 예시는 사용자의 일반적인 작업 구조를 보여줌

## namify:name 호출

**방식**: 워크플로우 내에서 자동 호출

- poc 스킬 실행 중 제품명 결정 단계에서 자동으로 `namify:name` 실행
- 사용자가 별도로 호출할 필요 없음

## 열린 질문

- [x] 스킬 이름: ~~`create-poc` vs~~ **`poc`** ~~vs `kickoff`~~ → **확정**
- [x] 프로젝트 경로: **사용자에게 물어봄** (예시 제공) → **확정**
- [x] namify:name: **자동 호출** → **확정**
- [ ] WORK.md 템플릿 구조?
