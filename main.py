# problema 10
def is_even(n: int) -> bool:
    """
    Verifica daca numarul e par.
    :param n: int, numarul verificat
    :return: bool
    """
    if n % 2 == 0:
        return True
    else:
        return False


def get_longest_all_even(lst: list[int]) -> list[int]:
    """
    Se afla secventa cea mai lunga cu numere pare.
    :param lst: lista de int-uri
    :return: secventa cea mai lunga de numere pare
    """
    lst1 = []
    count = 0
    maxi = 0
    x = 0
    for i in range(len(lst)):
        if is_even(lst[i]):
            count += 1
            if count > maxi:
                maxi = count
                x = i + 1
        else:
            count = 0
    for i in range(x - maxi, x):
        lst1.append(int(lst[i]))
    return lst1


# problema 13
def isprime(n: int) -> bool:
    """
    Se verifica daca un numar e prim.
    :param n: int, numarul ce este verificat
    :return: bool
    """
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True

    else:
        return False


def get_prime_digits_for_one(a: int) -> bool:
    """
    Se verifica daca toate cifrele unui numar sunt prime.
    :param a: int, numaru ale carui cifre sunt verificate
    :return: bool
    """
    b = a
    c = 0
    c1 = 0
    while b > 0:
        c1 += 1
        n = b % 10
        if isprime(n):
            c += 1
        b = b // 10
    if c == c1:
        return True
    else:
        return False


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """
    Se afla cea mai lunga secventa de numere ce au doar cifre prime.
    :param lst: lista de int-uri
    :return: secventa cea mai lunga alcatuita din numere ce au cifre prime
    """
    lst1 = []
    count = 0
    maxi = 0
    x = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            if get_longest_prime_digits_for_one(lst[i]):
                count += 1
                if count > maxi:
                    maxi = count
                    x = i + 1
            else:
                count = 0
    for i in range(x - maxi, x):
        lst1.append(int(lst[i]))
    return lst1


# problema 3
def alternating_signs_of_2(a: int, b: int) -> bool:
    """
    Se verifica daca 2 numere au semne alternative.
    :param a: int
    :param b: int
    :return: bool
    """
    if a < 0 and b > 0:
        return True
    elif a > 0 and b < 0:
        return True
    else:
        return False


def get_longest_alternating_signs(lst2: list[int]) -> list[int]:
    """
    Se cauta cea mai lunga secventa alcatuita doar din numere ale caror semn difera.
    :param lst2: lista de int-uri
    :return: secventa cea mai lunga 
    """
    lst1 = []
    x = 0
    count = 0
    maxi = 0
    for i in range(0, len(lst2) - 1):
        if alternating_signs_of_2(lst2[i], lst2[i + 1]):
            count += 1
            if count > maxi:
                maxi = count
                x = i + 1
        else:
            count = 0

    for i in range(x - maxi, x + 1):
        lst1.append(lst2[i])
    return lst1


def printmenu():
    print("1. Citire date.")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sa aibe semne diferite.")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sa fie formate din cifre prime.")
    print("4. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sa fie pare.")
    print("x. Iesire.")


def citirelista() -> list[int]:
    lst = []
    n = int(input("Dati numarul de elemente:"))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-3, 2, -5, -10, 11]) == [-3, 2, -5]
    assert get_longest_alternating_signs([2, 3, -5, -13]) == [3, -5]
    assert get_longest_alternating_signs([-3, -5, -16, -11]) == [-3]
    assert get_longest_alternating_signs([-3, 2, -5, 10, -11]) == [-3, 2, -5, 10, -11]
    assert get_longest_alternating_signs([-3, 0, -5, -10, 11]) == [-10, 11]


test_get_longest_alternating_signs()


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([35, 57, 33, 43, 77]) == [35, 57, 33]
    assert get_longest_prime_digits([12, 35, 57, 33, 43, 77, 2, 7, 5, 1, 29]) == [77, 2, 7, 5]
    assert get_longest_prime_digits([35, 57, 33]) == [35, 57, 33]
    assert get_longest_prime_digits([12, 4, 66, 43, 88]) == []
    assert get_longest_prime_digits([35, 54, 33, 43, 77]) == [35]


test_get_longest_prime_digits()


def test_get_longest_all_even():
    assert get_longest_all_even([3, 2, 4, 5]) == [2, 4]
    assert get_longest_all_even([3, 2, 4, 5, 12, 22, 64, 11]) == [12, 22, 64]
    assert get_longest_all_even([0, 2, 4, 5]) == [0, 2, 4]
    assert get_longest_all_even([2, 4]) == [2, 4]
    assert get_longest_all_even([3, 5, 7, 5]) == []


test_get_longest_all_even()


def main():
    lst = []
    while True:
        printmenu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            lst = citirelista()
        elif optiune == "2":
            l1 = get_longest_alternating_signs(lst)
            print(l1)
        elif optiune == "3":
            l1 = get_longest_prime_digits(lst)
            print(l1)
        elif optiune == "4":
            l1 = get_longest_all_even(lst)
            print(l1)
        elif optiune == "x":
            break


if __name__ == "__main__":
    main()
