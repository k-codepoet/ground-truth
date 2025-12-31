# 지식 파이프라인 구조 개선 대화

> 날짜: 2025-12-31
> 출처: /grow 세션
> 유형: conversation

---

## 발단

inbox/2025-12-31-knowledge-pipeline-naming-confusion.md에서 시작.
- `/seed` 명령어가 `inbox/`로 저장되는 명명 불일치 문제 제기

## 핵심 발견

### 1. seed vs 외부 재료 분리

**문제**: inbox에 두 종류가 섞여 있었음
- 내 생각의 씨앗 (진짜 seed)
- 외부 재료 (INFRA-SETUP, learn-nexon 같은 이미 정리된 문서)

**통찰**:
> "seed는 진짜 막 떠오른 생각. 기존 정리된 내용도 새로운 생각을 만나면 해체분석되서 재조립될 수 있음. 반복하다 보면 밀도 있는 지식이 됨."

### 2. 새로운 구조 도출

```
seed/      ← 내 생각의 씨앗 (/seed)
materials/ ← 외부 재료 (/import - 나중에)
    ↓
growing/   ← 둘이 만나서 섞이는 곳 (/grow)
    ↓
corpus/    ← 밀도 있는 지식 (/digest)
```

### 3. 참조 패턴

seed가 material을 참조하는 구조:
```
seed: "/import 명령어 필요"
  └─ references: materials/2025-12-31-knowledge-pipeline-structure-grow.md
```

## 결정 사항

1. `seed/` 폴더 생성 (inbox 대신)
2. `materials/` 폴더 생성 (외부 재료용)
3. `/import` 명령어는 나중에 구현
4. 기존 inbox 파일들을 materials로 이동

## 열린 질문

- [ ] `/import` 명령어 설계 (나중에)
- [ ] growing에서 seed + materials 합치는 방식 구체화
