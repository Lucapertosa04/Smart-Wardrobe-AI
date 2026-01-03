# utils/validators.py

def validate_user_input(data: dict):
    """
    Valida i dati ricevuti dall'utente tramite richiesta JSON.

    :param data: dizionario con i dati dell'utente
    :return: None se i dati sono validi, stringa di errore se non validi
    """

    # Campi obbligatori
    required_fields = ["usage_time", "wear_level"]

    # Controlla che i campi obbligatori esistano
    for field in required_fields:
        if field not in data:
            return f"Campo obbligatorio mancante: {field}"
        

    # Valori consentiti per i menu a tendina
    USAGE_TIME_OPTIONS = ["1 settimana o più", "1 giorno", "mezza giornata", "mai usato"]
    WEAR_LEVEL_OPTIONS = ["alto", "medio", "basso", "nuovo"]

    # Controlla che i valori siano validi
    if data["usage_time"] not in USAGE_TIME_OPTIONS:
        return f"Valore non valido per usage_time: {data['usage_time']}"

    if data["wear_level"] not in WEAR_LEVEL_OPTIONS:
        return f"Valore non valido per wear_level: {data['wear_level']}"

    # Note sono opzionali, se presenti devono essere una stringa
    if "notes" in data and not isinstance(data["notes"], str):
        return "Il campo notes deve essere una stringa"

    # Se tutto è valido
    return None
