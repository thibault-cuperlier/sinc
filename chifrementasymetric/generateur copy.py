import random
from sympy import isprime

# Fonction pour générer un nombre premier de 100 chiffres
def generer_premier_100_chiffres():
    while True:
        # Générer un nombre aléatoire de 100 chiffres
        num = random.randint(10**99, 10**100 - 1)  # Entre 10^99 et 10^100-1
        # Vérifier si le nombre est premier
        if isprime(num):
            return num

# Générer les nombres premiers p et q
p = generer_premier_100_chiffres()
q = generer_premier_100_chiffres()

# Afficher les résultats
print(f"Le nombre premier p est : {p}")
print(f"Le nombre premier q est : {q}")
