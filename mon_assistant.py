import os
import json
from dotenv import load_dotenv
from google import genai

# 1. Charger les variables d'environnement
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Erreur : Clé API non trouvée dans le fichier .env")
else:
    # 2. Configuration du client moderne
    client = genai.Client(api_key=api_key)

    # On utilise le modèle que ton scan a trouvé
    MODEL_ID = "gemini-2.5-flash"


    def lancer_ia():
        try:
            # 3. Charger les vêtements
            with open('vetements.json', 'r', encoding='utf-8') as f:
                inventaire = json.load(f)

            # Simulation météo Montréal (Il fait 8°C ce soir)
            temp = 8

            # Filtrer les habits selon la température
            possibilites = [i for i in inventaire if i['temp_min'] <= temp <= i['temp_max']]

            if not possibilites:
                print(f"⚠️ Rien pour {temp}°C dans ton inventaire.")
                return

            prompt = f"""
            Tu es un assistant expert en style (Techwear & Old Money). 
            Il fait {temp}°C à Montréal.
            Voici mon inventaire : {json.dumps(possibilites, ensure_ascii=False)}

            Consignes :
            1. Propose une tenue complète et stylée.
            2. Priorise les habits déjà portés (compteur > 0) pour optimiser les cycles de lavage.
            3. Sois bref et utilise un ton amical.
            """

            print(f"🧠 {MODEL_ID} analyse ta garde-robe...")

            # 4. Appel à l'IA
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt
            )

            print("\n--- TA TENUE DU JOUR ---")
            print(response.text)

        except Exception as e:
            print(f"❌ Erreur lors du lancement : {e}")


    if __name__ == "__main__":
        lancer_ia()