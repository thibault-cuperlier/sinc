import asyncio
import json
from aiortc import RTCPeerConnection, RTCSessionDescription
from supabase import create_client, Client

# 🔐 Supabase credentials
SUPABASE_URL = "https://isglyvyafrpnvoxjcgjy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlzZ2x5dnlhZnJwbnZveGpjZ2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MDQ0NTMsImV4cCI6MjA2MDQ4MDQ1M30.Fw6qoLSQGty7PsYGxh8krxt-JCSIN9Nd1r4kMRLfU9I"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Utiliser la même boucle d'événements
loop = asyncio.get_event_loop()

async def handle_chat(channel):
    while channel.readyState != 'open':  # Attendre que le canal soit ouvert
        print("⏳ En attente de l'ouverture du canal...")
        await asyncio.sleep(1)

    print("📡 Canal de données prêt. Vous pouvez maintenant envoyer des messages.")
    while True:
        message = input("Vous (B) : ")
        if message.lower() == 'exit':
            print("📤 Fermeture du canal.")
            await channel.close()
            break
        channel.send(message)
        print(f"📤 Message envoyé : {message}")

async def run_answer():
    pc = RTCPeerConnection()

    @pc.on("datachannel")
    def on_datachannel(channel):
        print("📡 DataChannel reçu de A :", channel.label)

        @channel.on("open")
        def on_open():
            print("✅ DataChannel ouvert côté B. Vous pouvez maintenant envoyer des messages.")

        @channel.on("message")
        def on_message(message):
            print(f"📨 Message reçu de A : {message}")

    # 1) Récupération de l'offre
    print("🔍 En attente de l'offre depuis A…")
    offer_record = None
    while not offer_record:
        res = supabase.table("webrtc_signaling") \
            .select("*") \
            .eq("peer_id", "A") \
            .eq("type", "offer") \
            .order("created_at", desc=False) \
            .limit(1) \
            .execute()
        data = res.data
        if data:
            offer_record = data[0]
        else:
            await asyncio.sleep(1)

    print("✅ Offre reçue :", json.dumps(offer_record, indent=2))

    # 2) Application de l'offre SDP
    offer = RTCSessionDescription(
        sdp=offer_record["sdp"],
        type=offer_record["type"]
    )
    await pc.setRemoteDescription(offer)

    # 3) Création et envoi de l'answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    answer_payload = {
        "peer_id": "B",
        "type": "answer",
        "sdp": pc.localDescription.sdp
    }
    supabase.table("webrtc_signaling").insert(answer_payload).execute()
    print("📤 Answer envoyée à A.")

    # 4) Maintien actif pour échanger via le datachannel
    await asyncio.Future()

if __name__ == "__main__":
    # S'assurer que l'événement s'exécute dans la même boucle
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_answer())
