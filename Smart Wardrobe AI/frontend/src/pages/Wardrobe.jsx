//Pagina principale

import { useState } from "react";
import Dropdown from "../components/Dropdown";
import TextInput from "../components/TextInput";
import ImageUpload from "../components/ImageUpload";
import Button from "../components/Button";

export default function Wardrobe() {
  const [usageTime, setUsageTime] = useState("");
  const [wearLevel, setWearLevel] = useState("");
  const [notes, setNotes] = useState("");
  const [image, setImage] = useState(null);

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

      <Button
        text="Analizza capo"
        onClick={() => {
          console.log("Dati inviati:", {
            usageTime,
            wearLevel,
            notes,
            image
          });
        }}
      />
    </div>
  );
}
