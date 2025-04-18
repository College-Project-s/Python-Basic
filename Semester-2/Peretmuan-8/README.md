Siap Farhan! Ini dia dokumentasi program kamu dalam format `README.md` yang bisa kamu pakai langsung untuk laporan atau dokumentasi tugas 💪

---

### 📄 `README.md` - Program Penyimpanan Data Kendaraan ke Excel

---

## 1️⃣ Judul  
**Program Input Data Kendaraan + Simpan ke Excel + Tampilkan dalam Bentuk List, Tuple, dan Set**

---

## 📌 Apa yang terjadi?

Program ini menerima data kendaraan dari user, lalu menyimpan data tersebut ke file Excel (`kendaraan.xlsx`) menggunakan library `openpyxl`. Program juga mampu menampilkan seluruh data kendaraan yang sudah diinput dalam bentuk:

- 🔹 List
- 🔹 Tuple
- 🔹 Set

---

## 🔍 Kenapa pakai ini?

| Fitur                         | Penjelasan                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| `openpyxl`                   | Untuk membaca dan menulis file Excel (.xlsx)                              |
| `os.path.exists`             | Mengecek apakah file sudah ada, kalau belum maka buat file baru           |
| `while True`                 | Agar user bisa input data lebih dari satu kali                            |
| `input()`                    | Mengambil data dari user                                                   |
| `ws.append()`                | Menambahkan baris baru ke sheet Excel                                     |
| `values_only=True`           | Mengambil hanya nilai dari cell saat membaca data                         |
| `set()`                      | Menampilkan data unik (menghindari duplikat)                              |

---

## 🧾 Struktur Program

| Bagian Program                | Penjelasan                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| **1. Setup & Cek File**      | Mengecek apakah `kendaraan.xlsx` sudah ada. Kalau belum, buat file baru. |
| **2. Input Data**            | User akan diminta memasukkan `Merk`, `Tahun`, dan `Warna`.                |
| **3. Simpan ke Excel**       | Data yang dimasukkan akan disimpan sebagai baris baru di sheet.           |
| **4. Tanya Ulang**           | Program akan bertanya: "Ingin input lagi?" dan lanjut jika jawab `ya`.    |
| **5. Baca Semua Data**       | Setelah user selesai, program akan membaca semua data dari file.          |
| **6. Tampilkan Data**        | Ditampilkan dalam 3 format: List, Tuple, dan Set.                         |

---

## 💡 Contoh Output

```
Masukkan data kendaraan:
Merk: Honda
Tahun: 2020
Warna: Hitam
Ingin input data lagi? (ya/tidak): ya

Masukkan data kendaraan:
Merk: Yamaha
Tahun: 2022
Warna: Biru
Ingin input data lagi? (ya/tidak): tidak

📋 Data dalam bentuk LIST:
[('Honda', '2020', 'Hitam'), ('Yamaha', '2022', 'Biru')]

🔒 Data dalam bentuk TUPLE:
(('Honda', '2020', 'Hitam'), ('Yamaha', '2022', 'Biru'))

🎯 Data dalam bentuk SET (unik):
{('Honda', '2020', 'Hitam'), ('Yamaha', '2022', 'Biru')}
```

---