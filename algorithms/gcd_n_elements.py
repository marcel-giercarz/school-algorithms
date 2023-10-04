import unittest
def find_gcd(a : int, b: int) -> int:
    if b > 0:
        return find_gcd(b, a % b)
    else:
        return a

def find_gcd_n_elements(numbers : list) -> int:
    if len(numbers) == 2:
        return find_gcd(numbers[0], numbers[1])
    elif len(numbers) < 2:
        return False

    nwd = find_gcd(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        nwd = find_gcd(nwd, numbers[i])

    return nwd

class TestFindGCDNElements(unittest.TestCase):
    def test_find_gcd_n_elements(self):
        self.assertEqual(find_gcd_n_elements([1]), False)
        self.assertEqual(find_gcd_n_elements([184, 152]), 8)
        self.assertEqual(find_gcd_n_elements([12, 18, 24]), 6)
        self.assertEqual(find_gcd_n_elements([15, 30, 45, 60]), 15)
        self.assertEqual(find_gcd_n_elements([7, 14, 21]), 7)
        self.assertEqual(find_gcd_n_elements([17, 34, 51]), 17)
        self.assertEqual(find_gcd_n_elements([60, 96, 624, 174]), 6)

if __name__ == '__main__':
    unittest.main()
