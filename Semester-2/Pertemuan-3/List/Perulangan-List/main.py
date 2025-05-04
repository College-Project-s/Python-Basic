list_kosong = []

jumlah_elemen = int(input('Masukkan Jumlah Element : '))

for item in range(jumlah_elemen):
    elemen = input(f'Masukkan elemen ke-{item+1} :')
    list_kosong.append(elemen)

print('list yang telah di isi : ',list_kosong)