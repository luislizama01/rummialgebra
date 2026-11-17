# Releasing and archiving RummiAlgebra

**Live application:** https://luislizama01.github.io/rummialgebra/  
**Repository:** https://github.com/luislizama01/rummialgebra

## 1. Check the release candidate

- Open the website in a private window and try the six exercises, including joker examples.
- Run `python tests/verify_examples.py` (expected: six successful comparisons).
- Review whether UAM approval is needed and choose a suitable software license. This public repository currently has **no explicit reuse license**.
- Do not include game trademarks or third-party copyrighted imagery beyond authorized uses.

## 2. Create a fixed GitHub release

- Open https://github.com/luislizama01/rummialgebra/releases/new
- Propose tag `v2.0.0` pointing to the reviewed commit (only if this version does not already exist).
- Title: `RummiAlgebra V2.0.0 — polynomial learning with jokers`.
- Include app URL, checker command, mathematical scope and software limitations.
- Publish the release. The release's Git tag identifies the source revision used in the paper.

## 3. Archive the release in Zenodo

- Sign in at https://zenodo.org/ and inspect the GitHub integration for this repository.
- **Enable Zenodo archiving before creating the GitHub release** when possible. If the release was created earlier and not imported, follow Zenodo's current instructions or create a new versioned release after enabling archiving.
- If GitHub integration is not available, create a Zenodo software record and upload the release source archive manually.
- Check that the metadata lists the correct author, title, software version and source link.
- Publish the record and obtain its actual **version-specific DOI**.

## 4. Cite the permanent artifact

Only after a DOI is issued, add the DOI to `CITATION.cff` and to the Software availability paragraph in the manuscript. The current `main` branch and GitHub Pages address are mutable; a version DOI identifies the archived artifact.

Suggested metadata: **RummiAlgebra: Interactive Polynomial Learning with Jokers**; creator **Luis Adrián Lizama Pérez**; affiliation **Universidad Autónoma Metropolitana, Unidad Lerma**; resource type **Software**; year **2026**.

**Scope:** rule-aware verification of final arrangements in an educational model; this does not cover all tournament-specific joker-recovery procedures, provide formal machine verification of the JavaScript, or establish learning gains in students.
