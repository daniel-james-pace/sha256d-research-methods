"""Empirical minimum-detectable-effect estimation via permutation nulls.

Demonstration module: two-sample mean-difference testing with a permutation
null, empirical power via synthetic effect injection, and MDE estimation as
the smallest injected effect reaching target power. Synthetic data only;
fully deterministic under a caller-supplied seed.
"""

from __future__ import annotations

import numpy as np


def permutation_pvalue(x: np.ndarray, y: np.ndarray, n_perm: int,
                       rng: np.random.Generator) -> float:
    """Two-sided permutation p-value for difference in means.

    Uses the add-one estimator (never returns 0) and label reshuffling of the
    pooled sample.
    """
    observed = abs(x.mean() - y.mean())
    pooled = np.concatenate([x, y])
    nx = len(x)
    hits = 0
    for _ in range(n_perm):
        perm = rng.permutation(pooled)
        stat = abs(perm[:nx].mean() - perm[nx:].mean())
        if stat >= observed:
            hits += 1
    return (hits + 1) / (n_perm + 1)


def empirical_power(effect: float, n_per_group: int, alpha: float,
                    n_trials: int, n_perm: int, seed: int) -> float:
    """Fraction of synthetic trials (unit-variance normal, mean shift =
    ``effect``) whose permutation p-value falls below ``alpha``."""
    rng = np.random.default_rng(seed)
    rejections = 0
    for _ in range(n_trials):
        x = rng.standard_normal(n_per_group) + effect
        y = rng.standard_normal(n_per_group)
        if permutation_pvalue(x, y, n_perm, rng) < alpha:
            rejections += 1
    return rejections / n_trials


def estimate_mde(effect_grid: np.ndarray, n_per_group: int, alpha: float,
                 target_power: float, n_trials: int, n_perm: int,
                 seed: int) -> tuple[float, dict[float, float]]:
    """Smallest effect in ``effect_grid`` whose empirical power reaches
    ``target_power``; returns (mde, {effect: power}).

    Returns ``float('inf')`` as the MDE when no grid point reaches target —
    the caller sees an explicit not-detectable-at-this-depth answer rather
    than a silent extrapolation.
    """
    powers: dict[float, float] = {}
    mde = float("inf")
    for i, effect in enumerate(np.sort(np.asarray(effect_grid, dtype=float))):
        p = empirical_power(effect, n_per_group, alpha, n_trials, n_perm,
                            seed + i)
        powers[float(effect)] = p
        if p >= target_power and mde == float("inf"):
            mde = float(effect)
    return mde, powers
