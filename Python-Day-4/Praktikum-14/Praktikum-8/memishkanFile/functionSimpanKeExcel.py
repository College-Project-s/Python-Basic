import openpyxl
import os

FILE_NAME = 'data_pembelian.xlsx'
def pilih_item():
    """
    Menampilkan pilihan barang dan mengembalikan harga barang yang dipilih pengguna.
    """
    
    print("Pilih item yang ingin dibeli:")
    print("1. Barang A - Rp 1000")
    print("2. Barang B - Rp 2000")
    print("3. Barang C - Rp 3000")
    
    pilihan = input("Masukkan pilihan item (1/2/3): ")
    
    if pilihan == '1':
        harga = 1000
        nama_barang = "Barang A"
    elif pilihan == '2':
        harga = 2000
        nama_barang = "Barang B"
    elif pilihan == '3':
        harga = 3000
        nama_barang = "Barang C"
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.") 
        return None, None
    
    return nama_barang, harga

def simpan_ke_excel(nama_barang, jumlah_beli, total_harga):
    """
    Menyimpan data pembelian ke file Excel.
    """
    # Cek jika file Excel belum ada, buat file baru
    if not os.path.exists(FILE_NAME):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Pembelian"
    # Tambahkan header
        sheet.append(["Nama Barang", "Jumlah Beli", "Total Harga"])
    else:
            workbook = openpyxl.load_workbook(FILE_NAME) 
            sheet = workbook["Pembelian"]
            
    # Tambahkan data pembelian
    sheet.append([nama_barang, jumlah_beli, total_harga])
    # Simpan file Excel
    workbook.save(FILE_NAME)
    print("Data pembelian berhasil disimpan ke Excel.")