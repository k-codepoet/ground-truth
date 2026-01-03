---
title: "gemify:capture-pair 수동 호출 패턴 관찰"
date: 2026-01-03
source: "terrafy 플러그인 개발 세션"
type: document
status: raw
used_in: null
---

## 관찰된 패턴

플러그인 개발 중 오류 상황 발생 시:

1. 문제 발생 (plugin.json agents 필드 오류)
2. 문제 해결
3. 사용자가 수동으로 `/gemify:capture-pair` 호출
4. material + thought 저장

## 캡처 트리거가 될 수 있는 상황들

- 오류 발생 → 해결 → "이거 기록해둬야겠다"
- 의사결정 완료 → "나중에 참고해야 할 것 같아"
- 새로운 인사이트 발견 → "이거 중요하네"
- 반복되는 문제 패턴 발견 → "매번 이런다"

## 현재 워크플로우

```
사용자: [문제 해결 후] "gemify:capture-pair로 기록해줘"
Claude: [수동으로 material + thought 생성]
```

## 이상적인 워크플로우

```
[오류 해결 또는 의사결정 완료 감지]
Claude: "이 상황을 기록해두시겠어요? (capture-pair 제안)"
사용자: "응" 또는 자동 저장
```
