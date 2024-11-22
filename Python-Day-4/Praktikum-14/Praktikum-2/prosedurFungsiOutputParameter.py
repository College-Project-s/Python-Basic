# Parameter output
def Persegi():
    sisi = int(input('Masukan sisi : '))
    luas = sisi*sisi
    keliling = 4*sisi
    return luas, keliling

luas, keliling = Persegi()
print('Luas : ',luas,"\n"'Keliling : ',keliling)