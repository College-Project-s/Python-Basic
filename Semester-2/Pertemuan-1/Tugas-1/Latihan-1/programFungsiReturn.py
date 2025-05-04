def angka_positif(angka):
    if angka > 0 :
        return True
    print ("Angka bukan positif, ulangi pemanggilan fungsi")
angka = int(input("Masukkan Nilai yang ingin di cek : "))
angka_positif(angka)