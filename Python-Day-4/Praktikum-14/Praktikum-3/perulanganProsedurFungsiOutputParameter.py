def hitung_luas_dan_keliling_persegi_panjang(panjang, lebar):
    # Menghitung luas dan keliling 
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Algoritma pemanggil procedure 
n = int(input("Masukkan jumlah persegi panjang yang ingin dihitung: "))

for i in range(n):
    print(f"\nPersegi Panjang ke-{i + 1}:")
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    
    # Memanggil fungsi untuk menghitung luas dan keliling
    luas, keliling = hitung_luas_dan_keliling_persegi_panjang(panjang, lebar)
    
    # Menampilkan hasil
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")