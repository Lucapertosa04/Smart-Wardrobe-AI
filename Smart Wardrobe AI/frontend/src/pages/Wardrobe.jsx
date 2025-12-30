// Pagina principale

import { useState } from "react";
import Dropdown from "../components/Dropdown";
import TextInput from "../components/TextInput";
import ImageUpload from "../components/ImageUpload";
import Button from "../components/Button";

// Import delle API
import { analyzeGarment } from "../api/wardrobeApi";
import { analyzeOcrImage } from "../api/ocrApi";

export default function Wardrobe() {
  const [usageTime, setUsageTime] = useState("");
  const [wearLevel, setWearLevel] = useState("");
  const [notes, setNotes] = useState("");
  const [image, setImage] = useState(null);

  /**
   * Funzione principale di analisi del capo.
   * 1. Invia l'immagine al backend OCR
   * 2. Riceve i dati dell'etichetta
   * 3. Invia tutto al backend wardrobe
   */
  async function handleAnalyze() {

    // ✅ CORREZIONE 1:
    // L'OCR non è obbligatorio per forza:
    // se vuoi renderlo obbligatorio va bene così,
    // altrimenti questo controllo può essere tolto in futuro
    if (!image) {
      alert("Seleziona un'immagine dell'etichetta");
      return;
    }

    if (!usageTime || !wearLevel) {
      alert("Compila tutti i campi");
      return;
    }

    try {
      // 1️⃣ OCR: invio immagine al backend
      const ocrResponse = await analyzeOcrImage(image);

      // ✅ CORREZIONE 2:
      // Controllo difensivo: se l'API OCR ritorna errore o null
      if (!ocrResponse || ocrResponse.status !== "ok") {
        alert("Errore durante l'analisi OCR");
        return;
      }

      // 2️⃣ Costruzione payload completo
      const payload = {
        usage_time: usageTime,
        wear_level: wearLevel,
        notes: notes,

        // ✅ CORREZIONE 3 (IMPORTANTE):
        // label_info arriva dall'OCR, ma il backend wardrobe
        // AL MOMENTO non lo usa.
        // Va bene passarlo, ma il backend deve ignorarlo o gestirlo.
        label_info: ocrResponse.label_info
      };

      // 3️⃣ Analisi capo (menu + note)
      const wardrobeResponse = await analyzeGarment(payload);

      // Debug temporaneo
      console.log("RISULTATO FINALE:", {
        ocr: ocrResponse,
        wardrobe: wardrobeResponse
      });

      alert("Analisi completata! Guarda la console 🚀");

    } catch (error) {
      console.error("Errore analisi:", error);
      alert("Errore durante l'analisi");
    }
  }

  return (
    <div className="container">
      <h1>Smart Wardrobe AI</h1>

      <Dropdown
        label="Tempo di utilizzo"
        options={[
          "1 settimana o più",
          "1 giorno",
          "mezza giornata",
          "mai usato"
        ]}
        value={usageTime}
        onChange={(e) => setUsageTime(e.target.value)}
      />

      <Dropdown
        label="Livello di usura"
        options={["alto", "medio", "basso", "nuovo"]}
        value={wearLevel}
        onChange={(e) => setWearLevel(e.target.value)}
      />

      <TextInput
        label="Note"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />

      {/* Upload immagine OCR */}
      <ImageUpload onFileSelect={setImage} />

      {/* Mostra info se l'immagine è stata selezionata */}
      {image && (
        <p className="image-info">
          📸 Immagine selezionata: <strong>{image.name}</strong>
        </p>
      )}

      {/* ✅ onClick punta SOLO alla funzione */}
      <Button text="Analizza capo" onClick={handleAnalyze} />
    </div>
  );
}
