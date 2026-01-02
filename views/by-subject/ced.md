---
title: "Claude Extension Dev (CED) Plugin 종합 View"
subject: ced
updated: 2026-01-02
sources:
  - plugin:~/k-codepoet/my-claude-plugins/plugins/claude-extension-dev/
---

# Claude Extension Dev (CED) Plugin 종합 View

## 구조 (도식)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CED (Claude Extension Dev)                    │
│         "Claude Code 확장 개발 한국어 가이드"                    │
└─────────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │  Commands   │    │   Skills    │    │   Guides    │
    │  (실행 도구) │    │ (자동 활성화)│    │ (7개 주제)  │
    └─────────────┘    └─────────────┘    └─────────────┘
         │                   │                   │
    ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
    │ create  │         │ plugin  │         │ workflow│
    │ compose │         │ command │         │ 실전예시│
    │ validate│         │ agent   │         │         │
    │ update  │         │ skill   │         │         │
    │ help    │         │ hook    │         │         │
    │ howto   │         │ market  │         │         │
    └─────────┘         └─────────┘         └─────────┘

    확장 개발 플로우:
    ┌─────────────────────────────────────────────────────────────┐
    │  Skill 작성 → Agent 작성 → Plugin 패키징 → Marketplace 배포 │
    │                                                              │
    │  /ced:create     소스 기반 플러그인 자동 생성                │
    │  /ced:compose    여러 플러그인 조립                          │
    │  /ced:validate   가이드라인 준수 검증                        │
    │  /ced:update     최신 규격으로 업데이트                      │
    └─────────────────────────────────────────────────────────────┘
```

## 스토리 (왜 → 뭘 → 어디까지)

### 왜 만들었나

Claude Code 확장 개발(Skills, Commands, Agents, Hooks, Plugins, Marketplace)을 위한 **한국어 가이드**가 필요했다. 공식 문서는 영어이고 흩어져 있어서, 한 곳에서 체계적으로 참조할 수 있는 가이드 플러그인을 만듦.

### 무엇을 만들었나

**CED (Claude Extension Dev)** - 6개 커맨드 + 7개 가이드 스킬

| 구분 | 내용 |
|------|------|
| 버전 | 1.3.0 |
| 위치 | ~/k-codepoet/my-claude-plugins/plugins/claude-extension-dev/ |
| 특징 | 가이드 제공 + 실행 도구 (생성/조립/검증/업데이트) |

**Commands (6개)**:

| 커맨드 | 설명 |
|--------|------|
| `/ced:help` | 도움말 표시 |
| `/ced:howto [topic]` | 주제별 가이드 조회 |
| `/ced:create <path>` | 소스 기반 플러그인 자동 생성 |
| `/ced:compose <topic> <plugins...>` | 여러 플러그인 조립 |
| `/ced:validate [path]` | 가이드라인 준수 검증 + 리팩토링 |
| `/ced:update [path]` | 최신 규격으로 업데이트 |

**Skills (7개 가이드)**:

| 가이드 | 핵심 내용 |
|--------|----------|
| plugin-guide | plugin.json 구조, 설치 스코프, CLI 명령어 |
| command-guide | 슬래시 커맨드 작성법, frontmatter 필드 |
| agent-guide | 서브에이전트 작성법, 내장 에이전트 종류 |
| skill-guide | SKILL.md 작성법, Progressive Disclosure |
| hook-guide | hooks.json 작성법, 11가지 이벤트 타입 |
| marketplace-guide | marketplace.json 구조, 배포 방법 |
| workflow-guide | Skill → Agent → Plugin → Marketplace 실전 예시 |

### 어디까지 왔나

```
v1.0.0: 기본 가이드 (plugin, command, agent, skill)     ✅
v1.1.0: hook, marketplace 가이드 추가                   ✅
v1.2.0: workflow 실전 가이드 추가                       ✅
v1.3.0: create, compose, validate, update 커맨드 추가  ✅ (현재)
```

## 핵심 개념

### Claude Code 확장 유형

| 유형 | 호출 방식 | 용도 |
|------|----------|------|
| **Skill** | 자동 (컨텍스트 기반) | 도메인 지식, 참조 문서 |
| **Command** | 명시적 (`/command`) | 사용자 인터랙션 워크플로우 |
| **Agent** | 자동/명시적 | 복잡한 태스크 위임 |
| **Hook** | 이벤트 트리거 | 자동화, 검증, 로깅 |

### Progressive Disclosure 원칙

```
1단계: Metadata (frontmatter)     - Claude가 로드 여부 판단
2단계: Instructions (본문)        - 필요시 로드
3단계: Resources (references/)    - 심화 자료
```

### 플러그인 구조

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json           # 필수: 매니페스트
├── commands/                 # 슬래시 커맨드
│   └── my-command.md
├── skills/                   # 자동 활성화 스킬
│   └── my-skill/
│       └── SKILL.md
├── agents/                   # 서브에이전트
│   └── my-agent.md
├── scripts/                  # 훅/커맨드에서 사용
│   └── my-script.sh
└── README.md
```

## 핵심 원칙

1. **한국어 우선**: 모든 가이드와 출력이 한국어
2. **실행 도구 제공**: 가이드만 아니라 create/compose/validate/update로 실제 작업 수행
3. **자동 활성화**: 대화 컨텍스트 분석하여 관련 가이드 자동 로드
4. **Progressive Disclosure**: 정보를 단계적으로 제공

## 사용 시나리오

### 새 플러그인 만들기
```
/ced:howto workflow    # 전체 흐름 파악
/ced:create ~/my-scripts docker-helper    # 소스 기반 생성
/ced:validate          # 검증
```

### 기존 플러그인 개선
```
/ced:validate ./my-plugin    # 문제점 확인
/ced:update ./my-plugin      # 최신 규격 적용
```

### 여러 플러그인 조립
```
/ced:compose my-combo plugin-a plugin-b    # 선택 컴포넌트 조립
```

## 관련 문서

### 플러그인 소스
- [CED 플러그인](~/k-codepoet/my-claude-plugins/plugins/claude-extension-dev/) - 실제 플러그인 코드

### 가이드 참조
- `/ced:howto plugin` - 플러그인 구조
- `/ced:howto command` - 커맨드 작성
- `/ced:howto agent` - 에이전트 작성
- `/ced:howto skill` - 스킬 작성
- `/ced:howto hook` - 훅 작성
- `/ced:howto marketplace` - 마켓플레이스 배포
- `/ced:howto workflow` - 실전 워크플로우
