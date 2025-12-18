# Importa la classe principale Flask per creare l'applicazione
from flask import Flask

# Importa CORS per permettere richieste dal frontend (es. React, browser)
from flask_cors import CORS

# Importa il blueprint delle rotte wardrobe
from routes.wardrobe import wardrobe_bp

# Crea l'istanza dell'app Flask
app = Flask(__name__)

# Abilita CORS su tutta l'applicazione
# Serve per evitare problemi di "Cross-Origin" dal frontend
CORS(app)

# Registra il blueprint wardrobe
# Tutte le rotte inizieranno con /api/wardrobe
app.register_blueprint(wardrobe_bp, url_prefix='/api/wardrobe')

# Avvia il server Flask solo se il file viene eseguito direttamente
if __name__ == '__main__':
    # Avvia il server in modalità debug (auto-reload + errori dettagliati)
    app.run(debug=True)
