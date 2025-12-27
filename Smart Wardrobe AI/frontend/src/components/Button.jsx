
//Crezione di un bottone

export default function Button({ text, onClick }) {
  return (
    <button className="primary-btn" onClick={onClick}>
      {text}
    </button>
  );
}
