const path = '/home/mohamed/.local/share/pi-node/node-v22.23.0-linux-x64/lib/node_modules/playwright';
const { chromium } = require(path);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 900 } });
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.message));

  const url = 'file:///media/mohamed/projects4/renal/%20internal%20medcine%20topics/Nephrology_MindMaps.html';
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(700);

  // Screenshot A: default view folder 1
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/final_a_default.png' });

  // Expand topic 1 (Principles) then focus-zoom "Definition"
  const toggles = await page.$$('.toggle-circle');
  await toggles[1].click(); await page.waitForTimeout(600);
  const cards = await page.$$('.node-group:not(.is-root) .node-bg');
  await cards[1].click({ force: true }); await page.waitForTimeout(900);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/final_b_focus.png' });

  // Expand all on folder 3 (CKD) — densest topic, screenshot
  await page.click('.tab-btn:nth-child(3)'); await page.waitForTimeout(400);
  await page.click('#expand-all-btn'); await page.waitForTimeout(1800);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/final_c_ckd.png' });

  // collapse-all back to clean root view
  await page.click('#collapse-all-btn'); await page.waitForTimeout(1000);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/final_d_clean.png' });

  console.log('JS ERRORS:', errors.length ? errors : 'none');
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
