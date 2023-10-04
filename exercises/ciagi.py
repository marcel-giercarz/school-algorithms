import unittest

def znajdz_ciag(liczby):
    liczby.sort()
    ciag = []
    temp = []
    r = 1
    
    while r != liczby[len(liczby)-1]:
        for a1 in liczby:
            ciag.append(a1)
            
            for i in range(len(liczby)):
                if a1 + r*(i+1) in liczby and (a1 + r*(i + 1)) - (a1 + r*(len(ciag)-1)) == r:
                    ciag.append(a1 + r*(i+1))

            if len(ciag) < 2:
                ciag = []
                continue
            
            if len(ciag) > len(temp):
                temp = ciag

            ciag = []
        r += 1
        
    return temp

class TestZnajdzCiag(unittest.TestCase):
    def test_znajdz_ciag(self):
        self.assertEqual(znajdz_ciag([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 17, 18, 19, 20, 21, 22, 23, 24, 25, 100, 104, 108, 112, 116, 120, 121, 122, 123, 124, 126, 128, 129, 132, 136, 140, 141, 144]), [100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144])
        self.assertEqual(znajdz_ciag([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(znajdz_ciag([255, 510, 511, 512, 765, 822, 1020]), [255, 510, 765, 1020])

if __name__ == "__main__":
    unittest.main()