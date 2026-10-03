# Filter Hero Mobile Legends — OOP + Functional Programming

Project ini membaca data hero Mobile Legends dari file JSON, membungkusnya jadi objek dengan konsep **OOP (Object-Oriented Programming)**, lalu memfilter hero yang berperan sebagai **Exp laner** saja menggunakan pendekatan **Functional Programming** (`filter` + `map` + `lambda`). Hasil akhirnya disimpan ke file CSV.

## Struktur Folder

```
.
├── data/
│   ├── heroess.json          # data mentah (input) — 13 hero ML
│   └── heroes_exp.csv       # hasil filter role Exp (output, dibuat otomatis)
├── heroes_fp.py             # script utama: baca JSON, filter+map, simpan CSV
└── README.md
```

## Format Data (`data/heroes.json`)

```json
{
    "hero": [
        {"nama": "Zilong", "role": "Exp", "ulti": "Supreme Warrior", "asal": "Dataran Naga, Asia Timur"}
    ]
}
```

| Key | Keterangan |
|---|---|
| `nama` | Nama hero |
| `role` | Role/lane hero (`Exp`, `Mid`, `Gold`, `Roam`, `Jungle`) |
| `ulti` | Nama skill ultimate hero |
| `asal` | Asal daerah/negeri hero dalam lore Mobile Legends |

Total ada 13 hero di dalamnya, 5 di antaranya ber-role `Exp` (Zilong, Yu Zhong, Paquito, Chou, Thamuz).

## Cara Menjalankan

Pastikan struktur foldernya sesuai (file `.py` sejajar dengan folder `data/`), lalu jalankan dari root folder project:

```bash
python heroes_fp.py
```

Kalau berhasil, akan muncul:
```
[SUCCESS] 5 hero role Exp disimpan di: data/heroes_exp.csv
```

## Penjelasan Kode

### `hero.py` — Class `Hero` (OOP)

Satu hero dibungkus jadi satu objek `Hero`, bukan sekadar dictionary lepas. Ada 3 method penting:

- **`from_dict(data)`** — *classmethod* yang menerima dictionary hasil parsing JSON, lalu mengembalikan objek `Hero` baru. Ini jembatan dari data mentah (JSON) ke objek OOP.
- **`is_exp_role()`** — mengecek apakah `role` hero ini sama dengan `"Exp"` (dipakai nanti sebagai syarat `filter()`).
- **`to_csv_row()`** — mengubah objek `Hero` jadi dictionary siap tulis ke CSV, sekalian mengubah nama jadi huruf kapital.

### `heroes_fp.py` — Script Utama (Functional Programming)

1. **Baca JSON** — file dibuka, lalu `payload.get("hero")` dipakai untuk ambil list hero mentahnya (ada juga pengecekan jaga-jaga kalau bentuk JSON-nya langsung berupa list).
2. **Bungkus jadi objek OOP** — tiap dictionary mentah diubah jadi objek `Hero` lewat `Hero.from_dict(item)`.
3. **Filter** — `filter(lambda hero: hero.is_exp_role(), heroes)` menyaring, hanya menyisakan hero yang method `is_exp_role()`-nya mengembalikan `True`.
4. **Map** — `map(lambda hero: hero.to_csv_row(), exp_heroes)` mengubah tiap objek `Hero` yang lolos filter menjadi dictionary siap tulis.
5. **Simpan ke CSV** — hasil `map()` dibungkus `list(...)` (karena `map()` itu *lazy iterator*), lalu ditulis ke `data/heroes_exp.csv` pakai `csv.DictWriter`.
