# routes/ocr.py

# Blueprint serve per organizzare le rotte Flask
from flask import Blueprint, jsonify, request

# Importiamo la logica OCR dal service
from services.ocr_services import extract_label_info

# Creiamo il blueprint OCR
ocr_bp = Blueprint("ocr", __name__)


@ocr_bp.route("/analyze", methods=["POST"])
def analyze_ocr():
    """
    Endpoint API per analizzare un'etichetta OCR.

    Riceve:
    {
        "ocr_text": "Lavare a 30°, ciclo delicato..."
    }

    Restituisce:
    JSON con le informazioni estratte
    """

    # Leggiamo il JSON dalla richiesta in modo sicuro
    data = request.get_json(silent=True)

    # Controlliamo che il JSON esista e contenga il campo necessario
    if not data or "ocr_text" not in data:
        return jsonify({
            "error": "Campo ocr_text mancante"
        }), 400

    # Estraiamo il testo OCR
    ocr_text = data["ocr_text"]

    # Passiamo il testo alla logica OCR
    label_info = extract_label_info(ocr_text)

    # Restituiamo la risposta al frontend
    return jsonify({
        "status": "ok",
        "label_info": label_info
    })
