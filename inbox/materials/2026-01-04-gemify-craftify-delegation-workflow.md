---
title: Gemify → Craftify 위임 워크플로우 세션
date: 2026-01-04
source: Tetritime 프로젝트 시작 세션
type: conversation
status: raw
---

# Gemify → Craftify 위임 워크플로우 세션

## 실행된 워크플로우

Tetritime 프로젝트를 시작하면서 실제로 수행한 단계:

### Step 1: triage로 시작점 찾기
```
/gemify:triage 초등학교 딸아이 시간표앱 개발 시작하고 싶어
```
- inbox 클러스터링
- 관련 기존 자료 발견 (materials, thoughts)
- 다음 액션 제안

### Step 2: draft로 아이디어 구체화
```
/gemify:draft yunseul-schedule-build-plan
```
- inbox → drafts 이동
- facet 모드로 대화하며 구체화
- 기술스택, 배포환경 결정 (Cloudflare Pages, SSR)

### Step 3: namify:name으로 제품명 결정
```
/namify:name 초등학교 시간표 앱 - 방과후 스케줄링
```
- 메타포 탐색 (테트리스)
- 이름 후보 생성
- **Tetritime** 확정

### Step 4: view subject로 서사 구조
```
/gemify:view subject tetritime
```
- 문제 → 해결책 → 여정 구조화
- views/by-subject/tetritime.md 생성

### Step 5: 프로젝트 폴더 셋업
```
mkdir -p /path/to/products/tetritime
# WORK.md 생성 (작업 계획 문서)
git init && git commit
```
- Craftify가 바로 작업 시작할 수 있는 상태

### Step 6: library에 spec 저장
```
/gemify:library
```
- drafts → library/specs/ 이동
- draft status를 `set`으로 변경

## 위임 결과물

| 파일 | 역할 |
|------|------|
| `WORK.md` (프로젝트 폴더) | Craftify 작업 지시서 |
| `library/specs/tetritime-work-spec.md` | 영구 보관용 스펙 |
| `views/by-subject/tetritime.md` | 프로젝트 서사/컨텍스트 |

## 핵심 패턴

**Gemify의 역할**: 지식 생산 (what to build)
**Craftify의 역할**: 실행 (how to build)

위임 인터페이스 = `WORK.md` (작업 지시서)
