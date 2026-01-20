// Pagina principale

import { useState } from "react";
import Dropdown from "../components/Dropdown";
import TextInput from "../components/TextInput";
import ImageUpload from "../components/ImageUpload";
import Button from "../components/Button";
import logo from "../pages/Logo Smart Wardrobe AI without background.png"

// Import delle API
import { analyzeGarment } from "../api/wardrobeApi";
import { analyzeOcrImage } from "../api/ocrApi";

export default function Wardrobe() {
  const [usageTime, setUsageTime] = useState("");
  const [wearLevel, setWearLevel] = useState("");
  const [notes, setNotes] = useState("");
  const [image, setImage] = useState(null);
  const [aiResponse, setAiResponse] = useState("");
 
  
  async function handleAnalyze() {

    if (!image) {
      alert("Seleziona un'immagine dell'etichetta");
      return;
    }

    if (!usageTime || !wearLevel) {
      alert("Compila tutti i campi");
      return;
    }

    try {
      // OCR: invio immagine al backend
      const ocrResponse = await analyzeOcrImage(image);

      if (!ocrResponse || ocrResponse.status !== "ok") {
        alert("Errore durante l'analisi OCR");
        return;
      }

      const payload = {
        usage_time: usageTime,
        wear_level: wearLevel,
        notes: notes,

        label_info: ocrResponse.label_info
      };

      const wardrobeResponse = await analyzeGarment(payload);
  
      setAiResponse(wardrobeResponse.advice);
      
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
      <h1>
  Smart Wardrobe AI
  <img
    src={logo}
    alt="Logo"
    style={{
      width: "100px",
      height: "90px",
      marginLeft: "15px",
      verticalAlign: "middle"
    }}
  />
</h1>


      <Dropdown
        label="Tempo di utilizzo"
        options={[
          "Indossato di frequente",
          "Indossato occasionalmente",
          "Indossato raramente",
          "Mai indossato"
        ]}
        value={usageTime}
        onChange={(e) => setUsageTime(e.target.value)}
      />

      <Dropdown
        label="Livello di usura"
        options={["Usurato", "Mediocre", "Buono", "Ottimo", "Nuovo"]}
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

      {/* onClick punta SOLO alla funzione */}
      <Button text="Analizza capo" onClick={handleAnalyze} />
      <Button
        text="Reset"
        onClick={() => {
          setUsageTime("");
          setWearLevel("");
          setNotes("");
          setImage(null);
          setAiResponse("");
      }}
    />
      {/* Risposta dell'AI */}
      {aiResponse && (
        <div className="container">
          <h2>Consiglio AI</h2>
          <p>{aiResponse}</p>
        </div>
      )}  
</div>
  );
}


