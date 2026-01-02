---
title: Claude Code env 정보 자동 주입 발견
date: 2026-01-02
source: claude-code-session
type: conversation
status: used
used_in: drafts/claude-code-hidden-context.md
---

# Claude Code env 정보 자동 주입

## 발견 과정

additionalDirectories로 접근 가능한 경로를 물었더니 Claude가 바로 알고 있었다.

## 확인된 내용

Claude Code CLI는 대화 시작 시 시스템 프롬프트에 `<env>` 블록을 자동 주입:

```xml
<env>
Working directory: /home/choigawoon/k-codepoet/ground-truth
Is directory a git repo: Yes
Additional working directories: /home/choigawoon/k-codepoet/my-claude-plugins
Platform: linux
OS Version: Linux 6.8.0-88-generic
Today's date: 2026-01-02
</env>
```

## 포함 정보

- Working directory (현재 작업 디렉토리)
- Is directory a git repo (git 저장소 여부)
- Additional working directories (`--add-dir`로 추가한 경로들)
- Platform (운영체제)
- OS Version (OS 버전)
- Today's date (오늘 날짜)

## 특징

- 사용자에게는 보이지 않음
- Claude만 볼 수 있는 시스템 프롬프트 영역
- 대화 시작 시 자동 수집 및 주입
