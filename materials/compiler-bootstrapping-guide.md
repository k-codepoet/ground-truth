---
title: "Compiler Bootstrapping: The Art of Self-Creation"
date: 2025-01-02
source: "Claude 대화"
type: document
status: raw
used_in:
---

> **핵심 개념**: 컴파일러가 자기 자신을 컴파일할 수 있게 되는 순환적 구축 과정

---

## 1. Bootstrapping이란?

### 문제 정의

```
새로운 프로그래밍 언어 X를 만들었다.
    ↓
X 컴파일러를 X로 작성하고 싶다 (X의 모든 기능 활용)
    ↓
하지만 X 컴파일러가 없으면 X 코드를 실행할 수 없다
    ↓
닭이 먼저? 달걀이 먼저? 🐔🥚
```

### 해결 전략

```
Phase 0: 다른 언어로 "임시" 컴파일러 v0.1 작성
    ↓
Phase 1: v0.1로 X로 짠 "진짜" 컴파일러 v1.0 컴파일
    ↓
Phase 2: v1.0으로 v1.1 컴파일 (self-hosting)
    ↓
Phase 3: 임시 컴파일러(v0.1) 폐기
```

---

## 2. 역사적 사례

### 2.1 C 컴파일러 (1970s) - 전설의 시작

**배경**: Dennis Ritchie가 UNIX 개발을 위해 C 언어 설계

```
1970: B 언어 존재 (C의 전신)
    ↓
1971-1972: B로 간단한 C 컴파일러 작성
    ↓
1973: C로 작성된 새 C 컴파일러 컴파일 성공
    ↓
1973년 후반: C 컴파일러가 자기 자신을 컴파일 (self-hosting 달성)
    ↓
결과: B 언어 폐기, C로만 개발 진행
```

**왜 중요한가**:
- 어셈블리로 C 컴파일러 전체를 짜기엔 너무 복잡
- B는 C의 간단한 버전이라 빠르게 작성 가능
- 일단 C 컴파일러가 생기면 C의 모든 고급 기능 활용 가능

**실제 코드 예시**:
```c
// 초기 C 컴파일러 (B로 작성됨)
// B 문법으로 간단한 C 기능만 지원

// 이후 C 컴파일러 (C로 작성됨)
// 포인터, 구조체, 전처리기 등 모든 기능 활용
int main(int argc, char **argv) {
    // 이제 C의 모든 기능 사용 가능
}
```

---

### 2.2 Rust 컴파일러 (2010s) - 현대적 사례

**타임라인**:

| 시기 | 단계 | 사용 언어 | 상태 |
|------|------|----------|------|
| 2006-2010 | rustboot | OCaml | 최초 컴파일러 |
| 2010-2011 | rustc v0.1 | OCaml | 기본 기능 완성 |
| 2011년 4월 | rustc v0.2 | Rust | **Self-hosting 달성** |
| 2011-현재 | rustc | Rust | 지속 개발 |

**왜 OCaml을 선택했나**:
- 강력한 타입 시스템 (Rust와 철학 유사)
- 패턴 매칭 (컴파일러 구현에 유용)
- 함수형 프로그래밍 (AST 변환에 적합)

**Self-hosting 달성 순간** (2011년 4월):
```bash
# OCaml 컴파일러로 Rust 소스 컴파일
$ rustc_ocaml rustc.rs -o rustc_rust

# 이제 Rust 컴파일러가 자기 자신을 컴파일!
$ rustc_rust rustc.rs -o rustc_next

# OCaml 버전은 이제 필요없음
$ rm -rf rustboot/
```

**공식 발표**:
> "The Rust compiler is now self-hosting. This is a major milestone."
> - Rust Blog, April 2011

---

### 2.3 Go 컴파일러 (2015) - 점진적 전환

**배경**: Google이 개발한 Go 언어

```
2007-2009: C로 Go 컴파일러 설계 및 구현
    ↓
2009-2014: C로 작성된 gc 컴파일러 사용 (6g, 8g, 5g)
    ↓
2014: Go로 Go 컴파일러 재작성 프로젝트 시작
    ↓
2015년 8월: Go 1.5 릴리스 (완전한 Go 구현)
    ↓
현재: Go 컴파일러는 100% Go로 작성됨
```

