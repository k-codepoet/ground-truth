---
title: hooks 동작 검증용 플러그인 아이디어
type: thought
status: raw
created: 2026-01-04
references:
  - inbox/materials/2026-01-04-hooks-validation-need.md
tags: [claude-code, hooks, plugin, testing, idea]
---

## 핵심 인사이트

공식 문서대로 작업해도 안 되는 케이스들이 있음. hooks 전체에 대해 동작 여부를 체계적으로 검증할 플러그인이 필요함.

## 제안: hooks-validator 플러그인

### 목적
- 모든 hook 이벤트 타입별 동작 검증
- 플러그인 vs 사용자 설정 훅 차이 확인
- 문서화되지 않은 동작 발견

### 구조 아이디어

```
hooks-validator/
├── hooks/hooks.json          # 모든 이벤트 타입에 테스트 훅 등록
├── scripts/
│   ├── pre-tool-use.sh
│   ├── post-tool-use.sh
│   ├── stop.sh
│   ├── session-start.sh
│   └── ...
└── commands/
    └── validate.md           # 검증 결과 리포트 출력
```

### 검증 방식
1. 각 스크립트가 실행되면 로그 파일에 타임스탬프 기록
2. `/hooks-validator:validate` 명령으로 어떤 훅이 실제 동작했는지 확인
3. 결과를 테이블로 정리

## 다음 단계

- forgeify로 hooks-validator 플러그인 생성
- 모든 이벤트 타입 테스트
- 결과를 forgeify hook-guide에 반영
