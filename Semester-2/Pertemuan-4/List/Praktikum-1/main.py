listData = []
def menu():
    print ('======Menu===== \nA. Tampilkan data \nB. Tambah Data \nC. Edit Data \nD. Hapus Data \nE. Exit')
def tambah():
    data = input("Masukan data : ")
    listData.append(data)
    print ('data berhasil ditambahkan')

def tampil():
    print ('Data saat ini')
    for i, data in enumerate(listData):
        print(i, "-", data)
def edit():
    index=int(input("Masukan indeks data yang akan dirubah : "))
    if index < len (listData):
        dataBaru= input('Masukan data baru : ')
        listData[index]= dataBaru
        print('Data berhasil di rubah')
    else:
        print('Data gagal dirubah')
def hapus():
    index=int(input("Masukan indeks data yang akan dihapus : "))
    if index <= len(listData):
        dataHapus=listData.pop(index)
        print('Data',dataHapus,' telah dihapus')
    else:
        print('Index Tidak Valid')

#Program Utama
while True :
    menu()
    pilih = input("Pilih menu : ")
    if pilih == 'A' :
        tampil()
    elif pilih == 'B' :
        tambah()
    elif pilih == 'C' :
        edit()
    elif pilih == 'D' :
        hapus()
    elif pilih == 'E' :
        print ('Terima Kasih')
        break
    else:
        print("Kode menu salah")