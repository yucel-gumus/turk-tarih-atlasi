import { execFileSync } from 'node:child_process';
import { mkdtempSync, readdirSync, rmSync, cpSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
const run = (args, cwd = root) => execFileSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'inherit'] }).trim();
if (!existsSync(path.join(root, 'dist/index.html'))) throw new Error('Build output is missing. Run npm run deploy.');
if (run(['status', '--porcelain'])) throw new Error('Commit reviewed changes before deploying.');
const revision = run(['rev-parse', 'HEAD']);
const origin = run(['remote', 'get-url', 'origin']);
const releaseDir = mkdtempSync(path.join(tmpdir(), 'atlas-release-'));
try {
  run(['init', '-q'], releaseDir);
  run(['remote', 'add', 'origin', origin], releaseDir);
  // Preserve publication history and reject concurrent releases instead of force pushing.
  run(['fetch', '--depth=1', 'origin', 'gh-pages'], releaseDir);
  run(['checkout', '-q', '-b', 'gh-pages', 'FETCH_HEAD'], releaseDir);
  for (const file of readdirSync(releaseDir)) {
    if (file !== '.git') rmSync(path.join(releaseDir, file), { recursive: true, force: true });
  }
  for (const file of readdirSync(path.join(root, 'dist'))) {
    // Legacy deployments initialized a Git repository inside dist. Never copy
    // that metadata into the publication checkout.
    if (file !== '.git') cpSync(path.join(root, 'dist', file), path.join(releaseDir, file), { recursive: true });
  }
  writeFileSync(path.join(releaseDir, '.nojekyll'), '');
  writeFileSync(path.join(releaseDir, 'release.json'), JSON.stringify({ revision, publishedAt: new Date().toISOString() }, null, 2) + '\n');
  run(['add', '-A'], releaseDir);
  run(['commit', '-m', `Deploy atlas ${revision.slice(0, 12)}`], releaseDir);
  run(['push', 'origin', 'gh-pages'], releaseDir);
  console.log(`Published gh-pages for ${revision}. Verify GitHub Pages build and release.json before claiming it is live.`);
} finally {
  rmSync(releaseDir, { recursive: true, force: true });
}
