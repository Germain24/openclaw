import os
from dotenv import load_dotenv # AJOUTE CETTE LIGNE
from google import genai

# AJOUTE CETTE LIGNE pour charger ta clé du fichier .env
load_dotenv()

# MODIFIE CETTE LIGNE pour passer la clé au client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- LISTE DES MODÈLES DISPONIBLES ---")
try:
    for m in client.models.list():
        if "generateContent" in m.supported_actions:
            print(f"Modèle : {m.name}")
except Exception as e:
    print(f"❌ Erreur : {e}")