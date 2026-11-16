# AGENTS.md — CopperMized repository context

## Project

CopperMized is a lightweight Fabric client-side Minecraft modpack focused on performance, FPS, and quality-of-life improvements. Minecraft version 26.3, Fabric Loader 0.20.1, Sodium is the core mod.

## Repository layout

- `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `INCLUDED-MODS.md`, `CHANGELOG.md`.
- `pack/` — intended source tree for the Modrinth `.mrpack` layout (`modrinth.index.json` + `overrides/`).
- `docs/` — developer and Modrinth publishing documentation.
- `scripts/validate_mrpack.py` — validates `.mrpack` structure.
- `.github/` — issue templates, pull request template, GitHub Actions.
- `CopperMized 26.3.mrpack` — current modpack artifact at repository root.

## Important rules

- Do not invent mods, versions, links, or test results. Derive the mod list from `modrinth.index.json` inside the `.mrpack`.
- Do not store `.jar` files in Git.
- Do not edit or replace the existing `.mrpack` unless explicitly asked.
- Documentation is written in English.
- Commit messages follow Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, ...).
- License choice is pending; do not finalize or overwrite `LICENSE` without user confirmation.
- `overrides/servers.dat` and `overrides/servers.dat_old` are part of the modpack: they advertise the official GridMC server (`adequately-valet.tun.ply.gg`) with auto-downloaded resource packs. Do not remove, clear, or treat them as user data when cleaning the instance or editing the `.mrpack`.

## Validation

```bash
python3 scripts/validate_mrpack.py
```

## Useful commands

- List repository files: `find . -path ./.git -prune -o -type f -print`
- Check Git status: `git status`
- Run repository checks locally: `python3 scripts/validate_mrpack.py`
