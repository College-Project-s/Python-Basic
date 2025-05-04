# List multi-dimensi untuk menyimpan data menu
menu = {
    "Makanan": [],
    "Minuman": [],
    "Snack": []
}

while True:
    print("\nPilih kategori menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Snack")
    print("4. Selesai")
    
    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan == "4":
        break
    elif pilihan in ["1", "2", "3"]:
        kategori = "Makanan" if pilihan == "1" else "Minuman" if pilihan == "2" else "Snack"
        nama_menu = input(f"Masukkan nama {kategori}: ")
        harga_menu = input(f"Masukkan harga {kategori}: ")
        
        if harga_menu.isdigit():
            menu[kategori].append([nama_menu, int(harga_menu)])
        else:
            print("Harga harus berupa angka!")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

# Menampilkan hasil input
print("\n=== Daftar Menu Restoran ===")
for kategori, daftar_menu in menu.items():
    print(f"\n{kategori}:")
    for item in daftar_menu:
        print(f"- {item[0]}: Rp{item[1]}")
