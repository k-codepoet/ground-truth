---
title: "gemify:import 파일명 규칙 누락 수정 필요"
date: 2026-01-02
references: []
status: raw
used_in:
---

gemify:import로 material 만들 때 문서 내용(frontmatter 등)은 잘 처리하는데, 파일명 규칙(`YYYY-MM-DD-{slug}.md`)은 자동으로 안 해줘서 수동으로 고쳐야 했음. 스킬에서 파일명 생성 시 날짜 prefix 자동 추가하도록 수정 필요.
