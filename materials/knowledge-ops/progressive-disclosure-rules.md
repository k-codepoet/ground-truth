---
title: "Progressive Disclosure Rules - Claude YAML frontmatter"
date: 2025-12-31
source: "Perplexity 리서치"
type: article
status: raw
used_in:
---

# claude가 얘기하는 yaml frontmatter 양식

Claude AI에서 언급하는 YAML frontmatter는 주로 SKILL.md 파일의 맨 위에 위치하며, 스킬의 메타데이터를 정의하는 형식입니다. 이 frontmatter는 Claude가 스킬을 빠르게 인식하고 적합성을 판단하도록 돕습니다.[^1_1][^1_9]

## 기본 구조

YAML frontmatter는 `---`로 시작하고 끝나며, 필수 필드인 `name`과 `description`을 포함합니다. 예:

```
---
name: example-skill
description: "이 스킬은 PPT 생성을 위해 사용되며, presentation_content.md에서 로드맵을 만듭니다."
allowed-tools: ["Bash", "Read"]
version: 1.0.0
---
```

Claude는 대화 시작 시 모든 스킬의 frontmatter만 먼저 읽어 관련성을 판단합니다.[^1_8][^1_9][^1_1]

## 주요 필드

- **name**: 스킬의 고유 ID (소문자, 하이픈 권장).[^1_9]
- **description**: 스킬 용도와 사용 시나리오를 상세히 설명 (Claude의 판단 기준).[^1_1][^1_9]
- **allowed-tools**: 허용 도구 목록 (예: Bash, Read).[^1_10]
- **version**: 스킬 버전 관리.[^1_10]


## 활용 팁

frontmatter는 스킬의 "얼굴" 역할을 하며, description이 명확해야 Claude가 적절히 호출합니다. CLAUDE.md나 AGENTS.md 같은 프로젝트 지침서에도 유사 형식 사용.[^1_6][^1_1]
<span style="display:none">[^1_2][^1_3][^1_4][^1_5][^1_7]</span>

<div align="center">⁂</div>

[^1_1]: https://goddaehee.tistory.com/411

[^1_2]: https://www.reddit.com/r/ClaudeAI/comments/1hs0adv/best_format_to_feed_claude_documents/

[^1_3]: https://platform.claude.com/docs/ko/agents-and-tools/tool-use/code-execution-tool

[^1_4]: https://devocean.sk.com/blog/techBoardDetail.do?id=167718

[^1_5]: https://github.com/eyaltoledano/claude-task-master/issues/707

[^1_6]: https://www.daleseo.com/claude-md/

[^1_7]: https://javaexpert.tistory.com/1536

[^1_8]: https://discuss.pytorch.kr/t/anthropic-claude-claude-agent-skills/7979

[^1_9]: https://wikidocs.net/304779

[^1_10]: https://javaexpert.tistory.com/1477


---

# progressive disclosure를 적용하기 위한 양식 프로토콜이 뭐야?

Progressive disclosure를 적용하기 위한 “양식/프로토콜”은 한 번에 모든 지시를 넣지 않고, **메타(요약) → 본문(상세) → 외부 참조(필요 시 로드)**로 정보를 계층화해 두는 구조입니다. 특히 Claude Agent Skills에서는 “frontmatter 메타데이터가 1단계, 스킬 본문이 2단계”라는 형태로 이를 명시합니다.[^2_1][^2_2]

## Claude/Agent Skills식 프로토콜

- 1단계(Discovery): SKILL.md 상단 YAML frontmatter에 “언제 이 스킬을 쓰는지”만 적어, Claude가 관련성 판단만 하도록 합니다.[^2_2]
- 2단계(Load on demand): 관련성이 있을 때만 SKILL.md 본문(실제 절차/프롬프트)을 읽어 실행 세부를 가져오게 합니다.[^2_2]
- 3단계(Deep dive): 양식, 예시, 체크리스트 등은 `forms.md` 같은 별도 파일로 분리해 “필요할 때 읽어라”로 연결합니다.[^2_2]


## 권장 “양식” 템플릿

