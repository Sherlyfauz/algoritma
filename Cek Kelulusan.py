SHERLY FAUZIYAH SYAHARANI/20083000150/2F
#cek kelulusan, jika nilai > 60 maka status lulus
print ("==========================")
print (" CEK KELULUSAN ")
print ("==========================")
#setiap value yang diinputkan, secara default bertipe data STRING
n = input(">> Masukkan Nilai = ")
#cek nilai
if n>60:
    sts = "LULUS"
else:
    sts="ULANG"

print(sts)
