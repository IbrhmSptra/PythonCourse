#continue -> sebuah operasi untuk skip codingan yang ada dibawahnya lalu kembali lagi ke atas
angka = 0

while angka <5 :
    print("angka sekarang " ,angka)
    print("hallo")
    angka += 1 #flow control
    
    if angka == 3 :
        print("lompatt!!!")
        continue
    
    print("next")
    print("hallooo")
    

#break ->melpaskan perulangan secara paksa
angka1 = 0
while angka1 <5 :
    print("halo bang")
    if angka1 ==3 :
        print("cukup")
        break #->Keluar dari perulangan
    angka1 += 1

angka2=0
while True : #->Tanpa kondisi jalnkan perulangan mau tidak mau
    print("loop pakai true")
    angka2 += 1
    if angka2 == 5 :
        break #->keluar dari perulang secara paksa



print("akhir dari program")