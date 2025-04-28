# Table de correspondance lettres ↔ codes (ajout de l'espace)
table = {
    'A': 73, 'B': 56, 'C': 23, 'D': 84, 'E': 12, 'F': 61, 'G': 47, 'H': 90, 'I': 38,
    'J': 55, 'K': 11, 'L': 64, 'M': 19, 'N': 82, 'O': 71, 'P': 30, 'Q': 49, 'R': 20,
    'S': 87, 'T': 42, 'U': 77, 'V': 59, 'W': 18, 'X': 63, 'Y': 25, 'Z': 36,
    ' ': 0  # Ajout de l'espace
}

# Inverse de la table (codes ↔ lettres)
table_inverse = {v: k for k, v in table.items()}

# Fonction de conversion des codes → texte (en utilisant la table inverse)
def codes_vers_texte(codes):
    return ''.join([table_inverse.get(code, '?') for code in codes])  # '?' pour les codes non valides

# Fonction de déchiffrement RSA : M = C^d mod n
def dechiffrement_rsa(c, d, n):
    return pow(c, d, n)

# Fonction pour déchiffrer une suite de nombres
def dechiffrer_suite_de_nombres(suite, d, n):
    # Déchiffrement de chaque nombre
    return [dechiffrement_rsa(code, d, n) for code in suite]

# Saisie de l'utilisateur pour la clé privée d et n (saisie ensemble)
d, n = map(int, input("Entrez l'exposant privé d et le module n, séparés par une virgule : ").split(','))

# Saisie de la suite de nombres à déchiffrer (séparée par des virgules)
suite_de_nombres = list(map(int, input("Entrez la suite de nombres à déchiffrer (séparés par des virgules) : ").split(',')))

# Déchiffrement de la suite de nombres
suite_de_codes = dechiffrer_suite_de_nombres(suite_de_nombres, d, n)

# Conversion des codes déchiffrés en texte
texte_dechiffre = codes_vers_texte(suite_de_codes)

# Affichage du texte déchiffré
print("Le texte déchiffré est :", texte_dechiffre)
