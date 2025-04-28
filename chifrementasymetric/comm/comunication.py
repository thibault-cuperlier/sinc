import os
import time
from supabase import create_client, Client
from websocket import create_connection

# Configuration Supabase
SUPABASE_URL = "https://isglyvyafrpnvoxjcgjy.supabase.co"  # Remplacez par votre URL Supabase
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlzZ2x5dnlhZnJwbnZveGpjZ2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MDQ0NTMsImV4cCI6MjA2MDQ4MDQ1M30.Fw6qoLSQGty7PsYGxh8krxt-JCSIN9Nd1r4kMRLfU9I"  # Remplacez par votre clé API Supabase

# Initialisation du client Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def listen_to_table():
    """
    Écoute en temps réel les modifications sur la table 'crypt'.
    """
    print("Connexion au WebSocket pour écouter les modifications en temps réel...")
    ws_url = f"{SUPABASE_URL.replace('https', 'wss')}/realtime/v1/websocket?apikey={SUPABASE_KEY}"
    ws = create_connection(ws_url)

    # Envoi du message d'abonnement
    ws.send('''
    {
        "type": "subscribe",
        "topic": "realtime:public:crypt",
        "event": "INSERT",
        "payload": {},
        "ref": "1"
    }
    ''')

    try:
        while True:
            result = ws.recv()
            print("Message brut reçu :", result)
    except Exception as e:
        print("Erreur lors de la réception :", e)
    finally:
        ws.close()

def send_message(content: str):
    """
    Envoie un message dans la table 'crypt'.
    """
    data = {"message": content}
    response = supabase.table("crypt").insert(data).execute()
    print("Message envoyé :", response.data)

if __name__ == "__main__":
    print("Bienvenue dans la messagerie en temps réel.")
    print("1. Écouter les messages en temps réel")
    print("2. Envoyer un message")
    
    while True:
        choice = input("Choisissez une option (1 ou 2, 'q' pour quitter) : ")
        if choice == "1":
            listen_to_table()
        elif choice == "2":
            message = input("Entrez votre message : ")
            send_message(message)
        elif choice.lower() == "q":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")