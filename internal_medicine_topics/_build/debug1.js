const path = '/home/mohamed/.local/share/pi-node/node-v22.23.0-linux-x64/lib/node_modules/playwright';
const { chromium } = require(path);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 900 } });
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push('CONSOLE@' + errors.length + ': ' + msg.text()); });
  page.on('pageerror', err => errors.push('PAGEERROR: ' + err.message));

  const url = 'file:///media/mohamed/projects4/renal/%20internal%20medcine%20topics/Nephrology_MindMaps.html';
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(700);
  const vb0 = await page.$eval('#mindmap-svg', s => s.getAttribute('viewBox'));
  console.log('viewBox initial:', vb0);

  // Expand all on folder 1
  await page.click('#expand-all-btn'); await page.waitForTimeout(2500);
  const vb1 = await page.$eval('#mindmap-svg', s => s.getAttribute('viewBox'));
  console.log('viewBox after expand-all:', vb1);

  // Collapse all
  await page.click('#collapse-all-btn'); await page.waitForTimeout(400);
  const vb2 = await page.$eval('#mindmap-svg', s => s.getAttribute('viewBox'));
  console.log('viewBox after collapse-all (400ms):', vb2);
  await page.waitForTimeout(800);
  const vb3 = await page.$eval('#mindmap-svg', s => s.getAttribute('viewBox'));
  console.log('viewBox after collapse-all (1200ms):', vb3);

  // Inspect layout of collapsed tree: y positions of root children
  const ys = await page.$$eval('.node-group', els => els.map(e => {
    const t = e.getAttribute('transform');
    const r = e.querySelector('.node-bg');
    return { label: (e.querySelector('tspan')||{}).textContent || '', y: t, h: r ? r.getAttribute('height') : null };
  }));
  console.log('NODE COUNT (collapsed):', ys.length);
  ys.forEach(n => console.log('  ', n.label.slice(0, 34), '|', n.y, 'h=', n.h));

  console.log('ERRORS:', errors.length ? errors.join('\n') : 'none');
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
