def hitung_luas_segitiga(alas, tinggi):
    # Menghitung luas segitiga
    luas = 0.5 * alas * tinggi
    # Menampilkan hasil
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah: {luas}")
    
# Algoritma pemanggil procedure
# Mengambil input dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Memanggil fungsi untuk menghitung luas segitiga
hitung_luas_segitiga(alas, tinggi)