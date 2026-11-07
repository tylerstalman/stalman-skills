#!/usr/bin/env python3
"""Link the shared skill into Codex's personal discovery directory."""
import argparse
from pathlib import Path
import shutil
from datetime import datetime

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--retire-legacy-hook', action='store_true', help='Archive the old standalone hook skill outside discovery')
parser.add_argument('--home', type=Path, default=Path.home(), help=argparse.SUPPRESS)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = root / 'skills' / 'edit-tyler-social-clips'
target = args.home / '.agents' / 'skills' / source.name
assert (source / 'SKILL.md').is_file(), 'Missing source skill'
policy = (source / 'references' / 'video-authenticity.md').read_text().strip()
policy_start = '<!-- stalman-video-authenticity:start -->'
policy_end = '<!-- stalman-video-authenticity:end -->'
instructions = args.home / '.codex' / 'AGENTS.md'
existing_instructions = instructions.read_text() if instructions.exists() else ''
if existing_instructions.count(policy_start) != existing_instructions.count(policy_end) or existing_instructions.count(policy_start) > 1:
    raise SystemExit(f'Conflicting managed video preference markers; preserved without changes: {instructions}')
managed_policy = f'{policy_start}\n{policy}\n{policy_end}'
if policy_start in existing_instructions:
    before, remainder = existing_instructions.split(policy_start, 1)
    _, after = remainder.split(policy_end, 1)
    updated_instructions = before + managed_policy + after
else:
    updated_instructions = existing_instructions.rstrip() + ('\n\n' if existing_instructions.strip() else '') + managed_policy + '\n'
# Check every conflict before changing anything.
for candidate in (target, args.home / '.codex' / 'skills' / source.name):
    if candidate.exists() or candidate.is_symlink():
        if not (candidate.is_symlink() and candidate.resolve() == source):
            raise SystemExit(f'Existing skill needs review; preserved without changes: {candidate}')
legacy = [args.home / base / 'skills' / 'video-hook-template' for base in ('.agents', '.codex')]
present = [p for p in legacy if p.exists() or p.is_symlink()]
if present and not args.retire_legacy_hook:
    raise SystemExit('Standalone hook skill still exists. Review it, then rerun with --retire-legacy-hook to archive it.')
if present:
    backup = args.home / '.codex' / 'skill-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True)
    for index, item in enumerate(present):
        destination = backup / f'{index}-{item.name}'
        shutil.move(str(item), str(destination))
        print(f'Archived {item} to {destination}')
target.parent.mkdir(parents=True, exist_ok=True)
if not target.is_symlink():
    target.symlink_to(source, target_is_directory=True)
assert (target / 'SKILL.md').resolve() == (source / 'SKILL.md').resolve()
if updated_instructions != existing_instructions:
    instructions.parent.mkdir(parents=True, exist_ok=True)
    instructions.write_text(updated_instructions)
print(f'Installed {target} -> {source}')
print(f'Installed global video authenticity preferences in {instructions}; other instructions preserved.')
print('Start a new Codex chat and invoke $edit-tyler-social-clips to verify discovery.')
