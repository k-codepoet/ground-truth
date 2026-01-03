---
title: "Terrafy 플러그인 맥락 (병렬 작업용)"
date: 2026-01-03
source: "/home/choigawoon/k-codepoet/my-claude-plugins/plugins/terrafy/"
type: document
status: raw
used_in:
---

## 플러그인 기본 정보

| 항목 | 값 |
|------|-----|
| 이름 | terrafy |
| 버전 | 1.0.0 |
| 태그라인 | "Lay the groundwork for your digital city" |
| 역할 | 인프라 자동화 플러그인 |

## -fy Trilogy 위치

| Plugin | Role | Question |
|--------|------|----------|
| Gemify | 지식/설계 | WHAT - 뭘 만들지 |
| **Terrafy** | 인프라 | WHERE - 어디서 돌릴지 |
| Craftify | 개발 | HOW - 어떻게 만들지 |

## 스킬 구조

### k3s
- 쿠버네티스(K3s) 환경 구축
- Pod 배포, Helm 차트 사용
- GitOps 설정 (ArgoCD)
- Linux Ubuntu 전용

### portainer
- Portainer 기반 컨테이너 관리
- Docker 스택 배포
- GitOps 연동
- Linux/macOS 지원

### terraform
- 클라우드 인프라 프로비저닝
- AWS, GCP, Azure 리소스 관리
- 상태: 준비 중

## 커맨드

| 커맨드 | 설명 |
|--------|------|
| `/terrafy:help` | 도움말 |
| `/terrafy:init` | 인프라 환경 초기화 |
| `/terrafy:status` | 현재 인프라 상태 확인 |

## 에이전트

- `infra-setup.md` - 인프라 구축 위저드

## Input → Output

```
Raw server IP → Ready-to-deploy cluster
"SSH 접속 가능" → "kubectl 동작, ArgoCD 접속 가능"
```

## 플랫폼 지원

| 플랫폼 | 지원 수준 |
|--------|----------|
| Linux Ubuntu | Primary (전체 기능) |
| macOS | Partial (Docker/Portainer) |
| Windows | Not Supported |

## 병렬 작업자 안내

이 파일을 읽고 다음 단계 진행:
1. `inbox/thoughts/2026-01-03-terrafy-plugin-purpose.md` 함께 참고
2. `/gemify:draft` 실행하여 drafts 생성
3. facet 모드로 스킬별 시나리오 탐색
4. polish 모드로 핵심 정리
5. `/gemify:library`로 library 저장 (domain: product)
6. `/gemify:view`로 terrafy.md 생성

## 참고 경로

플러그인 소스: `/home/choigawoon/k-codepoet/my-claude-plugins/plugins/terrafy/`
