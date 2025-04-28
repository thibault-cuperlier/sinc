import time

a = 1664525
c = 1013904223
m = 2**32

def aleatoire(seed, min_value, max_value):
    x1 = (a * seed + c) % m
    x1 = x1 / m
    result = int(min_value + (x1 * (max_value - min_value + 1)))
    return result

def get_seed():
    current_time = time.time()
    time_str = str(current_time)
    full_seed = int(time_str.replace('.', ''))
    return full_seed

def nombrePremier(number):
    if number < 2:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

def generer_nombre_premier(nb_chiffres):
    min_value = 10**(nb_chiffres - 1)
    max_value = 10**nb_chiffres - 1
    while True:
        seed = get_seed()
        candidate = aleatoire(seed, min_value, max_value)
        if nombrePremier(candidate):
            return candidate
