#percabangan -> ngasilin Output yang bervariasi

""" 
Ini merupakan percabangan di bahasa lain

if (input == +) {
        angka1 + Angka2
}

"""

""" 
ini percabangan di python

if kondisi :
    aksi1
    aksi2
elif kondisi :
    aksi 1
else :    -> Aksi yang dijalankan ketika semua kondisi tidak terpenuhi
    aksi
akhir dari if
    
"""

suhu = float(input("Masukan Suhu Ruangan anda :"))
if suhu>30 and suhu<40 : #31 - 39
    print("Panas banget cuyyy!!")
elif suhu<20 and suhu>10: #11 - 19
    print("Dingin banget cuyy")
elif suhu>20 and suhu<30 : #21 - 29
    print("Suhu Normal")
else :
    print("Suhu tersebut tidak terbayangkan oleh umat manusia")

print("akhir dari program")


nama = input("masukan nama")
if nama == "baim" :
    print("oh gua kenal dia")
else :
    print("Sorry ga kenal")