import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Add assertions for your assigned pattern.
        self.assertEqual(len(segments), 4)
        self.assertGreater(segments[0].linear_x, 0)
        

    def test_my_pattern_order(self):
        # Check another property with a known expected result.
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        signs = [1 if segment.angular_z > 0 else -1 for segment in segments]
        expect = [1, -1, 1, -1]

        self.assertEqual(expect, signs)