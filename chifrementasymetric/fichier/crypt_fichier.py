import os
import tkinter as tk
from tkinter import filedialog

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
    return [chiffrement_rsa(code, e, n) for code in codes if code != -1]

# Fonction Tkinter pour choisir un fichier
def choisir_fichier():
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    fichier = filedialog.askopenfilename(title="Choisissez un fichier à chiffrer")
    return fichier

# --- Entrée utilisateur ---
e, n = map(int, input("Entrez l'exposant public e et le module n, séparés par une virgule : ").split(','))

chemin_fichier = choisir_fichier()
if not chemin_fichier:
    print("❌ Aucun fichier sélectionné. Opération annulée.")
    exit()

# --- Lecture et traitement du fichier ---
with open(chemin_fichier, 'rb') as fichier:
    contenu_binaire = fichier.read()

contenu_hex = contenu_binaire.hex()
texte_chiffre = chiffrer_texte(contenu_hex, e, n)

# --- Création du nouveau fichier .crypt ---
nom_fichier_sans_ext = os.path.splitext(chemin_fichier)[0]
nouveau_nom = nom_fichier_sans_ext + "_crypt.crypt"

# Sauvegarde des données chiffrées dans le fichier .crypt
with open(nouveau_nom, 'w') as fichier_sortie:
    fichier_sortie.write(','.join(map(str, texte_chiffre)))

print(f"✅ Fichier chiffré créé : {nouveau_nom}")
