---
created: 2026-01-04
status: raw
type: material
source: session-dialogue
tags: [gemify, craftify, plugin-design, delegation]
---

# Gemify → Craftify 위임 패턴 맥락

## 배경

session report viewer PoC 아이디어를 논의하던 중, craftify에게 작업을 위임하는 패턴이 반복될 것으로 예상됨.

## 관찰된 패턴

1. **gemify:improve-plugin** - 플러그인 개선 문서를 만들어 forgeify에 위임
2. **gemify:inbox → draft → library** - 지식 정제 파이프라인
3. 새로운 니즈: **gemify → craftify** 위임 패턴

## 선행 과제

- gemify ↔ craftify 간 작업 스키마/프로토콜 정의
- 문서 형식 표준화 (craftify가 이해할 수 있는 구조)
- 위임 인터페이스 설계

## 유사 사례

- `gemify:improve-plugin`: ground-truth 문서 → forgeify 실행
- 동일한 패턴으로 `gemify:craftify-poc` 스킬 필요
