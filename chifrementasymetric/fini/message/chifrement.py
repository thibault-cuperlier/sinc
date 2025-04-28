from math import gcd

p = int(input("Entrez un nombre premier p : "))
q = int(input("Entrez un nombre premier q : "))

n = p * q
phi = (p - 1) * (q - 1)
print(f"n = {n}")
print(f"φ(n) = {phi}")

possibles_e = [3, 5, 17, 257, 65537]
e = None
for candidate in possibles_e:
    if gcd(candidate, phi) == 1:
        e = candidate
        break

if e is None:
    print("Erreur : aucun exposant e valide trouvé avec φ(n).")
    exit()
else:
    print(f"Exposant public choisi automatiquement : e = {e}")

def inverse_modulaire(e, phi):
    r1, r2 = phi, e
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2

    if r1 != 1:
        return None
    else:
        return t1 % phi

d = inverse_modulaire(e, phi)

if d:
    print(f"La clé publique est : ({e},{n})")
    print(f"La clé privée est  : ({d},{n})")
else:
    print("Impossible de trouver d.")
