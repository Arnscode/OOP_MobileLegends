import json
import csv
from typing import List, Dict, Any

# 1. READ: Membaca file JSON
input_file_json: str = "data/heroess.json"
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Any = json.load(file)
raw_items: List[Dict[str, Any]] = payload if isinstance(payload, list) else payload.get("hero")
items: List[Dict[str, Any]] = raw_items if isinstance(raw_items, list) else []

# 2. TRANSFORM: Transformasi menggunakan filter dan lambda (tanpa OOP/class)
# [Langkah 1] Filter hero yang role-nya mengandung "EXPLine" (termasuk role gabungan seperti "Tank/EXPLine")
exp_items = filter(lambda item: "EXPLINE" in item["role"].upper().split("/"), items)

# [Langkah 2] Mapping dictionary mentah jadi dictionary siap ditulis ke CSV
formatted_data = map(
    lambda item: {
        "nama": item["nama"].upper(),
        "role": item["role"],
        "ulti": item["ulti"],
        "asal": item["asal"],
        "Asal/Wilayah(Lore/Inspirasi)": item["Asal/Wilayah(Lore/Inspirasi)"],
        "Kawasan/Budaya": item["Kawasan/Budaya"],
    },
    exp_items
)

# [Langkah 3] Convert map object jadi list
exp_hero_rows: List[Dict[str, Any]] = list(formatted_data)

# 3. WRITE: Menyimpan ke file CSV
output_path: str = "data/heroes_exp.csv"
headers: List[str] = list(exp_hero_rows[0].keys())

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(exp_hero_rows)

print(f"[SUCCESS] {len(exp_hero_rows)} hero role EXP Line disimpan di: {output_path}")