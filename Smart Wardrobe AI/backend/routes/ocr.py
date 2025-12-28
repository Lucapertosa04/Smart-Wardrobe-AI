# Modificato per ricevere un'immagine

from flask import Blueprint, request, jsonify
import os
from services.ocr_service import extract_text_from_image, parse_label_text

ocr_bp = Blueprint("ocr", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@ocr_bp.route("/analyze", methods=["POST"])
def analyze_ocr():
    """
    Endpoint OCR.
    Riceve un'immagine, estrae il testo e ritorna le info dell'etichetta.
    """

    if "image" not in request.files:
        return jsonify({"error": "Nessuna immagine ricevuta"}), 400

    image = request.files["image"]

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # OCR
    ocr_text = extract_text_from_image(image_path)
    parsed_data = parse_label_text(ocr_text)

    return jsonify({
        "status": "ok",
        "ocr_text": ocr_text,
        "label_info": parsed_data
    })
