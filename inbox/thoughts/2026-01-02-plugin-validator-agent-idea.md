---
title: 플러그인 검증 에이전트 아이디어
date: 2026-01-02
status: raw
used_in: null
references:
  - inbox/materials/2026-01-02-plugin-improvement-workflow.md
  - inbox/materials/2026-01-02-ced-plugin-official-docs-comparison.md
---

# 플러그인 검증 에이전트 구상

## 핵심 아이디어

방금 수행한 "공식 문서 기준 플러그인 검증" 워크플로우를 **gemify 에이전트**로 자동화하고 싶다.

## 에이전트 이름 후보
- `plugin-validator`
- `plugin-auditor`
- `doc-sync-checker`

## 에이전트 역할
1. **입력**: 플러그인 경로
2. **동작**:
   - 플러그인 내 가이드 파일 스캔
   - 공식 문서 검색 (WebSearch)
   - 항목별 비교 분석
   - 누락/차이점 리포트 생성
3. **출력**:
   - 검증 결과 리포트
   - 구체적인 수정 제안
   - (선택) 자동 수정 적용

## 필요한 도구
- `Read`, `Glob`: 플러그인 파일 읽기
- `WebSearch`, `WebFetch`: 공식 문서 확인
- `Write`, `Edit`: 리포트 생성 및 수정 적용

## gemify 플러그인에 추가할 위치
```
gemify/
└── agents/
    └── plugin-validator.md
```

## 다음 단계
1. 에이전트 스펙 상세 설계
2. gemify 플러그인에 agents/ 디렉토리 추가
3. plugin-validator.md 작성
4. 테스트: ced 플러그인으로 검증 실행
