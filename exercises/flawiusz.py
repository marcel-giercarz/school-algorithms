def flawiusz(n, k):
    soliders = [i for i in range(1, n+1)]
    j = 1

    while len(soliders) != 1:
        for i in soliders[:]:
            if j % k == 0:
                soliders.pop(soliders.index(i))
            j += 1

    return soliders[0]

def test_algorithm():
    assert flawiusz(7, 3) == 4
    assert flawiusz(7, 13) == 2
    assert flawiusz(61, 17) == 26