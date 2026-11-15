# Modrinth Publishing

CopperMized is published as a Modrinth modpack (`.mrpack`).

## `.mrpack` structure

A Modrinth modpack archive contains:

- `modrinth.index.json` — modpack metadata, dependencies, and file list.
- `overrides/` — configuration files and other assets applied to the instance.

## Required metadata

`modrinth.index.json` must declare at least:

- `name` and `versionId`;
- `dependencies.minecraft`;
- `dependencies.fabric-loader`;
- `files`, where each entry includes `path`, `hashes`, `downloads`, `fileSize`, and `env`.

## Current state

The repository contains the assembled artifact `CopperMized 26.3.mrpack`. Source files for the pack are intended to live under `pack/`. Automated publishing to Modrinth is not yet configured.

## Release process (planned)

1. Validate the `.mrpack` with `scripts/validate_mrpack.py`.
2. Attach the `.mrpack` to a GitHub Release.
3. Publish the same artifact to Modrinth manually or through a future workflow.

Do not publish untested or incomplete artifacts.
