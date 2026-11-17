# RummiAlgebra V2 — Public trial guide

## Quick functional test (10 minutes)

1. Open the published `index.html`; confirm the tile board and algebra notebook appear.
2. Challenge 1: regroup table 3R–6R with hand 7R 6A 6V; target 12 played-hand points.
3. Challenge 2: the opening challenge; target 30.
4. Challenge 3: existing-tile regrouping; target 42.
5. Challenge 4: 5R, 7R, joker → assign 6R; target 18.
6. Challenge 5: 9R, 9A, joker → assign a third color at 9; target 27.
7. Challenge 6: 4R, 7R, two jokers. Try 4R–7R (22), then 7R–9R (24; 4R remains unused).
8. Enter a custom exercise and verify that an illegal group or run is rejected.
9. Test the same actions by touch on a phone or tablet.

The targets above are the reference optima, not necessarily the first configuration that a student creates.

## Independent reference check

With Python installed, run `python tests/verify_examples.py`; this checks the six built-in instances independently of the web app.

## Report issues

- Challenge number or custom tiles (table / hand):
- Desired operation, including joker roles:
- Steps to reproduce:
- Expected behavior:
- Actual behavior:
- Browser and version:
- Device/OS:
- Optional screenshot without identifiable student data:

**Do not report personal educational records or identifiable information.**