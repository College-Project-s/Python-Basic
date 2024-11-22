def memisahkan_string():
    kode = input("Masukkan 6 karakter (Contoh : 01A504):")
    # Validasi panjang input
    if len(kode) != 6:
        print("Input harus terdiri dari 6 karakter.") 
        exit()
    
    # Memisahkan bagian-bagian dari input
    jenis_buku = kode[0:2] # 2 karakter pertama 
    nomor_rak = kode[2:4] # 2 karakter berikutnya 
    jumlah_buku = int(kode[4:6]) # 2 karakter terakhir 
    return jenis_buku, nomor_rak, jumlah_buku

def jenis_buku(jenis_buku):
# Menentukan jenis buku berdasarkan input 
    if jenis_buku == "01":
        jenis_buku_nama = "Buku Sains"
    elif jenis_buku == "02":
        jenis_buku_nama = "Buku Cerita"
    elif jenis_buku == "03":
        jenis_buku_nama = "Buku Komputer" 
    else:
        jenis_buku_nama = "Jenis buku tidak dikenal"
    return jenis_buku_nama

# Memanggil fungsi untuk memisahkan string
jenis_buku_kode, nomor_rak, jumlah_buku = memisahkan_string()
# Mendapatkan nama jenis buku
jenis_buku_nama = jenis_buku(jenis_buku_kode)
# Menampilkan hasil
print(f"Jenis Buku: {jenis_buku_nama}")
print(f"Nomor Rak: {nomor_rak}")
print(f"Jumlah Buku: {jumlah_buku}")