table = {
    'A': 73, 'B': 56, 'C': 23, 'D': 84, 'E': 12, 'F': 61, 'G': 47, 'H': 90, 'I': 38,
    'J': 55, 'K': 11, 'L': 64, 'M': 19, 'N': 82, 'O': 71, 'P': 30, 'Q': 49, 'R': 20,
    'S': 87, 'T': 42, 'U': 77, 'V': 59, 'W': 18, 'X': 63, 'Y': 25, 'Z': 36,
    ' ': 0
}

table_inverse = {v: k for k, v in table.items()}

def texte_vers_codes(texte):
    return [table.get(c.upper(), -1) for c in texte]

def chiffrement_rsa(m, e, n):
    return pow(m, e, n)

def chiffrer_texte(texte, e, n):
    codes = texte_vers_codes(texte)
    return [chiffrement_rsa(code, e, n) for code in codes if code != -1]

e, n = map(int, input("Entrez l'exposant public e et le module n, séparés par une virgule : ").split(','))
texte = input("Entrez le texte à chiffrer : ")
texte_chiffre = chiffrer_texte(texte, e, n)
print("Le texte chiffré (en codes) est :", texte_chiffre)
