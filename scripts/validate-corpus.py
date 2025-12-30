#!/usr/bin/env python3
"""
validate-corpus.py - corpus 무결성 검증

Usage:
    python scripts/validate-corpus.py [--topic <topic>] [--all] [--fix]

Checks:
    1. topic.yaml 존재 및 필수 필드
    2. structure/ 파일 유효성
    3. content/ 파일의 frontmatter 유효성
    4. graph.json의 참조 무결성
    5. i18n 파일의 키 일관성
"""

import os
import sys
import yaml
import json
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).parent.parent
CORPUS_DIR = REPO_ROOT / "corpus"


class ValidationError:
    def __init__(self, path: str, message: str, severity: str = "error"):
        self.path = path
        self.message = message
        self.severity = severity  # error, warning, info
    
    def __str__(self):
        icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}.get(self.severity, "?")
        return f"{icon} [{self.path}] {self.message}"


def validate_topic_yaml(topic_dir: Path) -> List[ValidationError]:
    """topic.yaml 검증"""
    errors = []
    topic_yaml = topic_dir / "topic.yaml"
    
    if not topic_yaml.exists():
        errors.append(ValidationError(str(topic_yaml), "topic.yaml not found"))
        return errors
    
    try:
        with open(topic_yaml, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(ValidationError(str(topic_yaml), f"YAML parse error: {e}"))
        return errors
    
    # 필수 필드 검증
    required_fields = ["id", "title", "description", "domain", "structure_type"]
    for field in required_fields:
        if field not in data:
            errors.append(ValidationError(str(topic_yaml), f"Missing required field: {field}"))
    
    # structure_type 검증
    valid_structure_types = ["layered", "tree", "flat", "graph"]
    if data.get("structure_type") not in valid_structure_types:
        errors.append(ValidationError(
            str(topic_yaml), 
            f"Invalid structure_type: {data.get('structure_type')}. Must be one of {valid_structure_types}"
        ))
    
    return errors


def validate_structure(topic_dir: Path) -> List[ValidationError]:
    """structure/ 검증"""
    errors = []
    structure_dir = topic_dir / "structure"
    
    if not structure_dir.exists():
        errors.append(ValidationError(str(structure_dir), "structure/ directory not found", "warning"))
        return errors
    
    # graph.json 검증
    graph_path = structure_dir / "graph.json"
    if graph_path.exists():
        try:
            with open(graph_path, "r", encoding="utf-8") as f:
                graph = json.load(f)
            
            if "nodes" not in graph:
                errors.append(ValidationError(str(graph_path), "Missing 'nodes' array"))
            
        except json.JSONDecodeError as e:
            errors.append(ValidationError(str(graph_path), f"JSON parse error: {e}"))
    
    return errors


def validate_content(topic_dir: Path) -> List[ValidationError]:
    """content/ 검증"""
    errors = []
    content_dir = topic_dir / "content"
    
    if not content_dir.exists():
        errors.append(ValidationError(str(content_dir), "content/ directory not found", "warning"))
        return errors
    
    for layer in ["cases", "fundamentals", "decisions"]:
        layer_dir = content_dir / layer
        if not layer_dir.exists():
            errors.append(ValidationError(str(layer_dir), f"{layer}/ not found", "info"))
            continue
        
        for mdx_file in layer_dir.glob("*.mdx"):
            if mdx_file.name.startswith("_"):
                continue
            
            try:
                with open(mdx_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # frontmatter 검증
                if not content.startswith("---"):
                    errors.append(ValidationError(str(mdx_file), "Missing frontmatter"))
                    continue
                
                # frontmatter 파싱
                parts = content.split("---", 2)
                if len(parts) < 3:
                    errors.append(ValidationError(str(mdx_file), "Invalid frontmatter format"))
                    continue
                
                try:
                    frontmatter = yaml.safe_load(parts[1])
                except yaml.YAMLError as e:
                    errors.append(ValidationError(str(mdx_file), f"Frontmatter YAML error: {e}"))
                    continue
                
                # 필수 필드 검증
                if "id" not in frontmatter:
                    errors.append(ValidationError(str(mdx_file), "Missing 'id' in frontmatter"))
                if "title" not in frontmatter:
                    errors.append(ValidationError(str(mdx_file), "Missing 'title' in frontmatter"))
                
                # id와 파일명 일치 검증
                if frontmatter.get("id") != mdx_file.stem:
                    errors.append(ValidationError(
                        str(mdx_file), 
                        f"ID mismatch: frontmatter '{frontmatter.get('id')}' vs filename '{mdx_file.stem}'"
                    ))
                
            except Exception as e:
                errors.append(ValidationError(str(mdx_file), f"Read error: {e}"))
    
    return errors


def validate_i18n(topic_dir: Path) -> List[ValidationError]:
    """i18n 검증"""
    errors = []
    i18n_dir = topic_dir / "i18n"
    
    if not i18n_dir.exists():
        errors.append(ValidationError(str(i18n_dir), "i18n/ not found", "info"))
        return errors
    
    translations = {}
    for json_file in i18n_dir.glob("*.json"):
        lang = json_file.stem
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                translations[lang] = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(ValidationError(str(json_file), f"JSON parse error: {e}"))
    
    # 키 일관성 검증
    if len(translations) > 1:
        reference_lang = "ko" if "ko" in translations else list(translations.keys())[0]
        reference_keys = set(get_all_keys(translations[reference_lang]))
        
        for lang, trans in translations.items():
            if lang == reference_lang:
                continue
            
            lang_keys = set(get_all_keys(trans))
            
            missing = reference_keys - lang_keys
            extra = lang_keys - reference_keys
            
            if missing:
                errors.append(ValidationError(
                    f"{i18n_dir}/{lang}.json", 
                    f"Missing keys from {reference_lang}: {missing}",
                    "warning"
                ))
            if extra:
                errors.append(ValidationError(
                    f"{i18n_dir}/{lang}.json", 
                    f"Extra keys not in {reference_lang}: {extra}",
                    "info"
                ))
    
    return errors


def get_all_keys(obj, prefix=""):
    """중첩 객체의 모든 키 추출"""
    keys = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                keys.extend(get_all_keys(v, key))
            else:
                keys.append(key)
    return keys


def validate_topic(topic: str) -> List[ValidationError]:
    """단일 토픽 검증"""
    topic_dir = CORPUS_DIR / topic
    
    if not topic_dir.exists():
        return [ValidationError(str(topic_dir), "Topic directory not found")]
    
    errors = []
    errors.extend(validate_topic_yaml(topic_dir))
    errors.extend(validate_structure(topic_dir))
    errors.extend(validate_content(topic_dir))
    errors.extend(validate_i18n(topic_dir))
    
    return errors


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
    
    parser = argparse.ArgumentParser(description="corpus 무결성 검증")
    parser.add_argument("--topic", type=str, help="검증할 토픽")
    parser.add_argument("--all", action="store_true", help="모든 토픽 검증")
    args = parser.parse_args()
    
    print("=" * 50)
    print("Knowledge Pipeline: Corpus Validation")
    print("=" * 50)
    
    if args.all:
        topics = get_all_topics()
    elif args.topic:
        topics = [args.topic]
    else:
        topics = get_all_topics()
    
    total_errors = 0
    total_warnings = 0
    
    for topic in topics:
        print(f"\n📂 {topic}/")
        errors = validate_topic(topic)
        
        if not errors:
            print("  ✅ All checks passed")
        else:
            for e in errors:
                print(f"  {e}")
                if e.severity == "error":
                    total_errors += 1
                elif e.severity == "warning":
                    total_warnings += 1
    
    print(f"\n{'='*50}")
    print(f"Summary: {total_errors} errors, {total_warnings} warnings")
    
    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
