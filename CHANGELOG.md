# Changelog

All notable changes to CopperMized are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project infrastructure and documentation.
- Repository structure for documentation, issue tracking, and GitHub Actions.
- Validation script for Modrinth `.mrpack` files.
- Included mod list generated from `CopperMized 26.3.mrpack`.
- Initial modpack artifact `CopperMized 26.3.mrpack`.

## [1.0.1] - 2026-11-16

### Changed

- Updated modpack configuration (MouseTweaks, render distance, Smooth Swapping, Axiom, Jade).
- Refreshed modpack artifact `CopperMized 26.3.mrpack` (versionId 1.0.1).

### Fixed

- Restored `servers.dat` and `servers.dat_old` advertising the official GridMC server (`adequately-valet.tun.ply.gg`) with auto-downloaded resource packs. These files are part of the modpack, not user data.

### Removed

- User-specific data from the modpack artifact (waypoints, FancyMenu last world, voice chat caches).