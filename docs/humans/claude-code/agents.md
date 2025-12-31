# Agents (서브에이전트)

## 개념

**특정 작업에 특화된 별도 컨텍스트를 가진 AI 어시스턴트**입니다. 각 서브에이전트는 독립적인 컨텍스트 윈도우를 유지하여 메인 대화를 복잡하게 만들지 않고 집중된 작업 실행을 가능하게 합니다.

## 주요 특징

### 컨텍스트 관리
- 각 서브에이전트는 별도의 컨텍스트를 유지
- 메인 대화의 정보 과부하 방지
- 작업별로 집중된 상호작용 가능

### 병렬 실행
- 여러 서브에이전트를 동시에 실행 가능
- 복잡한 워크플로우의 속도 향상

### 전문성
- 특정 도메인에 맞춘 상세한 지시사항 설정 가능
- 지정된 작업에서 높은 성공률 달성

### 유연한 권한 관리
- 각 서브에이전트마다 다른 도구 접근 권한 설정 가능
- 강력한 도구를 특정 서브에이전트 타입에만 제한 가능

## 디렉토리 구조

서브에이전트는 두 가지 위치에 정의할 수 있습니다:

```
# 사용자 레벨 (모든 프로젝트에서 사용 가능)
~/.claude/agents/
└── code-reviewer.md

# 프로젝트 레벨 (특정 프로젝트 전용, 팀과 공유 가능)
.claude/agents/
└── security-auditor.md
```

## 작성법

서브에이전트는 YAML frontmatter를 가진 마크다운 파일로 정의합니다:

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

When reviewing code:
- Identify security vulnerabilities
- Check for performance issues
- Verify adherence to coding standards
- Suggest specific improvements

Be thorough but concise in your feedback.
```

## YAML Frontmatter 필드

| 필드 | 타입 | 필수 | 설명 | 예시 |
|------|------|------|------|------|
| `name` | string | ✅ | 고유 식별자 (소문자와 하이픈만 사용) | `"code-reviewer"` |
| `description` | string | ✅ | 서브에이전트의 목적과 사용 시점을 설명하는 자연어 | `"Expert code review specialist..."` |
| `tools` | string | ⬜️ | 사용 가능한 도구 목록 (쉼표로 구분) | `"Read, Write, Edit, Bash"` |
| `model` | string | ⬜️ | 사용할 AI 모델 (`sonnet`, `opus`, `haiku`, `inherit`) | `"sonnet"` |
| `color` | string | ⬜️ | 아이콘 색상 (`red`, `blue`, `green`, `purple`, `yellow`, `orange`, `default`) | `"blue"` |

### 도구 목록
- `Read`: 파일 읽기
- `Write`: 파일 쓰기
- `Edit`: 파일 편집
- `Bash`: 셸 명령 실행
- `Grep`: 텍스트 검색
- `Glob`: 파일 패턴 매칭
- 기타 Claude Code 도구들

### 모델 옵션
- `sonnet`: Claude Sonnet 모델
- `opus`: Claude Opus 모델
- `haiku`: Claude Haiku 모델
- `inherit`: 메인 대화와 동일한 모델 사용
- 생략 시: 기본 서브에이전트 모델 사용

## 사용 방법

### 1. 자동 위임 (Automatic Delegation)
Claude Code가 작업 설명과 서브에이전트의 `description` 필드를 기반으로 자동으로 적절한 서브에이전트에게 작업을 위임합니다.

```bash
# 코드 리뷰 요청 시 code-reviewer 서브에이전트가 자동으로 활성화될 수 있음
"Review the authentication implementation for security issues"
```

### 2. 명시적 호출 (Explicit Invocation)
특정 서브에이전트를 명시적으로 요청할 수 있습니다.

```bash
# 서브에이전트 이름을 명시적으로 언급
"Use the code-reviewer to review this pull request"
```

## 관리 명령어

`/agents` 명령어를 사용하여 서브에이전트를 대화형으로 관리할 수 있습니다:

- 서브에이전트 목록 보기
- 서브에이전트 생성 및 편집
- 서브에이전트 삭제
- 도구 권한 관리

## 예시: 보안 감사 서브에이전트

```markdown
---
name: security-auditor
description: Security specialist for vulnerability assessment and secure coding practices. Use when reviewing code for security issues, authentication, authorization, or data protection.
tools: Read, Grep, Bash
model: sonnet
color: red
---

# Security Auditor

You are a security expert specializing in:
- Vulnerability assessment
- Authentication and authorization
- Data protection and encryption
- Secure coding practices
- OWASP Top 10 compliance

When auditing code:
1. Identify security vulnerabilities
2. Check for common attack vectors
3. Verify secure coding practices
4. Recommend specific security improvements
5. Prioritize findings by severity

Provide actionable security recommendations.
```

## Plugin에 포함하기

서브에이전트를 플러그인에 포함하려면 `plugin.json`에서 `agents` 필드를 설정합니다:

```json
{
  "name": "my-plugin",
  "agents": "./agents/"
}
```

플러그인 디렉토리 구조:
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── agents/
    ├── code-reviewer.md
    └── security-auditor.md
```

## 참고

- [메인 가이드로 돌아가기](./README.md)
- [Plugin 구조](./plugin.md) - Agents를 Plugin에 포함하는 방법
- [공식 문서](https://docs.anthropic.com/en/docs/claude-code/sub-agents) - Claude Code Subagents 공식 문서
- [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - 100개 이상의 프로덕션 준비된 서브에이전트 컬렉션
