---
title: CED 플러그인 개선 계획
date: 2026-01-02
status: raw
used_in: null
references:
  - inbox/materials/2026-01-02-ced-plugin-official-docs-comparison.md
---

# CED 플러그인 개선 필요사항

## 핵심 인사이트

공식 문서와 비교해본 결과, ced 플러그인의 가이드들은 **대체로 정확**하지만 일부 누락된 필드와 이벤트가 있다.

## 수정 우선순위

### 1. Command Guide (높음)
- `model` 필드 추가: 커맨드별 모델 지정 가능
- `disable-model-invocation` 필드 추가: Claude가 자동으로 호출 못하게 차단

### 2. Hook Guide (중간)
- 누락 이벤트 추가: `Stop`, `SubagentStop`, `PreCompact`
- `PostToolUseFailure` 검증: 실제 존재하는지 확인 필요
- Hook 타입 `agent` 검증: 공식 문서에서 확인 안됨

## 검수 프로세스

1. ced 플러그인 소스 파일 확인
2. 누락된 내용 추가
3. 불확실한 내용 제거 또는 주석 처리
4. `/ced:validate`로 검증

## 결론

플러그인 품질 유지를 위해 공식 문서 변경사항을 주기적으로 반영해야 한다. 특히 Claude Code 버전 업데이트 시 가이드 동기화 필요.
