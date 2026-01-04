---
title: "tidy/triage 스킬 설계 및 구현"
date: 2026-01-04
duration: ~2h
---

# 세션 리포트: tidy/triage 스킬 설계 및 구현

## Summary

gemify 플러그인에 tidy와 triage 스킬을 설계하고 구현 완료.

- **tidy**: 역방향 검증 (views ↔ artifact 일치 검사)
- **triage**: 순방향 정리 (inbox 클러스터링)
- **map**: 클러스터 맵 생성/관리 (triage에서 참조)

설계 과정에서 공통 프로토콜 필요성 발견 → 별도 subtask로 완성.

## Outputs

### ground-truth (설계 문서)

| 유형 | 파일 |
|------|------|
| library | `library/ai-automation/gemify-tidy-skill.md` |
| library | `library/ai-automation/gemify-triage-skill.md` |
| improve-plugin | `library/engineering/plugin-improvements/gemify-add-tidy-skill.md` |
| improve-plugin | `library/engineering/plugin-improvements/gemify-add-triage-skill.md` |
| drafts | `drafts/gemify-tidy.md` (status: set) |
| drafts | `drafts/gemify-triage.md` (status: set) |

### views 마이그레이션

5개 views에 artifact 필드 추가:
- forgeify.md → `artifact: plugins/forgeify/`
- gemify.md → `artifact: plugins/gemify/`
- namify.md → `artifact: plugins/namify/`
- terrafy.md → `artifact: plugins/terrafy/`
- craftify.md → `artifact: plugins/craftify/`

### gemify 플러그인 (구현)

| 파일 | 역할 |
|------|------|
| `skills/tidy/SKILL.md` | 역방향 검증 스킬 |
| `commands/tidy.md` | tidy 커맨드 |
| `skills/triage/SKILL.md` | 순방향 정리 스킬 |
| `commands/triage.md` | triage 커맨드 |
| `skills/map/SKILL.md` | 클러스터 맵 생성 스킬 |
| `commands/map.md` | map 커맨드 |

## Stashed for Next

### sidebar로 캡처한 것

| 파일 | 내용 |
|------|------|
| `inbox/materials/2026-01-04-tidy-triage-protocol-need.md` | 프로토콜 필요성 맥락 |
| `inbox/thoughts/2026-01-04-ground-truth-protocol-schema.md` | 스키마 제안 |

→ 별도 subtask로 `library/operations/ground-truth-protocol.md` 완성됨

## Key Decisions

1. **tidy 출력 포맷**: 하나씩 집중 (한 번에 하나의 불일치만)
2. **triage 출력 포맷**: 전체 리포트 후 선택
3. **map 분리**: 설계는 triage 내장이었으나, 구현에서 별도 스킬로 분리 (더 나은 관심사 분리)
4. **실행 순서**: tidy → triage (깨진 유리창 먼저 수리)
5. **클러스터 맵 저장**: `meta/cluster/current.md` + `.history/` 버전 관리

## Next Actions

- [ ] `meta/cluster/` 구조 실제 생성 (첫 triage 실행 시)
- [ ] tidy/triage 실제 사용 테스트
- [ ] SessionStart hook에서 triage 자동 호출 옵션 검토
