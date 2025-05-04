# Definisi himpunan berdasarkan gaya belajar
V = {"Aulia", "Dhela", "Epi", "Farhan", "Hari", "Jaenal", "Kheiza", "Mahardika", "Moch Zidan", "Muhamad Syaeful"}
A = {"Andi", "Calvin", "Dhela", "Gefira", "Hari", "Juanico", "Kheiza", "Moch Zidan", "Muhammad Dhiyaul", "Muhammad Ihsan"}
K = {"Agung", "Andi", "Calvin", "Epi", "Farhan", "Gefira", "Iknas", "Jaenal", "Kheiza", "Moch Zidan", "Muhamad Syaeful", "Muhammad Ihsan"}

# Operasi Gabungan (Union)
print("Gabungan V dan A:", V | A)
print("Gabungan A dan K:", A | K)
print("Gabungan V dan K:", V | K)

# Operasi Irisan (Intersection)
print("Irisan V dan A:", V & A)
print("Irisan A dan K:", A & K)
print("Irisan V dan K:", V & K)

# Operasi Selisih (Difference)
print("Selisih V - A:", V - A)
print("Selisih A - K:", A - K)
print("Selisih K - V:", K - V)

# Operasi Komplemen (Menggunakan perbedaan dengan semua siswa)
all_students = V | A | K
print("Komplemen V (Bukan Visual):", all_students - V)
print("Komplemen A (Bukan Auditori):", all_students - A)
print("Komplemen K (Bukan Kinestetik):", all_students - K)
