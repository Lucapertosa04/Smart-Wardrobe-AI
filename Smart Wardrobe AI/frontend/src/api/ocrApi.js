// src/api/ocrApi.js

export async function analyzeOcrImage(imageFile) {
  const API_URL = "http://127.0.0.1:5000/api/ocr/analyze";

  // FormData è OBBLIGATORIO per upload file
  const formData = new FormData();
  formData.append("image", imageFile);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error("Errore nella chiamata OCR API");
    }

    return await response.json();

  } catch (error) {
    console.error("Errore OCR API:", error);
    return {
      status: "error",
      message: error.message
    };
  }
}
