
# request per leggere i dati della richiesta HTTP
from flask import Blueprint, jsonify, request

# Importa la funzione di validazione input
from utils.validators import validate_user_input

#Importa funzione per LLM
from services.llm_services import genera_advice

# Crea un blueprint chiamato 'wardrobe'
wardrobe_bp = Blueprint('wardrobe', __name__)

# Definisce una rotta POST all'endpoint /analyze
@wardrobe_bp.route('/analyze', methods=['POST'])
def analyze():
    # Legge il JSON dalla richiesta HTTP in modo sicuro
    data = request.get_json(force=True)

    # Se il JSON non è valido o mancante
    if not data:
        return jsonify({'error': 'JSON non valido'}), 400

    # Valida i dati dell'utente
    error = validate_user_input(data)
    if error:
        print(" VALIDATION ERROR:", error)
        print(" DATA RICEVUTI:", data)
        return jsonify({'error': error}), 400

    label_info = data.get("label_info", "")
    if isinstance(label_info, dict):
        label_info = str(label_info)

    # Chiama la logica di valutazione del capo
    advice = genera_advice(
        usage_time=data['usage_time'],   
        wear_level=data['wear_level'],   
        notes=data.get('notes'),
        label_info = label_info        
    )

    # Ritorna la risposta finale in formato JSON
    return jsonify({
        'status': 'ok',
        'advice': advice
    })
