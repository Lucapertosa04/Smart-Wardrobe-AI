import requests
import sys
import os

# Path assoluto del backend
sys.path.append(r"C:\Users\flavi\Desktop\Smart Wardrobe AI\backend")

from models.user_input import UserInput


print("\n===============================")
print(" TEST MENU A TENDINA (BACKEND) ")
print("===============================\n")

# -------------------------------
# 1️⃣ TEST VALORI AMMESSI
# -------------------------------
print("▶ Test valori AMMESSI")

valid_usage_times = [
    "1 settimana o più",
    "1 giorno",
    "mezza giornata",
    "mai usato"
]

valid_wear_levels = [
    "alto",
    "medio",
    "basso",
    "nuovo"
]

for usage in valid_usage_times:
    for wear in valid_wear_levels:
        user = UserInput(usage_time=usage, wear_level=wear)
        valid, error = user.is_valid()
        assert valid, f"❌ Valore valido rifiutato: {usage}, {wear}"

print("✅ Tutti i valori ammessi sono accettati\n")


# -------------------------------
# 2️⃣ TEST VALORI NON AMMESSI
# -------------------------------
print("▶ Test valori NON ammessi")

invalid_inputs = [
    {"usage_time": "due settimane", "wear_level": "nuovo"},
    {"usage_time": "1 giorno", "wear_level": "rottissimo"},
    {"usage_time": "", "wear_level": "medio"},
    {"usage_time": "mai", "wear_level": ""}
]

for data in invalid_inputs:
    user = UserInput(
        usage_time=data["usage_time"],
        wear_level=data["wear_level"]
    )
    valid, error = user.is_valid()
    assert not valid, f"❌ Valore NON valido accettato: {data}"

print("✅ Tutti i valori non ammessi vengono rifiutati\n")


# -------------------------------
# 3️⃣ TEST API CON INPUT VALIDO
# -------------------------------
print("▶ Test API /analyze")

user_input = UserInput(
    usage_time="1 giorno",
    wear_level="nuovo",
    notes="Macchia di sugo sul lato"
)

valid, error = user_input.is_valid()
assert valid, error

url = "http://127.0.0.1:5000/api/wardrobe/analyze"

response = requests.post(url, json=user_input.to_dict())

print("Status code:", response.status_code)
print("Response JSON:", response.json())

assert response.status_code == 200, "❌ API non ha risposto correttamente"

print("\n✅ TEST COMPLETO: USER INPUT + MENU A TENDINA + API\n")
