#  Start
print (" ")
uangPinjam = int (input("Masukkan Uang Pinjaman : "))
print("--------------------------------")

# Step 1 
uangBunga = int (uangPinjam * 10/100)
print("Besar Uang Bunga : ", uangBunga)
print("--------------------------------")

# Step 2
uangTotal = int (uangPinjam + uangBunga)
print("Besar Uang Total : ", uangTotal)
print("--------------------------------")

# Finish
uangPerBulan = int (uangTotal / 12)
print("Besar Cicilan Per Bulan : ", uangPerBulan)
print("--------------------------------")