**흥미로운 점**:
- 5년간 C 버전 사용 (안정성 우선)
- C→Go 변환 도구 사용 (자동 변환 후 수동 정리)
- GC(Garbage Collector)도 Go로 재작성

**Go 1.5 릴리스 노트**:
```
The compiler and runtime are now implemented in Go and assembler,
without C. The only C source left in the tree is related to testing
or to cgo.
```

---

### 2.4 Python (PyPy) - 특별한 케이스

**전통적 CPython**:
- C로 작성된 Python 인터프리터
- Self-hosting 아님 (C 의존)

**PyPy의 시도**:
```
Python으로 Python 인터프리터 작성 (RPython)
    ↓
RPython → C 변환기 (Translation Toolchain)
    ↓
C 컴파일러로 최종 바이너리 생성
    ↓
결과: Python으로 짠 인터프리터가 CPython보다 빠름!
```

**Meta-level Bootstrapping**:
- Python으로 Python을 실행하는 Python을 만듦
- 3단계 메타 레벨 (mind-bending!)

---

## 3. Three-Stage Bootstrap - 검증 방법

### 개념

자기 자신을 컴파일하는 것만으론 부족. **동일성 검증** 필요.

### 과정

```bash
# Stage 1: 기존(신뢰할 수 있는) 컴파일러로 새 소스 컴파일
$ old_compiler new_compiler_source.c -o compiler_v1

# Stage 2: 새 컴파일러로 자기 소스 컴파일
$ ./compiler_v1 new_compiler_source.c -o compiler_v2

# Stage 3: Stage 2 결과물로 한 번 더
$ ./compiler_v2 new_compiler_source.c -o compiler_v3

# 검증: 바이너리 완전 동일해야 함
$ diff compiler_v2 compiler_v3
# (아무 출력 없음 = 성공)
```

### 왜 3단계인가?

| Stage | 목적 | 검증 대상 |
|-------|------|----------|
| 1 | 새 컴파일러 생성 | 소스 코드 정확성 |
| 2 | Self-compilation | 컴파일러 자체 일관성 |
| 3 | 재현성 검증 | **결정론적 동작** |

**Stage 2 ≠ Stage 3인 경우**:
- Non-deterministic 코드 생성
- 타임스탬프나 랜덤 값 포함
- 버그 존재 (심각!)

### 실제 사용 예시 (GCC)

```bash
# GCC 빌드 시스템이 자동으로 수행
$ make bootstrap

# 내부적으로:
# 1. 시스템 컴파일러로 stage1 빌드
# 2. stage1으로 stage2 빌드  
# 3. stage2로 stage3 빌드
# 4. stage2 == stage3 검증
```

---

## 4. Trust Issues - Ken Thompson의 경고

### "Reflections on Trusting Trust" (1984)

**문제**: Self-hosting 컴파일러에 백도어를 숨길 수 있다.

```c
// 악의적인 컴파일러 코드
if (compiling_login_program) {
    inject_backdoor();  // 비밀번호 검증 우회
}

if (compiling_compiler) {
    inject_this_same_code();  // 자기 복제!
}
```

**결과**:
```
1. 악의적 컴파일러 A로 정상 소스 컴파일
    ↓
2. 생성된 바이너리 B도 악의적
    ↓
3. B로 다시 컴파일해도 악의적 C 생성
    ↓
소스 코드를 아무리 봐도 백도어 없음!
```

**해결책**:
- Diverse Double-Compiling (DDC)
- Reproducible Builds
- Multiple independent implementations

---

## 5. Cross-Compilation Bootstrapping

### 시나리오: Mac에서 Linux용 컴파일러 만들기

```
Phase 1: Mac 네이티브 컴파일러 준비
    ↓
Phase 2: Linux 타겟 크로스 컴파일러 생성
    ↓
Phase 3: 크로스 컴파일러로 Linux 네이티브 컴파일러 빌드
    ↓
Phase 4: Linux에 복사하여 self-hosting
```

