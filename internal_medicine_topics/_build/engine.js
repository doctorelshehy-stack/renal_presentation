// ================================================================
// Rendering engine — adapted from notebook-lm-mindmap template
// Changes vs original: top tabs = folders (no "All" merge tab),
// label wrap limits raised so no content is truncated.
// ================================================================

(() => {
  'use strict';

  // ==== Folders (tabs) =====
  const FOLDERS = [
    folderGlomerular,
    folderAKI,
    folderCKD,
    folderElectrolytes,
    folderStructural
  ];

  function countNodes(n) {
    let c = 1;
    if (n.children) for (const ch of n.children) c += countNodes(ch);
    return c;
  }

  // ==== DOM refs ====
  const svg = document.getElementById('mindmap-svg');
  const connectionsLayer = document.getElementById('connections-layer');
  const nodesLayer = document.getElementById('nodes-layer');
  const container = document.getElementById('svg-container');
  const topbar = document.getElementById('topbar');

  // ==== State ====
  const state = {
    expanded: new Set(),
    nodeMap: {},
    focusedNodeId: null,
    folderIdx: 0,
  };

  let nodeCounter = 0;
  const X_GAP = 90;
  const Y_GAP = 14;
  let needsViewFit = true;

  // ================================================================
  //  TREE BUILDING — called once per folder switch
  // ================================================================

  function buildTree() {
    state.nodeMap = {};
    nodeCounter = 0;

    function cloneAndId(node, parentId) {
      const n = { label: node.label };
      n.id = 'n' + (nodeCounter++);
      if (node.children) n.children = node.children.map(c => cloneAndId(c, n.id));
      n.parentId = parentId || null;
      state.nodeMap[n.id] = n;
      return n;
    }

    const root = cloneAndId(FOLDERS[state.folderIdx], null);
    state.expanded.add(root.id);
    return root;
  }

  // ================================================================
  //  COLOR ASSIGNMENT
  // ================================================================

  function assignColors(node, depth, branchIdx) {
    const colors = ['color-0','color-1','color-2','color-3','color-4','color-5','color-6','color-7'];
    if (depth === 0) node._colorClass = 'is-root';
    else if (depth === 1) node._colorClass = colors[branchIdx % colors.length];
    else node._colorClass = colors[branchIdx % colors.length];
    if (node.children) node.children.forEach((c, i) => assignColors(c, depth + 1, depth === 0 ? i : branchIdx));
  }

  // ================================================================
  //  TEXT MEASUREMENT — raised limits so full labels are never cut
  // ================================================================

  function measureText(text, fontSize) {
    const c = document.createElement('canvas');
    const ctx = c.getContext('2d');
    ctx.font = fontSize + 'px Arial, Helvetica, sans-serif';
    return ctx.measureText(text || '').width;
  }

  function wrapText(text, maxWidth, fontSize) {
    if (!text) return [{ text: '', width: 0 }];
    const words = text.split(/\s+/);
    const lines = [];
    let cur = '', curW = 0;
    for (const w of words) {
      const ww = measureText(w + ' ', fontSize);
      if (curW + ww > maxWidth && cur) {
        lines.push({ text: cur.trim(), width: curW });
        cur = w + ' '; curW = ww;
      } else { cur += w + ' '; curW += ww; }
    }
    if (cur.trim()) lines.push({ text: cur.trim(), width: curW });
    return lines.slice(0, 14);
  }

  function computeDims(label, fontSize, isRoot) {
    const maxChars = isRoot ? 40 : 64;
    const cw = fontSize * 0.58;
    const maxTW = maxChars * cw;
    const lines = wrapText(label, maxTW, fontSize);
    const lh = fontSize * 1.35;
    const tw = Math.max(...lines.map(l => l.width));
    const th = lines.length * lh;
    const px = isRoot ? 24 : 16;
    const py = isRoot ? 14 : 10;
    return {
      width: Math.max(isRoot ? 100 : 56, tw + px * 2),
      height: Math.max(isRoot ? 40 : 30, th + py * 2),
      lines, lineHeight: lh,
    };
  }

  // ================================================================
  //  LAYOUT — sequential top-to-bottom, uses state.expanded
  // ================================================================

  function layout(node, depth, startX, startY) {
    const isRoot = depth === 0;
    const fs = isRoot ? 15 : 12.5;
    const dims = computeDims(node.label, fs, isRoot);
    node.isRoot = isRoot;
    node._dims = dims;
    node._x = startX;
    node._y = startY;
    node._w = dims.width;
    node._h = dims.height;

    if (!node.children || node.children.length === 0 || !state.expanded.has(node.id)) return;

    const childX = startX + dims.width + X_GAP;
    let curY = startY;
    for (const child of node.children) {
      layout(child, depth + 1, childX, curY);
      curY += subtreeHeight(child) + Y_GAP;
    }
  }

  function subtreeHeight(node) {
    if (!node._h) return 0;
    if (!node.children || node.children.length === 0 || !state.expanded.has(node.id)) return node._h;
    let total = 0;
    for (const c of node.children) total += subtreeHeight(c);
    return Math.max(node._h, total + (node.children.length - 1) * Y_GAP);
  }

  function computeBounds(root) {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    function walk(n) {
      if (n._x === undefined) return;
      const pad = 50;
      minX = Math.min(minX, n._x - pad);
      minY = Math.min(minY, n._y - pad);
      maxX = Math.max(maxX, n._x + n._w + pad);
      maxY = Math.max(maxY, n._y + n._h + pad);
      if (n.children && state.expanded.has(n.id)) n.children.forEach(walk);
    }
    walk(root);
    if (minX === Infinity) return { minX: -200, minY: -200, maxX: 200, maxY: 200 };
    return { minX, minY, maxX, maxY };
  }

  // ================================================================
  //  RENDER
  // ================================================================

  function render() {
    const root = state.currentRoot;
    if (!root) return;

    connectionsLayer.innerHTML = '';
    nodesLayer.innerHTML = '';

    layout(root, 0, 30, 30);

    if (needsViewFit) {
      needsViewFit = false;
      const b = computeBounds(root);
      const pad = 60;
      const vw = (b.maxX - b.minX) + pad * 2;
      const vh = (b.maxY - b.minY) + pad * 2;
      const vcx = (b.minX + b.maxX) / 2;
      const vcy = (b.minY + b.maxY) / 2;
      svg.setAttribute('viewBox', `${vcx - vw / 2} ${vcy - vh / 2} ${vw} ${vh}`);
      svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    }

    function renderNode(node) {
      if (node._x === undefined) return;

      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      g.classList.add('node-group', node._colorClass || 'color-0');
      if (node.isRoot) g.classList.add('is-root');
      if (node.id === state.focusedNodeId) g.classList.add('focused');
      g.setAttribute('role', 'treeitem');
      const hasCh = !!(node.children && node.children.length > 0);
      const isExp = state.expanded.has(node.id);
      g.setAttribute('aria-expanded', hasCh ? (isExp ? 'true' : 'false') : 'undefined');
      g.setAttribute('aria-label', node.label + (hasCh ? (isExp ? ' — expanded' : ' — collapsed, ' + node.children.length + ' items') : ''));
      g.setAttribute('tabindex', '0');
      g.dataset.nodeId = node.id;

      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', 0); rect.setAttribute('y', 0);
      rect.setAttribute('width', node._w); rect.setAttribute('height', node._h);
      rect.setAttribute('rx', '8'); rect.setAttribute('ry', '8');
      rect.classList.add('node-bg');
      rect.setAttribute('filter', node.isRoot ? 'url(#root-shadow)' : 'url(#node-shadow)');
      g.appendChild(rect);

      const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      txt.classList.add('node-text');
      txt.setAttribute('font-size', node.isRoot ? 15 : 12.5);
      const d = node._dims;
      const th = d.lines.length * d.lineHeight;
      const sy = (node._h - th) / 2 + d.lineHeight / 2;
      d.lines.forEach((line, i) => {
        const t = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
        t.setAttribute('x', node._w / 2);
        t.setAttribute('y', sy + i * d.lineHeight);
        t.setAttribute('class', 'label');
        t.textContent = line.text;
        txt.appendChild(t);
      });
      g.appendChild(txt);

      if (hasCh) {
        const cx = node._w + 10, cy = node._h / 2;
        const circ = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circ.setAttribute('cx', cx); circ.setAttribute('cy', cy);
        circ.setAttribute('r', '8');
        circ.classList.add('toggle-circle');
        g.appendChild(circ);
        const ic = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        ic.setAttribute('x', cx); ic.setAttribute('y', cy);
        ic.setAttribute('text-anchor', 'middle');
        ic.setAttribute('font-size', '11'); ic.setAttribute('font-weight', '700');
        ic.setAttribute('fill', '#ffffff'); ic.setAttribute('dominant-baseline', 'central');
        ic.textContent = isExp ? '−' : '+';
        ic.classList.add('toggle-text');
        g.appendChild(ic);
      }

      g.setAttribute('transform', `translate(${node._x}, ${node._y})`);

      if (node.parentId && state.nodeMap[node.parentId]) {
        const p = state.nodeMap[node.parentId];
        if (p._x !== undefined) {
          const sx = p._x + p._w, sy2 = p._y + p._h / 2;
          const ex = node._x, ey = node._y + node._h / 2;
          const cp = sx + (ex - sx) * 0.5;
          const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path.setAttribute('d', `M${sx},${sy2} C${cp},${sy2} ${cp},${ey} ${ex},${ey}`);
          path.classList.add('connector');
          if (node.id === state.focusedNodeId || p.id === state.focusedNodeId) path.classList.add('focused');
          connectionsLayer.appendChild(path);
        }
      }

      nodesLayer.appendChild(g);

      if (hasCh && isExp) node.children.forEach(renderNode);
    }

    renderNode(root);
  }

  // ================================================================
  //  FOLDER SWITCHING
  // ================================================================

  function switchFolder(idx) {
    state.folderIdx = idx;
    state.expanded.clear();
    state.focusedNodeId = null;
    state.currentRoot = buildTree();
    assignColors(state.currentRoot, 0, 0);
    needsViewFit = true;
    document.getElementById('fit-branch-btn').disabled = true;
    // reset expand-all button (pure action, no toggle state)
    const eab = document.getElementById('expand-all-btn');
    eab.innerHTML = '<span>▸</span> Expand all';
    renderTopbar();
    render();
  }

  function renderTopbar() {
    topbar.innerHTML = '';
    FOLDERS.forEach((f, i) => {
      const btn = document.createElement('button');
      btn.className = 'tab-btn' + (i === state.folderIdx ? ' active' : '');
      btn.setAttribute('role', 'tab');
      btn.setAttribute('aria-selected', i === state.folderIdx ? 'true' : 'false');
      btn.dataset.topic = i;
      btn.innerHTML = `${f.label} <span class="count">(${countNodes(f)})</span>`;
      btn.addEventListener('click', () => switchFolder(i));
      topbar.appendChild(btn);
    });
  }

  // ================================================================
  //  TOGGLE / FOCUS / ZOOM
  // ================================================================

  function toggleNode(nodeId) {
    const node = state.nodeMap[nodeId];
    if (!node || !node.children || node.children.length === 0) return;

    if (state.expanded.has(nodeId)) {
      state.expanded.delete(nodeId);
      function closeDesc(n) {
        if (n.children) n.children.forEach(c => { state.expanded.delete(c.id); closeDesc(c); });
      }
      closeDesc(node);
    } else {
      state.expanded.add(nodeId);
    }
    render();
  }

  function focusNode(nodeId) {
    const node = state.nodeMap[nodeId];
    if (!node) return;
    let cur = node;
    while (cur.parentId) {
      state.expanded.add(cur.parentId);
      cur = state.nodeMap[cur.parentId];
    }
    if (node.children && node.children.length > 0) state.expanded.add(node.id);

    state.focusedNodeId = nodeId;
    render();

    zoomToNode(node);
    document.getElementById('fit-branch-btn').disabled = false;
  }

  function zoomToNode(node) {
    if (!node._x) return;
    const pad = 80;
    const startX = node.parentId ? state.nodeMap[node.parentId]._x - 40 : state.currentRoot._x - 40;
    const endX = branchRightmost(node);
    const w = endX - startX + pad * 2;
    const cy = node._y + node._h / 2;
    const h = Math.max(w * 0.7, node._h * 6);
    animateViewBox({ x: startX - pad, y: cy - h / 2, w, h });
  }

  function branchRightmost(node) {
    if (!node.children || node.children.length === 0 || !state.expanded.has(node.id)) return node._x + node._w;
    let max = node._x + node._w;
    for (const c of node.children) max = Math.max(max, branchRightmost(c));
    return max;
  }

  function animateViewBox(target) {
    const cur = svg.getAttribute('viewBox').split(' ').map(Number);
    const [cx, cy, cw, ch] = cur;
    const [tx, ty, tw, th] = [target.x, target.y, target.w, target.h];
    const dur = 200;
    const t0 = performance.now();
    function step(now) {
      const p = Math.min(1, (now - t0) / dur);
      const e = 1 - (1 - p) * (1 - p) * (1 - p);
      svg.setAttribute('viewBox',
        `${cx + (tx - cx) * e} ${cy + (ty - cy) * e} ${cw + (tw - cw) * e} ${ch + (th - ch) * e}`);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function expandAll() {
    function ex(n) { if (n.children) { state.expanded.add(n.id); n.children.forEach(ex); } }
    ex(state.currentRoot);
    state.focusedNodeId = null;
    document.getElementById('fit-branch-btn').disabled = true;
    render();
  }

  function collapseAll() {
    function col(n) {
      if (n.children) {
        if (n.id !== state.currentRoot.id) state.expanded.delete(n.id);
        n.children.forEach(col);
      }
    }
    col(state.currentRoot);
    state.focusedNodeId = null;
    document.getElementById('fit-branch-btn').disabled = true;
    render();
    resetView();
  }

  function resetView() {
    const b = computeBounds(state.currentRoot);
    const pad = 60;
    const vw = (b.maxX - b.minX) + pad * 2;
    const vh = (b.maxY - b.minY) + pad * 2;
    const vcx = (b.minX + b.maxX) / 2;
    const vcy = (b.minY + b.maxY) / 2;
    animateViewBox({ x: vcx - vw / 2, y: vcy - vh / 2, w: vw, h: vh });
  }

  // ================================================================
  //  EVENTS
  // ================================================================

  function setupEvents() {

    nodesLayer.addEventListener('click', (e) => {
      const g = e.target.closest('.node-group');
      if (!g) return;
      const id = g.dataset.nodeId;

      if (e.target.closest('.toggle-circle') || e.target.closest('.toggle-text')) {
        toggleNode(id);
        return;
      }

      if (id !== state.focusedNodeId) {
        focusNode(id);
      } else {
        state.focusedNodeId = null;
        document.getElementById('fit-branch-btn').disabled = true;
        resetView();
      }
    });

    nodesLayer.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const g = e.target.closest('.node-group');
        if (g) focusNode(g.dataset.nodeId);
      }
    });

    document.getElementById('zoom-in').addEventListener('click', () => zoomViewBox(0.75));
    document.getElementById('zoom-out').addEventListener('click', () => zoomViewBox(1.33));
    document.getElementById('zoom-reset').addEventListener('click', resetView);

    function zoomViewBox(factor) {
      const vb = svg.getAttribute('viewBox').split(' ').map(Number);
      const [vx, vy, vw, vh] = vb;
      const nw = vw * factor, nh = vh * factor;
      svg.setAttribute('viewBox', `${vx + (vw - nw) / 2} ${vy + (vh - nh) / 2} ${nw} ${nh}`);
    }

    const eab = document.getElementById('expand-all-btn');
    eab.addEventListener('click', () => {
      expandAll();
    });

    document.getElementById('collapse-all-btn').addEventListener('click', collapseAll);

    document.getElementById('fit-branch-btn').addEventListener('click', () => {
      if (state.focusedNodeId) zoomToNode(state.nodeMap[state.focusedNodeId]);
    });

    container.addEventListener('wheel', (e) => {
      e.preventDefault();
      const vb = svg.getAttribute('viewBox').split(' ').map(Number);
      const [vx, vy, vw, vh] = vb;

      if (e.shiftKey) {
        const panX = e.deltaY * vw / container.clientWidth * 0.5;
        svg.setAttribute('viewBox', `${vx + panX} ${vy} ${vw} ${vh}`);
      } else {
        const rect = container.getBoundingClientRect();
        const relX = (e.clientX - rect.left) / container.clientWidth;
        const relY = (e.clientY - rect.top) / container.clientHeight;
        const factor = e.deltaY > 0 ? 1.12 : 0.89;
        const nw = vw * factor, nh = vh * factor;
        const nx = vx + relX * (vw - nw);
        const ny = vy + relY * (vh - nh);
        svg.setAttribute('viewBox', `${nx} ${ny} ${nw} ${nh}`);
      }
    }, { passive: false });

    let drag = false, dsx, dsy, dvb;
    container.addEventListener('mousedown', (e) => {
      if (e.target.closest('.toolbar') || e.target.closest('.topbar') || e.target.closest('.node-group')) return;
      drag = true;
      dsx = e.clientX; dsy = e.clientY;
      const vb = svg.getAttribute('viewBox').split(' ').map(Number);
      dvb = { x: vb[0], y: vb[1], w: vb[2], h: vb[3] };
      container.style.cursor = 'grabbing';
    });
    window.addEventListener('mousemove', (e) => {
      if (!drag) return;
      const dx = e.clientX - dsx, dy = e.clientY - dsy;
      const sx = dvb.w / container.clientWidth, sy = dvb.h / container.clientHeight;
      svg.setAttribute('viewBox', `${dvb.x - dx * sx} ${dvb.y - dy * sy} ${dvb.w} ${dvb.h}`);
    });
    window.addEventListener('mouseup', () => { if (drag) { drag = false; container.style.cursor = 'grab'; } });

    let tsx, tsy, tvb;
    container.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1 && !e.target.closest('.toolbar') && !e.target.closest('.topbar')) {
        tsx = e.touches[0].clientX; tsy = e.touches[0].clientY;
        const vb = svg.getAttribute('viewBox').split(' ').map(Number);
        tvb = { x: vb[0], y: vb[1], w: vb[2], h: vb[3] };
      }
    }, { passive: true });
    container.addEventListener('touchmove', (e) => {
      if (e.touches.length === 1 && tvb) {
        e.preventDefault();
        const dx = e.touches[0].clientX - tsx, dy = e.touches[0].clientY - tsy;
        const sx = tvb.w / container.clientWidth, sy = tvb.h / container.clientHeight;
        svg.setAttribute('viewBox', `${tvb.x - dx * sx} ${tvb.y - dy * sy} ${tvb.w} ${tvb.h}`);
      }
    }, { passive: false });
    container.addEventListener('touchend', () => { tvb = null; }, { passive: true });
  }

  // ================================================================
  //  INIT
  // ================================================================

  renderTopbar();
  state.currentRoot = buildTree();
  assignColors(state.currentRoot, 0, 0);
  needsViewFit = true;
  render();
  setupEvents();
})();
