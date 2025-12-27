//Upload immagini


export default function ImageUpload({ onFileSelect }) {
  function handleChange(event) {
    const file = event.target.files[0];
    if (file) {
      onFileSelect(file);
    }
  }

  return (
    <div className="upload-box">
      <label className="upload-label">
        Trascina un'immagine oppure clicca per selezionarla
        <input
          type="file"
          accept="image/*"
          hidden
          onChange={handleChange}
        />
      </label>
    </div>
  );
}
