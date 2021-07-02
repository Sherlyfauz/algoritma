"""
SHERLY FAUZIYAH SYAHARANI/20083000150/2F
02-07-2021
Program Hitung Transaksi Pembelian Multi Item
"""
ulang="y"
while ulang=="y" or ulang =="Y":
#Program Transaksi
    print ("")
    print ("============================")
    print ("Daftar Menu Makanan")
    print ("=================================")
    print ("a = Nasi Goreng        Rp.15.000")
    print ("b = Lontong Goreng     Rp.14.900")
    print ("c = Bakso Goreng       Rp.12.900")
    print ("d = Rujak Goreng       Rp.13.000")
    print ("e = Rujak Bakso        Rp.15.000")
    print ("f = Rujak Bakso Pecel  Rp.17.000")
    print ("=================================")
    print ("Daftar Menu Minuman")
    print ("====================================")
    print ("g = Teh Dingin/Hangat/Panas Rp.2.500")
    print ("h = Kopi Dingin             Rp.5.000")
    print ("i = Kopi Teh Panas          Rp.6.500")
    print ("j = Coca Cola Dingin        Rp.3.500")
    print ("k = Coca Cola Panas         Rp.5.000")
    print ("====================================")
    print ("")

    #SIAPKAN VARIABEL
    kode=['a','b','c','d','e','f']
    namaMakanan=['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    Harga1=[15000,14900,12900,13000,15000,17000]
    kode2=['g','h','i','j','k']
    namaMinuman=['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    Harga2=[2500,5000,6500,3500,5000]

    #INPUT PILIHAN
    pilihanMkn = input(">>Masukkan Kode Makanan  = ")
    pilihanMnm = input(">>Masukkan Kode Minuman  = ")

    #INPUT QTY
    qtyMkn = input(">>Masukkan Jumlah Makanan yang Dipesan = ")
    qtyMnm = input(">>Masukkan Jumlah Minuman yang Dipesan = ")

    #HITUNG BAYAR MAKANAN
    i = 0
    while i<len(namaMakanan):
        if kode[i] == pilihanMkn:

            #Ambil Nama Pesanan
            nm_Mkn = namaMakanan[i]

            #Ambil Harga Satuan
            hrgsat1 = Harga1[i]

        #Jika tidak cocok, lanjut ke i berikutnya
        i+=1

    tot_HrgMkn = hrgsat1 * int(qtyMkn)

    #HITUNG BAYAR MINUMAN
    i = 0
    while i<len(namaMinuman):
        if kode2[i] == pilihanMnm:

            #Ambil Nama Pesanan
            nm_Mnm = namaMinuman[i]

            #Ambil Harga Satuan
            hrgsat2 = Harga2[i]
            
        #Jika tidak cocok, lanjut ke i berikutnya
        i+=1

    tot_HrgMnm = hrgsat2 * int(qtyMnm)

    #Total Bayar Pesanan dengan kembalian
    tot_Bayar = tot_HrgMkn+tot_HrgMnm

#Tampilkan Hasil
    print(">>> NAMA MAKANAN YANG DIPESAN   :"+ nm_Mkn)
    print(">>> HARGA MAKANAN         :"+ str(hrgsat1))
    print(">>> JUMLAH MAKANAN YANG DIPESAN :"+ qtyMkn)
    print(">>> NAMA MINUMAN YANG DIPESAN   :"+ nm_Mnm)
    print(">>> HARGA MINUMAN         :"+ str(hrgsat2))
    print(">>> JUMLAH MINUMAN YANG DIPESAN :"+ qtyMnm)
    print(("----------------------------------------"))
    print(">>> TOTAL BAYAR    :"+ str(tot_Bayar))

    #Total Uang Kembalian
    Bayar = int(input("Jumlah Nominal Uang = Rp."))
    Kembalian = (Bayar-tot_Bayar)
    print(">>> UANG KEMBALIAN : Rp." , Kembalian)

    ulang = input(" Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break