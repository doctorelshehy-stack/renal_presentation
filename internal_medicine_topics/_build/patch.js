// Patch the assembled HTML: toolbar above topbar + expand-all reset already in engine
const fs = require('fs');
const file = '/media/mohamed/projects4/renal/ internal medcine topics/Nephrology_MindMaps.html';
let h = fs.readFileSync(file, 'utf8');

const fixes = [
  // keep tabs clear of the floating toolbar
  ['    padding: 8px 12px;',
   '    padding: 8px 12px;\n    padding-right: 340px; /* keep tabs clear of the floating toolbar */'],
  // toolbar above topbar so its buttons are clickable
  ['position: fixed; top: 16px; right: 16px; z-index: 100;',
   'position: fixed; top: 16px; right: 16px; z-index: 300;'],
  // mobile: same two fixes
  ['.topbar { padding: 6px 8px; gap: 2px; }',
   '.topbar { padding: 6px 8px; padding-right: 270px; gap: 2px; }']
];

let applied = 0;
for (const [from, to] of fixes) {
  const n = h.split(from).length - 1;
  h = h.split(from).join(to);
  applied += n;
  console.log(`'${from.slice(0, 45)}...' -> ${n} occurrence(s)`);
}
fs.writeFileSync(file, h);
console.log('applied', applied, 'fixes; final size', h.length);
