#Importato il blueprint OCR

# Importa la classe principale Flask per creare l'applicazione
from flask import Flask

# Importa CORS per permettere richieste dal frontend
from flask_cors import CORS

# Importa i blueprint delle rotte
from routes.wardrobe import wardrobe_bp
from routes.ocr import ocr_bp   

# Crea l'istanza dell'app Flask
app = Flask(__name__)

# Abilita CORS su tutta l'applicazione
CORS(app)

# Registra i blueprint
app.register_blueprint(wardrobe_bp, url_prefix="/api/wardrobe")
app.register_blueprint(ocr_bp, url_prefix="/api/ocr")  

# Avvia il server Flask solo se il file viene eseguito direttamente
if __name__ == "__main__":
    app.run( host="0.0.0.0",
        port=5000,
        debug=False)
