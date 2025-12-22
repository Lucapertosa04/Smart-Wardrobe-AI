import requests
from services.ocr_services import extract_label_info
from models.user_input import UserInput

print("\n===============================")
print(" TEST BACKEND SMART WARDROBE ")
print("===============================\n")

# --------------------------------
# 1️⃣ TEST MENU A TENDINA
# --------------------------------
print("▶ Test menu a tendina (valori ammessi)")

usage_times = [
    "1 settimana o più",
    "1 giorno",
    "mezza giornata",
    "mai usato"
]

wear_levels = [
    "alto",
    "medio",
    "basso",
    "nuovo"
]

for u in usage_times:
    for w in wear_levels:
        user = UserInput(usage_time=u, wear_level=w)
        valid, error = user.is_valid()
        assert valid, f"Valore valido rifiutato: {u}, {w}"

print("✅ Menu a tendina validi\n")

# --------------------------------
# 2️⃣ TEST MENU A TENDINA (errori)
# --------------------------------
print("▶ Test menu a tendina (valori NON ammessi)")

invalid_cases = [
    ("due settimane", "nuovo"),
    ("1 giorno", "rotto"),
    ("", "medio"),
    ("mai", "")
]

for usage, wear in invalid_cases:
    user = UserInput(usage_time=usage, wear_level=wear)
    valid, error = user.is_valid()
    assert not valid, f"Valore NON valido accettato: {usage}, {wear}"

print("✅ Valori non ammessi rifiutati\n")

# --------------------------------
# 3️⃣ TEST API FLASK
# --------------------------------
print("▶ Test API /api/wardrobe/analyze")

user = UserInput(
    usage_time="1 giorno",
    wear_level="nuovo",
    notes="Macchia di sugo sul lato"
)

valid, error = user.is_valid()
assert valid, error

url = "http://127.0.0.1:5000/api/wardrobe/analyze"
response = requests.post(url, json=user.to_dict())

print("Status code:", response.status_code)
print("Response JSON:", response.json())

assert response.status_code == 200, "API non ha risposto correttamente"

print("\n✅ TEST COMPLETO PASSATO\n")

#------------------------------------
# 4 TEST OCR_SERVICES
#------------------------------------

# -----------------------------------------------
# 4️⃣ TEST OCR_SERVICES
# -----------------------------------------------
print("\n▶ Test OCR Services")

# Test 1: Estrazione informazioni da testo OCR
print("Test 1: Estrazione informazioni base")
ocr_text_base = "Lavare a 30°C, ciclo delicato, non stirare"
label_info = extract_label_info(ocr_text_base)

assert label_info["wash_temperature"] == "30°C", f"Temperatura errata: {label_info['wash_temperature']}"
assert label_info["wash_type"] == "delicato", f"Tipo lavaggio errato: {label_info['wash_type']}"
assert label_info["iron_allowed"] == False, f"Stiratura errata: {label_info['iron_allowed']}"

print(f"✅ Test base OCR passato: {label_info}")

# Test 2: OCR con temperatura 40°C
print("\nTest 2: OCR con temperatura 40°C")
ocr_text_40 = "Lavaggio a 40 gradi, normale, lavaggio a secco"
label_info_40 = extract_label_info(ocr_text_40)

assert label_info_40["wash_temperature"] == "40°C", f"Temperatura 40°C non rilevata"
assert label_info_40["wash_type"] == "normale", f"Tipo lavaggio normale non rilevato"
assert label_info_40["dry_clean"] == True, f"Lavaggio a secco non rilevato"

print(f"✅ Test 40°C OCR passato: {label_info_40}")

# Test 3: OCR con testo incompleto
print("\nTest 3: OCR con testo parziale")
ocr_text_partial = "Stirare a temperatura media"
label_info_partial = extract_label_info(ocr_text_partial)

assert label_info_partial["iron_allowed"] == True, "Stiratura non rilevata"
assert label_info_partial["wash_temperature"] is None, "Temperatura dovrebbe essere None"

print(f"✅ Test OCR parziale passato: {label_info_partial}")

# Test 4: OCR API endpoint (simulato)
print("\nTest 4: Simulazione API endpoint OCR")

# Simula il JSON che arriverebbe dal frontend
mock_request_data = {
    "ocr_text": "Lavare a 30°C, ciclo delicato, non stirare, lavaggio a secco"
}

# Simula l'estrazione
test_label_info = extract_label_info(mock_request_data["ocr_text"])

expected_result = {
    "wash_temperature": "30°C",
    "wash_type": "delicato",
    "iron_allowed": False,
    "dry_clean": True
}

for key in expected_result:
    assert test_label_info.get(key) == expected_result[key], f"OCR API test fallito per {key}: {test_label_info.get(key)} != {expected_result[key]}"

print(f"✅ Test API OCR passato: {test_label_info}")

print("\n" + "="*50)
print("✅ TUTTI I TEST OCR PASSATI CON SUCCESSO!")
print("="*50)

