def hitung_luas_segitiga():
    # Mengambil input dari pengguna 
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    # Menghitung luas segitiga
    luas = 0.5 * alas * tinggi
    # Menampilkan hasil
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah: {luas}")
    # Algoritma pemanggil procedure
    
hitung_luas_segitiga()