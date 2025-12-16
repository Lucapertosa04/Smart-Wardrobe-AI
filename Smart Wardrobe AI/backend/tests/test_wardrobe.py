# tests/test_wardrobe_user_input.py

import requests

import sys
import os

sys.path.append(r"C:\Users\flavi\Desktop\Smart Wardrobe AI\backend")

from models.user_input import UserInput

# --- Dati di test simulati dall'utente ---
test_data = {
    "usage_time": "1 giorno",       # Tempo di utilizzo del capo
    "wear_level": "nuovo",          # Livello di usura
    "activity": "lavoro",           # Attività svolta (non ancora usata)
    "notes": "Macchiata di rosso"   # Note libere dell'utente
}

# --- Creazione oggetto UserInput ---
user_input = UserInput(
    usage_time=test_data["usage_time"],
    wear_level=test_data["wear_level"],
    notes=test_data.get("notes", "")
)

# --- Validazione dei dati ---
valid, error = user_input.is_valid()

if not valid:
    print("Errore validazione input:", error)
else:
    print("Dati validi, invio al backend:", user_input.to_dict())

    # --- Invio richiesta POST al backend solo se i dati sono validi ---
    url = "http://127.0.0.1:5000/api/wardrobe/analyze"
    response = requests.post(url, json=user_input.to_dict())

    # --- Stampa risultati ---
    print("Status code:", response.status_code)
    try:
        print("JSON response:", response.json())
    except Exception as e:
        print("Errore nel parsing JSON:", e)
        print("Testo risposta:", response.text)
