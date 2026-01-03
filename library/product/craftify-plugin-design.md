---
title: Craftify - 개발환경 구축 플러그인 설계
domain: product
views: [craftify]
---

## Context

AI Company 구축을 위한 -ify Trilogy 중 HOW(어떻게 만들지)를 담당하는 플러그인이 필요함.

```
Gemify  💎  WHAT  - 뭘 만들지 (지식 → 설계도)
Terrafy 🏗️  WHERE - 어디서 돌릴지 (서버 → 인프라)
Craftify 🔨 HOW   - 어떻게 만들지 (설계도 → 코드) ← 이것
```

## Decision

### 핵심 컨셉

**Craftify** 🔨 - "Craft your products with AI"

- turborepo + Cloudflare 기반 개발환경 자동화 Claude Code 플러그인
- Progressive disclosure: 필요할 때만 복잡함 노출
- 타겟: 본인 먼저 → 오픈소스 범용 도구

### 첫 번째 마일스톤

`/craftify:create webapp` - boilerplate 생성

| 타입 | 이름 | 스택 |
|------|------|------|
| SSR | react-router-cloudflare | React Router 7 + Cloudflare Workers + Tailwind v4 |
| SPA | react-router-spa | React Router 7 + Tailwind v4 |

### 배포 경로

```
webapp → Cloudflare Workers/Pages → wrangler → GitHub 연동 시 자동 배포
```

### 플러그인 구조

```
craftify/
├── plugin.json
├── skills/
│   ├── create.md       # /craftify:create - 프로젝트 생성
│   ├── dev.md          # /craftify:dev - 로컬 개발 환경
│   └── deploy.md       # /craftify:deploy - Cloudflare 배포
├── agents/
│   └── setup-wizard.md # 단계별 가이드
├── commands/
│   └── status.md       # /craftify:status - 현재 상태
└── templates/
    └── webapp/
        ├── react-router-cloudflare/
        └── react-router-spa/
```

### turborepo 전략

- 기본: 새 turborepo 루트 생성 (각 서비스마다 독립)
- 옵션: 기존 turborepo 경로 입력 시 → 구조 분석 후 apps/my-app으로 추가

## Outcome

- 플러그인 이름: Craftify
- 첫 기능: `/craftify:create webapp`
- templates 초기 내장, 안정화 후 별도 repo 분리

## References

- boilerplate 소스: `/home/choigawoon/k-codepoet/my-materials/authored-repos/ai-devteam/boilerplates/`
- 네이밍 결정: inbox/materials/2026-01-03-ai-company-trilogy-naming.md
