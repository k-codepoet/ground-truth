---
title: Claude Code 플러그인 종속성 관리 체계 설계
created: 2026-01-03
updated: 2026-01-03
turns: 1
revision: 1
status: cutting
sources:
  - inbox/thoughts/2026-01-03-plugin-version-dependency-research.md
history: []
---

# Claude Code 플러그인 종속성 관리 체계

## 핵심 문제

현재 Claude Code 플러그인 시스템은 **npm/pip 수준의 종속성 관리가 없음**.
- 플러그인 A가 플러그인 B@1.0을 필요로 해도 명시할 방법 없음
- 설치 시 항상 최신 버전만 가져옴
- 버전 충돌 시 해결 메커니즘 없음

## 현재 구조 분석

| 파일 | 역할 | 종속성 지원 |
|------|------|-----------|
| plugin.json | 플러그인 메타데이터 | version만 있음, dependencies 없음 |
| marketplace.json | 마켓플레이스 목록 | 일부만 version, dependencies 없음 |
| installed_plugins.json | 설치된 플러그인 추적 | version+SHA, 종속성 그래프 없음 |

## 제안: 3단계 접근

### Phase 1: 스키마 확장 (우리가 할 수 있는 것)
- plugin.json에 `dependencies`, `peerDependencies` 필드 추가
- marketplace.json에 버전 명시 의무화
- semver 기반 버전 범위 표기 (`^1.0.0`, `>=1.0.0 <2.0.0`)

### Phase 2: 도구 지원 (forgeify 확장)
- `/forgeify:validate`에서 종속성 검증 추가
- 설치 전 종속성 트리 시각화

### Phase 3: 커뮤니티/공식 지원 요청
- Claude Code 팀에 RFC 제출
- 설치 로직에 종속성 해결 포함 요청

---

## 중단 사유 (2026-01-03)

**결론: 지금 하지 않는다.**

- 실제 문제 발생한 적 없음
- 현재 사용자는 나 혼자
- 미래 걱정으로 시작한 작업 → YAGNI 원칙 위반

**재개 조건:**
- 실제로 버전/종속성 문제가 발생했을 때
- 다른 사용자가 생겨서 배포가 필요할 때

---

## Open Questions (나중에 참고)

1. **범위**: 지금 당장 우리 플러그인에만 적용할지, 표준 제안까지 갈지?
2. **호환성**: 기존 플러그인과의 하위 호환성 유지 방법?
3. **실제 필요성**: gemify→forgeify 외에 실제로 어떤 종속성이 있나?
4. **우선순위**: 이게 지금 가장 급한 문제인가?

---

## Facets to Explore (나중에 참고)

- [ ] 실제 사용 시나리오에서 종속성 문제 경험?
- [ ] 다른 플러그인 시스템(VSCode, JetBrains) 참고?
- [ ] 최소한의 구현으로 시작할 수 있는 방법?
