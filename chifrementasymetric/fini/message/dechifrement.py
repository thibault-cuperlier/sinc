table = {
    'A': 73, 'B': 56, 'C': 23, 'D': 84, 'E': 12, 'F': 61, 'G': 47, 'H': 90, 'I': 38,
    'J': 55, 'K': 11, 'L': 64, 'M': 19, 'N': 82, 'O': 71, 'P': 30, 'Q': 49, 'R': 20,
    'S': 87, 'T': 42, 'U': 77, 'V': 59, 'W': 18, 'X': 63, 'Y': 25, 'Z': 36,
    ' ': 0
}

table_inverse = {v: k for k, v in table.items()}

def codes_vers_texte(codes):
    return ''.join([table_inverse.get(code, '?') for code in codes])

def dechiffrement_rsa(c, d, n):
    return pow(c, d, n)

def dechiffrer_suite_de_nombres(suite, d, n):
    return [dechiffrement_rsa(code, d, n) for code in suite]

d, n = map(int, input("Entrez l'exposant privé d et le module n, séparés par une virgule : ").split(','))
suite_de_nombres = list(map(int, input("Entrez la suite de nombres à déchiffrer (séparés par des virgules) : ").split(',')))
suite_de_codes = dechiffrer_suite_de_nombres(suite_de_nombres, d, n)
texte_dechiffre = codes_vers_texte(suite_de_codes)
print("Le texte déchiffré est :", texte_dechiffre)
