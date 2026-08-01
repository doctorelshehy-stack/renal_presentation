const fs = require('fs');
const path = require('path');

const dir = '/media/mohamed/projects4/renal/ internal medcine topics/_build';

// Load data
const part1 = fs.readFileSync(path.join(dir, 'data_part1.js'), 'utf8');
const part2 = fs.readFileSync(path.join(dir, 'data_part2.js'), 'utf8');
const part3 = fs.readFileSync(path.join(dir, 'data_part3.js'), 'utf8');
const part4 = fs.readFileSync(path.join(dir, 'data_part4.js'), 'utf8');
const part5 = fs.readFileSync(path.join(dir, 'data_part5.js'), 'utf8');
const engine = fs.readFileSync(path.join(dir, 'engine.js'), 'utf8');

// Evaluate data in a sandbox
const folders = {};
function load(code, name) {
  const fn = new Function(code + `; return typeof ${name} !== 'undefined' ? ${name} : null;`);
  const v = fn();
  if (!v) throw new Error('failed to load ' + name);
  return v;
}
const f1 = load(part1, 'folderGlomerular');
const f2 = load(part2, 'folderAKI');
const f3 = load(part3, 'folderCKD');
const f4 = load(part4, 'folderElectrolytes');
const f5 = load(part5, 'folderStructural');

// Validation
function walk(n, pathStr, issues) {
  if (!n || typeof n.label !== 'string' || !n.label.trim()) {
    issues.push('Empty/missing label at ' + pathStr);
    return;
  }
  if (n.label.length > 400) issues.push('Very long label (' + n.label.length + ') at ' + pathStr);
  if (n.children) {
    if (!Array.isArray(n.children)) issues.push('children not array at ' + pathStr);
    else n.children.forEach((c, i) => walk(c, pathStr + ' > ' + n.label.slice(0, 40), issues));
  }
}
function count(n) {
  let c = 1;
  if (n.children) for (const ch of n.children) c += count(ch);
  return c;
}

const all = [['01 Glomerular Diseases', f1], ['02 Acute Kidney Injury', f2], ['03 CKD & RRT', f3], ['04 Electrolytes & Acid-Base', f4], ['05 Structural & Vascular', f5]];
let totalNodes = 0, totalIssues = 0;
for (const [name, f] of all) {
  const issues = [];
  walk(f, name, issues);
  const n = count(f);
  totalNodes += n;
  console.log(`${name}: ${n} nodes, ${f.children.length} topics, issues=${issues.length}`);
  issues.forEach(i => console.log('   ! ' + i));
  totalIssues += issues.length;
}
console.log('TOTAL nodes:', totalNodes, '| issues:', totalIssues);

// Read template
const template = fs.readFileSync('/home/mohamed/.pi/agent/skills/notebook-lm-mindmap/assets/template.html', 'utf8');

// Split template: everything before the first <script> stays; replace the whole script block with data + engine
const scriptStart = template.indexOf('<script>');
const headPart = template.slice(0, scriptStart + '<script>'.length);
const tailPart = '\n</script>\n</body>\n</html>\n';

// Update title
const newTitle = '<title>Nephrology Mind Maps — Internal Medicine · Dr. Hassan Abd-Elhady</title>';
const headPart2 = headPart.replace(/<title>.*<\/title>/, newTitle);
const headPart3 = headPart2.replace('aria-label="Medical disorder topics"', 'aria-label="Nephrology units — one mind map per folder"');

const dataBlock = [
  '// ============================================================',
  '// NEPHROLOGY — INTERNAL MEDICINE (Dr. Hassan Abd-Elhady, Menoufia University)',
  '// One mind map per folder, selectable from the top tab bar.',
  '// Full content preserved — nothing summarized or omitted.',
  '// ============================================================',
  part1, part2, part3, part4, part5, engine
].join('\n\n');

const out = headPart3 + dataBlock + tailPart;

const outPath = path.join('/media/mohamed/projects4/renal/ internal medcine topics', 'Nephrology_MindMaps.html');
fs.writeFileSync(outPath, out);
console.log('Wrote:', outPath, '| size:', fs.statSync(outPath).size, 'bytes');
