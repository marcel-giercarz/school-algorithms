with open('dane.txt') as f:
    liczby_dane = [int(line.rstrip("\n")) for line in f]


def find_szczesliwe(liczby):
    szczesliwe = [liczby[0]]
    for i in liczby[:]:
        if i % 2 == 0:
            liczby.remove(i)
    try:
        for j in range(1, len(liczby)):
            szczesliwe.append(liczby[j])
            counter = 1
            for i in liczby:
                if counter == liczby[j]:
                    liczby.remove(i)
                    counter = 1
                elif counter > len(liczby):
                    break
                counter += 1
    except IndexError:
        return szczesliwe


def is_pierwsza(a):
    counter = 0
    for i in range(1, a + 1):
        if a % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

szczesliwe = find_szczesliwe([i for i in range(1, 10000)])

def z1():
    result = 0
    for i in liczby_dane:
        if i in szczesliwe:
            result += 1

    print(result)

def z2():
    temp = []
    happy_streak = []
    streak = 0
    for i in liczby_dane:
        if i in szczesliwe:
            temp.append(i)
            streak += 1
        else:
            if len(happy_streak) < len(temp):
                happy_streak = temp
            temp = []

    print(len(happy_streak))
    print(happy_streak[0])

def z3():
    result = 0
    for i in liczby_dane:
        if i in szczesliwe and is_pierwsza(i):
            result += 1
    print(result)
