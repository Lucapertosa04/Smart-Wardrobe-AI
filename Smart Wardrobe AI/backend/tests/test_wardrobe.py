import requests
import sys

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
