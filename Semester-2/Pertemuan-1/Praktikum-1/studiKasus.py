def hitung_biaya(jam):
    harga_per_jam = 5000
    return jam * harga_per_jam

def input_jam_bermain():
    while True:
        jam = int(input("Masukkan jumlah jam bermain: "))
        if jam <= 0:
            print("Waktu bermain harus lebih dari 0.")
            continue  # Continue jika input tidak valid
        return jam

def bayar_tagihan(total):
    while True:
        bayar = int(input(f"Total tagihan: {total}. Masukkan jumlah pembayaran: "))
        if bayar < total:
            print("Uang tidak cukup, silakan masukkan jumlah yang sesuai.")
            continue  # Continue jika pembayaran kurang
        print(f"Pembayaran sukses! Kembalian Anda: {bayar - total}")
        break  # Break setelah pembayaran sukses

def transaksi_warnet():
    jam = input_jam_bermain()
    if not jam:
        return  # Break transaksi jika input tidak valid
    
    total = hitung_biaya(jam)
    bayar_tagihan(total)
    print("Terima kasih telah bermain di warnet kami!")

# Jalankan program
transaksi_warnet()
