# 👕 Smart Wardrobe AI
<p align="center">
  <img src="https://github.com/Lucapertosa04/Smart-Wardrobe-AI/blob/main/Logo%20Smart%20Wardrobe%20AI.png" alt="Logo:" width="300">
</p>
Smart Wardrobe AI è un’applicazione intelligente progettata per supportare l’utente nella valutazione delle caratteristiche dei capi di abbigliamento, con particolare attenzione alla durabilità, all’affidabilità e alla sostenibilità. Il sistema combina tecniche di Intelligenza Artificiale, OCR (Optical Character Recognition) e analisi dei dati per estrarre informazioni dalle etichette dei capi e fornire output chiari e interpretabili.

---

## 🎯 Scopo dell’applicazione

L’obiettivo di Smart Wardrobe AI è fornire un supporto decisionale all’utente, trasformando informazioni non strutturate (etichette tessili) e dati eterogenei in output strutturati e significativi.

Il sistema è progettato per:
- automatizzare l’estrazione dei dati tramite OCR (Optical Character Recognition);
- normalizzare e validare input eterogenei;
- eseguire inferenza tramite un modello predittivo;
- restituire risultati trasparenti e affidabili.

---

## 🧩 Caratteristiche

- Caricamento di immagini delle etichette dei capi
- Estrazione automatica del testo tramite OCR
- Pulizia e normalizzazione dei dati estratti
- Integrazione dei dati inseriti manualmente dall’utente
- Modello predittivo con output interpretabili
- Indicatore di affidabilità associato a ogni stima
- Gestione dei casi di input incompleti o incoerenti
- Architettura modulare e facilmente estendibile

---

## 🏗️ Architettura del sistema

L’applicazione è basata su un’architettura modulare composta da:

- **Frontend**  
  Interfaccia utente per il caricamento delle immagini, l’inserimento dei dati e la visualizzazione dei risultati.

- **Backend**  
  Gestisce la logica applicativa, la preparazione dei dati, l’integrazione del modulo OCR e la comunicazione con il modello predittivo tramite API.

- **Modulo OCR**  
  Responsabile dell’estrazione del testo dalle immagini delle etichette.

- **Modello di Intelligenza Artificiale**  
  Elabora i dati normalizzati e produce le stime finali, includendo un indicatore di affidabilità.

---

## 📋 Requisiti

### Requisiti
- Dispositivo con fotocamera o immagini delle etichette
- Connessione internet per l’interazione client-server
- Ambiente di esecuzione per backend (es. Python)
- Docker
- Browser web moderno per il frontend

---

## ⚙️ Installazione

1. Aprire il terminale e clonare il repository:
    ```bash
    git clone https://github.com/Lucapertosa04/Smart-Wardrobe-AI.git
    ```

2.Posizionarsi sulla cartella principale del progetto (Smart Wardrobe AI) e accedere alla directory del backend del progetto:
    ```bash
    cd backend
    ```

3. Creare l'immagine Docker del backend:
    ```bash
    docker build -t smart-wardrobe-backend .
    ```
    
4. Lanciare il comando con le porte (backend):
    ```bash
    docker run -d --name sw-backend -p 5000:5000 smart-wardrobe-backend
    ```

5.Accedere alla directory del frontend del progetto:
    ```bash
    cd ../frontend
    ```

6. Creare l'immagine Docker del frontend:
    ```bash
    docker build -t smart-wardrobe-frontend .
    ```

7. Lanciare il comando con le porte (frontend):
    ```bash
    docker run -d --name sw-frontend -p 8080:80 smart-wardrobe-frontend
    ```

8. Aprire il browser all'indirizzo:
    ```bash
    http://localhost:8080
    ```

## 👤 Autori

**Luca Pertosa** e **Flavio Monaco**  
Progetto di tesi – Smart Wardrobe AI
