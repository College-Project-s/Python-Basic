def hitungTotalGaji(gajiPokok, jumlahAnak): 
    # Menentukan tunjangan per anak (5% dari gaji pokok) 
    tunjanganPerAnak = 0.05 * gajiPokok
    
    # Membatasi jumlah anak maksimal 2
    if jumlahAnak > 2:
        jumlahAnak = 2
    
    # Menghitung total tunjangan
    totalTunjangan = tunjanganPerAnak * jumlahAnak
    
    # Menghitung total gaji
    totalGaji = gajiPokok + totalTunjangan
    
    return totalGaji

# Meminta input dari pengguna
print("----Golongan Pegawai----")
print("1. Golongan 1")
print("2. Golongan 2")
print("3. Golongan 3")

# Kondisi Cek Golongan Pegawai
golonganKaryawan = int(input("Masukkan Golongan Pegawai: "))
jumlahAnak = int(input("Masukkan jumlah anak: "))
if golonganKaryawan == 1 :
    gajiPokok = 1000000
elif golonganKaryawan == 2 :
    gajiPokok = 1500000
elif golonganKaryawan == 3 :
    gajiPokok = 2000000
else :
    print("Golongan Tidak Valid !")
    gajiPokok = 0 



# Memanggil fungsi untuk menghitung total gaji 
totalGaji = hitungTotalGaji(gajiPokok, jumlahAnak)

# Menampilkan total gaji
print(f"Total Gaji (Gaji Pokok + Tunjangan): Rp. {totalGaji}")