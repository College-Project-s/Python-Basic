harga = 1000
totalAkhir = 0

while True:
    beli = int(input('Masukan jumlah beli : '))
    total = harga*beli
    totalAkhir += total
    print(f'Total Akhir : {totalAkhir}') 
    lagi = input('Apa mau beli lagi ?[Y/N] ') 
    if lagi == 'N' or lagi == 'n':
        break