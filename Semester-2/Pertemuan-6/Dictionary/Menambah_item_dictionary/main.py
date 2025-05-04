pertemuan_hari_ini = {
    'judul': 'Belajar Directory Pada Python 3',
    'tanggal': '13 Maret 2023',
    'kategori': ['Python', 'Python Dasar'],
    'page_view': 10,
    'published': True,
    'share_count': {
        'facebook': 0,
        'twitter': 2,
        },
}

# Menambahkan Value
pertemuan_hari_ini['author'] = 'John Doe'

for key in pertemuan_hari_ini:
    print(key, '->', pertemuan_hari_ini[key])