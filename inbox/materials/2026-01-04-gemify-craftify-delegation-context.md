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

## 현재 수동 위임 방식 (craftify 플러그인 미구현 상태)

craftify 플러그인이 아직 "첫 마일스톤 구현" 전이라서, 현재는 수동으로 위임해야 함:

### 방법 1: 스펙 파일 경로 전달
```
ground-truth/library/product/session-report-viewer-spec.md 스펙대로 PoC 만들어줘
```

### 방법 2: 스펙 내용 직접 붙여넣기
```
이 스펙대로 Session Report Viewer PoC 앱을 만들어줘:
[session-report-viewer-spec.md 내용]
```

## gemify:craftify-poc 스킬 구현 시 고려사항

1. **입력**: library/product/ 또는 drafts/의 스펙 문서
2. **출력**: craftify가 이해할 수 있는 형식으로 변환
3. **위임**: craftify worktree/프로젝트에서 실행할 프롬프트 생성
4. **참고**: session-report-viewer가 첫 번째 사례가 될 예정
