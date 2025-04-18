import openpyxl
from openpyxl import Workbook, load_workbook
import os

# Nama file excel
file_excel = 'kendaraan.xlsx'

# Cek apakah file ada, kalau tidak buat baru
if not os.path.exists(file_excel):
    wb = Workbook()
    ws = wb.active
    ws.title = 'DataKendaraan'
    ws.append(['Merk', 'Tahun', 'Warna'])
    wb.save(file_excel)

# Perulangan input data
while True:
    print("\nMasukkan data kendaraan:")
    merk = input("Merk: ")
    tahun = input("Tahun: ")
    warna = input("Warna: ")

    # Simpan ke file Excel
    wb = load_workbook(file_excel)
    ws = wb['DataKendaraan']
    ws.append([merk, tahun, warna])
    wb.save(file_excel)

    # Tanya lanjut
    lanjut = input("Ingin input data lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        break

# Ambil semua data dari Excel
wb = load_workbook(file_excel)
ws = wb['DataKendaraan']
data_kendaraan = []
for row in ws.iter_rows(min_row=2, values_only=True):  # skip header
    data_kendaraan.append(row)

# Tampilkan hasil
print("\n📋 Data dalam bentuk LIST:")
print(data_kendaraan)

print("\n🔒 Data dalam bentuk TUPLE:")
print(tuple(data_kendaraan))

print("\n🎯 Data dalam bentuk SET (unik):")
print(set(data_kendaraan))
