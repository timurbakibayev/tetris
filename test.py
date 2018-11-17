import unittest
import halflife


class TestHalfLife(unittest.TestCase):
    def test_under_population(self):
        self.assertEqual(
            halflife.step([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ])[1][1],
            0
        )

    def test_survival(self):
        self.assertEqual(
            halflife.step([
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ])[1][1],
            1
        )

    def test_overcrowding(self):
        self.assertEqual(
            halflife.step([
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ])[1][1],
            0
        )

    def test_reproduction(self):
        self.assertEqual(
            halflife.step([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 1],
            ])[1][1],
            1
        )

if __name__ == '__main__':
    unittest.main()
