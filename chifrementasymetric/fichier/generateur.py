import random
from sympy import isprime

def generer_nombre_premier(nb_chiffres):
    """Génère un nombre premier ayant exactement nb_chiffres chiffres."""
    assert nb_chiffres >= 1
    borne_min = 10**(nb_chiffres - 1)
    borne_max = 10**nb_chiffres - 1

    while True:
        candidat = random.randint(borne_min, borne_max)
        if isprime(candidat):
            return candidat

# Générer deux nombres premiers de 10 chiffres
p = generer_nombre_premier(10)
q = generer_nombre_premier(10)

# Affichage
print(f"🔢 Nombre premier p : {p}")
print(f"🔢 Nombre premier q : {q}")
print(f"🧮 Module n = p × q : {p * q}")
