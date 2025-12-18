# Importa Blueprint per creare un modulo di rotte
# jsonify per restituire JSON
# request per leggere i dati della richiesta HTTP
from flask import Blueprint, jsonify, request

# Importa la funzione che valuta il capo
from services.evaluation import evaluate_garment

# Importa la funzione di validazione input
from utils.validators import validate_user_input

# Crea un blueprint chiamato 'wardrobe'
wardrobe_bp = Blueprint('wardrobe', __name__)

# Definisce una rotta POST all'endpoint /analyze
@wardrobe_bp.route('/analyze', methods=['POST'])
def analyze():
    # Legge il JSON dalla richiesta HTTP in modo sicuro
    data = request.get_json(silent=True)

    # Se il JSON non è valido o mancante
    if not data:
        return jsonify({'error': 'JSON non valido'}), 400

    # Valida i dati dell'utente
    error = validate_user_input(data)
    if error:
        # Se la validazione fallisce, ritorna errore 400
        return jsonify({'error': error}), 400

    # Chiama la logica di valutazione del capo
    advice = evaluate_garment(
        usage_time=data['usage_time'],   # Tempo di utilizzo
        wear_level=data['wear_level'],   # Livello di usura
        notes=data.get('notes')           # Note opzionali
    )

    # Ritorna la risposta finale in formato JSON
    return jsonify({
        'status': 'ok',
        'advice': advice
    })
