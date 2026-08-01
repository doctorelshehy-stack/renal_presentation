/* ============================================
   Renal Medicine — Presentation Library
   Main Application Logic
   ============================================ */

(function () {
  'use strict';

  /* --- Constants --- */
  const STORAGE_KEY = 'renal_presenter';
  const ANIMATION_DURATION = 250;

  /* --- State --- */
  let manifest = null;
  let currentTopic = null;
  let currentSlide = 0;
  let visitedSlides = new Set();
  let sidebarOpen = false;
  let autoHideTimer = null;

  /* ============================================
     UTILITIES
     ============================================ */

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return [...(ctx || document).querySelectorAll(sel)]; }

  function loadManifest() {
    // Try inline manifest first (works on file:// protocol)
    if (window.__MANIFEST__) {
      return Promise.resolve(window.__MANIFEST__);
    }
    // Fallback: fetch from server
    return fetch('manifest.json')
      .then(r => { if (!r.ok) throw new Error('Manifest not found'); return r.json(); })
      .catch(err => {
        console.error('Failed to load manifest:', err);
        return { topics: [] };
      });
  }

  /* --- LocalStorage helpers --- */
  function getState() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch { return {}; }
  }

  function saveState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn('LocalStorage save failed:', e);
    }
  }

  function getProgress() {
    return getState().progress || {};
  }

  function saveTopicProgress(topicId, slideIndex, totalSlides) {
    const state = getState();
    if (!state.progress) state.progress = {};
    const tp = state.progress[topicId] || { visited: [], lastSlide: 0 };
    if (!tp.visited.includes(slideIndex)) tp.visited.push(slideIndex);
    tp.lastSlide = slideIndex;
    tp.completed = tp.visited.length >= totalSlides;
    state.progress[topicId] = tp;
    state.lastSession = { topicId, slideIndex, timestamp: Date.now() };
    saveState(state);
  }

  function getLastSession() {
    return getState().lastSession || null;
  }

  /* ============================================
     HOMEPAGE
     ============================================ */

  function renderHomepage() {
    if (!manifest || !manifest.topics.length) {
      document.body.innerHTML = `
        <div class="home-container">
          <div class="hero">
            <h1>Renal Medicine</h1>
            <p class="subtitle">Gastrointestinal Module</p>
          </div>
          <div style="text-align:center;padding:60px 20px;color:var(--text-secondary)">
            <p>No presentations found.</p>
            <p style="margin-top:8px;font-size:0.85rem">Make sure manifest.json is in the same directory.</p>
          </div>
        </div>`;
      return;
    }

    const progress = getProgress();
    const actualTopics = manifest.topics.filter(t => t.type !== 'heading');
    const totalSlides = actualTopics.reduce((s, t) => s + (t.slideCount || 0), 0);
    const totalCompleted = actualTopics.filter(t => {
      const p = progress[t.id];
      return p && p.completed;
    }).length;

    let html = `
      <div class="home-container">
        <div class="hero">
          <div class="hero-content">
            <h1>${manifest.title || 'Renal Medicine'}</h1>
            <p class="subtitle">${manifest.subtitle || 'Gastrointestinal Module'}</p>
            <div class="stats">
              <div class="stat">
                <span class="stat-value">${actualTopics.length}</span>
                <span class="stat-label">Topics</span>
              </div>
              <div class="stat">
                <span class="stat-value">${totalSlides}</span>
                <span class="stat-label">Slides</span>
              </div>
              <div class="stat">
                <span class="stat-value">${totalCompleted}</span>
                <span class="stat-label">Completed</span>
              </div>
            </div>
          </div>
        </div>

        <div class="search-container">
          <span class="search-icon">🔍</span>
          <input type="text" class="search-input" placeholder="Search topics..." id="searchInput" autocomplete="off">
        </div>

        <div class="topics-grid" id="topicsGrid">
          ${renderTopicCards(progress)}
        </div>
      </div>

      <style>
        .section-heading {
          grid-column: 1 / -1;
          display: flex;
          align-items: center;
          gap: 14px;
          padding: 28px 0 8px 0;
          margin-top: 12px;
          border-bottom: 2px solid var(--border-color, #e0e0e0);
        }
        .section-heading .section-icon {
          font-size: 28px;
          line-height: 1;
        }
        .section-heading .section-text {
          flex: 1;
        }
        .section-heading .section-title {
          font-family: 'Segoe UI', system-ui, sans-serif;
          font-size: 20px;
          font-weight: 700;
          color: var(--text-primary, #1a1a2e);
          margin: 0;
          line-height: 1.3;
        }
        .section-heading .section-desc {
          font-family: 'Segoe UI', system-ui, sans-serif;
          font-size: 13px;
          color: var(--text-secondary, #666);
          margin: 2px 0 0 0;
        }
        [data-theme="dark"] .section-heading {
          border-bottom-color: var(--border-color, #2d2d3d);
        }
        [data-theme="dark"] .section-heading .section-title {
          color: var(--text-primary, #e6e6e6);
        }
        [data-theme="dark"] .section-heading .section-desc {
          color: var(--text-secondary, #999);
        }
      </style>

      <div class="modal-overlay" id="resumeModal">
        <div class="modal">
          <h3>Resume previous session?</h3>
          <p id="resumeModalText">Continue where you left off.</p>
          <div class="modal-actions">
            <button class="modal-btn secondary" id="startOverBtn">Start Over</button>
            <button class="modal-btn primary" id="continueBtn">Continue</button>
          </div>
        </div>
      </div>`;

    document.body.innerHTML = html;
    document.body.classList.remove('viewer-body');

    // Event: search
    const searchInput = $('#searchInput');
    searchInput.addEventListener('input', () => {
      const q = searchInput.value.toLowerCase().trim();
      // Show/hide cards and their headings during search
      const grid = $('#topicsGrid');
      if (!q) {
        $$('#topicsGrid > div').forEach(el => el.style.display = '');
      } else {
        let lastHeading = null;
        $$('#topicsGrid > div').forEach(el => {
          if (el.dataset.heading === 'true') {
            lastHeading = el;
            el.style.display = 'none';
          } else if (el.dataset.topicId) {
            const text = el.dataset.searchText || '';
            const match = text.includes(q);
            el.style.display = match ? '' : 'none';
            if (match && lastHeading) {
              lastHeading.style.display = '';
            }
          }
        });
      }
    });

    // Event: card clicks
    $$('.topic-card').forEach(card => {
      card.addEventListener('click', (e) => {
        // If clicking the mindmap link, let it open in a new tab naturally
        if (e.target.closest('.card-mindmap')) {
          return;
        }
        const topicId = card.dataset.topicId;
        openTopic(topicId);
      });
    });

    // Check for resume
    checkResumeSession();
  }

  function renderTopicCards(progress) {
    return manifest.topics.map((topic, idx) => {
      // Section heading
      if (topic.type === 'heading') {
        return `
          <div class="section-heading" data-heading="true" style="animation-delay:${idx * 0.05}s">
            <div class="section-icon">${topic.icon || '📌'}</div>
            <div class="section-text">
              <div class="section-title">${topic.title}</div>
              ${topic.description ? `<div class="section-desc">${topic.description}</div>` : ''}
            </div>
          </div>`;
      }

      // Regular topic card
      const p = progress[topic.id];
      const visited = p ? p.visited.length : 0;
      const pct = Math.round((visited / topic.slideCount) * 100);
      const isCompleted = p && p.completed;
      const isStarted = visited > 0 && !isCompleted;
      const statusClass = isCompleted ? 'completed' : (isStarted ? 'continue' : 'new');
      const statusText = isCompleted ? 'Completed' : (isStarted ? 'Continue' : 'Start');
      const cardClass = isCompleted ? 'topic-card completed' : 'topic-card';

      return `
        <div class="${cardClass}" data-topic-id="${topic.id}" data-search-text="${(topic.title + ' ' + topic.description).toLowerCase()}" style="animation-delay:${idx * 0.05}s">
          <div class="card-header">
            <div class="card-icon">${topic.icon || '📄'}</div>
            <div class="card-info">
              <div class="card-title">${topic.title}</div>
              <div class="card-description">${topic.description}</div>
            </div>
          </div>
          <div class="card-meta">
            <span class="card-slides">${topic.slideCount} Slides</span>
            <div class="card-progress">
              <div class="progress-bar">
                <div class="progress-fill ${isCompleted ? 'complete' : ''}" style="width:${pct}%"></div>
              </div>
              <span class="card-status ${statusClass}">${visited}/${topic.slideCount}</span>
            </div>
          </div>
          <div class="card-actions">
            <div class="card-open">${statusText} →</div>
            ${topic.mindmapPath ? `<a class="card-mindmap" href="${topic.mindmapPath}" target="_blank" title="Open Mind Map">🧠</a>` : ''}
          </div>
        </div>`;
    }).join('');
  }

  function checkResumeSession() {
    const session = getLastSession();
    if (!session || !session.topicId) return;

    const topic = manifest.topics.find(t => t.id === session.topicId);
    if (!topic) return;

    const modal = $('#resumeModal');
    const text = $('#resumeModalText');
    const progress = getProgress();
    const p = progress[session.topicId];
    const visited = p ? p.visited.length : 0;

    text.textContent = `${topic.title} — Slide ${session.slideIndex + 1} of ${topic.slideCount} (${visited} visited)`;

    modal.classList.add('active');

    $('#continueBtn').onclick = () => {
      modal.classList.remove('active');
      openTopic(session.topicId, session.slideIndex);
    };

    $('#startOverBtn').onclick = () => {
      modal.classList.remove('active');
      // Clear last session so modal won't show again
      const state = getState();
      delete state.lastSession;
      saveState(state);
    };
  }

  /* ============================================
     VIEWER
     ============================================ */

  function openTopic(topicId, startSlide) {
    const topic = manifest.topics.find(t => t.id === topicId);
    if (!topic) return;

    currentTopic = topic;
    currentSlide = startSlide || 0;
    visitedSlides = new Set();

    // Load progress
    const progress = getProgress();
    const p = progress[topicId];
    if (p && p.visited) {
      p.visited.forEach(v => visitedSlides.add(v));
    }

    // Navigate
    const url = `viewer.html?topic=${encodeURIComponent(topicId)}&slide=${currentSlide}`;
    window.location.href = url;
  }

  function initViewer() {
    const params = new URLSearchParams(window.location.search);
    const topicId = params.get('topic');
    const slideParam = parseInt(params.get('slide'), 10);

    if (!topicId || !manifest) {
      window.location.href = 'index.html';
      return;
    }

    const topic = manifest.topics.find(t => t.id === topicId);
    if (!topic) {
      window.location.href = 'index.html';
      return;
    }

    currentTopic = topic;
    currentSlide = isNaN(slideParam) ? 0 : Math.max(0, Math.min(slideParam, topic.slideCount - 1));

    // Load visited
    const progress = getProgress();
    const p = progress[topicId];
    if (p && p.visited) p.visited.forEach(v => visitedSlides.add(v));

    document.body.classList.add('viewer-body');
    renderViewer();
    loadSlide(currentSlide);
    updateURL();
    saveProgress();
  }

  function renderViewer() {
    const topic = currentTopic;
    let sidebarItems = '';
    for (let i = 0; i < topic.slideCount; i++) {
      const title = topic.slideTitles ? topic.slideTitles[i] : `Slide ${i + 1}`;
      sidebarItems += `
        <div class="sidebar-item" data-slide="${i}">
          <span class="slide-num">${i + 1}</span>
          <span class="slide-title">${title}</span>
        </div>`;
    }

    document.body.innerHTML = `
      <!-- Navbar -->
      <nav class="navbar" id="navbar">
        <div class="nav-left">
          <button class="nav-btn" id="backBtn" title="Back to Home (Esc)">←</button>
          <button class="nav-btn" id="sidebarToggle" title="Toggle Sidebar">☰</button>
          <span class="nav-topic">${topic.title}</span>
        </div>
        <div class="nav-center">
          <span class="nav-counter" id="slideCounter">Slide ${currentSlide + 1} / ${topic.slideCount}</span>
        </div>
        <div class="nav-right">
          <div class="jump-form">
            <span class="jump-label">Go to:</span>
            <input type="number" class="jump-input" id="jumpInput" min="1" max="${topic.slideCount}" value="${currentSlide + 1}">
            <button class="jump-btn" id="jumpBtn">Go</button>
          </div>
          <button class="nav-btn" id="fullscreenBtn" title="Fullscreen (F)">⛶</button>
          <button class="nav-btn" id="themeBtn" title="Toggle Theme">◐</button>
          <button class="nav-btn" id="helpBtn" title="Keyboard Shortcuts (?)">?</button>
        </div>
      </nav>

      <!-- Top Progress -->
      <div class="top-progress">
        <div class="top-progress-fill" id="topProgressFill"></div>
      </div>

      <!-- Sidebar -->
      <aside class="sidebar" id="sidebar">
        ${sidebarItems}
      </aside>

      <!-- Slide Area -->
      <main class="slide-area" id="slideArea">
        <button class="slide-nav-btn prev" id="prevBtn" title="Previous (←)">‹</button>
        <div class="slide-wrapper" id="slideWrapper">
          <div class="spinner" id="slideSpinner"></div>
        </div>
        <button class="slide-nav-btn next" id="nextBtn" title="Next (→)">›</button>
      </main>

      <!-- Keyboard Help -->
      <div class="kbd-help-overlay" id="kbdHelp">
        <div class="kbd-help">
          <h3>Keyboard Shortcuts</h3>
          <div class="kbd-grid">
            <div class="kbd-row"><span class="kbd-label">Previous</span><kbd>←</kbd> <kbd>A</kbd> <kbd>PageUp</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Next</span><kbd>→</kbd> <kbd>D</kbd> <kbd>PageDown</kbd> <kbd>Space</kbd></div>
            <div class="kbd-row"><span class="kbd-label">First slide</span><kbd>Home</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Last slide</span><kbd>End</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Jump to slide</span><kbd>Ctrl+G</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Fullscreen</span><kbd>F</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Sidebar</span><kbd>S</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Help</span><kbd>?</kbd></div>
            <div class="kbd-row"><span class="kbd-label">Back to home</span><kbd>Esc</kbd></div>
          </div>
          <div style="text-align:center;margin-top:20px">
            <button class="modal-btn secondary" id="closeKbdHelp" style="display:inline-block;width:auto;padding:8px 24px">Close</button>
          </div>
        </div>
      </div>`;

    // Apply theme
    const savedTheme = localStorage.getItem(STORAGE_KEY + '_theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);

    // Bind events
    bindViewerEvents();
  }

  function bindViewerEvents() {
    // Navigation buttons
    $('#backBtn').addEventListener('click', () => { window.location.href = 'index.html'; });
    $('#prevBtn').addEventListener('click', () => navigate(-1));
    $('#nextBtn').addEventListener('click', () => navigate(1));

    // Sidebar toggle
    $('#sidebarToggle').addEventListener('click', toggleSidebar);

    // Sidebar items
    $$('.sidebar-item').forEach(item => {
      item.addEventListener('click', () => {
        const idx = parseInt(item.dataset.slide, 10);
        goToSlide(idx);
      });
    });

    // Jump to slide
    $('#jumpBtn').addEventListener('click', jumpToSlide);
    $('#jumpInput').addEventListener('keydown', (e) => {
      if (e.key === 'Enter') jumpToSlide();
    });

    // Fullscreen
    $('#fullscreenBtn').addEventListener('click', toggleFullscreen);

    // Theme
    $('#themeBtn').addEventListener('click', toggleTheme);

    // Keyboard help
    $('#helpBtn').addEventListener('click', () => {
      $('#kbdHelp').classList.toggle('active');
    });
    $('#closeKbdHelp').addEventListener('click', () => {
      $('#kbdHelp').classList.remove('active');
    });

    // Keyboard
    document.addEventListener('keydown', handleKeyboard);

    // Touch swipe
    let touchStartX = 0;
    let touchStartY = 0;
    document.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });
    document.addEventListener('touchend', (e) => {
      const dx = e.changedTouches[0].screenX - touchStartX;
      const dy = e.changedTouches[0].screenY - touchStartY;
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 50) {
        if (dx > 0) navigate(-1);
        else navigate(1);
      }
    }, { passive: true });

    // Mouse wheel
    let wheelTimeout = null;
    document.addEventListener('wheel', (e) => {
      if (wheelTimeout) return;
      wheelTimeout = setTimeout(() => { wheelTimeout = null; }, 400);
      if (e.deltaY > 30) navigate(1);
      else if (e.deltaY < -30) navigate(-1);
    }, { passive: true });

    // Auto-hide navbar
    const slideArea = $('#slideArea');
    slideArea.addEventListener('mousemove', () => {
      $('#navbar').classList.remove('hidden');
      clearTimeout(autoHideTimer);
      autoHideTimer = setTimeout(() => {
        if (document.fullscreenElement) {
          $('#navbar').classList.add('hidden');
        }
      }, 3000);
    });
  }

  /* --- Navigation --- */
  function navigate(dir) {
    const newSlide = currentSlide + dir;
    if (newSlide >= 0 && newSlide < currentTopic.slideCount) {
      goToSlide(newSlide);
    }
  }

  function goToSlide(idx) {
    if (idx < 0 || idx >= currentTopic.slideCount || idx === currentSlide) return;
    currentSlide = idx;
    loadSlide(idx);
    updateURL();
    saveProgress();
    updateUI();
  }

  function jumpToSlide() {
    const input = $('#jumpInput');
    const val = parseInt(input.value, 10);
    if (isNaN(val) || val < 1 || val > currentTopic.slideCount) {
      input.value = currentSlide + 1;
      input.style.borderColor = 'var(--danger)';
      setTimeout(() => { input.style.borderColor = ''; }, 1000);
      return;
    }
    goToSlide(val - 1);
  }

  /* --- Slide Loading (Lazy + Preload) --- */
  function loadSlide(idx) {
    const wrapper = $('#slideWrapper');
    const spinner = $('#slideSpinner');
    if (spinner) spinner.style.display = '';

    // Remove old iframe
    const oldIframe = wrapper.querySelector('iframe');
    if (oldIframe) {
      oldIframe.remove();
    }

    // Remove old error
    const oldError = wrapper.querySelector('.error-slide');
    if (oldError) oldError.remove();

    const slideFile = currentTopic.slides[idx];
    const slidePath = `${currentTopic.slidesPath}/${slideFile}`;

    const iframe = document.createElement('iframe');
    iframe.className = 'slide-iframe';
    iframe.style.opacity = '0';
    iframe.style.transition = 'opacity 0.2s ease';
    iframe.title = currentTopic.slideTitles ? currentTopic.slideTitles[idx] : `Slide ${idx + 1}`;
    iframe.setAttribute('aria-label', `Slide ${idx + 1} of ${currentTopic.slideCount}`);

    iframe.onload = () => {
      if (spinner) spinner.style.display = 'none';
      iframe.style.opacity = '1';
      // Preload adjacent slides
      preloadAdjacent(idx);
    };

    iframe.onerror = () => {
      if (spinner) spinner.style.display = 'none';
      showError(idx);
    };

    // Show loading state
    iframe.src = slidePath;
    wrapper.appendChild(iframe);

    // Timeout fallback
    setTimeout(() => {
      if (spinner && spinner.style.display !== 'none') {
        spinner.style.display = 'none';
      }
    }, 5000);
  }

  function preloadAdjacent(idx) {
    const toPreload = [idx - 1, idx + 1];
    toPreload.forEach(i => {
      if (i >= 0 && i < currentTopic.slideCount) {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = `${currentTopic.slidesPath}/${currentTopic.slides[i]}`;
        document.head.appendChild(link);
      }
    });
  }

  function showError(idx) {
    const wrapper = $('#slideWrapper');
    const spinner = $('#slideSpinner');
    if (spinner) spinner.style.display = 'none';

    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-slide';
    errorDiv.innerHTML = `
      <h2>⚠️ Failed to load slide</h2>
      <p>Slide ${idx + 1} could not be loaded.</p>
      <button onclick="location.reload()">Retry</button>`;
    wrapper.appendChild(errorDiv);
  }

  /* --- UI Updates --- */
  function updateUI() {
    // Counter
    const counter = $('#slideCounter');
    if (counter) counter.textContent = `Slide ${currentSlide + 1} / ${currentTopic.slideCount}`;

    // Jump input
    const jumpInput = $('#jumpInput');
    if (jumpInput) jumpInput.value = currentSlide + 1;

    // Progress bar
    const fill = $('#topProgressFill');
    if (fill) {
      const pct = ((currentSlide + 1) / currentTopic.slideCount) * 100;
      fill.style.width = `${pct}%`;
    }

    // Nav buttons
    const prevBtn = $('#prevBtn');
    const nextBtn = $('#nextBtn');
    if (prevBtn) prevBtn.disabled = currentSlide === 0;
    if (nextBtn) nextBtn.disabled = currentSlide === currentTopic.slideCount - 1;

    // Sidebar
    $$('.sidebar-item').forEach((item, i) => {
      item.classList.toggle('active', i === currentSlide);
      item.classList.toggle('visited', visitedSlides.has(i));
    });

    // Scroll active sidebar item into view
    const activeItem = $('.sidebar-item.active');
    if (activeItem) {
      activeItem.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
  }

  function updateURL() {
    const url = `viewer.html?topic=${encodeURIComponent(currentTopic.id)}&slide=${currentSlide}`;
    window.history.pushState({ topic: currentTopic.id, slide: currentSlide }, '', url);
  }

  function saveProgress() {
    visitedSlides.add(currentSlide);
    saveTopicProgress(currentTopic.id, currentSlide, currentTopic.slideCount);
  }

  /* --- Sidebar --- */
  function toggleSidebar() {
    sidebarOpen = !sidebarOpen;
    const sidebar = $('#sidebar');
    const toggle = $('#sidebarToggle');
    if (sidebar) sidebar.classList.toggle('open', sidebarOpen);
    if (toggle) toggle.classList.toggle('active', sidebarOpen);
  }

  /* --- Fullscreen --- */
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen();
    }
  }

  /* --- Theme --- */
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem(STORAGE_KEY + '_theme', next);
  }

  /* --- Keyboard --- */
  function handleKeyboard(e) {
    // Skip if typing in input
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    const kbdHelp = $('#kbdHelp');
    if (kbdHelp && kbdHelp.classList.contains('active')) {
      if (e.key === 'Escape') kbdHelp.classList.remove('active');
      return;
    }

    switch (e.key) {
      case 'ArrowLeft':
      case 'a':
      case 'A':
        e.preventDefault();
        navigate(-1);
        break;
      case 'ArrowRight':
      case 'd':
      case 'D':
      case ' ':
        e.preventDefault();
        navigate(1);
        break;
      case 'PageUp':
        e.preventDefault();
        navigate(-1);
        break;
      case 'PageDown':
        e.preventDefault();
        navigate(1);
        break;
      case 'Home':
        e.preventDefault();
        goToSlide(0);
        break;
      case 'End':
        e.preventDefault();
        goToSlide(currentTopic.slideCount - 1);
        break;
      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;
      case 's':
      case 'S':
        e.preventDefault();
        toggleSidebar();
        break;
      case 'Escape':
        e.preventDefault();
        window.location.href = 'index.html';
        break;
      case '?':
        e.preventDefault();
        if (kbdHelp) kbdHelp.classList.toggle('active');
        break;
      case 'g':
      case 'G':
        if (e.ctrlKey || e.metaKey) {
          e.preventDefault();
          const jumpInput = $('#jumpInput');
          if (jumpInput) jumpInput.focus();
        }
        break;
    }
  }

  /* --- Browser History --- */
  window.addEventListener('popstate', (e) => {
    if (!currentTopic) return;
    const state = e.state;
    if (state && state.topic === currentTopic.id) {
      currentSlide = state.slide;
      loadSlide(currentSlide);
      updateUI();
    }
  });

  /* ============================================
     INIT
     ============================================ */

  async function init() {
    manifest = await loadManifest();

    const isViewer = window.location.pathname.includes('viewer.html');
    if (isViewer) {
      initViewer();
    } else {
      renderHomepage();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
