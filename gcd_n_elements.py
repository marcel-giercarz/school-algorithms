def find_gcd(a : int, b: int) -> int:
    if b > 0:
        return find_gcd(b, a % b)
    else:
        return a

def find_gcd_n_elements(numbers : list) -> int:
    if len(list) == 2:
        return find_gcd(numbers[0], numbers[1])
    elif len(list) < 2:
        return False

    nwd = find_gcd(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        nwd = find_gcd(nwd, numbers[i])

    return nwd

def test_algorithm():
    assert find_gcd_n_elements([60, 96, 624, 174]) == 6