**실제 명령어**:
```bash
# Mac에서
$ gcc -target=x86_64-linux new_compiler.c -o cross_compiler

# Linux 네이티브 컴파일러 생성
$ ./cross_compiler new_compiler.c -o linux_compiler

# Linux로 전송
$ scp linux_compiler linux-machine:/tmp/

# Linux에서 self-hosting
$ ssh linux-machine
$ /tmp/linux_compiler new_compiler.c -o native_compiler
$ ./native_compiler new_compiler.c -o next_gen
$ diff native_compiler next_gen  # 검증
```

---

## 6. Knowledge-ops와의 비교

### 구조적 유사성

| 측면 | Compiler Bootstrapping | Knowledge-ops Bootstrapping |
|------|----------------------|---------------------------|
| **순환 문제** | X 컴파일러를 X로 짜려면<br>X 컴파일러가 필요 | 지식 시스템을 만드는 방법을<br>지식 시스템으로 문서화하려면... |
| **임시 도구** | C, OCaml 등으로<br>v0.1 작성 | 수동으로<br>knowledge-ops 초안 작성 |
| **Self-hosting** | X 컴파일러가<br>자기 자신을 컴파일 | knowledge-ops로<br>knowledge-ops 문서화 |
| **검증** | 3-stage bootstrap<br>(바이너리 동일성) | Phase 2:<br>"이 시스템으로 만들었다" 증명 |
| **폐기** | 임시 컴파일러 삭제 | 수동 과정은<br>자동화로 대체 |
| **확장** | 이제 모든 X 프로그램<br>컴파일 가능 | 이제 모든 topic에<br>시스템 적용 가능 |

### 철학적 유사성

**Compiler**:
> "The compiler is now written in the language it compiles."

**Knowledge-ops**:
> "The knowledge system is now documented using the knowledge system."

둘 다 **Self-reference의 힘**을 활용:
- 자기 자신을 설명할 수 있으면 → 완전하다
- 자기 자신에게 적용 가능하면 → 일반화 가능하다

---

## 7. 현대적 도구들의 Bootstrapping

### 7.1 LLVM/Clang

```
Phase 1: GCC로 LLVM 컴파일
    ↓
Phase 2: LLVM으로 Clang 컴파일
    ↓
Phase 3: Clang으로 LLVM + Clang 재컴파일 (self-hosting)
    ↓
현재: Clang이 자기 자신과 LLVM 컴파일
```

### 7.2 Swift

```
2010-2014: C++로 Swift 컴파일러 작성
    ↓
2015: Swift로 재작성 시작
    ↓
2019: Swift 컴파일러 100% Swift로 전환
```

### 7.3 Zig

```
현재: C++로 작성 (Stage 0)
계획: Zig로 재작성하여 self-hosting
목표: 컴파일러도 Zig의 zero-cost abstractions 활용
```

---

## 8. Bootstrapping 패턴 정리

### Pattern 1: Language Evolution

```
Simple Language → Complex Language → Self-hosting

예: B → C → Self-hosting C Compiler
```

### Pattern 2: External Language

```
Established Language → New Language → Self-hosting

예: OCaml → Rust → Self-hosting Rust Compiler
```

### Pattern 3: Gradual Migration

```
Legacy Language → Mixed → Full New Language

예: C → C+Go → Pure Go (Go 1.5)
```

### Pattern 4: Meta-circular

```
Language A → Intermediate → Back to A

예: Python → RPython → PyPy (runs Python)
```

---

## 9. 실용적 교훈

### For Compiler Developers

1. **Start Simple**: 완벽한 v0.1보다 작동하는 v0.1이 낫다
2. **Choose Your Bootstrap Language Wisely**: 
   - 철학이 유사한 언어 (Rust ← OCaml)
   - 강력한 도구 지원 (대부분 C 선택)
3. **Plan for Migration**: Self-hosting을 염두에 두고 설계
4. **Verify Rigorously**: 3-stage bootstrap은 필수

### For Knowledge System Builders

