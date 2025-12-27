

 //Crea menù a tendina
export default function Dropdown({ label, options, value, onChange }) {
  return (
    <div className="field">
      <label>{label}</label>

      <select value={value} onChange={onChange}>
        <option value="">Seleziona</option>

        {options.map((opt, index) => (
          <option key={index} value={opt}>
            {opt}
          </option>
        ))}
      </select>
    </div>
  );
}
