import openpyxl
import os

# Nama file Excel untuk menyimpan data
FILE_NAME = 'data_pembelian.xlsx'

# Daftar harga barang
harga_barang_a = 1000
harga_barang_b = 2000
harga_barang_c = 3000

# Variabel untuk total belanja
totalAkhir = 0

# Fungsi untuk menampilkan menu dan mendapatkan pilihan
def pilih_barang():
    print("\nPilih item yang ingin dibeli:")
    print("1. Barang A - Rp 1000")
    print("2. Barang B - Rp 2000")
    print("3. Barang C - Rp 3000")
    
    pilihan = input('Masukkan pilihan item (1/2/3): ') 
    if pilihan == '1':
        return "Barang A", harga_barang_a
    elif pilihan == '2':
        return "Barang B", harga_barang_b
    elif pilihan == '3':
        return "Barang C", harga_barang_c 
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.") 
        return None, None

# Fungsi untuk menyimpan data pembelian ke Excel
def simpan_ke_excel(nama_barang, jumlah, harga_per_item, total_harga):
    # Cek apakah file Excel sudah ada
    if not os.path.exists(FILE_NAME):
        # Jika belum ada, buat file baru dengan header
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Pembelian"
        sheet.append(['Nama Barang', 'Jumlah', 'Harga per Item', 'Total Harga'])
    else:
        # Jika sudah ada, buka file Excel 
        workbook = openpyxl.load_workbook(FILE_NAME) 
        sheet = workbook['Pembelian']
    # Tambahkan data ke Excel
    sheet.append([nama_barang, jumlah, harga_per_item, total_harga])
    
    # Simpan perubahan
    workbook.save(FILE_NAME)
    
    # Program utama
while True:
    nama_barang, harga_per_item = pilih_barang()
    if nama_barang is None: 
        continue # Kembali ke awal loop jika pilihan tidak valid

    jumlah = int(input('Masukkan jumlah item yang dibeli: ')) 
    total_harga = harga_per_item * jumlah
    totalAkhir += total_harga
    print(f'Total sementara: Rp {totalAkhir}')
        
    # Simpan data pembelian ke Excel
    simpan_ke_excel(nama_barang, jumlah, harga_per_item, total_harga)
    lagi = input('Apakah Anda ingin membeli item lain? [Y/N]: ') 
    if lagi.lower() == 'n':
        break  
print(f'\nTerima kasih! Total belanja Anda adalah Rp {totalAkhir}.')