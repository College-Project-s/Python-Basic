akhir = int(input("Masukkan Angka Akhir : "))
jumlah = 0
x = 1 

for x in range(1, akhir + 1):
    print(x)
    if x % 2 == 1:
        jumlah += x

print(f"Jumlah deret bilangan ganjil adalah {jumlah}")
