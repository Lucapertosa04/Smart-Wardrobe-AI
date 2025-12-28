#Codice con API che legge OCR

import pytesseract
from PIL import Image
import re


def extract_text_from_image(image_path: str)->str:
   
   #Estrae il testo da una immagine

   image = Image.open(image_path)
   text = pytesseract.image_to_string(image, lang = "ita")

   return text 

def parse_label_text(ocr_text: str) -> dict:
   #Analizza il testo dell'OCR dell'etichetta

   text = ocr_text.lower()

   result = {
        "wash_30": "30°" in text,
        "wash_40": "40°" in text,
        "no_bleach": "non candeggiare" in text or "no bleach" in text,
        "dry_clean": "lavaggio a secco" in text,
        "raw_text": ocr_text
   } 

   return result


