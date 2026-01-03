---
title: Craftify - 개발환경 구축 플러그인
created: 2026-01-03
updated: 2026-01-03
turns: 12
revision: 1
status: set
sources:
  - inbox/thoughts/2026-01-03-devenv-plugin-idea.md
history: []
library_docs:
  - library/product/craftify-plugin-design.md
  - library/product/ify-trilogy-strategy.md
  - library/engineering/craftify-progressive-disclosure.md
---

## 핵심 컨셉

**Craftify** 🔨 - "Craft your products with AI"

turborepo + Cloudflare 기반 개발환경 자동화 Claude Code 플러그인

**역할**: HOW - 어떻게 만들지 (설계도 → 코드)

**철학**: Progressive disclosure - 필요할 때만 복잡함 노출

**타겟**: 본인 먼저 → 오픈소스 범용 도구

### -ify Trilogy에서의 위치

```
Gemify  💎  WHAT  - 뭘 만들지 (지식 → 설계도)
Terrafy 🏗️  WHERE - 어디서 돌릴지 (서버 → 인프라)
Craftify 🔨 HOW   - 어떻게 만들지 (설계도 → 코드) ← 이것
```

## 첫 번째 마일스톤

`/craftify:create webapp` - boilerplate 생성

### 지원 boilerplate

| 타입 | 이름 | 스택 |
|------|------|------|
| SSR | react-router-cloudflare | React Router 7 + Cloudflare Workers + Tailwind v4 |
| SPA | react-router-spa | React Router 7 + Tailwind v4 |

### 배포 경로

```
webapp → Cloudflare Workers/Pages
       → wrangler로 배포
       → GitHub 연동 시 자동 배포
```

## 플러그인 구조 (계획)

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

## boilerplate 생성 시 포함될 것

```
my-app/
├── src/
├── package.json
├── turbo.json
├── DEVENV.md            # 사용법 + 철학 링크
└── .devenv/
    └── guides/
        ├── 01-local-dev.md
        ├── 02-cloudflare-setup.md
        └── 03-auto-deploy.md
```

## 단계별 흐름 (Progressive Disclosure)

```
[1단계: 생성]
/craftify:create webapp my-app
→ boilerplate 복제, turborepo 설정

[2단계: 로컬 개발]
pnpm dev
→ 자유롭게 개발

[3단계: 배포 준비]
/craftify:deploy
→ wrangler.toml 설정 가이드
→ Cloudflare 연결

[4단계: 자동 배포]
GitHub 연동
→ push 시 Cloudflare가 자동 빌드/배포
```

## 소스 경로 (복사해올 것)

### boilerplate templates
```
/home/choigawoon/k-codepoet/my-materials/authored-repos/ai-devteam/boilerplates/
├── web/react-router-cloudflare/   # SSR 풀스택
└── web/react-router-spa/          # SPA 목업용
```

### 참고 문서
```
/home/choigawoon/k-codepoet/my-materials/authored-repos/ai-devteam/boilerplates/README.md
```

## 향후 확장

- slack-app boilerplate
- discord-app boilerplate
- Docker/k3s 기반 self-hosted 경로 (API, 백엔드용)

## Open Questions

1. **플러그인 이름** ✓ 결정됨
   - **Craftify** 🔨 - "Craft your products with AI"
   - -ify Trilogy (Gemify, Terrafy, Craftify)의 일원
   - 참고: inbox/materials/2026-01-03-ai-company-trilogy-naming.md

2. **templates 위치** ✓ 결정됨
   - 초기: 플러그인 내장
   - 안정화 후: 별도 GitHub repo로 분리

3. **turborepo 루트 구조** ✓ 결정됨
   - 기본: 새 turborepo 루트 생성 (각 서비스마다 독립)
   - 옵션: 기존 turborepo 경로 입력 시 → 구조 분석 후 apps/my-app으로 추가

---

*다음: `/gemify:draft drafts/devenv-plugin.md`로 이어가기*
