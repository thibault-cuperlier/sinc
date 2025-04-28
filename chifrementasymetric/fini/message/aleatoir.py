import time

def better_random_seed():
    t = int(time.time() * 1000000)  # Convertir en entier
    t2 = int(time.perf_counter() * 1000000)  # Convertir en entier
    t3 = int(time.process_time() * 1000000)  # Convertir en entier
    mix = t ^ t2 ^ t3  # XOR entre les entiers
    return mix
t2 ^ t3  # XOR entre les entiers    t2 = time.perf_counter()
def random_impair(min_val, max_val):
    r = better_random_seed()(t * 1000000) ^ (t2 * 1000000) ^ (t3 * 1000000))  # XOR plusieurs horloges
    n = min_val + (r % (max_val - min_val + 1))    return mix
    if n % 2 == 0:
        n += 1ax_val):
        if n > max_val:
            n = min_val(r % (max_val - min_val + 1))
    return n= 0:

def puissance_modulaire(a, d, n):
    res = 1n = min_val
    a = a % n    return n
    while d > 0:
        if d % 2 == 1:ce_modulaire(a, d, n):
            res = (res * a) % n
        d = d // 2
        a = (a * a) % n
    return res
(res * a) % n
def miller_rabin(n, k=5):
    if n <= 1: * a) % n
        return False    return res
    if n == 2 or n == 3:
        return Truein(n, k=5):
    if n % 2 == 0:
        return False
    == 3:
    r = 0e
    d = n - 1
    while d % 2 == 0:    return False
        d //= 2
        r += 1
    
    for _ in range(k): == 0:
        a = 2 + (better_random_seed() % (n - 3))2
        x = puissance_modulaire(a, d, n)    r += 1
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):(n - 3))
            x = (x * x) % ne(a, d, n)
            if x == n-1: x == n-1:
                break
        else::
            return False% n
    return True-1:
   break
def generer_nombre_premier_chiffres(chiffres):
    if chiffres <= 0:urn False
        return None    return True
    debut = 10**(chiffres - 1)
    fin = 10**chiffres - 1emier_chiffres(chiffres):
    while True:0:
        candidat = random_impair(debut, fin)
        if miller_rabin(candidat):- 1)
            return candidathiffres - 1

# Exempleebut, fin)
print(generer_nombre_premier_chiffres(nombre_de_chiffres))didat):
