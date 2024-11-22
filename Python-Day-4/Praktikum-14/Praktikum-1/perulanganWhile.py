akhir = int(input("Masukkan Angka Akhir : "))
jumlah = 0
x = 1 

while x <= akhir:
    if x % 2 == 1:
        jumlah += x
    x += 1
print(f"Jumlah deret bilangan ganjil adalah {jumlah}")
