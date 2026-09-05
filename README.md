# SHA-256d Research Methods

This repository documents methods developed during a long-running independent
research program (2023–present) studying the internal computation of SHA-256d
in its real-world deployment context. The working question: whether that
computation's internal structure yields measurable information beyond direct
evaluation. This repository makes no security claim and no practical-mining
claim.

The research record — representations tested, corpus construction, coverage
depth, findings — is deliberately unpublished. What's documented here is how
the program was run: the outcome taxonomy, controls, artifact ledger, and
correction rules under which its results — positive and negative — were
recorded and scoped.

## What's here

- `src/round_carry_demo/` — vectorized SHA-256 round primitives with
  explicit carry tracking; synthetic inputs, deterministic seeds.
- `src/mde_demo/` — empirical minimum-detectable-effect estimation via
  permutation nulls; synthetic data.
- `tests/` — unit tests for both modules.

These are illustrative simplifications, not the research instruments.

Quickstart:

```bash
python -m pip install -e .
python -m unittest discover tests
```

## Program shape

Multi-year; hundreds of staged experiments under progressively stricter
controls, with later stages increasingly preregistered — endpoint, metric,
and null construction specified before evaluation. Results are recorded
under a fixed outcome taxonomy and revisited under a standing correction
discipline.

## Outcome taxonomy

Each evaluated claim receives one primary disposition:

- **Structural fact** — an exact or reproducible property of the
  computation.
- **Interesting** — an enrichment or near-miss that fails continuity,
  replication, or artifact controls. Recorded as an artifact-aware class,
  never treated as a weak signal.
- **Signal** — a controlled, replicating result within a defined frame.
- **Covered-null / covered-empty** — the tested method did not detect a
  signal at its stated depth. This is a statement about the method and
  depth, never a claim of absence.
- **Open by construction** — higher-order, infeasible, or unfalsifiable
  tails, named as such rather than absorbed into a negative.

## Controls ladder

For promotion, a candidate must clear the controls appropriate to its frame,
including: matched (not merely balanced) null populations; held-out
replication with direction stability; random-feature, label-shuffle, and
shuffled-pairing nulls; selection-tautology and endpoint guards; and — for
any claim of practical utility — comparison against an optimized baseline
rather than a naive one.

## Artifact classes

The program maintains a ledger of the ways false positives arise in this
kind of search, each paired with the control that kills it:

| Artifact class | Governing control |
|---|---|
| Format/provenance leakage | Format-matched controls, cross-era tests |
| Enumeration fingerprint | Source quarantine, control-vs-control |
| Selection tautology | Endpoint guards; non-promotable reference class |
| Endpoint contamination | Endpoint-neutral statistics |
| Conditioning circularity | Region independence, preserving-neighbor tests |
| Representation/display confusion | Single canonical mapping, used everywhere |
| Hidden enumeration | Non-enumerative residual audit |
| Structural-base mismatch | Matched structural bases |
| Scope inflation | Uniqueness and universality audits |
| Finite-sample instability | Fresh holdouts, sign-stability requirements |
| More-is-better fallacy | Subset ablation, wall-clock measurement |

## Correction discipline

A standing index records identified cases where a later result changed the
scope of an earlier one. The recurring failure modes it exists to catch:

- a proposed experiment later described as completed;
- two separate findings compressed into one phrase;
- a benchmark number repeated without its original test regime;
- a negative conclusion stated more broadly than the instrument that
  established it.

Most corrections narrow wording while leaving downstream conclusions
intact — which is the point: precision about scope is what makes the record
reusable.

## Covered-empty semantics

A null here means *not detected by these methods at this depth* — never
absence. A covered frame is not rerun deeper without stating why depth was
binding and what effect size becomes detectable. Negative results are
first-class findings and are reported with the same care as positives.

## Soundness vocabulary

"Sound" is never used unqualified. The program distinguishes:

- **Witness-consistent** — does not contradict one specific known
  assignment. Cheap; necessary; never sufficient.
- **Panel-consistent** — holds across a validation panel. Catches
  case-specific overfits, not all structural failures.
- **Mathematically sound** — true for all assignments, by proof or
  exhaustive narrow-width enumeration.
- **Encoding-sound** — for constraint-level work: the relation is true and
  its encoding correctly represents it, with an explicit validation basis
  stated per claim.

Claims in this framework state their validation tier.

## Selected working rules

1. Freeze the data split and null before evaluating features.
2. Separate enrichment from continuity; subtract baseline continuity from
   candidate continuity.
3. Compare "interesting" density against a random-feature baseline.
4. Report distinct features separately from feature-context products.
5. Require held-out, same-context replication — then apply
   independent-axis, sibling, and preserving-neighbor checks to survivors.
6. Use cheap triage only as triage; it never promotes a result.
7. Compact routine negative logs; preserve full provenance for every
   non-negative outcome.
8. Replication is necessary but never sufficient on its own — replicated
   results still face independent-axis and circularity checks.

## License

MIT — see `LICENSE`.
