---
title: "Mermaid Chart Clone PRD"
date: 2025-12-31
source: "리서치"
type: document
status: raw
used_in:
---

Mermaid Chart처럼 예쁘고 유연하게 렌더링하려면, 기본은 mermaid.js + ELK 레이아웃 + 커스텀 테마 시스템 + 뷰 모드(UI) 설계라고 보면 됩니다.[1][2][3][4]

## 1. 목표와 범위

- 목표
  - Mermaid DSL을 입력하면 auto layout(ELK 등)으로 보기 좋게 배치.
  - 노드/엣지 스타일, 테마, 레이아웃 방향(TB/LR/BT/RL)을 UI에서 즉시 변경.
  - 일부 다이어그램에서 manual layout(좌표 기반 혹은 별도 레이아웃) 지원.
- 범위
  - MVP에서는 Mermaid 지원 다이어그램 중 flowchart/sequence/class 정도 우선.[5][6]
  - 프로젝트 단위로 다이어그램 저장, 버전 관리, 공유 링크는 2차 범위.[4]

## 2. 핵심 기능 목록

- Mermaid 렌더링
  - mermaid.js ESM import, `mermaid.initialize` + `mermaid.render` 사용.[7][5]
  - `securityLevel: 'loose'`, 전역 테마/레이아웃 옵션 설정.[2][7]
- Auto layout
  - 기본: dagre, 고급: ELK(`@mermaid-js/layout-elk`).[8][3][9][1]
  - UI에서 layout: `dagre | elk | tidy-tree | cose-bilkent` 선택 가능하게.[3]
- Manual layout
  - 옵션 1: Mermaid의 레이아웃 옵션(elk params, 간격, 방향 등)을 UI에서 제어해 “반 수동” 조정.[3][8]
  - 옵션 2(고급): 별도의 캔버스(React Flow 등)에서 좌표/엣지 직접 편집 후 Mermaid 코드로 역직렬화 (후순위).
- Look & theme
  - Mermaid 기본 테마(`default`, `dark`, `forest`, `neutral`, `base`) 선택.[10][2]
  - `themeVariables`를 이용한 커스텀 테마 생성 (브랜드 컬러, 노드/엣지 색 등).[2]
  - 다이어그램별 frontmatter/`%%{init: ... }%%` directive로 theme override.[10][7]
- Layout / direction 변경
  - `graph TB/LR/BT/RL` 등 direction 토글 UI 제공.[6][5]
  - ELK 사용 시에도 방향, 노드 간격 등 주요 파라미터 UI 연결.[8][3]
- 미리보기 & 인터랙션
  - 코드 입력 ↔ 실시간 preview (debounce).
  - 확대/축소, 캔버스 드래그, 노드 hover/클릭 이벤트 지원 (필요 시).[11][12]
- Export / 공유
  - SVG/PNG export (브라우저에서 SVG → PNG 변환).[13][11]
  - 다이어그램 상태를 JSON/URL hash에 직렬화해 공유 링크 생성.[13]

## 3. 기술 스택 및 재료

### 프론트엔드

- **기술 스택**
  - React + TypeScript + TailwindCSS (또는 shadcn UI 컴포넌트)
  - Remix(Router v7) 기반 SPA 모드
- **주요 라이브러리**
  - `mermaid` (코어 다이어그램 렌더링).[12][14]
  - `@mermaid-js/layout-elk` (ELK 레이아웃 플러그인).[9][1]
  - 코드 에디터: `@monaco-editor/react` 또는 `codemirror` (mermaid syntax highlight).
  - 상태관리: React Query or Remix loader/action + local state.
- **구성**
  - `DiagramEditor` 컴포넌트
    - 좌: 코드 에디터 (Mermaid DSL, `%%{init: ... }%%` 포함).[7][10]
    - 우: Preview(`div`에 `mermaid.render` 결과 SVG 주입).
  - `ThemePanel`
    - 테마 선택: default / dark / forest / neutral / custom.[10][2]
    - 커스텀 테마 변수 입력(기본: primaryColor, lineColor 등).[2]
  - `LayoutPanel`
    - 레이아웃 엔진: dagre / elk / tidy-tree / cose-bilkent.[3]
    - 방향: TB / LR / BT / RL.[15][5]
    - 노드 간격, 레이어 간 간격 등 ELK 파라미터.[8][3]
  - `Toolbar`
    - Undo/redo(코드 히스토리), zoom in/out, fit to screen, export.

### 백엔드

- **기술 스택**
  - FastAPI (Python) + PostgreSQL (Prisma로 접근)  
- **핵심 엔티티**
  - `Project`: id, name, owner_id, created_at
  - `Diagram`: id, project_id, title, mermaid_code, config(theme/layout JSON), created_at, updated_at
  - `DiagramVersion`: id, diagram_id, mermaid_code, config, created_at
