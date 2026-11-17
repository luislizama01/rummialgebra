# RummiAlgebra V2 — Interactive algebra learning with jokers

**Research prototype**, accompanying the manuscript *RummiAlgebra: A Polynomial Representation Framework for Game-Based Algebra Learning with Jokers* (preprint draft, 2026).

Author: Luis Adrián Lizama Pérez, Universidad Autónoma Metropolitana, Unidad Lerma.

## Play

**[Play RummiAlgebra online](https://luislizama01.github.io/rummialgebra/)**. Alternatively, open [`index.html`](index.html) locally in a browser. The game runs entirely client-side and requires no account or installation. No online services or external scripts are used by the HTML file.

Six activities include algebraic rearrangement, first-meld threshold, regrouping and one/two jokers. The exercise editor supports custom tile sets. For jokers, choose a value and a color and check the polynomial substitution and meld legality. The objective is educational: a correct polynomial identity alone does not guarantee a legal meld.

## Public access and versioning

- **Live application:** https://luislizama01.github.io/rummialgebra/
- **Source code:** https://github.com/luislizama01/rummialgebra
- **Test instructions:** [TESTING.md](TESTING.md)
- **Independent reference checks:** [tests/verify_examples.py](tests/verify_examples.py), run `python tests/verify_examples.py`
- **Frozen v2.0.0 source:** [GitHub release](https://github.com/luislizama01/rummialgebra/releases/tag/v2.0.0)
- **Archived v2.0.0 record:** [Zenodo DOI](https://doi.org/10.5281/zenodo.24323391).
- **Archiving guide:** [ARCHIVING_ZENODO.md](ARCHIVING_ZENODO.md)

The Pages website shows the current main-branch version; for scientific reproducibility, cite a tagged, archived release rather than a mutable branch.

## Evaluation and feedback

See [TESTING.md](TESTING.md). For a bug or usability report, open a GitHub Issue in the repository with the steps to reproduce, the selected challenge, observed output, expected output, browser and device. Do not post student names or identifiable classroom data.

## Scope

- Educational final-arrangement rules: runs of >=3 same-color consecutive numbers; groups of 3–4 equal numbers with distinct colors; up to two duplicates per numbered tile; at most two jokers.
- Requires every tile originally on the table to be used in a legal meld. Checks special 30-point opening challenge.
- The implementation does **not** verify all physical procedures for reclaiming a table joker, tournament-specific rules or strategy under hidden information.
- The six example optima were cross-checked with a separate small-instance enumerator. This is not a formal verification of the JavaScript implementation and not an educational efficacy study.

## Citation and license

The [CITATION.cff](CITATION.cff) file supplies author/title/version metadata. Cite the archived V2.0.0 software using DOI [`10.5281/zenodo.24323391`](https://doi.org/10.5281/zenodo.24323391). The editable current `main` branch and GitHub Pages version may differ from the archived release.

**Licensing decision required before general software reuse.** This kit does not grant an open-source license. Public access for testing is different from granting modification or redistribution rights. Select and add an explicit license after reviewing institutional ownership and any third-party materials.

Rummikub is a proprietary game name; this is an independent, non-official educational adaptation with no claim of endorsement.