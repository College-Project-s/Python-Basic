print("==== List Menu Restoran Iknas ====")
print("| A1 | Ayam Goreng | 15000       |")
print("| A2 | Ayam Bakar  | 20000       |")
print("| B1 | Es Jeruk    | 8000        |")
print("| B2 | Teh Manis   | 5000        |")
print("==================================")

# Daftar harga menu
menu = {
    "A1": ("Ayam Goreng", 15000),
    "A2": ("Ayam Bakar", 20000),
    "B1": ("Es Jeruk", 8000),
    "B2": ("Teh Manis", 5000)
}

while True:
    # Input kode menu
    DataInput = input("Masukkan Kode Menu (Contoh: A105): ")
    
    # Validasi panjang input dan huruf kapital
    if len(DataInput) != 4 or not DataInput.isupper():
        print("Format kode salah! Harus 4 karakter dan huruf besar. Silakan coba lagi.")
        continue
    
    # Mengambil kode menu dan jumlah beli
    type_menu = DataInput[:2]  # Dua karakter pertama untuk kode menu
    jumlah_beli = DataInput[2:]  # Sisanya untuk jumlah beli
    
    if type_menu in menu and jumlah_beli.isdigit():
        jumlah_beli = int(jumlah_beli)
        nama_menu, harga = menu[type_menu]
        total_harga = harga * jumlah_beli
        print(f"\nMenu: {nama_menu}")
        print(f"Jumlah Beli: {jumlah_beli}")
        print(f"Total Harga: Rp{total_harga}")
        break
    else:
        print("Kode menu tidak ditemukan atau format salah! Silakan masukkan lagi.")