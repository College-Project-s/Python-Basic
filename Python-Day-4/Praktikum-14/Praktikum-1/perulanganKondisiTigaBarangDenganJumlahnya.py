harga_barang_a = 1000
harga_barang_b = 2000 
harga_barang_c = 3000
totalAkhir = 0
# Menyimpan jumlah pembelian untuk setiap barang
jumlah_barang_a = 0
jumlah_barang_b = 0
jumlah_barang_c = 0
while True:
    print("Pilih item yang ingin dibeli:")
    print("1. Barang A - Rp 1000")
    print("2. Barang B - Rp 2000")
    print("3. Barang C - Rp 3000")
    
    pilihan = input('Masukkan pilihan item (1/2/3): ') 
    jumlah = int(input('Masukkan jumlah beli: ')) 
    if pilihan == '1':
        harga = harga_barang_a
        jumlah_barang_a += jumlah
    elif pilihan == '2':
        harga = harga_barang_b
        jumlah_barang_b += jumlah
    elif pilihan == '3':
        harga = harga_barang_c
        jumlah_barang_c += jumlah
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        continue # Kembali ke awal loop jika pilihan tidak valid
    
    # Hitung total untuk item yang dibeli
    total = harga * jumlah
    totalAkhir += total
    print(f'Total Akhir: Rp {totalAkhir}')
    
    lagi = input('Apa mau beli lagi? [Y/N]: ')
    if lagi == 'N' or lagi == 'n':
        break # Keluar dari loop jika pengguna memasukkan 'N' atau 'n'
    
# Menampilkan jumlah pembelian setiap item 
print(f'\nJumlah pembelian:')
print(f'Barang A: {jumlah_barang_a} item')
print(f'Barang B: {jumlah_barang_b} item')
print(f'Barang C: {jumlah_barang_c} item')    
print(f'Terima kasih! Total belanja Anda adalah Rp {totalAkhir}.')