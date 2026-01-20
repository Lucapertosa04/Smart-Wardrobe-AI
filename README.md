# 👕 Smart Wardrobe AI
<p align="center">
  <img src="https://github.com/Lucapertosa04/Smart-Wardrobe-AI/blob/main/Logo%20Smart%20Wardrobe%20AI.png" alt="Logo:" width="300">
</p>
Smart Wardrobe AI è un’applicazione intelligente progettata per supportare l’utente nella valutazione delle caratteristiche dei capi di abbigliamento, con particolare attenzione alla durabilità, all’affidabilità e alla sostenibilità. Il sistema combina tecniche di Intelligenza Artificiale, OCR (Optical Character Recognition) e analisi dei dati per estrarre informazioni dalle etichette dei capi e fornire output chiari e interpretabili.

---

🎯 Scopo dell’applicazione
L’obiettivo di Smart Wardrobe AI è fornire un supporto decisionale all’utente, trasformando informazioni non strutturate (etichette dei capi) e dati eterogenei in output strutturati e significativi.

In particolare, il sistema è progettato per:
- automatizzare l’estrazione dei dati tramite OCR;
- normalizzare e validare input eterogenei;
- eseguire inferenza tramite un modello predittivo;
- restituire risultati trasparenti, interpretabili e affidabili.

🧩 Caratteristiche
📷 Caricamento di immagini delle etichette dei capi
🔍 Estrazione automatica del testo tramite OCR
🧹 Pulizia e normalizzazione dei dati estratti
✍️ Integrazione dei dati inseriti manualmente dall’utente
🤖 Modello predittivo con output interpretabili
📊 Indicatore di affidabilità associato a ogni stima
⚠️ Gestione di input incompleti o incoerenti
🧱 Architettura modulare e facilmente estendibile
🏗️ Architettura del sistema

L’applicazione è basata su un’architettura modulare composta dai seguenti componenti:

🔹 Frontend
- Interfaccia utente web
- Caricamento immagini
- Inserimento dati manuali
- Visualizzazione dei risultati

🔹 Backend
- Logica applicativa
- Preparazione e validazione dei dati
- Integrazione del modulo OCR
- Comunicazione con il modello AI tramite API

🔹 Modulo OCR
- Estrazione automatica del testo dalle immagini delle etichette

🔹 Modello di Intelligenza Artificiale
- Analisi dei dati normalizzati
- Produzione delle stime finali
- Calcolo dell’indicatore di affidabilità

📋 Requisiti
  Requisiti software
- Docker
- Ollama
- Ambiente di esecuzione backend (es. Python)
- Browser web moderno
- Requisiti hardware
- Dispositivo con fotocamera oppure immagini delle etichette
- Connessione Internet per l’interazione client-server

⚙️ Installazione
1️⃣ Installazione di Ollama
  Scaricare e installare Ollama dal sito ufficiale:
  [Link ufficiale Ollama](https://ollama.com/download)

  Avviare Ollama dal terminale:
  ```bash
  ollama run mistral
  ```


2️⃣ Clonazione del repository
Posizionarsi in una directory del proprio PC e clonare il progetto:
  ```bash
  git clone https://github.com/Lucapertosa04/Smart-Wardrobe-AI.git
  ```


3️⃣ Avvio del backend
Posizionarsi sulla directory principale del progetto (Smart Wardrobe AI) e accedere alla directory del backend:
  ```bash
  cd backend
  ```

Creare l’immagine Docker:
  ```bash
  docker build -t smart-wardrobe-backend .
  ```
    
Avviare il container:
  ```bash
  docker run -d --name sw-backend -p 5000:5000 smart-wardrobe-backend
  ```


4️⃣ Avvio del frontend
Accedere alla directory del frontend:
  ```bash
  cd ../frontend
  ```

Creare l’immagine Docker:
  ```bash
  docker build -t smart-wardrobe-frontend .
  ```

Avviare il container:
  ```bash
  docker run -d --name sw-frontend -p 3000:80 smart-wardrobe-frontend
  ```


5️⃣ Avvio dell’applicazione
Aprire il browser all’indirizzo:
  ```bash
  http://localhost:3000
  ```

## 👤 Autori

**Luca Pertosa** e **Flavio Monaco**  
Progetto di tesi – Smart Wardrobe AI
