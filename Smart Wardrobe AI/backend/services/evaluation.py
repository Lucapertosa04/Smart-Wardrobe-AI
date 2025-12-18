def evaluate_garment(usage_time, wear_level, notes):
    advice = []

    if usage_time in ["giornata intera", "più giorni"]:
        advice.append("Si consiglia il lavaggio")

    if wear_level in ["medio", "alto"]:
        advice.append("Usare un ciclo delicato")

    if notes and "macchia" in notes.lower():
        advice.append("Trattare la macchia prima del lavaggio")

    if not advice:
        advice.append("Nessuna azione necessaria al momento")

    return advice