- **API 예시**
  - `POST /projects`, `GET /projects/:id`
  - `POST /diagrams`, `PUT /diagrams/:id`
  - `GET /diagrams/:id` (뷰 모드용 read-only)
- **스토리지 전략**
  - Mermaid DSL 전체를 텍스트로 저장.
  - UI에서 쓰는 theme/layout 옵션은 별도 JSON으로 저장해 재편집 시 바로 패널에 반영.

## 4. 동작 플로우 (Auto / Manual Layout)

- 초기화
  - 앱 로드 시 `mermaid.initialize({ startOnLoad: false, theme, securityLevel: 'loose', flowchart: { defaultRenderer: 'elk' } })`.[1][7][2]
  - ELK 레이아웃 플러그인 등록: `mermaid.registerLayoutLoaders(elkLayouts)` 또는 `registerExternalDiagrams`.[9][1][8]
- Auto layout 모드
  - 사용자가 노드를 추가/삭제하면 Mermaid DSL 업데이트.
  - 선택된 layout 엔진, direction, spacing 등을 init directive 또는 frontmatter config에 반영.[7][3][10]
  - 렌더 호출 시 ELK/dagre가 자동 배치.
- Manual layout 모드(1차 버전)
  - 레이아웃 파라미터들을 세밀하게 조정(간격, 방향 등) → 사실상 “튜닝된 auto layout”으로 제공.[3][8]
  - 완전한 드래그 앤 드롭 수동 좌표 편집은 추후 React Flow 통합 시 도입.

## 5. PRD 요약

- 사용자 스토리
  - “Mermaid 코드를 작성하면, 최대한 예쁘게 auto layout된 다이어그램을 즉시 보고 싶다.”
  - “토글 몇 번으로 테마/색/레이아웃 방향을 바꾸며 결과를 비교하고 싶다.”[16][2]
  - “복잡한 그래프를 ELK로 자동 정리해서 선이 덜 꼬이게 만들고 싶다.”[17][1][8]
- 필수 요구사항(Must)
  - Mermaid DSL 에디터 + 실시간 프리뷰.
  - 테마 선택(기본 + 커스텀 기본 변수) UI.[10][2]
  - 레이아웃 엔진/방향 변경 UI + ELK 통합.[1][9][3]
  - 다이어그램 저장/불러오기(프로젝트/다이어그램 단위, 버전 최소 1개).
- 우선순위 높은 옵션(Should)
  - SVG/PNG export.[11][13]
  - URL 기반 공유(읽기 전용 뷰).
- 나중에( Could )
  - 완전 manual layout 모드(React Flow + Mermaid 변환).
  - 협업(실시간 커서, 코멘트).[4]

***

요청대로라면 이 정도가 1차 PRD 초안이고,  
다음 단계로는 “Remix 라우트 구조 + 주요 React 컴포넌트/훅 설계”까지 쪼개 줄 수 있습니다.  
원하면 `routes` 구조랑 `DiagramEditor` 내부 API/타입 설계까지 바로 이어서 적어줄게요.

[1](https://github.com/mermaid-js/mermaid/issues/5969)
[2](https://mermaid.ai/open-source/config/theming.html)
[3](https://mermaid.js.org/config/layouts.html)
[4](https://docs.mermaidchart.com/mermaid-oss/intro/getting-started.html)
[5](https://swimm.io/learn/mermaid-js/mermaid-js-a-complete-guide)
[6](https://mermaid.js.org/syntax/classDiagram.html)
[7](https://mermaid.js.org/config/configuration)
[8](https://blog.csdn.net/gitblog_01176/article/details/152098877)
[9](https://www.npmjs.com/package/@mermaid-js/layout-elk)
[10](https://mermaid.ai/open-source/config/directives.html)
[11](https://mermaid.live)
[12](https://mermaid.js.org)
[13](https://github.com/mermaid-js/mermaid-live-editor)
[14](https://github.com/mermaid-js/mermaid)
[15](https://handbook.gitlab.com/handbook/tools-and-tips/mermaid/)
[16](https://docs.mermaidchart.com/blog/posts/gui-for-editing-mermaid-class-diagrams)
[17](https://www.drawio.com/blog/mermaid-elk-layout)
[18](https://www.mermaidchart.com/app/projects/9dc2d766-3c7d-451c-b31a-7b7571002cbb/diagrams/6eb96e88-c390-4f68-ae92-2b664175303e/version/v0.1/edit)
[19](https://mermaid.js.org/intro/syntax-reference.html)
[20](https://forum.obsidian.md/t/let-the-user-decide-the-size-and-alignment-of-mermaid-diagrams/7019)
[21](https://community.lucid.co/ideas/format-shape-styles-and-colors-in-mermaid-styling-9236)
[22](https://stackoverflow.com/questions/74894540/mermaid-js-flow-chart-full-list-of-available-options-to-style-a-node)
[23](https://github.com/squidfunk/mkdocs-material/discussions/4582)