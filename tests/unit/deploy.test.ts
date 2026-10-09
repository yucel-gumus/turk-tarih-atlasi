import { it, expect } from 'vitest';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

it('preserves publication history, excludes legacy dist Git metadata and rejects dirty source', () => {
  const temp = mkdtempSync(path.join(tmpdir(), 'atlas-deploy-test-'));
  const checkout = path.join(temp, 'source');
  const remote = path.join(temp, 'remote.git');
  const env = { ...process.env, GIT_AUTHOR_NAME: 'Atlas Test', GIT_AUTHOR_EMAIL: 'atlas@example.invalid', GIT_COMMITTER_NAME: 'Atlas Test', GIT_COMMITTER_EMAIL: 'atlas@example.invalid' };
  const git = (args: string[], cwd = checkout) => execFileSync('git', args, { cwd, env, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
  try {
    mkdirSync(path.join(checkout, 'scripts'), { recursive: true });
    mkdirSync(path.join(checkout, 'dist', '.git'), { recursive: true });
    writeFileSync(path.join(checkout, 'scripts', 'deploy.mjs'), readFileSync('scripts/deploy.mjs'));
    writeFileSync(path.join(checkout, '.gitignore'), 'dist/\n');
    writeFileSync(path.join(checkout, 'dist', 'index.html'), '<h1>Verified atlas</h1>');
    writeFileSync(path.join(checkout, 'dist', '.git', 'unwanted'), 'legacy');
    git(['init', '-q', '-b', 'main']);
    git(['add', '.']); git(['commit', '-qm', 'source']);
    git(['branch', 'gh-pages']);
    git(['init', '--bare', '-q', remote]);
    git(['remote', 'add', 'origin', remote]);
    git(['push', '-q', 'origin', 'main', 'gh-pages']);
    const revision = git(['rev-parse', 'HEAD']);
    execFileSync(process.execPath, ['scripts/deploy.mjs'], { cwd: checkout, env, stdio: 'pipe' });
    const published = git(['--git-dir', remote, 'show', 'gh-pages:release.json']);
    expect(JSON.parse(published).revision).toBe(revision);
    expect(git(['--git-dir', remote, 'rev-list', '--count', 'gh-pages'])).toBe('2');
    expect(git(['--git-dir', remote, 'ls-tree', '--name-only', 'gh-pages'])).toBe('.nojekyll\nindex.html\nrelease.json');
    writeFileSync(path.join(checkout, '.gitignore'), 'dist/\nchanged\n');
    expect(() => execFileSync(process.execPath, ['scripts/deploy.mjs'], { cwd: checkout, env, stdio: 'pipe' })).toThrow();
    expect(git(['--git-dir', remote, 'rev-list', '--count', 'gh-pages'])).toBe('2');
  } finally { rmSync(temp, { recursive: true, force: true }); }
});
