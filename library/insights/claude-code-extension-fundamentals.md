---
title: Claude Code 확장 개발 기초
type: insight
origin: digested
views:
  - views/by-subject/forgeify.md
---

## Context

Claude Code는 플러그인 시스템을 통해 기능을 확장할 수 있다. 직접 플러그인을 개발하려면 구조와 각 컴포넌트의 역할을 이해해야 한다. 이 문서는 플러그인 개발의 기초를 정리한 **시초 문서**로, 이후 자동화 도구(forgify 등)의 맥락을 제공한다.

## Content

### 플러그인 구조

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # 필수: 매니페스트
├── commands/              # 슬래시 명령어 (/plugin:action)
├── skills/                # 컨텍스트 기반 자동 활성화 지식
│   └── my-skill/
│       └── SKILL.md
├── agents/                # 전문화된 서브에이전트
│   └── my-agent.md
├── hooks/                 # 이벤트 기반 자동 실행
│   └── hooks.json
└── scripts/               # 유틸리티 스크립트
```

### 5대 컴포넌트

| 컴포넌트 | 호출 방식 | 용도 |
|----------|-----------|------|
| **Commands** | `/plugin:action` 명시적 호출 | 특정 작업 자동화 |
| **Skills** | Claude가 컨텍스트 보고 자동 로드 | 재사용 가능한 전문 지식 |
| **Agents** | 자연어 트리거 또는 명시적 호출 | 독립 컨텍스트의 전문가 |
| **Hooks** | 이벤트 발생 시 자동 실행 | 결정론적 자동화 (LLM 불필요) |
| **MCP Servers** | 도구 확장 | 외부 서비스 연동 |

### Skills vs Commands vs Agents

```
Skills    = 지식 (Claude가 알아서 꺼내씀)
Commands  = 도구 (사용자가 직접 호출)
Agents    = 전문가 (별도 컨텍스트에서 작업)
```

- **Skills**: "PDF 작업할 때 이 지식이 필요해" → 자동 로드
- **Commands**: `/deploy --env production` → 명시적 실행
- **Agents**: "코드 리뷰해줘" → 별도 세션에서 전문 작업

### plugin.json 필수 필드

```json
{
  "name": "my-plugin",           // kebab-case, 고유 식별자
  "version": "1.0.0",            // semver
  "description": "간결한 설명",
  "author": { "name": "작성자" }
}
```

### 주요 규칙

1. **agents 필드는 개별 .md 파일만** (디렉토리 불가)
   ```json
   // ❌ 잘못됨
   "agents": ["./agents/"]

   // ✅ 올바름
   "agents": ["./agents/my-agent.md"]
   ```

2. **${CLAUDE_PLUGIN_ROOT}** 환경변수로 플러그인 루트 참조
   ```bash
   ${CLAUDE_PLUGIN_ROOT}/scripts/my-script.sh
   ```

3. **Progressive Disclosure** - 메타데이터는 가볍게, 상세 내용은 필요시 로드

### 개발 사이클

```
설계 → 작성 → 검증 → 설치 → 테스트 → 배포
               ↑
          validate로 규격 확인
```

- **로컬 테스트**: `/plugin marketplace add ./my-plugin`
- **디버그 모드**: `claude --debug`
- **배포**: GitHub에 푸시 → 마켓플레이스 자동 등록 (24시간 내)

## Connections

- [ced-plugin-agents-marketplace-fix](../specs/ced-plugin-agents-marketplace-fix.md) - agents 검증 자동화
- [craftify-progressive-disclosure](../how-tos/craftify-progressive-disclosure.md) - UX 패턴
- [forgify-plugin-review](./forgify-plugin-review.md) - 이 기초를 자동화한 도구 검토
