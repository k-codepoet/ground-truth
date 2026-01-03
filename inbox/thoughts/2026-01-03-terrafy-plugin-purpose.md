---
title: "Terrafy - -fy Trilogy의 WHERE 담당"
date: 2026-01-03
references:
  - library/product/ify-trilogy-strategy.md
status: raw
used_in:
---

## 핵심 아이디어

Terrafy는 -fy Trilogy에서 **WHERE(어디서 돌릴지)**를 담당하는 인프라 자동화 플러그인.

## 왜 필요한가

AI Company를 만들려면 세 가지가 필요:
1. 뭘 만들지 결정 (Gemify - WHAT)
2. 어디서 돌릴지 준비 (Terrafy - WHERE) ← 이것
3. 어떻게 만들지 실행 (Craftify - HOW)

코드를 배포하려면 인프라가 먼저 있어야 함. 서버 IP만 있으면 배포 가능한 클러스터로 변환해주는 도구.

## 도시 메타포에서의 역할

```
마스터플랜 (Gemify) - 설계
    ↓
인프라 공사 (Terrafy) - 도로, 전기, 수도  ← 이것
    ↓
건물 시공 (Craftify) - 주거지, 상업지, 공장
    ↓
살아있는 도시 (Live Services)
```

건물을 짓기 전에 도로와 전기, 수도가 먼저 깔려야 하듯이.

## 태그라인

> "Lay the groundwork for your digital city"

## 다음 단계

- 플러그인 README와 plugin.json 정보를 materials에 정리
- `/gemify:draft`로 스펙 확장
- view 생성하여 Trilogy 연결
