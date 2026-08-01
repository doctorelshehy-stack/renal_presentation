const path = '/home/mohamed/.local/share/pi-node/node-v22.23.0-linux-x64/lib/node_modules/playwright';
const { chromium } = require(path);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 900 } });
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push('CONSOLE: ' + msg.text()); });
  page.on('pageerror', err => errors.push('PAGEERROR: ' + err.message));

  const url = 'file:///media/mohamed/projects4/renal/%20internal%20medcine%20topics/Nephrology_MindMaps.html';
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(800);

  // 1. Default view (folder 1, collapsed): should show root + 7 branches nicely sized
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot5_default.png' });

  // 2. Expand topic 1 only, then focus-zoom into its "Causes" area by clicking a node card
  const toggles = await page.$$('.toggle-circle');
  await toggles[1].click(); // expand topic 1 (Principles of Glomerulopathies)
  await page.waitForTimeout(700);
  // click the "Definition" sub-node card (2nd level) to focus-zoom
  const nodeCards = await page.$$('.node-group:not(.is-root) .node-bg');
  // nodeCards[0] = topic 1 card, nodeCards[1] = Definition card
  await nodeCards[1].click({ force: true });
  await page.waitForTimeout(800);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot6_focus.png' });

  // 3. Expand-all then collapse-all on folder 1: view must reset to fit root+branches
  await page.click('#expand-all-btn'); await page.waitForTimeout(2000);
  await page.click('#collapse-all-btn'); await page.waitForTimeout(1200);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot7_after_collapse.png' });

  // measure collapsed node sizes: root card should be substantial (not tiny)
  const sizes = await page.$$eval('.node-group:not(.is-root) .node-bg', els =>
    els.slice(0, 7).map(r => ({ w: Math.round(+r.getAttribute('width')), h: Math.round(+r.getAttribute('height')) })));
  console.log('collapsed branch node sizes:', JSON.stringify(sizes));

  const vb = await page.$eval('#mindmap-svg', s => s.getAttribute('viewBox'));
  console.log('viewBox after collapse:', vb);

  console.log('JS ERRORS:', errors.length ? errors : 'none');
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
