from functionSimpanKeExcel import pilih_item, simpan_ke_excel
def main():
    total_akhir = 0
    
    while True:
        # Pilih barang
        nama_barang, harga = pilih_item() 
        if nama_barang is None: # Jika pilihan tidak valid, kembali ke awal loop
            continue
        
        # Input jumlah beli
        try:
            jumlah_beli = int(input("Masukkan jumlah beli: ")) 
        except ValueError:
            print("Input jumlah beli harus berupa angka.")
            continue
        
        total_harga = harga * jumlah_beli
        total_akhir += total_harga
        print(f"Total Harga untuk {jumlah_beli} {nama_barang}: Rp {total_harga}")
        print(f"Total Akhir: Rp {total_akhir}")
        
        # Simpan data pembelian ke Excel
        simpan_ke_excel(nama_barang, jumlah_beli, total_harga)
        # Tanya apakah ingin membeli lagi 
        lagi = input("Apa mau beli lagi? [Y/N]: ").strip().lower()
        if lagi == 'n':
            break
    
    print(f"Terima kasih! Total belanja Anda adalah Rp {total_akhir}.")
    
# Menjalankan program utama
main()