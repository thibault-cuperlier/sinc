# Table de correspondance lettres ↔ codes (ajout de l'espace)
table = {
    'A': 73, 'B': 56, 'C': 23, 'D': 84, 'E': 12, 'F': 61, 'G': 47, 'H': 90, 'I': 38,
    'J': 55, 'K': 11, 'L': 64, 'M': 19, 'N': 82, 'O': 71, 'P': 30, 'Q': 49, 'R': 20,
    'S': 87, 'T': 42, 'U': 77, 'V': 59, 'W': 18, 'X': 63, 'Y': 25, 'Z': 36,
    ' ': 0  # Ajout de l'espace
}

# Inverse de la table (codes ↔ lettres)
table_inverse = {v: k for k, v in table.items()}

# Fonction de conversion texte → codes (en utilisant la table personnalisée)
def texte_vers_codes(texte):
    return [table.get(c.upper(), -1) for c in texte]  # -1 si lettre non trouvée

# Fonction de chiffrement RSA : C = M^e mod n
def chiffrement_rsa(m, e, n):
    return pow(m, e, n)

# Fonction de déchiffrement RSA : M = C^d mod n
def dechiffrement_rsa(c, d, n):
    return pow(c, d, n)

# Fonction pour chiffrer un texte complet
def chiffrer_texte(texte, e, n):
    # Conversion du texte en codes
    codes = texte_vers_codes(texte)
    # Chiffrement de chaque code
    return [chiffrement_rsa(code, e, n) for code in codes if code != -1]  # Si le code est valide

# Fonction pour déchiffrer une suite de nombres
def dechiffrer_suite_de_nombres(suite, d, n):
    # Déchiffrement de chaque nombre
    return [dechiffrement_rsa(code, d, n) for code in suite]

# Fonction pour générer la clé privée et publique
def generer_cles(p, q):
    # Calcul du module n
    n = p * q
    # Calcul de la fonction d'Euler φ(n)
    phi = (p - 1) * (q - 1)

    # Choix de l'exposant public e (doit être premier avec φ(n))
    e = 17  # Exemple d'exposant public
    while gcd(e, phi) != 1:
        e += 2  # Incrémenter jusqu'à ce que e soit premier avec φ(n)

    # Calcul de l'exposant privé d (inverse modulaire de e mod φ(n))
    d = mod_inverse(e, phi)
    
    return e, n, d, n

# Fonction pour calculer l'inverse modulaire (algorithme d'Euclide étendu)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Exemple de nombres premiers p et q
p = 61  # Premier
q = 53  # Premier

# Génération des clés publique et privée
e, n, d, n_prime = generer_cles(p, q)

# Affichage des clés dans le format demandé
print(f"La clé publique est : ({e},{n})")
print(f"La clé privée est : ({d},{n_prime})")

# Saisie du texte à chiffrer
texte = input("Entrez le texte à chiffrer : ")

# Chiffrement du texte
texte_chiffre = chiffrer_texte(texte, e, n)

# Affichage du texte chiffré en codes
print("Le texte chiffré (en codes) est :", texte_chiffre)

# Saisie de la suite de nombres à déchiffrer
suite_de_nombres = list(map(int, input("Entrez la suite de nombres à déchiffrer (séparés par des virgules) : ").split(',')))

# Déchiffrement de la suite de nombres
suite_de_codes = dechiffrer_suite_de_nombres(suite_de_nombres, d, n)

# Conversion des codes déchiffrés en texte
texte_dechiffre = ''.join([table_inverse.get(code, '?') for code in suite_de_codes])

# Affichage du texte déchiffré
print("Le texte déchiffré est :", texte_dechiffre)
