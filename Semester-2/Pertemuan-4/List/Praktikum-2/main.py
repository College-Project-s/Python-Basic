# Fungsi untuk menampilkan semua data mahasiswa
def tampil():
    print("Daftar Mahasiswa:")
    print("NIM\tNama\tAlamat")
    for student in data_mahasiswa:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")

def tambah():
    # Fungsi untuk menambahkan data mahasiswa baru
    nim = input("Masukkan NIM mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa:")
    data_mahasiswa.append([nim, nama, alamat])
    print("Data mahasiswa berhasil ditambahkan.")

# Inisialisasi list 2 dimensi untuk menyimpan data mahasiswa 
data_mahasiswa = []

# Menampilkan menu
while True:
    print("\nPilih operasi:")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Keluar")
    print("Data Mahasiswa berhasil ditambahkan")
    
    pilih = input("Masukkan Pilihan : ")
    
    if pilih == "1":
        tampil()
    elif pilih == "2":
        tambah()
    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")