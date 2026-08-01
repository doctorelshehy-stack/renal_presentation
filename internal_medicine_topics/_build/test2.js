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
  await page.waitForTimeout(700);

  // Toolbar buttons now clickable?
  await page.click('#zoom-in'); await page.waitForTimeout(150);
  await page.click('#zoom-out'); await page.waitForTimeout(150);
  await page.click('#zoom-reset'); await page.waitForTimeout(150);
  console.log('toolbar buttons OK');

  // Expand a topic branch by clicking its + toggle (first topic branch of folder 1)
  const toggles = await page.$$('.toggle-circle');
  await toggles[1].click(); await page.waitForTimeout(600);
  const afterToggle = await page.$$eval('.node-group', els => els.length);
  console.log('nodes after expanding topic 1:', afterToggle);

  // Click a node card to focus-zoom (first child of the first branch)
  const nodes = await page.$$('.node-group:not(.is-root)');
  await nodes[1].click(); await page.waitForTimeout(600);
  const fitDisabled = await page.$eval('#fit-branch-btn', el => el.disabled);
  console.log('fit-branch enabled after focus:', !fitDisabled);

  // Switch to folder 3 & 4, expand all
  await page.click('.tab-btn:nth-child(3)'); await page.waitForTimeout(400);
  await page.click('#expand-all-btn'); await page.waitForTimeout(1500);
  const n3 = await page.$$eval('.node-group', els => els.length);
  console.log('folder 3 expanded:', n3);

  await page.click('.tab-btn:nth-child(4)'); await page.waitForTimeout(400);
  await page.click('#expand-all-btn'); await page.waitForTimeout(1500);
  const n4 = await page.$$eval('.node-group', els => els.length);
  console.log('folder 4 expanded:', n4);

  // Screenshot: folder 4 fully expanded (medium density), then collapse
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot3_folder4.png' });
  await page.click('#collapse-all-btn'); await page.waitForTimeout(500);
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot4_collapsed.png' });

  console.log('JS ERRORS:', errors.length ? errors : 'none');
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
