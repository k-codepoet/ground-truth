---
title: Terrafy 플러그인 스펙
type: spec
origin: original
views: [terrafy]
---

## Context

AI Company 구축을 위한 -fy Trilogy에서 인프라 자동화 담당이 필요함. 코드를 배포하려면 인프라가 먼저 있어야 하는데, 이 부분을 자동화하는 도구가 없었음.

## Decision

### Terrafy의 역할

-fy Trilogy에서 **WHERE(어디서 돌릴지)**를 담당하는 인프라 자동화 플러그인.

| 플러그인 | 역할 | 핵심 질문 |
|---------|------|----------|
| Gemify | WHAT | 뭘 만들지 |
| **Terrafy** | **WHERE** | **어디서 돌릴지** |
| Craftify | HOW | 어떻게 만들지 |

### 도시 메타포

```
마스터플랜 (Gemify) - 설계
    ↓
인프라 공사 (Terrafy) - 도로, 전기, 수도  ← 이것
    ↓
건물 시공 (Craftify) - 주거지, 상업지, 공장
    ↓
살아있는 도시 (Live Services)
```

### 기능 범위

**Phase 1+2 (현재 목표):**
- 클러스터 설치 (K3s, Docker 등)
- 네트워크 설정

**Phase 3 (향후):**
- GitOps 연동

### 기술 스택

**내부 레이어 (Reverse Proxy):**
- Traefik
- Nginx
- Caddy

**외부 연결 (Tunnel/DNS):**
- Cloudflare Tunnel
- External DNS

**네트워크 전략:**
- VPN/내부망으로 격리
- 외부 공인망에 선택적 노출

### 사용자 워크플로우

```
1. 서버 IP 입력
2. 옵션 선택 (프록시: traefik/nginx/caddy, 터널: cloudflare/external-dns)
3. Terrafy 실행 → 배포 가능한 클러스터 완성
```

### 태그라인

> "Lay the groundwork for your digital city"

## Outcome

- 서버 IP만 있으면 배포 가능한 클러스터로 변환
- Craftify(GitOps)와의 경계 명확화: 인프라까지 Terrafy, 배포부터 Craftify
- 내부망 격리 + 외부 노출의 유연한 전략 지원

## References

- library/decisions/ify-trilogy-strategy.md
- library/specs/craftify-plugin-design.md
