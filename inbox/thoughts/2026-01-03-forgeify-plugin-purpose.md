---
title: "Forgeify - Claude Code 플러그인 개발의 메타 도구"
date: 2026-01-03
references:
  - library/ai-automation/forgify-plugin-review.md
status: raw
used_in:
---

## 핵심 아이디어

Forgeify는 **다른 플러그인을 만들기 위한 플러그인**. Claude Code 확장 개발을 학습하고 실행하는 메타 레벨 도구.

> "Forge your ideas into Claude extensions"

## 왜 필요한가

-fy 플러그인들(Gemify, Terrafy, Craftify, Namify)을 만들 때:
- 어떻게 skill 파일을 작성하는지
- agent는 어떤 구조인지
- hook은 언제 쓰는지
- plugin.json은 어떤 필드가 필요한지

이런 질문에 바로 답해주는 가이드가 필요했음.

## 7개 가이드 체계

| 가이드 | 주제 |
|--------|------|
| plugin-guide | 플러그인 구조, plugin.json |
| skill-guide | SKILL.md 작성법, Agent Skills 표준 |
| agent-guide | 서브에이전트 정의, frontmatter |
| command-guide | 슬래시 커맨드 작성 |
| hook-guide | Hook 이벤트, hooks.json |
| marketplace-guide | 마켓플레이스 배포 |
| workflow-guide | 전체 개발 워크플로우 |

## -fy 제품군에서의 역할

다른 -fy 플러그인들과 달리 Forgeify는 **메타 레벨**:
- Gemify, Terrafy, Craftify, Namify = 사용자 문제 해결
- Forgeify = 위 플러그인들을 만드는 데 도움

## 다음 단계

- 플러그인 상세 정보를 materials에 정리
- `/gemify:draft`로 역할과 구조 확장
- view 생성하여 학습 경로 시각화