아래처럼 파일/섹션을 쪼개면 progressive disclosure가 자연스럽게 구현됩니다.[^2_3][^2_1]

- `CLAUDE.md` (항상 로드되는 범용 규칙): 프로젝트 공통 규칙 + “어디에 무엇이 있는지(인덱스)”만 유지.[^2_1]
- `SKILL.md` (조건부 로드):
    - YAML frontmatter: 목적/트리거/입력·출력만 짧게.[^2_2]
    - 본문: 실제 실행 단계, 예외 처리, 도구 사용 규칙.[^2_2]
    - “If needed, read X”: 상세 폼/정책/참고자료는 파일로 분리.[^2_2]
- `forms/*.md` or `docs/*.md` (희귀/상세): 템플릿, 엣지케이스, 긴 예시, 정책 전문.[^2_2]


## UX 관점 체크포인트

초기 화면(초기 컨텍스트)에는 사용자가 자주 필요한 핵심만 두고, 드문/고급 옵션은 2차 화면(추가 문서/추가 단계)로 보내는 게 progressive disclosure의 핵심입니다. 또한 순차적으로 반드시 거쳐야 하는 흐름(예: 무조건 입력해야 하는 단계)은 “숨김”보다 “비활성화/단계 진행”이 더 적합하다는 가이드도 있습니다.[^2_4][^2_5][^2_6]

원하는 적용 대상이 “Claude 스킬/프롬프트 파일 구조”인지, 아니면 “제품 UI/설정 화면”인지 한 줄로만 알려주면, 그 대상에 맞춘 최소 양식(폴더 구조 + frontmatter 필드 + 섹션 규칙)으로 더 구체화해줄게요.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://www.humanlayer.dev/blog/writing-a-good-claude-md

[^2_2]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

[^2_3]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

[^2_4]: https://www.interaction-design.org/literature/topics/progressive-disclosure

[^2_5]: https://www.nngroup.com/articles/progressive-disclosure/

[^2_6]: https://docs.appian.com/suite/help/25.4/sail/ux-progressive-disclosure.html

[^2_7]: https://blog.logrocket.com/ux-design/progressive-disclosure-ux-types-use-cases/

[^2_8]: https://userpilot.com/blog/progressive-disclosure-examples/

[^2_9]: https://blog.prototypr.io/designing-for-progressive-disclosure-aabb5ddfbab4

[^2_10]: https://thedecisionlab.com/reference-guide/design/progressive-disclosure

[^2_11]: https://www.braintrust.dev/articles/systematic-prompt-engineering

[^2_12]: https://www.lightflows.co.uk/blog/progressive-disclosure-in-ux-design/

[^2_13]: https://discuss.pytorch.kr/t/anthropic-claude-claude-agent-skills/7979

[^2_14]: https://www.linkedin.com/posts/huikang-tong_delivering-instructions-to-ai-models-activity-7385970271918223360-PxrT

[^2_15]: https://frankspillers.com/progressive-disclosure-the-best-interaction-design-technique/

[^2_16]: https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/

[^2_17]: https://dev.to/lymah/best-practices-for-prompt-engineering-with-goose-3m6h

[^2_18]: https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/progressive-disclosure

[^2_19]: https://aimaker.substack.com/p/the-10-step-system-prompt-structure-guide-anthropic-claude

[^2_20]: https://www.reddit.com/r/PromptEngineering/comments/1pyh7oh/prompting_with_progressiveabstraction/


---

# 그 구조가 실제로 어떻게 생겼는데

실제로는 “최소 메타(항상 로드) + 필요할 때만 상세를 읽게 하는 파일 분리” 형태로 생깁니다. Anthropic Agent Skills 기준으로는 스킬 하나가 “폴더 + SKILL.md(필수)”이고, SKILL.md 맨 위 YAML frontmatter의 `name`/`description`만 먼저 로드됩니다.[^3_1][^3_2]

## 폴더 구조 예시

아래처럼 스킬별 폴더를 만들고, 상세 자료는 같은 폴더 안에 선택 파일로 둡니다.[^3_2][^3_3]

