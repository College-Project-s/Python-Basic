data_set = {'A','B','c','D','E','F','G'} 
print(data_set)
#Menghapus nilai, jika nilai tidak ada akan error 
data_set.remove('A')
print(data_set)
#Menghapus nilai, jika nilai tidak ada tidak akan error 
data_set.discard('B')
print(data_set)
#Menghapus nilai dari kiri
data_set.pop()
print(data_set)
#Menghapus semua anggota
data_set.clear()
print(data_set)