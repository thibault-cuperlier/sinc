import os
import time
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

# Table inverse des codes numériques vers caractères hexadécimaux
table_inverse = {
    10: '0', 11: '1', 12: '2', 13: '3', 14: '4', 15: '5',
    16: '6', 17: '7', 18: '8', 19: '9',
    20: 'A', 21: 'B', 22: 'C', 23: 'D', 24: 'E', 25: 'F'
}

# Fonction de déchiffrement RSA : M = C^d mod n
def dechiffrement_rsa(c, d, n):
    return pow(c, d, n)

# Fonction principale de déchiffrement avec barre de progression
def dechiffrer_codes(codes_chiffres, d, n):
    codes_dechiffres = []
    for c in tqdm(codes_chiffres, desc="🔓 Déchiffrement", unit="code", dynamic_ncols=True):
        m = dechiffrement_rsa(c, d, n)
        codes_dechiffres.append(m)
    hex_chars = [table_inverse.get(code, '?') for code in codes_dechiffres]
    return ''.join(hex_chars)

# Fonction Tkinter pour choisir le fichier à déchiffrer
def choisir_fichier():
    root = tk.Tk()
    root.withdraw()
    fichier = filedialog.askopenfilename(title="Choisissez un fichier .crypt à déchiffrer", filetypes=[("Fichiers cryptés", "*.crypt")])
    return fichier

# --- Entrée utilisateur ---
d, n = map(int, input("Entrez la clé privée d et le module n (séparés par une virgule) : ").split(','))
fichier_codes = choisir_fichier()

if not fichier_codes:
    print("❌ Aucun fichier sélectionné. Opération annulée.")
    exit()

extension = input("Entrez l'extension du fichier original (ex: .pdf, .png, .txt) : ")

# Lecture des codes chiffrés
with open(fichier_codes, 'r') as f:
    ligne = f.read().strip()
    codes_chiffres = list(map(int, ligne.split(',')))

# Chronométrage + déchiffrement
debut = time.time()
hex_resultat = dechiffrer_codes(codes_chiffres, d, n)
fin = time.time()

# Conversion hexadécimal → binaire
donnees_binaires = bytes.fromhex(hex_resultat)

# Génération automatique du nom du fichier de sortie
nom_base = os.path.splitext(fichier_codes)[0]
if nom_base.endswith("_crypt"):
    nom_base = nom_base[:-6]
fichier_sortie = nom_base + "_reconstruit" + extension

# Écriture du fichier final
with open(fichier_sortie, 'wb') as f:
    f.write(donnees_binaires)

# Résultat + temps
duree = fin - debut
print(f"\n✅ Fichier déchiffré et sauvegardé sous : {fichier_sortie}")
print(f"⏱️ Temps total de déchiffrement : {duree:.2f} secondes")
