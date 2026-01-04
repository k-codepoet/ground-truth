---
title: "Claude Code 생태계 가이드"
type: how-to
origin: digested
---

# Claude Code 생태계 가이드

Claude Code는 5가지 핵심 요소로 구성된 확장 시스템을 제공합니다.

## 계층 구조

```
Marketplace (마켓플레이스)
└── Plugin (플러그인) - 패키징 단위
    ├── Commands (슬래시 커맨드) - 사용자가 명시적으로 실행
    ├── Skills (스킬) - Claude가 자동으로 판단해서 사용
    ├── Agents (서브에이전트) - 특정 작업에 특화된 별도 컨텍스트
    ├── Hooks (훅) - 이벤트 기반 자동 실행
    └── MCP Servers - 외부 도구/서비스 연결
```

## 핵심 요소 빠른 참조

| 요소 | 목적 | 실행 방식 | 표준 |
|------|------|-----------|------|
| **Skills** | 전문 지식/워크플로우 | Claude 자동 판단 | Agent Skills (오픈) |
| **Commands** | 명시적 작업 실행 | 사용자 `/` 호출 | Claude Code 전용 |
| **Agents** | 특화된 서브작업 | Claude 위임 | Claude Code 전용 |
| **Hooks** | 이벤트 기반 자동화 | 이벤트 트리거 | Claude Code 전용 |
| **Plugin** | 패키징/배포 단위 | - | Claude Code 전용 |
| **Marketplace** | 플러그인 카탈로그 | - | Claude Code 전용 |

---

## Skills (스킬)

**Claude가 작업 컨텍스트를 보고 자동으로 로드하여 사용하는 전문 지식과 워크플로우**

### 디렉토리 구조

```
my-skill/
├── SKILL.md           # 필수: 스킬 정의
├── scripts/           # 선택: 실행 가능한 스크립트
├── references/        # 선택: 상세 참고 문서
└── assets/            # 선택: 템플릿, 이미지 등
```

### SKILL.md 작성법

```markdown
---
name: pdf-processing
description: Extract text and tables from PDF files. Use when working with PDF documents.
license: Apache-2.0
compatibility: Requires python3, poppler-utils
metadata:
  author: myorg
  version: "1.0"
allowed-tools: Bash(python3:*) Read Write
---

# PDF Processing Skill

## Overview
이 스킬은 PDF 문서 작업을 지원합니다...
```

### 필수 필드

| 필드 | 필수 | 제약사항 |
|------|------|----------|
| `name` | O | 1-64자, 소문자+숫자+하이픈만, 디렉토리명과 일치 |
| `description` | O | 1-1024자, 무엇을 하는지 + 언제 사용하는지 포함 |

### Progressive Disclosure 원칙

1. **Metadata** (~100 토큰): `name`과 `description`은 시작 시 모든 스킬에 대해 로드
2. **Instructions** (<5000 토큰 권장): `SKILL.md` 본문은 스킬 활성화 시 로드
3. **Resources** (필요시): `scripts/`, `references/` 파일은 필요할 때만 로드

---

## Commands (커맨드)

**사용자가 `/` 슬래시로 명시적으로 실행하는 커스텀 명령어**

### Skills vs Commands 비교

| 구분 | Skills | Commands |
|------|--------|----------|
| 호출 방식 | Claude가 자동 판단 | 사용자가 명시적으로 `/command` |
| 범위 | 작업별, 필요시 로드 | 항상 사용 가능 |
| 표준 | Agent Skills 오픈 스탠다드 | Claude Code 전용 |

### 작성법

```markdown
---
name: deploy
description: Deploy the application to production
---

# Deploy Command

## Steps
1. Build the application
2. Run tests
3. Deploy to production
```

---

## Agents (서브에이전트)

**특정 작업에 특화된 별도 컨텍스트를 가진 AI 어시스턴트**

### 주요 특징

- **컨텍스트 관리**: 각 서브에이전트는 별도의 컨텍스트를 유지
- **병렬 실행**: 여러 서브에이전트를 동시에 실행 가능
- **전문성**: 특정 도메인에 맞춘 상세한 지시사항 설정 가능

### 디렉토리 구조

```
# 사용자 레벨 (모든 프로젝트에서 사용 가능)
~/.claude/agents/
└── code-reviewer.md

# 프로젝트 레벨 (특정 프로젝트 전용)
.claude/agents/
└── security-auditor.md
```

### 작성법

