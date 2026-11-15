#!/usr/bin/env python3
"""Validate Modrinth .mrpack files found in the repository root."""

import json
import sys
import zipfile
from pathlib import Path


REQUIRED_TOP = ("name", "versionId", "dependencies", "files")
REQUIRED_DEPS = ("minecraft", "fabric-loader")
REQUIRED_FILE = ("path", "hashes", "downloads", "fileSize", "env")


def validate_archive(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
            if "modrinth.index.json" not in names:
                return [f"{path}: missing modrinth.index.json at archive root"]

            try:
                index = json.loads(zf.read("modrinth.index.json"))
            except (json.JSONDecodeError, KeyError) as exc:
                return [f"{path}: invalid modrinth.index.json ({exc})"]

            for key in REQUIRED_TOP:
                if key not in index:
                    errors.append(f"{path}: missing top-level field '{key}'")

            deps = index.get("dependencies", {})
            if not isinstance(deps, dict):
                errors.append(f"{path}: 'dependencies' must be an object")
            else:
                for dep in REQUIRED_DEPS:
                    if dep not in deps:
                        errors.append(f"{path}: missing dependency '{dep}'")

            files = index.get("files", [])
            if not isinstance(files, list) or not files:
                errors.append(f"{path}: 'files' must be a non-empty array")
            else:
                seen_paths: set[str] = set()
                for i, entry in enumerate(files):
                    if not isinstance(entry, dict):
                        errors.append(f"{path}: files[{i}] is not an object")
                        continue
                    for key in REQUIRED_FILE:
                        if key not in entry:
                            errors.append(f"{path}: files[{i}] missing '{key}'")
                    file_path = entry.get("path")
                    if file_path in seen_paths:
                        errors.append(f"{path}: duplicate file path '{file_path}'")
                    if file_path is not None:
                        seen_paths.add(file_path)
                    hashes = entry.get("hashes", {})
                    if not isinstance(hashes, dict) or "sha1" not in hashes:
                        errors.append(f"{path}: files[{i}] missing sha1 hash")
                    downloads = entry.get("downloads")
                    if not isinstance(downloads, list) or not downloads:
                        errors.append(f"{path}: files[{i}] missing downloads")
                    if not isinstance(entry.get("fileSize"), int):
                        errors.append(f"{path}: files[{i}] has invalid fileSize")
                    if not isinstance(entry.get("env"), dict):
                        errors.append(f"{path}: files[{i}] has invalid env")

            return errors
    except (zipfile.BadZipFile, OSError) as exc:
        return [f"{path}: cannot read archive ({exc})"]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    archives = sorted(root.glob("*.mrpack"))

    if not archives:
        print("No .mrpack files found in repository root.")
        return 0

    all_errors: list[str] = []
    for archive in archives:
        errors = validate_archive(archive)
        if errors:
            all_errors.extend(errors)
        else:
            with zipfile.ZipFile(archive) as zf:
                index = json.loads(zf.read("modrinth.index.json"))
            print(
                f"OK: {archive.name} "
                f"({len(index['files'])} files, "
                f"minecraft {index['dependencies']['minecraft']}, "
                f"fabric {index['dependencies']['fabric-loader']})"
            )

    if all_errors:
        print("\nValidation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
