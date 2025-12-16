def evaluate_garment(usage_time, wear_level, notes):
    """
    Funzione che valuta lo stato di un capo di abbigliamento
    e restituisce una lista di consigli basati su regole semplici.
    
    Parametri:
    - usage_time: quanto tempo il capo è stato indossato
    - wear_level: livello di usura del capo
    - notes: note testuali inserite dall'utente (opzionale)
    """

    # Lista che conterrà tutti i consigli da restituire all'utente
    advice = []

    # Se il capo è stato indossato per un'intera giornata o più giorni
    # è probabile che debba essere lavato
    if usage_time in ['1 settimana o più']:
        advice.append('Si consiglia il lavaggio')

    if usage_time in ['1 giorno']:
        advice.append('Può essere ancora indossato, ma considerare il lavaggio')

    # Se il livello di usura è medio o alto
    # si suggerisce un ciclo di lavaggio delicato per non rovinare il capo
    if wear_level in ['medio', 'alto']:
        advice.append('Usare un ciclo delicato')

    if wear_level in ['nuovo']:
        advice.append('Evitare lavaggi frequenti per preservare il capo')

    # Se l'utente ha inserito delle note
    # e nelle note è presente la parola "macchia"
    # si consiglia di trattare la macchia prima del lavaggio
    if notes and "macchia" in notes.lower():
        advice.append('Trattare la macchia prima del lavaggio')

    # Se nessuna delle regole precedenti ha generato consigli
    # significa che il capo non necessita di azioni particolari
    if not advice:
        advice.append('Nessuna azione necessaria al momento')

    # Ritorna la lista finale dei consigli
    return advice