```markdown
---
name: code-reviewer
description: Expert code review specialist. Use for quality, security, and maintainability reviews.
tools: Read, Grep, Glob, Bash
model: sonnet
color: blue
---

# System Prompt

You are a code review specialist with expertise in security, performance, and best practices.
```

### YAML Frontmatter 필드

| 필드 | 필수 | 설명 |
|------|------|------|
| `name` | O | 고유 식별자 (소문자와 하이픈만 사용) |
| `description` | O | 서브에이전트의 목적과 사용 시점 |
| `tools` | X | 사용 가능한 도구 목록 (쉼표로 구분) |
| `model` | X | 사용할 AI 모델 (`sonnet`, `opus`, `haiku`, `inherit`) |
| `color` | X | 아이콘 색상 |

---

## Hooks (훅)

**특정 이벤트 발생 시 자동으로 실행되는 스크립트** (LLM에 의존하지 않고 결정론적으로 동작)

### 이벤트 타입

| 이벤트 | 설명 |
|--------|------|
| `PreToolUse` | 도구 실행 전 (차단 가능) |
| `PostToolUse` | 도구 실행 후 |
| `UserPromptSubmit` | 사용자 프롬프트 제출 시 |
| `SessionStart` | 세션 시작 시 |
| `SessionEnd` | 세션 종료 시 |

### 작성 예시

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Plugin (플러그인)

**Commands, Skills, Agents, Hooks, MCP Servers를 하나로 묶은 배포 단위**

### 필수 구조

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # 필수: 플러그인 매니페스트
├── commands/              # 선택: 커맨드
├── agents/                # 선택: 서브에이전트
├── skills/                # 선택: 스킬
├── hooks/                 # 선택: 훅 설정
│   └── hooks.json
└── scripts/               # 선택: 유틸리티 스크립트
```

### plugin.json 작성법

```json
{
  "name": "my-plugin",
  "version": "1.2.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Author Name"
  },
  "commands": ["./custom/commands/special.md"],
  "agents": "./custom/agents/",
  "skills": "./custom/skills/",
  "hooks": "./config/hooks.json"
}
```

### 중요 환경 변수

**`${CLAUDE_PLUGIN_ROOT}`**: 플러그인 디렉토리의 절대 경로. 모든 스크립트와 경로에서 사용 필수.

### 설치 스코프

| 스코프 | 설정 파일 | 용도 |
|--------|-----------|------|
| `user` | `~/.claude/settings.json` | 개인용, 모든 프로젝트에서 사용 (기본값) |
| `project` | `.claude/settings.json` | 팀 공유용, 버전 관리 포함 |
| `local` | `.claude/settings.local.json` | 프로젝트별, gitignore |

### CLI 명령어

```bash
# 플러그인 설치
claude plugin install <plugin>[@marketplace] --scope user|project|local

# 플러그인 제거
claude plugin uninstall <plugin>

# 플러그인 업데이트
claude plugin update <plugin>
```

---

## Marketplace (마켓플레이스)

**플러그인 카탈로그를 관리하는 저장소**. GitHub에 `.claude-plugin/marketplace.json` 파일이 있으면 24시간 내 자동 등록.

### 필수 구조

```
my-marketplace/
├── .claude-plugin/
│   └── marketplace.json   # 필수 위치
└── plugins/
    ├── plugin-1/
    └── plugin-2/
```

### marketplace.json 작성법

```json
{
  "name": "my-marketplace",
  "owner": {
    "name": "author-name"
  },
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./plugins/my-plugin",
      "description": "Plugin description"
    }
  ]
}
```

### 마켓플레이스 사용

```bash
# GitHub에서 추가
/plugin marketplace add owner/repo

# 특정 마켓플레이스에서 플러그인 설치
/plugin install plugin-name@marketplace-name
```

---

## 실전 워크플로우

### 1. Skill 만들기

```bash
mkdir pdf-processor
cd pdf-processor
# SKILL.md 작성
skills-ref validate ./pdf-processor
```

### 2. Plugin으로 패키징

```bash
mkdir my-plugin && cd my-plugin
mkdir -p .claude-plugin skills commands scripts
# plugin.json 작성
cp -r ../pdf-processor skills/
```

### 3. Marketplace 만들기

```bash
mkdir my-marketplace && cd my-marketplace
mkdir -p .claude-plugin plugins
# marketplace.json 작성
# GitHub에 푸시
```

### 4. 마켓플레이스 사용

```bash
/plugin marketplace add your-name/my-marketplace
/plugin install my-plugin@my-marketplace
```
