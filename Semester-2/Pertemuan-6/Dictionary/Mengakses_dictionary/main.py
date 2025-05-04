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

# Jika single / hanya data level 1 nya saja
print('Judul :', pertemuan_hari_ini.get('judul'))
print('tanggal :', pertemuan_hari_ini['tanggal']) # ✅ Use Ini better

# Jika double / mengambil data sampai level 2 (Berutun)
print('Facebook Share :', pertemuan_hari_ini.get('share_count').get('facebook'))
print('Twitter Share :', pertemuan_hari_ini['share_count']['twitter']) # ✅ Use Ini better