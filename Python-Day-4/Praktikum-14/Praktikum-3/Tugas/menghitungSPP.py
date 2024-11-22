# Program Menghitung SPP Berdasarkan Tahun Angkatan
def hitungSpp(tahun_angkatan, SKS):
    if tahun_angkatan == 2021:
        biayaAngkatan = 100000
    elif tahun_angkatan == 2020:
        biayaAngkatan = 80000
    elif tahun_angkatan == 2019:
        biayaAngkatan = 60000
    else:
        return None  # Jika tahun angkatan tidak valid
    
    SPP = biayaAngkatan * SKS
    return SPP

# Input data dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
tahun_angkatan = int(input("Masukkan Tahun Angkatan (2019/2020/2021): "))
SKS = int(input("Masukkan Jumlah SKS: "))

# Hitung biaya SPP
SPP = hitungSpp(tahun_angkatan, SKS)

# Output hasil
if SPP:
    print("\n--- Informasi Pembayaran SPP ---")
    print(f"Nama          : {nama}")
    print(f"NIM           : {nim}")
    print(f"Tahun Angkatan: {tahun_angkatan}")
    print(f"Biaya SPP     : Rp {SPP}")
else:
    print("Tahun angkatan tidak valid. Silakan masukkan tahun yang benar (2019/2020/2021).")
