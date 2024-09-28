print("---------------------------------------------------------")
kodeBuku = str(input("Masukkan Kode Buku Yang Ingin Dicari \t :"))
judulBuku = str
hargaBuku = int

if kodeBuku == "BK01" or kodeBuku == "bk01" :
    judulBuku = "Pemrograman Dasar"
    hargaBuku = 100000
    
elif kodeBuku == "BK02" or kodeBuku == "bk02" :
    judulBuku = "Algoritma dan Struktur Data"
    hargaBuku = 120000
    
elif kodeBuku == "BK03" or kodeBuku == "bk03" :
    judulBuku = "Jaringan Komputer"
    hargaBuku = 120000
    
elif kodeBuku == "BK04" or kodeBuku == "bk04" :
    judulBuku = "Basis Data"
    hargaBuku = 130000
    
else:
    judulBuku = "Maaf Data Tidak Ditemukan"
    hargaBuku = 0

print("---------------------------------------------------------")
if hargaBuku == 0:
    print("Data Buku Tidak Ditemukan")
else:
    print("Data Ditemukan")
    print("Judul Buku \t :", judulBuku)
    print("Harga Buku \t :", hargaBuku)
print("---------------------------------------------------------")