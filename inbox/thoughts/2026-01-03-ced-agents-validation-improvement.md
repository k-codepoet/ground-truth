---
title: "ced 플러그인 agents 검증 개선 필요"
date: 2026-01-03
status: used
used_in: drafts/ced-plugin-improvement.md
references:
  - inbox/materials/2026-01-03-plugin-json-agents-validation-error.md
---

## 핵심 인사이트

plugin.json의 agents 필드는 디렉토리가 아닌 개별 .md 파일만 허용하는데, 이게 commands/skills와 다른 패턴이라 매번 실수한다.

## 개선 방안

### 1. /ced:validate 강화
- plugin.json 검증 시 agents 필드 패턴 체크
- `./agents/`로 끝나면 경고 및 자동 수정 제안

### 2. /ced:create 개선
- 플러그인 생성 시 agents 필드를 올바른 형식으로 자동 생성
- 템플릿에 주석으로 차이점 명시

### 3. 가이드 문서 업데이트
- plugin-guide에 이 차이점 명확히 문서화
- "주의: agents는 디렉토리가 아닌 개별 파일 경로만 지원"

## 우선순위

높음 - 매번 발생하는 반복 오류이므로 자동 검증으로 예방해야 함
