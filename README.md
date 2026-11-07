# Stalman Skills

Shared personal Codex skills. This public GitHub repository is the authoritative version for both Macs and can be shared for installation on other computers.

## Included skill

[`edit-tyler-social-clips`](skills/edit-tyler-social-clips/SKILL.md) combines Tyler's short-form editing workflow, approved Staatliches opening hooks, default caption reference, and review requirements. It has no episode-specific batch instructions and no dependency on the old `video-hook-template` skill. Reference images are included.

## Install on either Mac

Requires GitHub access, `gh`, Git, and Python 3. Use an existing checkout if this repository is already cloned; do not create a second editable copy.

```sh
mkdir -p "$HOME/Documents/Codex"
gh repo clone tylerstalman/stalman-skills "$HOME/Documents/Codex/Shared Skills"
python3 "$HOME/Documents/Codex/Shared Skills/scripts/install.py" --retire-legacy-hook
```

The installer creates `~/.agents/skills/edit-tyler-social-clips` as a link to the checkout. It refuses to overwrite a conflicting installed skill. The flag archives the standalone `video-hook-template`, if present, under `~/.codex/skill-backups/`, outside discovery. Other skills are preserved. Review any additional preferences on the second Mac before retiring a different legacy version.

The installer also maintains a marked video-authenticity section in `~/.codex/AGENTS.md`, preserving other instructions. It prohibits Eye Contact and gaze correction in all Tyler video workflows, including inherited settings, and requires verification before export or posting. It also requires matching product identity to the actual discussion and using the manufacturer's exact short model name. Its shared source is [Video authenticity](skills/edit-tyler-social-clips/references/video-authenticity.md). Rerun the installer after pulling updates to refresh these global preferences on each Mac.

Start a new Codex chat and ask it to use `$edit-tyler-social-clips`; verify it identifies this combined skill. A working link verifies files and installation, not fresh-session discovery. Official discovery documentation: https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills

## Updates and version checks

Before editing, pull on that Mac:

```sh
git -C "$HOME/Documents/Codex/Shared Skills" pull --ff-only
```

Edit the skill in this checkout, review the diff, commit, and push. On the other Mac run the same pull command. The installed link follows the updated checkout. Compare `git -C "$HOME/Documents/Codex/Shared Skills" rev-parse HEAD` on both Macs to verify the same commit. If either checkout has uncommitted changes or divergent commits, reconcile them before updating; do not overwrite them or force-push.

Codex automations configured on November 6, 2026 reconcile user-authored skill changes at 9 a.m. and 9 p.m. America/Edmonton and report on Mondays at 9:15 a.m. Routine sync notifications are muted except failed runs. Local run records and pending destinations live in `.sync-state/` (excluded from Git). Runs depend on the scheduler and available access; offline or unsupported destinations remain pending. No system background services are installed. Local links do not automatically install skills on another computer, in Codex cloud, or in ChatGPT; each destination must be accessible and independently installed and verified.

## Recovery

If discovery fails, confirm GitHub authentication, the checkout path, and the installed symlink. Rerun the installer after restoring a moved or missing checkout. It preserves conflicting paths so they can be compared before replacement. Restore old hook files from `~/.codex/skill-backups/` only if deliberately reverting to the separate skill; avoid installing both versions.
