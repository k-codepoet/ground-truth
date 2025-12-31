# 실전 워크플로우

이 문서는 Claude Code 생태계의 핵심 요소들을 실제로 만들어보는 실습 가이드입니다.

## 1. Skill 만들기

```bash
mkdir pdf-processor
cd pdf-processor
```

**SKILL.md 작성:**

```markdown
---
name: pdf-processor
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF documents.
license: MIT
---

# PDF Processor

[지침 내용...]
```

```bash
# 검증
skills-ref validate ./pdf-processor
```

## 2. Plugin으로 패키징

```bash
mkdir my-plugin
cd my-plugin

# 디렉토리 구조 생성
mkdir -p .claude-plugin skills commands scripts
```

**.claude-plugin/plugin.json 작성:**

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "My custom plugin",
  "author": { "name": "Your Name" }
}
```

```bash
# Skill 복사
cp -r ../pdf-processor skills/

# Git 저장소로 만들기
git init
git add .
git commit -m "Initial plugin"
```

## 3. Marketplace 만들기

```bash
mkdir my-marketplace
cd my-marketplace

# 구조 생성
mkdir -p .claude-plugin plugins
```

**.claude-plugin/marketplace.json 작성:**

```json
{
  "name": "my-marketplace",
  "owner": { "name": "your-name" },
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./plugins/my-plugin",
      "description": "My custom plugin"
    }
  ]
}
```

```bash
# 플러그인을 서브모듈로 추가 (또는 직접 복사)
git submodule add https://github.com/your-name/my-plugin plugins/my-plugin

# GitHub에 푸시
git init
git add .
git commit -m "Initial marketplace"
git remote add origin https://github.com/your-name/my-marketplace
git push -u origin main
```

## 4. 마켓플레이스 사용

```bash
# Claude Code에서
/plugin marketplace add your-name/my-marketplace
/plugin install my-plugin@my-marketplace
```

## 참고

- [메인 가이드로 돌아가기](./README.md)
- [Skills](./skills.md) - Skill 작성 상세 가이드
- [Plugin](./plugin.md) - Plugin 구조 상세 가이드
- [Marketplace](./marketplace.md) - Marketplace 설정 상세 가이드
