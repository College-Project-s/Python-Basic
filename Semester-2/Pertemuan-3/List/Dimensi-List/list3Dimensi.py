#Membuat list 3 dimensi 3x3x2 dengan angka
list_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [10, 11],
        [13,14]
    ], 
    [
        [19, 20],
        [22, 23]
    ]
]

#Menampilkan list 3 Di mensi
for layer in list_3d :
    for baris in layer :
        print(baris)
    print()
print (list_3d[2][0][1])