```text
~/.claude/skills/
└── pdf-forms/
    ├── SKILL.md          # 필수 (frontmatter + 본문)
    ├── forms.md          # 선택 (자세한 폼/필드 정의 모음)
    ├── reference.md      # 선택 (규정/용어/FAQ)
    └── scripts/          # 선택 (필요 시 자동화 스크립트)
```


## SKILL.md “겉(메타) + 속(절차)”

Claude Code/Agent Skills 문서에서는 frontmatter가 1행 `---`로 시작/종료되고, 그 아래에 마크다운 지침이 이어지는 형태를 요구합니다.[^3_4][^3_2]

```md
---
name: pdf-forms
description: >
  PDF 양식/서류를 채우거나, 폼 필드를 해석해서 입력값을 만들 때 사용.
  사용자가 "pdf 작성", "양식 채우기", "form fill" 같은 말을 하면 이 스킬을 고려.
allowed-tools: [Read, Write, Bash]   # 옵션(구현/환경에 따라)
---

## What this skill does
- PDF/이미지/텍스트에서 폼 필드를 추출하고, 필요한 입력값을 만든다.

## When to use
- 사용자가 “이 PDF 양식 채워줘”라고 요청했을 때.
- 필드 목록/제약조건이 많아 별도 폼 스펙이 필요할 때.

## Procedure
1. 입력 파일(또는 텍스트)을 읽고 필드 목록을 만든다.
2. 불명확한 필드는 질문한다.
3. 확정된 값으로 결과를 생성한다.

## If needed
- 폼 필드 상세 스펙이 필요하면 `forms.md`를 읽어라.
```

`name`과 `description`이 “필수 메타데이터”이고, 에이전트는 시작 시 모든 스킬의 이 메타만 시스템 프롬프트에 미리 로드해 어떤 스킬을 쓸지 빨리 판단합니다.[^3_1][^3_2]

## forms.md (깊은 상세를 분리)

Anthropic은 `forms.md` 같은 “부록 파일”로 세부를 분리해, 실제로 폼을 채울 때만 읽게 하는 progressive disclosure를 설명합니다.[^3_1]

```md
# forms.md

## Form: W-8BEN (예시)
### Fields
- full_name: 여권 영문명과 동일
- country: ISO 국가명
- tin: 없으면 "N/A" 허용

### Validation rules
- 날짜는 YYYY-MM-DD
- 서명일은 오늘 이전/이하
```

원하는 게 “Claude Code 스킬(~/.claude/skills)” 구조인지, 아니면 “레포 안에서 CLAUDE.md + agent_docs/”로 운영하는 구조인지?
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18][^3_19][^3_20][^3_5][^3_6][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

[^3_2]: https://github.com/anthropics/skills

[^3_3]: https://claude-plugins.dev/skills/@whilp/dotfiles/meta

[^3_4]: https://code.claude.com/docs/en/skills

[^3_5]: https://digitalbourgeois.tistory.com/2504

[^3_6]: https://discuss.pytorch.kr/t/anthropic-claude-claude-agent-skills/7979

[^3_7]: https://www.maxitect.blog/posts/maximising-claude-code-building-an-effective-claudemd

[^3_8]: https://blog.langchain.com/using-skills-with-deep-agents/

[^3_9]: https://www.humanlayer.dev/blog/writing-a-good-claude-md

[^3_10]: https://mikhail.io/2025/10/claude-code-skills/

[^3_11]: https://goddaehee.tistory.com/411

[^3_12]: https://claude.com/blog/using-claude-md-files

[^3_13]: https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/

[^3_14]: https://rudaks.tistory.com/entry/Agent-Skills-번역-Skills

[^3_15]: https://www.claude.com/blog/using-claude-md-files

[^3_16]: https://opencode.ai/docs/skills/

[^3_17]: https://javaexpert.tistory.com/1477

[^3_18]: https://www.anthropic.com/engineering/claude-code-best-practices

[^3_19]: https://javaexpert.tistory.com/1459

[^3_20]: https://jangwook.net/en/blog/ko/anthropic-agent-skills-practical-guide/

