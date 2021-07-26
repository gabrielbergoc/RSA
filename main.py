from random import choice
from primes import primes_list


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


def generate_e(phi):
    primes = primes_list(phi)

    for i in range(len(primes)-1, -1, -1):
        if phi % primes[i] != 0:    # necessary to avoid using a factor of phi
            yield primes[i]

    return None


def RSA(x, n, e):
    return x**e % n


"""
p e q são primos secretos
n é o resultado da multiplicação entre p e q
n pode ser público, pois fatorar é difícil para p e q grandes 
    e com grande diferença entre si
phi é secreto, pois precisa de p e q para calcular, e é usado para calcular d
e é público e é usado para codificar a mensagem juntamente com n
d é privado e é usado para decodificar a mensagem juntamente com n;
"""

list_of_primes = primes_list(100)

p = choice(list_of_primes[10:])
print(p)

q = choice(list_of_primes[10:])

while p == q:
    q = choice(list_of_primes[10:])
print(q)

n = p * q
print(n)

phi = (p - 1) * (q - 1)
print(phi)

for e in generate_e(phi):
    print(e)
    print(e % phi)
    d = mcd_extended_euclidian(e, phi)[0]
    print(d)
    print(d % phi)

    if d < 0:
        d += phi
        print(d)
        print(d % phi)


    if e != d and phi % d != 0 and d > 2 and e > 2:
        break


msg = [25, 102, 7, 102, 93, 49, 91, 49, 92, 118, 23, 13, 10]

msg_encoded = [RSA(msg[i], n, e) for i in range(len(msg))]
print(msg_encoded)

msg_decoded = [RSA(msg_encoded[i], n, d) for i in range(len(msg_encoded))]
print(msg_decoded)

"""
Teste com valores do livro:

p = 11
q = 13

n = p * q

phi = (p - 1) * (q - 1)

e = 7
d = mcd_extended_euclidian(e, phi)[0]

if d < 0:
    d += phi

print(n)
print(phi)
print(e)
print(d)

msg = [25, 102, 7, 102, 93, 49, 91, 49, 92, 118, 23, 13, 10]

msg_encoded = [RSA(msg[i], n, e) for i in range(len(msg))]
print(msg_encoded)

msg_decoded = [RSA(msg_encoded[i], n, d) for i in range(len(msg_encoded))]
print(msg_decoded)

"""
