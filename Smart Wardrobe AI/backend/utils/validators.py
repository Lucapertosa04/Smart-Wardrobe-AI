def validate_user_input(data):
    """
    Funzione che valida i dati inviati dall'utente.
    Controlla che siano presenti i campi obbligatori.
    """

    # Lista dei campi obbligatori che devono essere presenti nel JSON
    required_fields = ["usage_time", "wear_level"]

    # Cicla su ogni campo obbligatorio
    for field in required_fields:
        # Se un campo manca nel JSON
        if field not in data:
            # Ritorna un messaggio di errore
            return f"Campo obbligatorio mancante: {field}"

    # Se tutto è valido, ritorna None (nessun errore)
    return None
