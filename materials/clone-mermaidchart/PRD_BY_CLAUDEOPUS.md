---
title: "Diagram Editor PRD - Mermaid Chart Style"
date: 2025-12-30
source: "Claude Opus"
type: document
status: raw
used_in:
---

Diagram Editor PRD (Product Requirements Document)

Mermaid Chart Style Diagram Editor - Technical Reference

Document Version: 1.0
Date: 2025-12-30
Author: Technical Research Team

—

Executive Summary
This PRD defines the technical requirements for building a diagram editor similar to Mermaid Chart, featuring auto/manual layout, theme customization, look variations, and direction control. This document serves as a technical reference for implementation.

Target Features:
Auto Layout: Automatic node positioning using graph algorithms
- Manual Layout: User-controlled drag-and-drop positioning
- Theme: Color scheme customization (default, dark, forest, neutral, base)
- Look: Visual style options (classic, handDrawn)
- Direction: Flow direction control (TB, BT, LR, RL)
—

Core Technology Stack
2.1 Layout Engines

PRIMARY: ELK (Eclipse Layout Kernel)
Library: elkjs
- NPM: - Purpose: Advanced graph layout algorithms
- Algorithms:
  * elk.layered - Hierarchical layout (default)
  * elk.stress - Stress-based layout
  * elk.force - Force-directed layout
  * elk.mrtree - Tree structure layout
  * elk.sporeOverlap - Overlap removal
SECONDARY: Dagre
Library: dagre-d3-es
- Purpose: Directed graph layout
- Key Features:
  * Rank calculation
  * Node spacing
  * Edge routing
2.2 Rendering

SVG Rendering: D3.js
DOM manipulation
- Curve generation (curveLinear, curveBasis)
- Event handling (drag, zoom, pan)
- Data binding
Hand-drawn Style: Rough.js
Sketch-style rendering
- Configurable roughness
- Seed-based randomization
2.3 Theming

Color Manipulation: Khroma
Functions: adjust, darken, lighten, invert, isDark
- CSS variable generation
- Color scheme derivation
2.4 Parsing

DSL Parser: Jison
Grammar definition
- AST generation
- Syntax validation
2.5 Build Tools

Vite: Build and bundling
- TypeScript: Type safety
- Vitest: Testing
—

Feature Specifications
3.1 Auto Layout

Description:
Automatically positions nodes and routes edges using graph layout algorithms.

Implementation:

// ELK Configuration
const elkConfig = {
  algorithm: ‘elk.layered’,
  ‘elk.direction’: ‘DOWN’,
  ‘elk.spacing.nodeNode’: 50,
  ‘elk.layered.spacing.nodeNodeBetweenLayers’: 100,
  ‘nodePlacementStrategy’: ‘BRANDES_KOEPF’,
  ‘forceNodeModelOrder’: false,
  ‘considerModelOrder’: ‘NODES_AND_EDGES’
};

// Dagre Configuration
graph.setGraph({
  rankdir: ‘TB’,
  nodesep: 50,
  ranksep: 100,
  marginx: 20,
  marginy: 20
});

Key Parameters:
nodeNode spacing: Distance between nodes in same layer
- nodeNodeBetweenLayers: Distance between layers
- rankdir: Layout direction
3.2 Manual Layout

Description:
Allows users to manually position nodes via drag-and-drop.

Implementation Approach:

// Store node positions
interface NodePosition {
  nodeId: string;
  x: number;
  y: number;
}

// D3 drag handler
const drag = d3.drag()
  .on(‘start’, dragStarted)
  .on(‘drag’, dragging)
  .on(‘end’, dragEnded);

function dragging(event, d) {
  d3.select(this)
    .attr(‘transform’, translate(${event.x}, ${event.y}));
  updateEdges(d.id, event.x, event.y);
}

// Persist positions
function savePositions() {
  const positions = nodes.map(n => ({
    nodeId: n.id,
    x: n.x,
    y: n.y
  }));
  localStorage.setItem(‘diagram-positions’, JSON.stringify(positions));
}

3.3 Direction Control

Description:
Controls the primary flow direction of the diagram.

Options:
TB (Top to Bottom): Default vertical flow
- BT (Bottom to Top): Reverse vertical flow
- LR (Left to Right): Horizontal flow
- RL (Right to Left): Reverse horizontal flow
Implementation:

// Mermaid syntax
flowchart TB  // Top to Bottom
flowchart LR  // Left to Right

// Dagre implementation
graph.setGraph({ rankdir: direction });

// ELK implementation
const directionMap = {
  ‘TB’: ‘DOWN’,
  ‘BT’: ‘UP’,
  ‘LR’: ‘RIGHT’,
  ‘RL’: ‘LEFT’
};
elkConfig[‘elk.direction’] = directionMap[direction];

3.4 Theme System

Description:
Customizable color schemes for diagram styling.

Available Themes:
default - Standard light theme
2. neutral - Black and white, print-friendly
3. dark - Dark mode compatible
4. forest - Green color scheme
5. base - Customizable base theme
Implementation:

