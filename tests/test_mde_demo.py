import unittest

import numpy as np

from mde_demo import empirical_power, estimate_mde, permutation_pvalue


class TestMdeDemo(unittest.TestCase):
    def test_null_type_i_error_near_alpha(self):
        rng = np.random.default_rng(42)
        rejections = 0
        trials = 200
        for _ in range(trials):
            x = rng.standard_normal(30)
            y = rng.standard_normal(30)
            if permutation_pvalue(x, y, 99, rng) < 0.05:
                rejections += 1
        self.assertLess(rejections / trials, 0.12)
        self.assertGreater(rejections, 0)

    def test_power_monotone_in_effect(self):
        p_small = empirical_power(0.1, 30, 0.05, 60, 99, seed=1)
        p_large = empirical_power(1.5, 30, 0.05, 60, 99, seed=1)
        self.assertGreater(p_large, p_small)
        self.assertGreater(p_large, 0.9)

    def test_mde_finite_and_ordered(self):
        grid = np.array([0.1, 0.5, 1.0, 1.5])
        mde, powers = estimate_mde(grid, 30, 0.05, 0.8, 40, 99, seed=3)
        self.assertTrue(np.isfinite(mde))
        self.assertGreaterEqual(powers[1.5], powers[0.1])

    def test_mde_inf_when_undetectable(self):
        grid = np.array([0.01])
        mde, _ = estimate_mde(grid, 10, 0.05, 0.99, 20, 49, seed=5)
        self.assertEqual(mde, float("inf"))


if __name__ == "__main__":
    unittest.main()
