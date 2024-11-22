harga_barang_a = 1000
harga_barang_b = 2000
harga_barang_c = 3000
totalAkhir = 0
from functionFormatRupiah import format_rupiah

while True:
    print("Pilih item yang ingin dibeli:")
    print("1. Barang A - Rp 1000")
    print("2. Barang B -Rp 2000")
    print("3. Barang C - Rp 3000")
    pilihan = input('Masukkan pilihan item (1/2/3): ')
    if pilihan == '1':
        harga = harga_barang_a
    elif pilihan == '2':
        harga = harga_barang_b
    elif pilihan == '3':
        harga = harga_barang_c
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.") 
        continue # Kembali ke awal loop jika pilihan tidak valid
    
    beli = int(input('Masukkan jumlah beli: '))
    total = harga * beli
    totalAkhir += total
    hasil_format = format_rupiah(totalAkhir)
    print(f'Total Sementara: Rp {hasil_format}')
    lagi = input("Apa mau beli lagi? [Y/N]: ")
    if lagi == 'N' or lagi == 'n':
        break # Keluar dari loop jika pengguna memasukkan 'N' atau 'n'
    
print(f'Terima kasih! Total belanja Anda adalah Rp {hasil_format}')