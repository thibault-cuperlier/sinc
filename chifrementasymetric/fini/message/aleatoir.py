import random

def random_impair(min_val, max_val):
    n = random.randint(min_val, max_val)
    if n % 2 == 0:
        n += 1
        if n > max_val:
            n = min_val
    return n

def puissance_modulaire(a, d, n):
    res = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            res = (res * a) % n
        d = d // 2
        a = (a * a) % n
    return res

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = puissance_modulaire(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def generer_nombre_premier_chiffres(chiffres):
    if chiffres <= 0:
        return None
    debut = 10**(chiffres - 1)
    fin = 10**chiffres - 1
    while True:
        candidat = random_impair(debut, fin)
        if miller_rabin(candidat):
            return candidat

nombre_de_chiffres = 100
p = generer_nombre_premier_chiffres(nombre_de_chiffres)
q = generer_nombre_premier_chiffres(nombre_de_chiffres)

print(f"Nombre premier p avec {nombre_de_chiffres} chiffres : {p}")
print(f"Nombre premier q avec {nombre_de_chiffres} chiffres : {q}")
