#!/usr/bin/env python3
"""
inbox-to-corpus.py - RAW 입력을 corpus로 변환하는 스크립트

Usage:
    python scripts/inbox-to-corpus.py [--dry-run] [--file <filename>]

Flow:
    1. inbox/ 폴더의 RAW 문서 읽기
    2. AI Agent가 분류/태깅/구조화
    3. 적절한 corpus/{topic}/content/{layer}/ 에 저장
    4. graph.json 업데이트
"""

import os
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime

# TODO: AI Agent 연동 (Claude API or Claude Code)
# from anthropic import Anthropic

REPO_ROOT = Path(__file__).parent.parent
INBOX_DIR = REPO_ROOT / "inbox"
CORPUS_DIR = REPO_ROOT / "corpus"
META_DIR = CORPUS_DIR / "_meta"


def load_domains():
    """도메인 정의 로드"""
    with open(META_DIR / "domains.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_content_types():
    """컨텐츠 타입 정의 로드"""
    with open(META_DIR / "content-types.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_inbox_files():
    """inbox/ 폴더의 처리할 파일 목록"""
    files = []
    for f in INBOX_DIR.iterdir():
        if f.is_file() and f.suffix in [".md", ".mdx"] and not f.name.startswith("_"):
            files.append(f)
    return files


def classify_document(content: str, domains: dict, content_types: dict) -> dict:
    """
    AI Agent를 통해 문서 분류
    
    Returns:
        {
            "topic": "game-development",
            "layer": "cases",
            "id": "new-game-case",
            "title": "제목",
            "description": "설명",
            "tags": [...],
            "connections": {...}
        }
    """
    # TODO: 실제 AI Agent 연동
    # 현재는 placeholder
    
    print("[TODO] AI Agent 연동 필요: 문서 분류")
    print("  - 어느 topic에 속하는지 판단")
    print("  - 어느 layer(cases/fundamentals/decisions)인지 판단")
    print("  - 관련 연결 추출")
    
    return None


def create_enhanced_document(raw_content: str, classification: dict) -> str:
    """
    분류 정보를 바탕으로 구조화된 문서 생성
    """
    # TODO: AI Agent가 템플릿에 맞춰 구조화
    pass


def update_graph(topic: str, new_node: dict):
    """
    corpus/{topic}/structure/graph.json 업데이트
    """
    graph_path = CORPUS_DIR / topic / "structure" / "graph.json"
    
    if graph_path.exists():
        with open(graph_path, "r", encoding="utf-8") as f:
            graph = json.load(f)
    else:
        graph = {"nodes": [], "cross_layer_connections": [], "metadata": {}}
    
    # 새 노드 추가
    graph["nodes"].append(new_node)
    graph["metadata"]["updated"] = datetime.now().isoformat()
    
    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)


def process_file(file_path: Path, dry_run: bool = False):
    """단일 파일 처리"""
    print(f"\n처리 중: {file_path.name}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    domains = load_domains()
    content_types = load_content_types()
    
    # 분류
    classification = classify_document(content, domains, content_types)
    
    if classification is None:
        print("  [SKIP] 분류 실패 또는 AI Agent 미연동")
        return False
    
    if dry_run:
        print(f"  [DRY-RUN] 분류 결과:")
        print(f"    Topic: {classification.get('topic')}")
        print(f"    Layer: {classification.get('layer')}")
        print(f"    ID: {classification.get('id')}")
        return True
    
    # 구조화된 문서 생성
    enhanced = create_enhanced_document(content, classification)
    
    # 저장
    topic = classification["topic"]
    layer = classification["layer"]
    doc_id = classification["id"]
    
    output_path = CORPUS_DIR / topic / "content" / layer / f"{doc_id}.mdx"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(enhanced)
    
    # 그래프 업데이트
    update_graph(topic, classification)
    
    # inbox에서 처리 완료 표시 (또는 이동)
    # TODO: processed/ 폴더로 이동 또는 frontmatter에 status 업데이트
    
    print(f"  [OK] 저장됨: {output_path}")
    return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="inbox → corpus 변환")
    parser.add_argument("--dry-run", action="store_true", help="실제 저장 없이 테스트")
    parser.add_argument("--file", type=str, help="특정 파일만 처리")
    args = parser.parse_args()
    
    print("=" * 50)
    print("Knowledge Pipeline: inbox → corpus")
    print("=" * 50)
    
    if args.file:
        files = [INBOX_DIR / args.file]
    else:
        files = get_inbox_files()
    
    if not files:
        print("\ninbox/에 처리할 파일이 없습니다.")
        return
    
    print(f"\n처리할 파일 수: {len(files)}")
    
    success = 0
    for f in files:
        if process_file(f, dry_run=args.dry_run):
            success += 1
    
    print(f"\n완료: {success}/{len(files)} 파일 처리됨")


if __name__ == "__main__":
    main()
