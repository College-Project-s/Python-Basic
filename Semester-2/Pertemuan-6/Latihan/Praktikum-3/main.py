import datetime
import string
import random

input_mahasiswa = {
    'nama' : 'nama',
    'nim' : '00000000',
    'nTugas' : 0,
    'nUTS' : 0,
    'nUAS' : 0,
    'nilai' : 0,
    'predikat' : 'A',
}
data_mahasiswa = {}

print(f"{'SELAMAT DATANG' : ^40}")
print('='*40)

while True:
    print(f"{'DATA MAHASISWA' : ^10}")
    
    # Membuat dictionary baru dengan key dari dictionary input_mahasiswa
    mahasiswa = dict.fromkeys(input_mahasiswa.keys())
    
    # Input data mahasiswa
    mahasiswa['nama'] = input('\tNama Mahasiswa : ')
    mahasiswa['nim'] = int(input('\tNIM Mahasiswa : '))
    mahasiswa['nTugas'] = int(input('\tNilai Tugas Mahasiswa : '))
    mahasiswa['nUTS'] = int(input('\tNilai UTS Mahasiswa : '))
    mahasiswa['nUAS'] = int(input('\tNilai UAS Mahasiswa : '))

    # Hitung Nilai Akhir Mahasiswa
    mahasiswa['nilai'] = int(mahasiswa['nTugas']*(40/100)) + (mahasiswa['nUTS']*(30/100)) + (mahasiswa['nUAS']*(30/100))

    # Hitung Predikat
    if mahasiswa['nilai'] >= 85:
        mahasiswa['predikat'] = "A"
    elif mahasiswa['nilai'] >= 78:
        mahasiswa['predikat'] = "AB"
    elif mahasiswa['nilai'] >= 70:
        mahasiswa['predikat'] = "B"
    elif mahasiswa['nilai'] >= 63:
        mahasiswa['predikat'] = "BC"
    elif mahasiswa['nilai'] >= 55:
        mahasiswa['predikat'] = "C"
    elif mahasiswa['nilai'] >= 40:
        mahasiswa['predikat'] = "D"
    else:
        mahasiswa['predikat'] = "E"
    
    # Membuat random key
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    
    # Menambahkan data ke dictionary
    data_mahasiswa.update({KEY: mahasiswa})
    
    # Menampilkan hasil
    print(f"\n{'KEY':<10} {'NAMA':<15} {'NIM':<10} {'NILAI':<10} {'PREDIKAT':<10}")
    print('-'*50)
    
    for key, value in data_mahasiswa.items():
        print(f"{key:<10} {value['nama']:<15} {value['nim']:<10} {value['nilai']:<10} {value['predikat']:<10}")
    print("\n")
    
    tambah = input("Mau tambah lagi bro (y/n)? ")
    if tambah.lower() == "n":  # Jika tidak menambah data maka berhenti
        break

print("\nAkhir dari program, terima kasih")