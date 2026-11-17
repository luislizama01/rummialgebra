# RummiAlgebra V2 — Interactive algebra learning with jokers

**Research prototype**, accompanying the manuscript *RummiAlgebra: A Polynomial Representation Framework for Game-Based Algebra Learning with Jokers* (preprint draft, 2026).

Author: Luis Adrián Lizama Pérez, Universidad Autónoma Metropolitana, Unidad Lerma.

## Play

Open [`index.html`](index.html) in a browser, or visit the GitHub Pages address after the site has been enabled. The game runs entirely client-side and requires no account or installation. No online services or external scripts are used by the HTML file.

Six activities include algebraic rearrangement, first-meld threshold, regrouping and one/two jokers. The exercise editor supports custom tile sets. For jokers, choose a value and a color and check the polynomial substitution and meld legality. The objective is educational: a correct polynomial identity alone does not guarantee a legal meld.

## Publish with GitHub Pages

1. Create a **public** GitHub repository, e.g. `rummialgebra`, and upload all files from this ZIP **at the repository root** (including `index.html`).
2. In **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/(root)**; save.
3. After deployment, copy the actual **Visit site** URL shown in Pages settings. Do not assume the URL until verified.
4. Open the site in an incognito browser, try Challenge 4 (joker as missing 6R), then Challenge 6 (two jokers), and verify on a phone.
5. Create a tagged GitHub Release for the version used in the paper, then deposit that release in Zenodo to obtain a version-specific DOI.

## Evaluation and feedback

See [TESTING.md](TESTING.md). For a bug or usability report, open a GitHub Issue in the repository with the steps to reproduce, the selected challenge, observed output, expected output, browser and device. Do not post student names or identifiable classroom data.

## Scope

- Educational final-arrangement rules: runs of >=3 same-color consecutive numbers; groups of 3–4 equal numbers with distinct colors; up to two duplicates per numbered tile; at most two jokers.
- Requires every tile originally on the table to be used in a legal meld. Checks special 30-point opening challenge.
- The implementation does **not** verify all physical procedures for reclaiming a table joker, tournament-specific rules or strategy under hidden information.
- The six example optima were cross-checked with a separate small-instance enumerator. This is not a formal verification of the JavaScript implementation and not an educational efficacy study.

## Citation and license

The [CITATION.cff](CITATION.cff) file supplies author/title/version metadata. Once a Zenodo DOI is assigned, add it here and to the article's Software Availability paragraph.

**Licensing decision required before general software reuse.** This kit does not grant an open-source license. Public access for testing is different from granting modification or redistribution rights. Select and add an explicit license after reviewing institutional ownership and any third-party materials.

Rummikub is a proprietary game name; this is an independent, non-official educational adaptation with no claim of endorsement.