// Theme class structure
class Theme {
  constructor() {
    this.background = ‘#f4f4f4’;
    this.primaryColor = ‘#fff4dd’;
    this.secondaryColor = ‘#fff0b3’;
    this.tertiaryColor = ‘#ffeb99’;
    this.primaryTextColor = ‘#333’;
    this.fontFamily = ‘“trebuchet ms”, verdana, arial, sans-serif’;
    this.fontSize = ‘16px’;
    this.THEME_COLOR_LIMIT = 12;
  }

  updateColors() {
    // Derive colors using Khroma
    this.secondaryColor = adjust(this.primaryColor, { h: 120 });
    this.lineColor = isDark(this.background) 
      ? lighten(this.background, 20) 
      : darken(this.background, 20);
  }
}

// Apply theme
mermaid.initialize({
  theme: ‘dark’,
  themeVariables: {
    primaryColor: ‘#BB2528’,
    primaryTextColor: ‘#fff’
  }
});

3.5 Look Variations

Description:
Visual rendering style options.

Options:
classic: Clean, standard SVG rendering
- handDrawn: Sketch-style using Rough.js
Implementation:

// Configuration
mermaid.initialize({
  look: ‘handDrawn’,
  handDrawnSeed: 12345  // For consistent rendering
});

// Rendering logic
function renderNode(node, shapeSvg) {
  if (node.look === ‘handDrawn’) {
    const rc = rough.svg(shapeSvg);
    return rc.rectangle(x, y, width, height, {
      roughness: 1.5,
      bowing: 2,
      stroke: ‘#333’,
      fill: node.fillColor,
      fillStyle: ‘hachure’
    });
  } else {
    // Standard SVG rendering
    return shapeSvg.append(‘rect’)
      .attr(‘x’, x)
      .attr(‘y’, y)
      .attr(‘width’, width)
      .attr(‘height’, height);
  }
}

—

4. Architecture Overview

4.1 Component Structure

DiagramEditor/
├── core/
│   ├── parser/          # Jison-based DSL parser
│   ├── layout/          # Layout algorithms (ELK, Dagre)
│   └── renderer/        # SVG rendering (D3, Rough.js)
├── themes/
│   ├── theme-base.js
│   ├── theme-dark.js
│   ├── theme-default.js
│   ├── theme-forest.js
│   └── theme-neutral.js
├── shapes/
│   ├── rectangle.ts
│   ├── circle.ts
│   ├── diamond.ts
│   └── …
└── config/
    └── defaultConfig.ts

4.2 Data Flow

User Input (DSL text) 
   → Parser (Jison) 
   → AST
2. AST 
   → Layout Engine (ELK/Dagre) 
   → Node/Edge positions
3. Positions + Theme 
   → Renderer (D3/Rough.js) 
   → SVG output
—

5. Dependencies

5.1 Required Packages

{
  “dependencies”: {
    “elkjs”: “^0.9.0”,
    “dagre-d3-es”: “^7.0.0”,
    “d3”: “^7.8.0”,
    “roughjs”: “^4.5.0”,
    “khroma”: “^2.0.0”,
    “jison”: “^0.4.18”
  },
  “devDependencies”: {
    “typescript”: “^5.0.0”,
    “vite”: “^5.0.0”,
    “vitest”: “^1.0.0”
  }
}

—

6. Implementation Roadmap

Phase 1: Core Infrastructure (Week 1-2)
[ ] Set up project with Vite + TypeScript
- [ ] Implement basic DSL parser
- [ ] Create SVG renderer foundation
- [ ] Integrate D3.js for DOM manipulation
Phase 2: Layout System (Week 3-4)
[ ] Integrate Dagre for basic layouts
- [ ] Add ELK for advanced layouts
- [ ] Implement direction control (TB/BT/LR/RL)
- [ ] Add auto-layout toggle
Phase 3: Manual Layout (Week 5)
[ ] Implement drag-and-drop with D3
- [ ] Add position persistence
- [ ] Create undo/redo system
- [ ] Edge re-routing on node move
Phase 4: Theming (Week 6)
[ ] Implement theme class system
- [ ] Integrate Khroma for color manipulation
- [ ] Create 5 default themes
- [ ] Add custom theme support
Phase 5: Look Variations (Week 7)
[ ] Integrate Rough.js
- [ ] Implement handDrawn look
- [ ] Add seed-based consistency
- [ ] Create look toggle UI
Phase 6: Polish (Week 8)
[ ] Performance optimization
- [ ] Error handling
- [ ] Documentation
- [ ] Testing
—

7. References

GitHub Repositories:
mermaid-js/mermaid: https://github.com/mermaid-js/mermaid
- kieler/elkjs: https://github.com/kieler/elkjs
- dagrejs/dagre: https://github.com/dagrejs/dagre
- rough-stuff/rough: https://github.com/rough-stuff/rough
Documentation:
Mermaid.js Docs: https://mermaid.js.org
- ELK Documentation: https://eclipse.dev/elk/
- D3.js: https://d3js.org
- Rough.js: https://roughjs.com
—

END OF DOCUMENT
