---
title: 플러그인 버전 관리 및 종속성 체계 조사
date: 2026-01-03
status: used
used_in: drafts/plugin-version-dependency.md
references:
  - /home/choigawoon/.claude/plugins/installed_plugins.json
  - /home/choigawoon/k-codepoet/my-claude-plugins/.claude-plugin/marketplace.json
---

# 플러그인 버전 관리 방식 조사

## 현재 상황 분석

### 1. 현재 Claude Code 플러그인 버전 관리 구조

**plugin.json 구조** (각 플러그인별):
```json
{
  "name": "gemify",
  "version": "1.7.0",
  "description": "...",
  "commands": ["./commands/"],
  "skills": ["./skills/"]
}
```
- 버전 필드는 존재하지만 **dependencies 필드가 없음**

**installed_plugins.json 구조**:
```json
{
  "gemify@k-codepoet-plugins": [{
    "scope": "user",
    "installPath": "...",
    "version": "1.6.0",
    "gitCommitSha": "fac054c242f3..."
  }]
}
```
- 설치된 버전 + git commit SHA 추적
- **종속성 정보 없음**

**marketplace.json 구조**:
```json
{
  "plugins": [{
    "name": "gemify",
    "source": "./plugins/gemify"
  }]
}
```
- 버전 명시 없음 (일부 플러그인만 버전 필드 있음)
- **dependencies 필드 없음**

### 2. 문제점

1. **무조건 최신 버전 가져옴**: 설치 시 항상 latest
2. **종속성 선언 불가**: A가 B@1.0 필요해도 명시할 방법 없음
3. **버전 충돌 해결 없음**: A→B@1.0, C→B@2.0 시 어떻게?
4. **lock 파일 없음**: 재현 가능한 설치 불가능

### 3. npm/pip 비교

| 기능 | npm | pip | Claude Plugin |
|------|-----|-----|---------------|
| dependencies 선언 | package.json | requirements.txt | 없음 |
| 버전 범위 | ^1.0.0, ~1.0.0 | >=1.0,<2.0 | 없음 |
| lock 파일 | package-lock.json | pip freeze | 없음 |
| 충돌 해결 | semver | manual | 없음 |
| peer dependencies | 지원 | 미지원 | 없음 |

### 4. 필요한 작업 (우선순위)

**Phase 1: 스키마 확장**
- plugin.json에 dependencies 필드 추가
- marketplace.json에 버전 명시 의무화
- 버전 범위 표기법 정의 (semver 채택?)

**Phase 2: 설치 로직 수정**
- 종속성 해결 알고리즘 구현
- installed_plugins.json에 종속성 그래프 저장
- 버전 충돌 감지 및 경고

**Phase 3: Lock 파일**
- plugin-lock.json 도입
- 재현 가능한 설치 보장

### 5. 예상 스키마

**plugin.json 확장**:
```json
{
  "name": "gemify",
  "version": "1.7.0",
  "dependencies": {
    "forgeify@k-codepoet-plugins": "^1.3.0"
  },
  "peerDependencies": {
    "commit-commands@claude-plugins-official": ">=1.0.0"
  }
}
```

**marketplace.json 확장**:
```json
{
  "plugins": [{
    "name": "gemify",
    "version": "1.7.0",
    "source": "./plugins/gemify",
    "dependencies": {...}
  }]
}
```

### 6. 실제 종속성 예시 (내 플러그인)

- **gemify** → forgeify 호출 가능 (improve-plugin)
- **forgeify** → 단독 사용 가능
- **craftify** → 단독 사용 가능
- **terrafy** → 단독 사용 가능
- **namify** → 단독 사용 가능

현재는 gemify가 forgeify를 "암묵적으로" 참조하지만 명시적 종속성 없음.

### 7. 조사해야 할 추가 사항

1. Claude Code 공식 문서에 dependencies 지원 계획 있는지
2. marketplace.schema.json 살펴보기
3. 실제 설치 로직 코드 위치 (CLI 소스)
