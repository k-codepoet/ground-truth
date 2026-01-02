---
title: CED 플러그인 공식 문서 동기화 작업 맥락
date: 2026-01-02
source: Claude Code 세션 - ced 플러그인 검수
type: conversation
status: raw
used_in: null
---

# CED 플러그인 동기화 작업 맥락

## 발단

ced 플러그인 검수 중 공식 문서와 가이드 간 미스매치 발견

## 발견된 차이점

### Command Guide
- `model` 필드 누락: 커맨드별 모델 지정 가능
- `disable-model-invocation` 필드 누락: Claude 자동 호출 차단

### Hook Guide
- 누락 이벤트: `Stop`, `SubagentStart`, `SubagentStop`, `PreCompact`
- `agent` 타입: 공식 문서에서 미지원 (제거 필요)
- `prompt` 타입: Stop/SubagentStop 전용으로 제한

## 조치

1. inbox 리서치 자료 확인
2. 웹검색으로 공식 문서 최신 사양 확인
3. 플러그인 가이드 파일 수정
4. inbox 파일 status → used 업데이트

## 참조

- [Slash commands - Claude Code Docs](https://code.claude.com/docs/en/slash-commands)
- [Hooks reference - Claude Code Docs](https://code.claude.com/docs/en/hooks)
