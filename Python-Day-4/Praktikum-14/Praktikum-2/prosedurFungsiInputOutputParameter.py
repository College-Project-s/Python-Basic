def Persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    return luas, keliling

sisi = int(input('Masukan sisi : '))
luas, keliling = Persegi(sisi)
print('Sisi : ',sisi,'\nLuas : ',luas,'\nKeliling : ',keliling)