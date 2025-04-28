import time

def better_random_seed():
    """Génère une graine aléatoire en concaténant des segments de 3 chiffres."""
    t = int(time.time() * 1000) % 1000  # 3 derniers chiffres de l'heure actuelle en millisecondes
    t2 = int(time.perf_counter() * 1000) % 1000  # 3 derniers chiffres du compteur haute précision
    t3 = int(time.process_time() * 1000) % 1000  # 3 derniers chiffres du temps CPU
    t4 = int((time.time_ns() // 1000) % 1000)  # 3 derniers chiffres du temps en nanosecondes
    t5 = (t ^ t2 ^ t3 ^ t4) % 1000  # Mélange des 3 chiffres précédents
    # Concaténation des segments pour former une graine
    seed = int(f"{t:03}{t2:03}{t3:03}{t4:03}{t5:03}")
    return seed

def random_impair(min_val, max_val):
    """Génère un nombre impair aléatoire dans une plage donnée."""
    r = better_random_seed()
    n = min_val + (r % (max_val - min_val + 1))
    if n % 2 == 0:
        n += 1
        if n > max_val:
            n = min_val
    return n

def puissance_modulaire(a, d, n):
    """Calcule (a^d) % n de manière efficace."""
    res = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            res = (res * a) % n
        d = d // 2
        a = (a * a) % n
    return res

def miller_rabin(n, k=5):
    """Teste si un nombre est probablement premier en utilisant le test de Miller-Rabin."""
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
        a = 2 + (better_random_seed() % (n - 3))
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
    """Génère un nombre premier avec un nombre donné de chiffres."""
    if chiffres <= 0:
        return None
    debut = 10**(chiffres - 1)
    fin = 10**chiffres - 1
    while True:
        candidat = random_impair(debut, fin)
        if miller_rabin(candidat):
            return candidat

# Exemple d'utilisation
nombre_de_chiffres = 100  # Remplacez par le nombre de chiffres souhaité
nombre_premier = generer_nombre_premier_chiffres(nombre_de_chiffres)
print(f"Nombre premier avec {nombre_de_chiffres} chiffres : {nombre_premier}")
