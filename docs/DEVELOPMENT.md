# Development Guide

This document describes the repository structure and the basic workflow for maintaining CopperMized.

## Repository structure

- `pack/` contains the intended source tree for the Modrinth `.mrpack` layout.
- `docs/` contains developer and publishing documentation.
- `scripts/` contains helper scripts.
- `.github/` contains issue templates, the pull request template, and GitHub Actions.

## Modpack artifact

The current modpack artifact is `CopperMized 26.3.mrpack` at the repository root. It is a Modrinth modpack archive containing `modrinth.index.json` and an `overrides/` directory.

## Validation

Run the validation script to check any `.mrpack` file found in the repository root:

```bash
python3 scripts/validate_mrpack.py
```

The script checks that:

- the archive contains `modrinth.index.json` at its root;
- required fields are present (`name`, `versionId`, `dependencies`, `files`);
- `dependencies` contains `minecraft` and `fabric-loader`;
- every file entry has a unique path, download URLs, hashes, and file size;
- the declared file count matches the number of entries.

## Updating the included mod list

`INCLUDED-MODS.md` is generated from `modrinth.index.json`. Regenerate it whenever the modpack contents change. Do not edit the list by hand unless the artifact itself has changed.

## Commits

Use Conventional Commits. Keep each commit focused on a single logical change.
