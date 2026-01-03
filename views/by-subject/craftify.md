---
title: "Craftify Plugin 종합 View"
subject: craftify
updated: 2026-01-03
sources:
  - library/product/craftify-plugin-design.md
  - library/product/ify-trilogy-strategy.md
  - library/engineering/craftify-progressive-disclosure.md
---

# Craftify Plugin 종합 View

## 구조 (도식)

```
┌─────────────────────────────────────────────────────────────────┐
│                       Craftify Plugin                            │
│         "Craft your products with AI"  🔨                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                    -ify Trilogy에서의 위치
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │  Gemify 💎  │    │ Terrafy 🏗️ │    │ Craftify 🔨│
    │    WHAT     │    │   WHERE     │    │    HOW     │
    │  뭘 만들지   │    │ 어디서 돌릴지│    │어떻게 만들지│
    └─────────────┘    └─────────────┘    └─────────────┘
           │                  │                  │
      지식 → 설계도      서버 → 인프라      설계도 → 코드
```

## Progressive Disclosure 흐름

```
[1단계: 생성]
/craftify:create webapp my-app
→ boilerplate 복제, turborepo 설정
→ 순수 코드만. 인프라 설정 없음

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

## 스토리 (왜 → 뭘 → 어디까지)

### 왜 만드나

AI Company 구축에서 "어떻게 만들지(HOW)"를 담당할 도구가 필요함. Gemify가 설계도를 만들면, Craftify가 실제 코드로 구현함. Progressive disclosure로 복잡함을 숨기고 필요할 때만 드러냄.

### 무엇을 만드나

**Craftify** 🔨 - turborepo + Cloudflare 기반 개발환경 자동화 플러그인

| 항목 | 내용 |
|------|------|
| 첫 마일스톤 | `/craftify:create webapp` |
| boilerplate | react-router-cloudflare (SSR), react-router-spa (SPA) |
| 배포 | Cloudflare Workers/Pages |
| 철학 | Progressive disclosure |

**플러그인 구조**:
```
craftify/
├── skills/
│   ├── create.md       # /craftify:create
│   ├── dev.md          # /craftify:dev
│   └── deploy.md       # /craftify:deploy
├── agents/
│   └── setup-wizard.md
├── commands/
│   └── status.md
└── templates/
    └── webapp/
```

**boilerplate 생성 시 포함될 것**:
```
my-app/
├── src/
├── package.json
├── turbo.json
├── CRAFTIFY.md          # 사용법 + 철학 링크
└── .craftify/
    └── guides/          # 단계별 가이드
```

### 어디까지 왔나

```
[x] 컨셉 정의           ✅ 완료
[x] 플러그인 구조 설계   ✅ 완료
[ ] 첫 마일스톤 구현     ← 다음 작업
[ ] slack-app 확장
[ ] discord-app 확장
[ ] Docker/k3s 경로 추가
```

## 핵심 원칙

1. **Progressive Disclosure**: 필요할 때만 복잡함 노출
2. **turborepo 독립**: 각 서비스마다 독립 repo (옵션으로 기존 repo 추가)
3. **Cloudflare 우선**: 첫 배포 경로는 Cloudflare (Docker/k3s는 향후)

## 관련 문서

### 설계/전략
- [Craftify 플러그인 설계](../../library/product/craftify-plugin-design.md) - 전체 설계
- [-ify Trilogy 전략](../../library/product/ify-trilogy-strategy.md) - Gemify, Terrafy, Craftify

### 구현/기술
- [Progressive Disclosure 패턴](../../library/engineering/craftify-progressive-disclosure.md) - 단계별 노출

## 소스 경로 (구현 시 참고)

```
boilerplate 템플릿:
/home/choigawoon/k-codepoet/my-materials/authored-repos/ai-devteam/boilerplates/
├── web/react-router-cloudflare/
└── web/react-router-spa/
```
