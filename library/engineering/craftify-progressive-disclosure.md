---
title: Craftify Progressive Disclosure 패턴
domain: engineering
views: [craftify]
---

## Context

개발환경 도구는 복잡해지기 쉬움. Docker, CI/CD, 배포 등 한꺼번에 보여주면 진입장벽이 높아짐.

## Decision

### Progressive Disclosure 적용

각 단계에서 필요할 때만 다음 레이어가 열리는 구조.

```
[1단계: 생성]
/craftify:create webapp my-app
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

### boilerplate 생성 시 포함될 것

```
my-app/
├── src/
├── package.json
├── turbo.json
├── CRAFTIFY.md          # 사용법 + 철학 링크
└── .craftify/
    └── guides/
        ├── 01-local-dev.md
        ├── 02-cloudflare-setup.md
        └── 03-auto-deploy.md
```

- CRAFTIFY.md: 사용법 선행, 철학 링크는 하단
- .craftify/guides/: 단계별 가이드 (필요할 때 참조)

## Outcome

- 처음엔 코드만 보임
- 배포 필요할 때 가이드 열림
- 복잡함은 숨기고, 필요할 때만 드러냄

## Lessons

- 사용자는 결론(사용법)만 볼 것
- 철학(why)은 링크로 제공
- 단계별 가이드는 폴더에 숨겨두고 필요시 안내
