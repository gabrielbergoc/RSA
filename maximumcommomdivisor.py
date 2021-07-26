import time


def mcd_rec(a, b):
    if a % b == 0:
        return b
    else:
        return mcd_rec(b, a % b)


def mcd_iter(a, b):
    rest = a % b
    while rest != 0:
        a = b
        b = rest
        rest = a % b

    return b


def mcd_extended_euclidian(a, b):
    x_2 = 1
    x_1 = 0
    y_2 = 0
    y_1 = 1
    r_2 = a
    r_1 = b
    r = r_2 % r_1
    q = r_2 // r_1

    while r != 0:
        x = x_2 - (q * x_1)
        y = y_2 - (q * y_1)
        x_2 = x_1
        x_1 = x
        y_2 = y_1
        y_1 = y
        r_2 = r_1
        r_1 = r
        r = r_2 % r_1
        q = r_2 // r_1

    return x_1, y_1, r_1


m = int(input())
n = int(input())

t0 = time.time()
print("Recursively: ", mcd_rec(m, n))
t = time.time() - t0
print(f"Runtime: {t}")

t0 = time.time()
print("Iteratively: ", mcd_iter(m, n))
t = time.time() - t0
print(f"Runtime: {t}")

t0 = time.time()
res = mcd_extended_euclidian(m, n)
print(f"Extended euclidian algorithm: \nalpha = {res[0]}\nbeta = {res[1]}\nmcd = {res[2]}")
t = time.time() - t0
print(f"Runtime: {t}\n")
