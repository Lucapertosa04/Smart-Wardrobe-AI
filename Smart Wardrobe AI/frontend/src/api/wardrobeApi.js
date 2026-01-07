//Funzione che invia al backend i dati inseriti dall'utente

export async function analyzeGarment(UserInput) {
    const API_URL = "http://127.0.0.1:5000/api/wardrobe/analyze";

    try{
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(UserInput)
        });

        if(!response.ok){
            const errorData = await response.json();

            throw new Error(errorData.error || "Errore nella richiesta");
        }

        const data = await response.json();

        return data;
    }catch(error){
        //stampa errore in console per facilitare debug
        console.error("Errore Wardrobe API: ", error);

        return{
            status: "error",
            message: error.message
        }
    }
}

//Ponte tra frontend e backend per quanto riguarda l'analisi del capo d'abbigliamento