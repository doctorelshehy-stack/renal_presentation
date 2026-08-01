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

  // 1. Tab bar present with 5 folder tabs
  const tabs = await page.$$eval('.tab-btn', els => els.map(e => e.textContent.trim()));
  console.log('TABS:', tabs.length, tabs.map(t => t.slice(0, 40)).join(' | '));

  // 2. Root label
  const rootLabel = await page.$eval('.is-root .node-text', el => el.textContent.trim());
  console.log('ROOT:', rootLabel);

  // 3. Branch count on folder 1
  let branches = await page.$$eval('.node-group:not(.is-root)', els => els.length);
  console.log('VISIBLE BRANCHES (folder 1 collapsed):', branches);

  // 4. Switch to folder 2 (AKI)
  await page.click('.tab-btn:nth-child(2)');
  await page.waitForTimeout(500);
  const root2 = await page.$eval('.is-root .node-text', el => el.textContent.trim());
  console.log('AFTER TAB 2 ROOT:', root2);
  const branches2 = await page.$$eval('.node-group:not(.is-root)', els => els.length);
  console.log('FOLDER 2 BRANCHES:', branches2);

  // 5. Switch to folder 5
  await page.click('.tab-btn:nth-child(5)');
  await page.waitForTimeout(500);
  const root5 = await page.$eval('.is-root .node-text', el => el.textContent.trim());
  console.log('AFTER TAB 5 ROOT:', root5);

  // 6. Expand all on folder 5
  await page.click('#expand-all-btn');
  await page.waitForTimeout(1200);
  const nodes5 = await page.$$eval('.node-group', els => els.length);
  console.log('FOLDER 5 EXPANDED NODES:', nodes5);

  // 7. Back to folder 1, expand all (heaviest)
  await page.click('.tab-btn:nth-child(1)');
  await page.waitForTimeout(400);
  await page.click('#expand-all-btn');
  await page.waitForTimeout(2500);
  const nodes1 = await page.$$eval('.node-group', els => els.length);
  console.log('FOLDER 1 EXPANDED NODES:', nodes1);

  // 8. Toggle a specific node: click the '+' of first branch child
  const toggleCount = await page.$$eval('.toggle-text', els => els.length);
  console.log('TOGGLE BUTTONS VISIBLE:', toggleCount);

  // 9. Check no text is truncated: every tspan should have text
  const emptyTs = await page.$$eval('tspan.label', els => els.filter(e => !e.textContent.trim()).length);
  console.log('EMPTY TSPANS:', emptyTs);

  // 10. Screenshot of expanded folder 1
  await page.screenshot({ path: '/media/mohamed/projects4/renal/ internal medcine topics/_build/shot2_expanded.png' });

  console.log('JS ERRORS:', errors.length ? errors : 'none');
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
