set_kelas_A = {'Ray','Sheva', 'Yusviana', 'Tsabit', 'Mika'} 
set_pengurus = {'Tsabit', 'Yusviana','Budi', 'Rikke','Doi'}

#Cara 1
#Anggota kelas A yang bukan Pengurus 
print(set_kelas_A - set_pengurus) 
print(set_kelas_A.difference(set_pengurus))
#Cara 2
#Anggota pengurus himpunan yang bukan Kelas A 
print(set_pengurus - set_kelas_A) 
print(set_pengurus.difference(set_kelas_A))

set_kelasA_nonPengurus = (set_kelas_A - set_pengurus) 
print(set_kelasA_nonPengurus)