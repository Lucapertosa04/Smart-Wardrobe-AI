//Campo note (testo utente)

export default function TextInput({ label, value, onChange }) {
  return (
    <div className="field">
      <label>{label}</label>

      <textarea
        rows="4"
        placeholder="Inserisci eventuali note..."
        value={value}
        onChange={onChange}
      />
    </div>
  );
}
