defaultList = [34, 12, 56, 78, 23, 45, 67, 89, 90, 11, 22, 44, 55, 66, 77]

inputList = []
for _ in range(10):
    angka = int(input("Masukkan angka : "))
    inputList.append(angka)

GabunganList = defaultList+inputList

print("List angka:", GabunganList)

GabunganList.sort()
angka_terkecil = GabunganList[:5]
print("Menampilkan 5 Angka Terkecil : ", angka_terkecil)

GabunganList.sort(reverse=True) 
angka_terbesar = GabunganList[:5] 
print("Menampilkan 5 Angka Terbesar : ", angka_terbesar)

jumlah21 = GabunganList.count(21)
print("Angka 21 muncul sebanyak:", jumlah21, "kali")

gabunganBesarKecil = angka_terkecil + angka_terbesar
print("Gabungan 5 angka terkecil dan 5 angka terbesar:", gabunganBesarKecil)