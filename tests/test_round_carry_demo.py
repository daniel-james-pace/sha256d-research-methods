import hashlib
import unittest

import numpy as np

from round_carry_demo import add_with_carry, rotr, sha256_single_block


class TestRoundCarryDemo(unittest.TestCase):
    def test_digests_match_hashlib(self):
        rng = np.random.default_rng(20260901)
        for length in (0, 1, 3, 32, 55):
            msgs = rng.integers(0, 256, size=(16, length), dtype=np.uint8) \
                if length else np.zeros((16, 0), dtype=np.uint8)
            digests, _ = sha256_single_block(msgs)
            for row in range(msgs.shape[0]):
                expected = hashlib.sha256(msgs[row].tobytes()).digest()
                self.assertEqual(digests[row].tobytes(), expected)

    def test_carry_counts_deterministic_and_positive(self):
        rng = np.random.default_rng(7)
        msgs = rng.integers(0, 256, size=(8, 32), dtype=np.uint8)
        _, c1 = sha256_single_block(msgs)
        _, c2 = sha256_single_block(msgs)
        self.assertTrue(np.array_equal(c1, c2))
        self.assertTrue((c1 > 0).all())

    def test_add_with_carry_edges(self):
        a = np.array([0xFFFFFFFF, 0, 0x80000000], dtype=np.uint32)
        b = np.array([1, 0, 0x80000000], dtype=np.uint32)
        s, c = add_with_carry(a, b)
        self.assertTrue(np.array_equal(s, np.array([0, 0, 0], dtype=np.uint32)))
        self.assertTrue(np.array_equal(c, np.array([1, 0, 1], dtype=np.uint32)))

    def test_rotr_roundtrip(self):
        x = np.array([0x12345678], dtype=np.uint32)
        self.assertEqual(rotr(rotr(x, 13), 19)[0], x[0])


if __name__ == "__main__":
    unittest.main()
