# Growing 파일 형식

## Frontmatter

```yaml
---
title: "{제목}"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD HH:MM"
turns: 5
status: growing | digested
sources:
  - seed/2025-12-31-my-idea.md
  - materials/some-article.md
---
```

## 본문 구조

```markdown
## Seed
{최초 아이디어}

## Sources
- seed/2025-12-31-my-idea.md
- materials/some-article.md

## Growth Log
### Session 1 - YYYY-MM-DD
- C: {Claude 질문}
- U: {사용자 답변}
- Insight: {도출된 통찰}

## Current State
{현재까지 종합}

## Open Questions
- [ ] 열린 질문들
```

## 소스 추적

seed/materials 파일 사용 시:
1. 해당 파일의 `status`를 `raw` → `used`로 변경
2. 해당 파일의 `used_in`에 growing 파일 경로 기록
3. growing 파일의 Sources 섹션에 목록 기록
