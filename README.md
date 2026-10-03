# Filter Hero Mobile Legends Functional Programming

Project ini membaca data hero Mobile Legends dari file JSON, lalu memfilter hero yang berperan sebagai **Exp laner** saja menggunakan pendekatan **Functional Programming** (`filter` + `map` + `lambda`). Hasil akhirnya disimpan ke file CSV.

## Struktur Folder

```
.
├── data/
│   ├── heroess.json          # data mentah json
│   └── heroes_exp.csv       # hasil filter role Exp (output, dibuat otomatis)
├── heroes_fp.py             # script utama: baca JSON, filter+map, simpan CSV
└── README.md
```



| Key | Keterangan |
|---|---|
| `nama` | Nama hero |
| `role` | Role/lane hero (`Exp`, `Mid`, `Gold`, `Roam`, `Jungle`) |
| `ulti` | Nama skill ultimate hero |
| `asal` | Asal daerah/negeri hero dalam lore Mobile Legends |
| `Asal/Wilayah(Lore/Inspirasi)` | Asal/Wilayah(Lore/Inspirasi) |
| `Kawasan/Budaya` | Kawasan/Budaya |

Total ada 133 hero di dalamnya, 44 di antaranya ber-role `Exp` (Zilong, Yu Zhong, Paquito, Chou, Thamuz, dst).

## Cara Menjalankan

Pastikan struktur foldernya sesuai (file `.py` sejajar dengan folder `data/`), lalu jalankan dari root folder project:

```bash
py heroes_fp.py
```

Kalau berhasil, akan muncul:
```
[SUCCESS] 5 hero role Exp disimpan di: data/heroes_exp.csv
```


