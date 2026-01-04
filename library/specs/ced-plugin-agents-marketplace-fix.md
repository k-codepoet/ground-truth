---
title: "ced 플러그인 개선 - agents 검증 및 마켓플레이스 자동 등록"
type: spec
origin: derived
views: []
---

## Context

/ced:create로 플러그인 생성 시 두 가지 반복 오류가 발생:
1. agents 필드가 디렉토리 형식으로 생성되어 설치 실패
2. 마켓플레이스에 수동 등록 필요

매번 플러그인 만들 때마다 같은 실수를 반복하므로 자동화로 예방해야 함.

## Content

### 핵심 문제

**1. agents 필드 검증 버그**

```json
// 잘못된 형식 (현재 생성됨)
"agents": ["./agents/"]

// 올바른 형식
"agents": ["./agents/infra-setup.md"]
```

- commands/skills는 디렉토리 지정 가능
- agents는 개별 .md 파일만 허용 (Claude Code 제약)

**2. 마켓플레이스 자동 등록 누락**

플러그인 생성 후 marketplace.json에 수동 등록 필요 → 검색 불가

### 해결 방안

**Task 1: /ced:validate 수정**
- agents 필드가 `.md`로 끝나는지 확인
- 디렉토리 형식이면 Error 리포트

**Task 2: /ced:create 수정**
- agents 필드를 개별 파일 경로로 생성
- 주석으로 차이점 명시

**Task 3: 마켓플레이스 자동 등록**
- 플러그인 생성 완료 시 marketplace.json에 자동 추가

**Task 4: 검증 호출**
- /ced:create 마지막에 /ced:validate 호출
- 문제 시 자동 수정 후 재검증

### 수정 대상 파일

| 파일 | 수정 내용 |
|------|----------|
| `commands/validate.md` | agents 필드 패턴 체크 추가 |
| `commands/create.md` | agents 형식 수정, 마켓플레이스 자동 등록, validate 호출 |

### 마켓플레이스 구조

```
{marketplace-repo}/
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    └── {plugin-name}/
```

## Connections

- 원본 오류: `inbox/materials/2026-01-03-plugin-json-agents-validation-error.md`
- 개선 아이디어: `inbox/thoughts/2026-01-03-ced-agents-validation-improvement.md`
