# services/ocr_service.py

def extract_label_info(ocr_text: str):
    """
    Questa funzione simula l'elaborazione OCR di un'etichetta.
    
    INPUT:
    - ocr_text: stringa di testo (risultato OCR o simulazione)

    OUTPUT:
    - dizionario con informazioni strutturate sull'etichetta
    """

    # Dizionario che conterrà le informazioni finali estratte
    # In futuro questo sarà letto dall'AI vera
    label_data = {
        "wash_temperature": None,  # Es. 30°C, 40°C
        "wash_type": None,         # delicato / normale
        "iron_allowed": None,      # True / False
        "dry_clean": None          # True / False
    }

    # Normalizziamo il testo per facilitare il parsing
    # (così evitiamo problemi con maiuscole/minuscole)
    text = ocr_text.lower()

    # ---------------------------
    # ANALISI TEMPERATURA
    # ---------------------------
    if "30°" in text or "30" in text:
        label_data["wash_temperature"] = "30°C"
    elif "40°" in text or "40" in text:
        label_data["wash_temperature"] = "40°C"

    # ---------------------------
    # ANALISI TIPO DI LAVAGGIO
    # ---------------------------
    if "delicato" in text:
        label_data["wash_type"] = "delicato"
    elif "normale" in text:
        label_data["wash_type"] = "normale"

    # ---------------------------
    # ANALISI STIRATURA
    # ---------------------------
    if "non stirare" in text:
        label_data["iron_allowed"] = False
    elif "stirare" in text:
        label_data["iron_allowed"] = True

    # ---------------------------
    # ANALISI LAVAGGIO A SECCO
    # ---------------------------
    if "lavaggio a secco" in text:
        label_data["dry_clean"] = True

    # Ritorniamo il dizionario finale
    return label_data
