# Membuat list 3 dimensi yang berisi nama mahasiswa
kelasTRPL1B = [
    [ 
        ["Agung", "Andi", "Aulia"], 
        ["Calvin", "Dhela", "Epi"], 
        ["Naura", "Prabu", "Zahra", "Zahwa"],
    ],
    [ 
        ["Farhan", "Gefira", "Iknas"], 
        ["Jaenal", "Juanico", "Kheiza"],   
        ["Raihan", "Salsa", "Sulton"],
    ],
    [ 
        ["Mahardika", "Zidan", "Syaeful"],  
        ["Diaz", "Ihsan", "Rifky"], 
        ["Tomie", "Tsenia", "Wibi", "Zacki"]
    ]
]
for layer in kelasTRPL1B :
    for baris in layer :
        print(baris)
    print()

nama1 = kelasTRPL1B[2][1][2]
print(f'Contoh Mengakses Ke-1 : ', nama1)
nama2 = kelasTRPL1B[0][1][0]
print(f'Contoh Mengakses Ke-2 : ', nama2)
nama3 = kelasTRPL1B[2][2][1]
print(f'Contoh Mengakses Ke-3 : ', nama3)
