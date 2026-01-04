---
title: "Namify Plugin 스펙"
type: spec
origin: original
views: [namify]
---

## Context

제품/서비스 네이밍을 도와주는 Claude Code 플러그인. 이름 만드는 과정이 메타포, 검증, 태그라인을 모두 포괄한다.

## Content

### 플러그인 정보

```yaml
Name: Namify
Tagline: "Name it right"
Role: 제품/서비스 이름 생성
```

### 핵심 스킬

```
/name [제품 설명]                    # 기본 이름 생성
/name [제품 설명] --pattern "-ify"   # 특정 패턴 적용
/name [제품 설명] --series "Gemify"  # 시리즈 일관성 유지
```

### 동작 흐름

```
1. 제품 핵심 가치 추출
2. 메타포 후보 탐색
3. 이름 생성 (사용자 패턴 반영)
4. 간단 검증 (발음, 기존 의미)
5. 추천 + 이유
```

### 사용 예시

```
/name "생각을 정제해서 지식으로 만드는 도구"
→ 메타포: 광물(gem), 증류(distill), 연금술(alchemy)
→ 후보: Gemify, Distillery, Alchemist
→ 검증: 발음 OK, 상표 확인 필요
→ 추천: Gemify (-ify 패턴, 변환 의미 명확)

/name "인프라 자동화 도구" --series "Gemify"
→ 패턴 인식: -ify
→ 후보: Terrafy, Infrafy, Provify
→ 추천: Terrafy (Terra=땅/기반, 인프라와 연결)
```

### 프레임워크 기반

- 브랜드 레이어 vs UX 레이어 분리
- 메타포 선택 5단계 프로세스
- 문화적 검증 체크리스트
- 안티패턴 회피

### 참고 사례

**-ify Trilogy**:
- Gemify (WHAT) - 지식/설계
- Terrafy (WHERE) - 인프라
- Craftify (HOW) - 개발

## Connections

- [제품 네이밍 프레임워크](../../inbox/materials/product-naming-branding-framework.md)
- [AI Company Trilogy](../../inbox/materials/2026-01-03-ai-company-trilogy-naming.md)
- [Gemify 브랜딩 의사결정](../decisions/gemify-branding-decision.md)
