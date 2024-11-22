harga_barang_a = 1000
harga_barang_b = 2000
harga_barang_c = 3000
totalAkhir = 0
def pilih_barang():
    print("\nPilih item yang ingin dibeli:")
    print("1. Barang A - Rp 1000")
    print("2. Barang B - Rp 2000")
    print("3. Barang C - Rp 3000")
    pilihan = input('Masukkan pilihan item (1/2/3): ')
    if pilihan == '1':
        return harga_barang_a
    elif pilihan == '2':
        return harga_barang_b
    elif pilihan == '3':
        return harga_barang_c
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.") 
        return None

# Program utama
while True:
    harga = pilih_barang()
    if harga is None:
        continue # Kembali ke awal loop jika pilihan tidak valid 
    jumlah = int(input('Masukkan jumlah item yang dibeli: '))
    total = harga * jumlah
    totalAkhir += total
    print(f'Total sementara: Rp {totalAkhir}')
    lagi = input('Apakah Anda ingin membeli item lain? [Y/N]: ') 
    if lagi.lower() == 'n':
        break
    
print(f'\nTerima kasih! Total belanja Anda adalah Rp {totalAkhir}')