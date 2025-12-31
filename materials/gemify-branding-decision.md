# Gemify 브랜딩 의사결정 기록

> **Date**: 2025-01-02
> **Context**: Knowledge Pipeline 제품의 네이밍 및 브랜딩 결정
> **Status**: Decision Made
> **Final Decision**: Gemify

---

## 1. 발단 (Origin)

Knowledge Pipeline의 phase naming에서 시작:

```
[Input] → [Process] → [Storage]
```

초기 제안: **Seed → Grow → Digest** (식물 메타포)

**문제 발견**: "Digest"에서 메타포 깨짐 (식물은 소화하지 않음)

---

## 2. 의사결정 여정

### Phase 1: 메타포 일관성 문제

| 단어 | 출처 | 문제 |
|------|------|------|
| Seed | 🌱 식물 | ✅ |
| Grow | 🌱 식물 | ✅ |
| Digest | 🍽️ 소화 | ❌ 메타포 깨짐 |

### Phase 2: 대안 메타포 검토

#### Option A: 술/증류 메타포
```
Gather → Ferment → Distill
  🌾        🍺        🥃
```
- ✅ "정제/농축" 의미 정확
- ❌ 연령 제한 (중고등학생)
- ❌ 성별 편향 가능성

#### Option B: 광물/보석 메타포 ⭐ 선택
```
Rough → Refine → Gem
  🪨       ✨      💎
```
- ✅ 모든 연령 OK (Minecraft 세대 친숙)
- ✅ 성별 중립
- ✅ "정제/가치 상승" 의미 명확
- ✅ Tech 연결 (Data Mining)

### Phase 3: BFS/DFS 모드 네이밍

기존 식물 메타포:
- branch (BFS) - 가지치기
- ripen (DFS) - 익히기

광물 메타포로 전환:
- **facet** (BFS) - 여러 면 탐색
- **polish** (DFS) - 깊이 연마

### Phase 4: 제품화 관점 재검토

**문제**: 강한 메타포가 사용자 혼란 유발 가능

성공 제품 분석:
| 제품 | 폴더명 | 메타포 위치 |
|------|--------|-------------|
| Notion | Pages, Database | 없음 |
| Obsidian | Vault | 브랜딩만 |
| Linear | Issues, Projects | 없음 |

**결론**: 구조는 직관적으로, 메타포는 브랜딩에만

### Phase 5: 직관적 구조 확정

```
ground-truth/
├── inbox/      # 원재료 (모두 이해)
├── drafts/     # 작업 중 (모두 이해)
├── library/    # 완성된 지식 (모두 이해)
└── exports/    # 출력물
```

| 단어 | 일반인 | 크리에이터 | 개발자 | 연구자 | AI Agent |
|------|:------:|:----------:|:------:|:------:|:--------:|
| inbox | ✅ | ✅ | ✅ | ✅ | ✅ |
| drafts | ✅ | ✅ | ✅ | ✅ | ✅ |
| library | ✅ | ✅ | ✅ | ✅ | ✅ |

### Phase 6: 플러그인 이름 결정

| 후보 | 장점 | 단점 |
|------|------|------|
| Gem | 짧음 | Ruby Gem 혼동, 검색 어려움 |
| Gemify | "-ify" 패턴 (Shopify), 동사화 | - |
| GemCraft | Craft 트렌드 | 약간 길다 |
| MindGem | 직관적 | 평범 |

**최종 선택: Gemify**

---

## 3. 최종 결정

### 브랜드명
```
Gemify
```

### 태그라인
```
Turn your thoughts into gems.
```

또는:
```
Your thoughts deserve to shine.
```

### 핵심 메시지
> 너의 생각도 보석만큼 가치 있어. 정제하면.

### 폴더 구조
```
├── inbox/      # Capture (포착)
├── drafts/     # Develop (발전)
│   ├── facet   # BFS - 넓게 탐색
│   └── polish  # DFS - 깊이 연마
├── library/    # File (정리)
└── exports/    # 출력물
```

### 명령어
```
/capture    → inbox/
/develop    → drafts/
/file       → library/
```

---

## 4. 선택 이유 요약

| 기준 | 결정 | 이유 |
|------|------|------|
| 메타포 | 광물/보석 | 연령/성별 중립, 정제 의미 명확 |
| 구조 | inbox/drafts/library | 5개 타겟 그룹 전부 즉시 이해 |
| 이름 | Gemify | "-ify" 변환 패턴, 검색 구별, 행동 유도 |
| 태그라인 | Turn your thoughts into gems | 가치 + 변환 강조 |

---

## 5. 타겟 사용자

| 그룹 | 어필 포인트 |
|------|-------------|
| 일반인 | "생각 정리" |
| 크리에이터 | "아이디어 관리" |
| 개발자 | "지식 파이프라인" |
| 연구자 | "체계적 문서화" |
| AI Agents | "시맨틱하게 명확한 구조" |

---

## 6. 브랜딩 에셋

### 영문
```
Gemify
Turn your thoughts into gems.

Capture → Develop → Library
   📥        ✏️        📚

From rough ideas to polished knowledge.
```

### 한국어
```
Gemify
당신의 생각을 보석으로.

생각을 포착하고, 발전시키고, 정리하세요.
모든 아이디어는 원석입니다.
```

---

## 7. 기각된 대안들

| 대안 | 기각 이유 |
|------|----------|
| Seed → Grow → Digest | 메타포 깨짐 |
| Gather → Ferment → Distill | 연령/성별 편향 |
| ore/flux/refining (폴더명) | 너무 강한 메타포, 혼란 |
| corpus (폴더명) | 일반인에게 설명 필요 |
| Gem (이름) | Ruby Gem 혼동, 검색 어려움 |

---

## 8. 다음 단계

- [ ] 로고 디자인 (💎 심볼)
- [ ] 랜딩 페이지 카피
- [ ] README.md 업데이트
- [ ] CLAUDE.md 구조 반영

---

**Author**: Claude (with Choi)
**Decision Date**: 2025-01-02
