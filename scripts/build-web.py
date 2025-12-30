#!/usr/bin/env python3
"""
build-web.py - corpus에서 인터랙티브 웹앱 빌드

Usage:
    python scripts/build-web.py [--topic <topic>] [--all]

Flow:
    1. corpus/{topic}/ 읽기
    2. structure/, content/, demos/, i18n/ 파싱
    3. React 템플릿 기반으로 exports/web/{topic}/ 생성
    4. 데모 컴포넌트 스캐폴딩
"""

import os
import sys
import yaml
import json
import shutil
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).parent.parent
CORPUS_DIR = REPO_ROOT / "corpus"
EXPORTS_DIR = REPO_ROOT / "exports" / "web"

# 템플릿 경로 (추후 별도 템플릿 레포에서 가져올 수 있음)
TEMPLATE_DIR = REPO_ROOT / "templates" / "web-interactive"


def load_topic(topic: str) -> dict:
    """토픽 메타데이터 로드"""
    topic_dir = CORPUS_DIR / topic
    
    if not topic_dir.exists():
        raise ValueError(f"Topic not found: {topic}")
    
    with open(topic_dir / "topic.yaml", "r", encoding="utf-8") as f:
        topic_meta = yaml.safe_load(f)
    
    return topic_meta


def load_structure(topic: str) -> dict:
    """토픽 구조 로드"""
    structure_dir = CORPUS_DIR / topic / "structure"
    
    result = {}
    
    # layers.yaml
    layers_path = structure_dir / "layers.yaml"
    if layers_path.exists():
        with open(layers_path, "r", encoding="utf-8") as f:
            result["layers"] = yaml.safe_load(f)
    
    # graph.json
    graph_path = structure_dir / "graph.json"
    if graph_path.exists():
        with open(graph_path, "r", encoding="utf-8") as f:
            result["graph"] = json.load(f)
    
    return result


def load_content(topic: str) -> dict:
    """토픽 컨텐츠 로드"""
    content_dir = CORPUS_DIR / topic / "content"
    
    result = {"cases": [], "fundamentals": [], "decisions": []}
    
    for layer in ["cases", "fundamentals", "decisions"]:
        layer_dir = content_dir / layer
        if layer_dir.exists():
            for f in layer_dir.glob("*.mdx"):
                if not f.name.startswith("_"):
                    result[layer].append({
                        "id": f.stem,
                        "path": str(f.relative_to(REPO_ROOT))
                    })
    
    return result


def load_demos(topic: str) -> list:
    """토픽 데모 로드"""
    demos_dir = CORPUS_DIR / topic / "demos"
    
    result = []
    if demos_dir.exists():
        for demo_dir in demos_dir.iterdir():
            if demo_dir.is_dir():
                spec_path = demo_dir / "spec.yaml"
                if spec_path.exists():
                    with open(spec_path, "r", encoding="utf-8") as f:
                        spec = yaml.safe_load(f)
                    result.append(spec)
    
    return result


def load_i18n(topic: str) -> dict:
    """토픽 다국어 파일 로드"""
    i18n_dir = CORPUS_DIR / topic / "i18n"
    
    result = {}
    if i18n_dir.exists():
        for f in i18n_dir.glob("*.json"):
            lang = f.stem
            with open(f, "r", encoding="utf-8") as fp:
                result[lang] = json.load(fp)
    
    return result


