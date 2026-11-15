# Pack source tree

This directory is reserved for the source form of the CopperMized Modrinth modpack.

Expected layout (Modrinth `.mrpack`):

```
pack/
├── modrinth.index.json
└── overrides/
    └── config/
        └── ...
```

`modrinth.index.json` declares the Minecraft and Fabric Loader versions, the list of mods and resource packs with their download URLs and hashes, and the environment for each file. The `overrides/` directory contains configuration files and other non-mod assets shipped with the pack.

The assembled `.mrpack` artifact currently lives at the repository root as `CopperMized 26.3.mrpack`. When a source tree is added here, keep it in sync with the published artifact.
