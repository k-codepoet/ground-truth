---
description: inbox 파일을 소화시켜 corpus로 분류/저장
arguments:
  - name: file
    description: inbox 파일 경로 (예: inbox/INFRA-SETUP.md)
    required: false
---

# /digest - 지식 소화 커맨드

knowledge-digest 스킬을 사용하여 inbox 파일을 처리한다.

## 사용법

```
/digest                      # inbox 목록 보여주고 선택
/digest inbox/파일명.md      # 특정 파일 처리
```

## 동작

1. $ARGUMENTS가 있으면 해당 파일 처리
2. 없으면 inbox 폴더의 파일 목록 표시 후 선택 요청
3. knowledge-digest 스킬의 워크플로우 실행
