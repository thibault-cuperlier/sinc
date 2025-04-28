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

# Fonction pour chiffrer un texte complet
def chiffrer_texte(texte, e, n):
    # Conversion du texte en codes
    codes = texte_vers_codes(texte)
    # Chiffrement de chaque code
    return [chiffrement_rsa(code, e, n) for code in codes if code != -1]  # Si le code est valide

# Saisie de l'utilisateur pour la clé publique e et n (saisie ensemble)
e, n = map(int, input("Entrez l'exposant public e et le module n, séparés par une virgule : ").split(','))

# Saisie du texte à chiffrer
texte = input("Entrez le texte à chiffrer : ")

# Chiffrement du texte
texte_chiffre = chiffrer_texte(texte, e, n)

# Affichage du texte chiffré en codes
print("Le texte chiffré (en codes) est :", texte_chiffre)