def generate_web_app(topic: str, topic_meta: dict, structure: dict, 
                     content: dict, demos: list, i18n: dict):
    """웹앱 생성"""
    output_dir = EXPORTS_DIR / topic
    
    print(f"\n웹앱 생성 중: {output_dir}")
    
    # 출력 디렉토리 생성
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. package.json 생성
    package_json = {
        "name": f"knowledge-{topic}",
        "version": "0.1.0",
        "private": True,
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        },
        "dependencies": {
            "react": "^19.0.0",
            "react-dom": "^19.0.0",
            "@tanstack/react-router": "^1.132.0",
            "framer-motion": "^11.0.0",
            "i18next": "^25.0.0",
            "react-i18next": "^16.0.0"
        },
        "devDependencies": {
            "vite": "^7.0.0",
            "@vitejs/plugin-react": "^4.3.0",
            "tailwindcss": "^4.0.0",
            "typescript": "^5.7.0"
        }
    }
    
    with open(output_dir / "package.json", "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2)
    
    # 2. 빌드 메타데이터 생성
    build_meta = {
        "topic": topic,
        "generated_at": datetime.now().isoformat(),
        "content_stats": {
            "cases": len(content["cases"]),
            "fundamentals": len(content["fundamentals"]),
            "decisions": len(content["decisions"]),
            "demos": len(demos)
        },
        "languages": list(i18n.keys())
    }
    
    with open(output_dir / "build-meta.json", "w", encoding="utf-8") as f:
        json.dump(build_meta, f, indent=2, ensure_ascii=False)
    
    # 3. 컨텐츠 데이터 복사
    data_dir = output_dir / "src" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    with open(data_dir / "structure.json", "w", encoding="utf-8") as f:
        json.dump(structure, f, indent=2, ensure_ascii=False)
    
    with open(data_dir / "content.json", "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    with open(data_dir / "demos.json", "w", encoding="utf-8") as f:
        json.dump(demos, f, indent=2, ensure_ascii=False)
    
    # 4. i18n 복사
    locales_dir = output_dir / "src" / "locales"
    locales_dir.mkdir(parents=True, exist_ok=True)
    
    for lang, translations in i18n.items():
        with open(locales_dir / f"{lang}.json", "w", encoding="utf-8") as f:
            json.dump(translations, f, indent=2, ensure_ascii=False)
    
    # 5. README 생성
    readme = f"""# {topic_meta['title']}

> Auto-generated from corpus/{topic}/

## Build

```bash
cd exports/web/{topic}
pnpm install
pnpm dev
```

## Content Stats

- Cases: {len(content['cases'])}
- Fundamentals: {len(content['fundamentals'])}
- Decisions: {len(content['decisions'])}
- Interactive Demos: {len(demos)}
- Languages: {', '.join(i18n.keys())}

## Generated

{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    with open(output_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    
    print(f"  [OK] package.json 생성됨")
    print(f"  [OK] 컨텐츠 데이터 복사됨")
    print(f"  [OK] i18n 파일 복사됨 ({len(i18n)} 언어)")
    print(f"  [TODO] React 컴포넌트 템플릿 적용 필요")
    
    return output_dir


def build_topic(topic: str):
    """단일 토픽 빌드"""
    print(f"\n{'='*50}")
    print(f"Building: {topic}")
    print(f"{'='*50}")
    
    # 데이터 로드
    topic_meta = load_topic(topic)
    structure = load_structure(topic)
    content = load_content(topic)
    demos = load_demos(topic)
    i18n = load_i18n(topic)
    
    # 웹앱 생성
    output_dir = generate_web_app(topic, topic_meta, structure, content, demos, i18n)
    
    print(f"\n빌드 완료: {output_dir}")
    return output_dir


def get_all_topics():
    """모든 토픽 목록"""
    topics = []
    for d in CORPUS_DIR.iterdir():
        if d.is_dir() and not d.name.startswith("_"):
            if (d / "topic.yaml").exists():
                topics.append(d.name)
    return topics


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="corpus → 웹앱 빌드")
    parser.add_argument("--topic", type=str, help="빌드할 토픽")
    parser.add_argument("--all", action="store_true", help="모든 토픽 빌드")
    args = parser.parse_args()
    
    if args.all:
        topics = get_all_topics()
    elif args.topic:
        topics = [args.topic]
    else:
        print("Usage: python build-web.py --topic <topic> 또는 --all")
        topics = get_all_topics()
        print(f"\n사용 가능한 토픽: {', '.join(topics)}")
        return
    
    for topic in topics:
        build_topic(topic)


if __name__ == "__main__":
    main()
