---
title: "ced 플러그인 개선 - agents 검증 및 마켓플레이스 자동 등록"
created: 2026-01-03
updated: 2026-01-03
turns: 2
revision: 1
status: set
sources:
  - inbox/materials/2026-01-03-plugin-json-agents-validation-error.md
  - inbox/thoughts/2026-01-03-ced-agents-validation-improvement.md
history: []
---

## 핵심 문제

### 1. agents 필드 검증 버그 (우선순위 높음)

**현상**: /ced:create로 플러그인 생성 시 agents 필드가 잘못된 형식으로 생성됨

```json
// 잘못된 형식 (현재 생성됨)
"agents": ["./agents/"]

// 올바른 형식
"agents": ["./agents/infra-setup.md"]
```

**원인**: commands/skills는 디렉토리 지정 가능하지만, agents는 개별 .md 파일만 허용

**영향**: 설치 시 validation error 발생, 매번 수동 수정 필요

### 2. 마켓플레이스 자동 등록 누락

**현상**: 플러그인 생성 후 marketplace.json에 수동 등록 필요

**영향**: 검색 불가, 추가 작업 발생

---

## 분석 결과

### 수정 대상 파일

**1. validate.md** (`/home/choigawoon/k-codepoet/my-claude-plugins/plugins/claude-extension-dev/commands/validate.md`)
- agents 필드 패턴 체크 추가 필요
- 검증 체크리스트에 "agents는 개별 .md 파일만 허용" 추가

**2. create.md** (`/home/choigawoon/k-codepoet/my-claude-plugins/plugins/claude-extension-dev/commands/create.md`)
- 67행: `"agents": ["./agents/"]` → 개별 파일 경로로 변경
- 마켓플레이스 자동 등록 단계 추가 (안내 → 실제 등록)
- 마지막에 /ced:validate 호출하여 검증

### 마켓플레이스 구조

```
/home/choigawoon/k-codepoet/my-claude-plugins/
├── .claude-plugin/
│   └── marketplace.json    ← 여기에 등록
└── plugins/
    └── {plugin-name}/
```

marketplace.json 형식:
```json
{
  "name": "k-codepoet-plugins",
  "plugins": [
    {
      "name": "{topic}",
      "source": "./plugins/{topic}",
      "description": "..."
    }
  ]
}
```

---

## 해결 방안 (확정)

### Task 1: /ced:validate 수정
- 검증 체크리스트 1번에 추가:
  - `agents` 필드가 있으면 각 항목이 `.md`로 끝나는지 확인
  - 디렉토리 형식(`./agents/`)이면 Error로 리포트

### Task 2: /ced:create 수정
- plugin.json 템플릿에서 agents 필드를 개별 파일 경로로 변경
- 주석으로 차이점 명시: "agents는 디렉토리가 아닌 개별 파일만 지원"

### Task 3: 마켓플레이스 자동 등록
- 5단계 "안내"를 실제 "등록"으로 변경
- marketplace.json 경로 탐색 후 자동 추가

### Task 4: 검증 호출
- /ced:create 마지막에 /ced:validate 호출
- 문제 있으면 자동 수정 후 재검증

---

## Next

작업 착수 준비 완료. 구현 시작하면 됨.
