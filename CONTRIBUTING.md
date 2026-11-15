# Contributing to CopperMized

Thank you for your interest in contributing to CopperMized.

## Before you start

- Read the [README](README.md) and [Code of Conduct](CODE_OF_CONDUCT.md).
- Search existing issues before opening a new one.
- For questions and general discussion, use the contact channels listed in the README.

## Reporting issues

- Use the issue templates provided in `.github/ISSUE_TEMPLATE/`.
- Include your Minecraft version, Fabric Loader version, launcher, and relevant logs.
- Do not report issues related to cheating software, piracy, or anything that violates Mojang's Terms of Service.

## Proposing changes

- Open an issue first for mod additions, removals, or significant configuration changes.
- Do not submit pull requests that directly change the modpack structure (such as adding or removing mods) without prior discussion.
- Small documentation, script, and tooling improvements are welcome via pull request.

## Pull requests

- Keep changes focused and minimal.
- Use clear commit messages following Conventional Commits (`feat:`, `fix:`, `docs:`, etc.).
- Update documentation when your change affects usage or repository structure.
- Run the validation script before submitting:

  ```bash
  python3 scripts/validate_mrpack.py
  ```

## Development setup

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for repository layout and validation details.
