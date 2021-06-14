"""
SHERLY FAUZIYAH SYAHARANI/20083000150/2F
11-06-2021
PROGRAM PERHITUNGAN NILAI TOTAL TRANSAKSI PEMBELIAN PRINTER
"""
ulang="y"
while ulang=="y" or ulang =="Y":
#Siapkan variabel
    print("===========================")
    print(" APLIKASI 6a")
    print("Pembelian printer")
    print ("Pembelian Diatas 1,5 Juta Mendapat Diskon 15% ")
    print("===========================")
    u=1
    #Hitung
    u =input(" Masukkan Banyak Printer = ")
    n=int(u)
    harga = n * 660000
    print(" Total Harga Pembelian Printer= Rp.",harga)
    if (harga)>1500000 :
        print("---------- Mendapat diskon 15% --------------")
        diskon = harga * 0.15
    else :
        diskon = 0
    
    totharga = harga - diskon
    print(" Diskon = Rp.",diskon)    
    print(" Total Harga = Rp.",totharga)

    ulang = input(" Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break