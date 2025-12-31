# Claude Code 생태계 가이드

## 개요

Claude Code는 5가지 핵심 요소로 구성된 확장 시스템을 제공합니다.

### 계층 구조

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

| 요소 | 목적 | 실행 방식 | 표준 | 상세 문서 |
|------|------|-----------|------|----------|
| **Skills** | 전문 지식/워크플로우 | Claude 자동 판단 | Agent Skills (오픈) | [skills.md](./skills.md) |
| **Commands** | 명시적 작업 실행 | 사용자 `/` 호출 | Claude Code 전용 | [commands.md](./commands.md) |
| **Agents** | 특화된 서브작업 | Claude 위임 | Claude Code 전용 | [agents.md](./agents.md) |
| **Hooks** | 이벤트 기반 자동화 | 이벤트 트리거 | Claude Code 전용 | [hooks.md](./hooks.md) |
| **Plugin** | 패키징/배포 단위 | - | Claude Code 전용 | [plugin.md](./plugin.md) |
| **Marketplace** | 플러그인 카탈로그 | - | Claude Code 전용 | [marketplace.md](./marketplace.md) |

## 상세 문서

각 요소에 대한 상세한 내용은 다음 문서를 참조하세요:

- **[Skills (스킬)](./skills.md)** - Claude가 자동으로 로드하는 전문 지식과 워크플로우
- **[Commands (커맨드)](./commands.md)** - 사용자가 명시적으로 실행하는 슬래시 커맨드
- **[Agents (서브에이전트)](./agents.md)** - 특정 작업에 특화된 별도 컨텍스트 AI 어시스턴트
- **[Hooks (훅)](./hooks.md)** - 이벤트 기반 자동 실행 스크립트
- **[Plugin (플러그인)](./plugin.md)** - Commands, Skills, Agents, Hooks를 묶은 배포 단위
- **[Marketplace (마켓플레이스)](./marketplace.md)** - 플러그인 카탈로그 저장소
- **[실전 워크플로우](./workflows.md)** - Skill, Plugin, Marketplace 만들기 실습
- **[참고 자료](./references.md)** - 공식 문서 및 예시 저장소

## 시작하기

1. **Skill 만들기**: [skills.md](./skills.md)에서 시작
2. **Plugin으로 패키징**: [plugin.md](./plugin.md) 참조
3. **Marketplace에 배포**: [marketplace.md](./marketplace.md) 참조
4. **실전 예제**: [workflows.md](./workflows.md) 따라하기
