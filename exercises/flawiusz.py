import unittest

def flawiusz(n : int, k : int) -> int:
    soliders = [i for i in range(1, n+1)]
    j = 1

    while len(soliders) != 1:
        for i in soliders[:]:
            if j % k == 0:
                soliders.pop(soliders.index(i))
            j += 1

    return soliders[0]

class TestFlawiusz(unittest.TestCase):
    def test_flawiusz(self):
        # Test cases
        self.assertEqual(flawiusz(5, 2), 3)
        self.assertEqual(flawiusz(7, 3), 4)
        self.assertEqual(flawiusz(7, 13), 2)
        self.assertEqual(flawiusz(61, 17), 26)

if __name__ == '__main__':
    unittest.main()

