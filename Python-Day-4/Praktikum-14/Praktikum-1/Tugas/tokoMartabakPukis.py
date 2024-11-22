# Deklarasi Variabel Untuk Martabak
martabakCoklat = 20000
martabakKeju = 25000
martabakKismis = 15000

# Deklarasi Variabel Untuk Pukis
pukisCoklat = 15000
pukisKeju = 20000
pukisKismis = 15000

# Menyimpan jumlah pembelian untuk setiap barang
jumlahMartabakCoklat = 0
jumlahMartabakKeju = 0
jumlahMartabakKismis = 0
jumlahPukisCoklat = 0
jumlahPukisKeju = 0
jumlahPukisKismis = 0

totalAkhir = 0

while True:
    print("Pilih item yang ingin dibeli:")
    print("Kategori Martabak")
    print("1. Martabak Coklat - 20000")
    print("2. Martabak Keju - 25000")
    print("3. Martabak Kismis - 15000")
    print("------------------------")
    print("Kategori Pukis")
    print("4. Pukis Coklat - 15000")
    print("5. Pukis Keju - 20000")
    print("6. Pukis Kismis - 15000")
    
    pilihan = input('Masukkan pilihan item (1/2/3/4/5/6): ') 
    jumlah = int(input('Masukkan jumlah beli: ')) 
    if pilihan == '1':
        harga = martabakCoklat
        jumlahMartabakCoklat += jumlah
    elif pilihan == '2':
        harga = martabakKeju
        jumlahMartabakKeju += jumlah
    elif pilihan == '3':
        harga = martabakKismis
        jumlahMartabakKismis += jumlah
    elif pilihan == '4':
        harga = pukisCoklat
        jumlahPukisCoklat += jumlah
    elif pilihan == '5':
        harga = pukisKeju
        jumlahPukisKeju += jumlah
    elif pilihan == '6':
        harga = pukisKismis
        jumlahPukisKismis += jumlah
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, 5 atau 6.")
        continue # Kembali ke awal loop jika pilihan tidak valid
    
    # Hitung total untuk item yang dibeli
    total = harga * jumlah
    totalAkhir += total
    print(f'Total Sementara: Rp {totalAkhir}')
    
    lagi = input('Apa mau beli lagi? [Y/N]: ')
    if lagi == 'N' or lagi == 'n':
        break # Keluar dari loop jika pengguna memasukkan 'N' atau 'n'
    
# Menampilkan jumlah pembelian setiap item 
print(f'\nJumlah pembelian:')
if jumlahMartabakCoklat >= 1: 
    print(f"Jumlah Martabak Coklat: {jumlahMartabakCoklat}")

if jumlahMartabakKeju >= 1:
    print(f"Jumlah Martabak Keju: {jumlahMartabakKeju}")

if jumlahMartabakKismis >= 1:
    print(f"Jumlah Martabak Kismis: {jumlahMartabakKismis}")

if jumlahPukisCoklat >= 1:
    print(f"Jumlah Pukis Coklat: {jumlahPukisCoklat}")

if jumlahPukisKeju >= 1:
    print(f"Jumlah Pukis Keju: {jumlahPukisKeju}")

if jumlahPukisKismis >= 1:
    print(f"Jumlah Pukis Kismis: {jumlahPukisKismis}")

print(f'Terima kasih! Total belanja Anda adalah Rp {totalAkhir}.')