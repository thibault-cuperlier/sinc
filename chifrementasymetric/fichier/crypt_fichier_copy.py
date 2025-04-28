import os
from tqdm import tqdm

# Table de correspondance hexadécimal ↔ codes numériques
table = {
    '0': 10, '1': 11, '2': 12, '3': 13, '4': 14, '5': 15,
    '6': 16, '7': 17, '8': 18, '9': 19,
    'A': 20, 'B': 21, 'C': 22, 'D': 23, 'E': 24, 'F': 25
}

# Fonction de conversion texte → codes
def texte_vers_codes(texte):
    return [table.get(c.upper(), -1) for c in texte if c.upper() in table]

# Fonction de chiffrement RSA
def chiffrement_rsa(m, e, n):
    return pow(m, e, n)

# Fonction pour chiffrer un texte complet
def chiffrer_texte(texte, e, n):
    codes = texte_vers_codes(texte)
    texte_chiffre = []
    for code in tqdm(codes, desc="🔒 Chiffrement en cours", unit="caractère"):
        if code != -1:
            texte_chiffre.append(chiffrement_rsa(code, e, n))
    return texte_chiffre

# Fonction pour rendre un fichier caché
def rendre_fichier_cache(chemin_fichier):
    os.system(f'attrib +h "{chemin_fichier}"')

# Fonction pour rendre un fichier visible
def rendre_fichier_visible(chemin_fichier):
    os.system(f'attrib -h "{chemin_fichier}"')

# --- Entrée utilisateur ---
e, n = map(int, input("Entrez l'exposant public e et le module n, séparés par une virgule : ").split(','))

# Récupération du chemin du bureau
chemin_bureau = os.path.join(os.path.expanduser("~"), "Desktop")

# Liste des fichiers sur le bureau
fichiers = [f for f in os.listdir(chemin_bureau) if os.path.isfile(os.path.join(chemin_bureau, f))]

if not fichiers:
    print("❌ Aucun fichier trouvé sur le bureau. Opération annulée.")
    exit()

# Traitement de chaque fichier
fichiers_originaux = []
fichiers_chiffres = []

for fichier in fichiers:
    chemin_fichier = os.path.join(chemin_bureau, fichier)
    fichiers_originaux.append(chemin_fichier)
    
    # Lecture et traitement du fichier
    with open(chemin_fichier, 'rb') as fichier_source:
        contenu_binaire = fichier_source.read()

    contenu_hex = contenu_binaire.hex()
    texte_chiffre = chiffrer_texte(contenu_hex, e, n)

    # Création du nouveau fichier .crypt
    nom_fichier_sans_ext = os.path.splitext(fichier)[0]
    nouveau_nom = nom_fichier_sans_ext + "_crypt.crypt"
    chemin_nouveau_fichier = os.path.join(chemin_bureau, nouveau_nom)

    # Sauvegarde des données chiffrées dans le fichier .crypt
    with open(chemin_nouveau_fichier, 'w') as fichier_sortie:
        fichier_sortie.write(','.join(map(str, texte_chiffre)))

    fichiers_chiffres.append(chemin_nouveau_fichier)

# Rendre les fichiers chiffrés visibles
for fichier_chiffre in fichiers_chiffres:
    rendre_fichier_visible(fichier_chiffre)

# Rendre les fichiers originaux cachés
for fichier_original in fichiers_originaux:
    rendre_fichier_cache(fichier_original)

print("✅ Tous les fichiers du bureau ont été chiffrés, les fichiers chiffrés sont visibles, et les fichiers originaux sont maintenant cachés.")
