---
title: "plugin.json agents 필드 검증 오류"
date: 2026-01-03
source: "terrafy 플러그인 개발 중 발생한 오류"
type: document
status: raw
used_in: null
---

## 오류 상황

Terrafy 플러그인 설치 시 발생한 오류:

```
Error: Failed to install: Plugin has an invalid manifest file at
/home/choigawoon/.claude/plugins/cache/temp_local_1767437400088_3uuwp7/.claude-plugin/plugin.json.
Validation errors: agents.0: Invalid input: must end with ".md"
```

## 원인

plugin.json에서 agents 필드를 디렉토리로 지정했음:

```json
{
  "commands": ["./commands/"],   // ✅ 디렉토리 OK
  "skills": ["./skills/"],       // ✅ 디렉토리 OK
  "agents": ["./agents/"]        // ❌ 오류! 파일만 가능
}
```

## 필드별 지원 방식

| 필드 | 디렉토리 지원 | 파일 지정 |
|------|--------------|----------|
| `commands` | ✅ `./commands/` | ✅ `./commands/help.md` |
| `skills` | ✅ `./skills/` | ✅ `./skills/help/` |
| `agents` | ❌ **안됨** | ✅ `./agents/infra-setup.md` |

## 해결

```json
{
  "agents": ["./agents/infra-setup.md"]  // 개별 파일 지정
}
```

## 문제점

- commands/skills는 디렉토리로 지정 가능한데 agents만 안 됨
- 일관성 없는 API로 플러그인 개발 시 매번 실수 발생
- 이번이 처음이 아님 - "매번 플러그인 만들때마다 이 오류가 발생"
