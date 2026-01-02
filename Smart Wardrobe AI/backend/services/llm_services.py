#Implementazione LLM

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def genera_advice(usage_time, wear_level, notes, label_info):

    prompt = f"""
Assistente espero in abbigliamento e cura dei capi

DATI UTENTE:
 - Tempo di utilizzo: {usage_time}
 - Livello di usura: {wear_level}
 - Note utente: {notes}

DATI OCR:
{label_info}

COSA DEVI FARE:
Scrivi un consiglio, umano e pratico su:
- come trattare il capo
- se lavarlo o meno
- evantuali attenzioni
- se è da buttare quindi riciclare o no

Rispondi con tono amichevole e semplice.
"""
    
    response = requests.post(
        OLLAMA_URL,
        json ={
            "model":"mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]