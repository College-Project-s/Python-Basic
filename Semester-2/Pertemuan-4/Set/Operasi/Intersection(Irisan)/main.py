set_kelas_A = {'Ray','Sheva', 'Yusviana', 'Tsabit', 'Mika'} 
set_pengurus = {'Tsabit', 'Yusviana','Budi', 'Rikke','Dodi'}

#Cara 1
print(set_kelas_A & set_pengurus)
#Cara 2
print(set_kelas_A.intersection(set_pengurus))

set_kelasA_pengurus = set_kelas_A & set_pengurus 
print(set_kelasA_pengurus)