1. **Start Manual**: 자동화보다 구조 먼저
2. **Use It on Itself**: Phase 2에서 self-documentation
3. **Validate Early**: 다른 topic에 빨리 적용 (Phase 3)
4. **Avoid Infinite Meta**: 시간 제한 두기

---

## 10. 타임라인 비교

```
1970s: C Compiler Bootstrapping (1-2년)
        수동 작업, 소규모 팀
            ↓
2010s: Rust Compiler Bootstrapping (5년)
        체계적 계획, 커뮤니티 참여
            ↓
2020s: Knowledge-ops Bootstrapping (목표: 1-2주)
        AI 활용, 1인 작업
```

**가속화 요인**:
- AI가 패턴 인식 및 자동화 지원
- 풍부한 선례 (컴파일러 역사)
- 도구 성숙도 (Git, CI/CD, 클라우드)

---

## 11. 결론: Bootstrapping의 본질

### 핵심 통찰

> **Bootstrapping은 순환이 아니라 나선이다.**
> 
> 같은 곳으로 돌아오는 것처럼 보이지만,
> 매번 한 단계 높은 수준에 도달한다.

```
v0.1 (다른 도구로 제작)
    ↓
v1.0 (자기 언어로 제작, v0.1로 컴파일)
    ↓
v1.1 (자기 언어로 제작, v1.0으로 컴파일)
    ↓
v1.2 (자기 언어로 제작, v1.1로 컴파일)
    ↓
...나선형 발전
```

### 왜 중요한가?

1. **Independence**: 외부 도구 의존성 제거
2. **Dog-fooding**: 자기 언어의 모든 기능 활용
3. **Validation**: Self-hosting = 완전성 증명
4. **Evolution**: 이제부터 빠른 개선 가능

### Knowledge-ops에 주는 교훈

```yaml
Phase 1: Manual work (수동으로 시스템 구축)
  → "작동하는 것"에 집중
  
Phase 2: Self-documentation (시스템으로 시스템 설명)
  → "완전성" 증명
  
Phase 3: Application (다른 topic에 적용)
  → "일반화 가능성" 검증
  
Phase 4+: Continuous improvement (나선형 발전)
  → 이제부터가 진짜 시작
```

---

## 12. 참고 자료

### 논문
- Thompson, Ken. "Reflections on Trusting Trust." 1984
- Wheeler, David A. "Countering Trusting Trust through Diverse Double-Compiling." 2009

### 블로그 & 문서
- [Rust Blog: Rust's Self-hosting](https://blog.rust-lang.org/)
- [Go Blog: Go 1.5 Compiler](https://go.dev/blog/go1.5)
- [GCC Bootstrapping Manual](https://gcc.gnu.org/install/)

### 책
- "Engineering a Compiler" - Keith Cooper & Linda Torczon
- "Compilers: Principles, Techniques, and Tools" - Aho, Lam, Sethi, Ullman (Dragon Book)

---

**작성**: Claude (inspired by Choi's question)  
**날짜**: 2025-01-02  
**라이선스**: CC BY-SA 4.0

---

## Appendix: Quick Reference

### Bootstrapping Checklist

- [ ] Phase 0: Choose bootstrap language
- [ ] Phase 1: Build minimal compiler
- [ ] Phase 2: Rewrite in target language
- [ ] Phase 3: Self-compile successfully
- [ ] Phase 4: Three-stage bootstrap verification
- [ ] Phase 5: Retire bootstrap compiler
- [ ] Phase 6: Continuous improvement

### Common Pitfalls

| 문제 | 증상 | 해결 |
|------|------|------|
| Over-engineering v0.1 | 진도 안 나감 | 최소 기능만 |
| Skipping validation | 미묘한 버그 | 3-stage 필수 |
| Infinite meta-work | 실제 사용 안 함 | 시간 제한 |
| Poor documentation | 다음 사람 막막 | 과정 기록 |

### Success Metrics

| Metric | Target |
|--------|--------|
| Self-compilation time | < 2x manual |
| Binary reproducibility | 100% (3-stage) |
| Bootstrap language LOC | Trending to 0 |
| Community adoption | Growing |
