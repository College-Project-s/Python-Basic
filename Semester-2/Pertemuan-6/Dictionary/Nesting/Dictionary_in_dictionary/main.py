user = {
    'Mahasiswa-1' : {
        'nama' : 'dadang',
        'email' : ' dadang@gmail.com ',
        'prodi' : 'sistem informasi',
    },
    'Mahasiswa-2': {
        'nama' : 'diding',
        'email' : ' diding@gmail.com ',
        'prodi' : 'keperawatan',
    },
    'Mahasiswa-3' : {
        'nama' : 'dudung',
        'email' : ' dudung@gmail.com ',
        'prodi' : 'perawatan mesin',
    },
}

for username, user_info in user.items():
    print ('\nUSER NAME : \n\t',username)
    print ('\t Nama \t: ',user_info['nama'])
    print ('\t Email \t: ',user_info['email'])
    print ('\t Prodi \t: ',user_info['prodi'])