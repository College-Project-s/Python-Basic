data_set = {'Bogor','Bandung','Jakarta'} 
print(len(data_set))

data_set2 = {1,2,3,4,5}
print(max(data_set2))
print(min(data_set2))
print(sum(data_set2))

#Menambah 1 elemen 
data_set.add('Subang') 
print(data_set)
data_set.add((10,20,30)) #bisa ditambah dengan tupple 
print(data_set)

#Menambah banyak elemen
set_hewan = {'Ayam','Sapi','Kambing'}
set_hewan.update({100,200,300}) #bisa ditambah dengan himpunan 
print(set_hewan)
set_hewan.update([1000,2000,3000]) #bisa ditambah dengan list 
print(set_hewan)