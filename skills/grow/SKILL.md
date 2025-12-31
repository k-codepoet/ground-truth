---
name: grow
description: seed와 materials를 대화로 확장하여 growing/에 기록. "확장해줘", "brainstorm", "키워봐" 등 요청 시 활성화. 익으면 /digest 전환 제안.
license: MIT
compatibility: 이 프로젝트의 seed/, materials/, growing/, corpus/ 구조 필요
metadata:
  author: choigawoon
  version: "0.2"
allowed-tools: Read Write Edit
---

# Grow Skill

seed + materials를 **대화를 통해 확장**합니다.

## 입력 소스

```
seed/      ← 내 생각의 씨앗
materials/ ← 외부 재료
    ↓
growing/   ← 해체 → 재조립 → 응축
```

## 핵심 행동

### 1. 대화 파트너

**도전**: "왜 필요해?", "반대로 생각하면?"
**확장**: "연결되는 건?", "극단적으로 밀면?"
**구체화**: "예를 들면?", "첫 번째 단계가 뭐야?"

### 2. 누적 기록

모든 대화는 `growing/{slug}.md`에 축적. (상세: `references/growing-format.md`)

### 3. 소스 추적

seed/materials 사용 시:
- 해당 파일 `status` → `used`
- 해당 파일 `used_in` → growing 경로 기록

### 4. 성숙도 감지

다음 조건 시 digest 전환 제안:
- turns >= 5
- Open Questions 대부분 해결
- 같은 포인트 반복

## 세션 동작

| 시점 | 동작 |
|------|------|
| 시작 | growing/ 확인, 진행 중 목록 표시 |
| 대화 | 매 턴 업데이트, turns 증가, 성숙도 체크 |
| 종료 | 상태 요약, "/grow {파일명}" 안내 |

## 규칙

- 질문은 **하나씩 순차적으로**
- **강요 안 함** - digest는 사용자 수락 시만
- 이전 세션 맥락 이어감
- `_template.md` 제외
