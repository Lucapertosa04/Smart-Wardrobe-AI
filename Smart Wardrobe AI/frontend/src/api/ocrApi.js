//Funzione che invia al backend il testo OCR

export async function analyzeOcrText(ocrText) {
    const API_URL = "http://127.0.0.1:5000/api/ocr/analyze";

    const payload = {
        ocr_text: ocrText
    };

    try{
        //Effettua una richiesta HTTP POST al backend
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type":"application/json" //Tipo di contenuto inviato
            },
            body: JSON.stringify(payload) //conversione del payload in JSON
        });

        if(!response.ok){
            throw new Error("Errore nella chiamata OCR");
        }

        const data = await response.json(); //converte la risposta HTTP in un ogetto javascript

        return data;
    }catch(error){
        //Gestione degli errori
        console.error("Errore OCR API:", error);

        return{
            status: "error",
            message: error.message
        }
    }
}

//Verrà importato nei componenti React più avanti