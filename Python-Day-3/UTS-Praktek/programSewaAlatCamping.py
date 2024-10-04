def format_rupiah(nilai):
    return "Rp. {:,}".format(int(nilai)).replace(",", ".")

ulangProgram = True  # Tambahkan variabel untuk kontrol loop utama
while ulangProgram:
    hargaTenda = 250000
    hargaSleepingBag = 90000
    hargaKomporPortable = 75000

    print("----------------------------------------------------------------")
    print("Toko Sewa Alat Camping\n")
    print("List Alat Camping : \n1. Tenda\t\t", format_rupiah(hargaTenda), "\n2. SleepingBag\t\t", format_rupiah(hargaSleepingBag), "\n3. KomporPortable\t", format_rupiah(hargaKomporPortable))
    print("----------------------------------------------------------------\n")

    lamaSewaTenda = int(input("Masukkan Lama Sewa Tenda (Hari) \t\t :"))
    lamaSewaSleepingBag = int(input("Masukkan Lama Sewa SleepingBag (Hari) \t\t :"))
    lamaSewaKomporPortable = int(input("Masukkan Lama Sewa KomporPortable (Hari) \t :"))
    print("----------------------------------------------------------------\n")

    biayaSewaTenda = hargaTenda * lamaSewaTenda
    biayaSewaSleepingBag = hargaSleepingBag * lamaSewaSleepingBag
    biayaSewaKomporPortable = hargaKomporPortable * lamaSewaKomporPortable

    totalBiaya = biayaSewaTenda + biayaSewaSleepingBag + biayaSewaKomporPortable
    totalLamaSewa = lamaSewaTenda + lamaSewaSleepingBag + lamaSewaKomporPortable
    
    while True:
        statusPenyewa = int(input("1. Member\n2. NonMember\nMasukkan status keanggotaan penyewa alat camping (No) \t : "))
        if statusPenyewa in [1, 2]:
            print("----------------------------------------------------------------\n")
            if statusPenyewa == 1:
                if totalLamaSewa >= 2 and totalLamaSewa < 5:
                    diskon = "10%"
                    biayaDiskon = totalBiaya * 10 / 100
                    hargaAkhir = totalBiaya - biayaDiskon
                elif totalLamaSewa >= 5:
                    diskon = "20%"
                    biayaDiskon = totalBiaya * 20 / 100
                    hargaAkhir = totalBiaya - biayaDiskon
                else:
                    diskon = "Tidak Mendapatkan Diskon"
                    biayaDiskon = 0
                    hargaAkhir = totalBiaya - biayaDiskon
            elif statusPenyewa == 2:
                if totalLamaSewa >= 5:
                    diskon = "5%"
                    biayaDiskon = totalBiaya * 5 / 100
                    hargaAkhir = totalBiaya - biayaDiskon
                else:
                    diskon = "Tidak Mendapatkan Diskon"
                    biayaDiskon = 0
                    hargaAkhir = totalBiaya - biayaDiskon

            if biayaDiskon == 0:
                print("Status Diskon\t : ", diskon)
                print("Harga Akhir \t ", format_rupiah(hargaAkhir))
            else:
                print("Status Diskon\t\t\t ", diskon)
                print("Nominal Diskon \t\t\t ", format_rupiah(biayaDiskon))
                print("Harga Awal Sebelum Diskon \t ", format_rupiah(totalBiaya))
                print("Harga Akhir Setelah Diskon \t ", format_rupiah(hargaAkhir))
            print("----------------------------------------------------------------\n")
            
            while True:
                repeat = str(input("Ulangi Program Sewa Alat Camping (y/n) \t :")).lower()
                if repeat == "y" or repeat == "ya":
                    break  # Keluar dari loop dalam dan mengulang program
                elif repeat == "n" or repeat == "no":
                    ulangProgram = False  # Set variabel ulangProgram menjadi False untuk menghentikan program
                    break
                else:
                    print("Yang Anda masukkan salah. Masukkan pilihan yang valid (y/n).")
                    print("----------------------------------------------------------------\n")
            break  # Keluar dari loop statusPenyewa
        else:
            print("Input salah. Silakan masukkan angka 1 (Member) atau 2 (NonMember).")
            print("----------------------------------------------------------------\n")
