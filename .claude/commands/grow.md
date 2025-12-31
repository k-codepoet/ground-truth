---
description: seed와 materials를 합쳐 대화로 확장 (expand/brew/brainstorm 통합)
arguments:
  - name: input
    description: seed 파일, materials 파일, growing 파일, 또는 새 아이디어
    required: false
---

# /grow - 생각 확장 커맨드

grow 스킬로 아이디어를 대화로 확장한다.

## 사용법

```
/grow                        # growing/ 목록 또는 새 시작
/grow "이런 생각이 있어..."    # 새 씨앗으로 시작
/grow growing/my-idea.md     # 기존 이어가기
/grow seed/my-seed.md        # seed에서 시작
/grow materials/article.md   # material과 함께 시작
```

## 입력 소스

```
seed/      ← 내 생각의 씨앗
materials/ ← 외부 재료 (기사, 문서, 대화 등)
    ↓
growing/   ← 둘이 만나서 해체 → 재조립 → 응축
```

## 동작

1. $ARGUMENTS 없으면 → growing/ 폴더의 파일 목록 표시 후 선택 또는 새 시작
2. 따옴표로 감싼 문자열이면 → 새 씨앗으로 growing/ 파일 생성 후 대화 시작
3. 파일 경로면 → 해당 파일 읽고 이어가기 (seed/, materials/, growing/ 모두 가능)

## 세 가지 모드 (자동 전환)

대화 흐름에 따라 Claude가 자연스럽게 모드 전환:

- **expand**: 아이디어를 넓히는 데 집중 ("연결되는 건?", "더 큰 그림에서?")
- **brew**: 아이디어를 깊이 숙성 ("왜 이게 중요해?", "핵심이 뭐야?")
- **brainstorm**: 제약 없이 자유롭게 ("미친 아이디어라면?", "반대로 하면?")

## 종료 조건

1. 사용자 선언: "digest 해줘", "정리하자", "이 정도면 됐어"
2. Claude 제안 수락: 성숙도 감지 후 "digest 해볼까?" → 사용자 OK
3. 세션 종료: 자동 저장, 다음에 `/grow 파일명`으로 이어가기

## digest 전환

```
사용자: "digest 해줘" 또는 "정리하자"
→ Claude: /digest 워크플로우 호출 (growing → corpus 직접 처리)
```
