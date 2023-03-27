#not, and , or , xor

#NOT // output kebalikan dari value aslinya
print("=======NOT======")
a = True
hasil = not a
print("value a :", a)
print("-----------NOT")
print("value a setelah di not :", hasil)

print()

#AND // keduanya harus true jika ingin true
print('====AND====')
a = False
b = False
hasil = a and b
print(a,'AND',b,'=',hasil)
a = False
b = True
hasil = a and b
print(a,'AND',b,' =',hasil)
a = True
b = False
hasil = a and b
print(a,' AND',b,'=',hasil)
a = True
b = True
hasil = a and b
print(a,' AND',b,' =',hasil)

print()

#OR // minimal salah satu ada yang true maka hasilnya true
print('====OR====')
a = False
b = False
hasil = a or b
print(a,'OR',b,'=',hasil)
a = False
b = True
hasil = a or b
print(a,'OR',b,' =',hasil)
a = True
b = False
hasil = a or b
print(a,' OR',b,'=',hasil)
a = True
b = True
hasil = a or b
print(a,' OR',b,' =',hasil)

print()

#XOR // akan false jika kedua nilainya sama
print('====XOR====')
a = False
b = False
hasil = a ^ b
print(a,'XOR',b,'=',hasil)
a = False
b = True
hasil = a ^ b
print(a,'XOR',b,' =',hasil)
a = True
b = False
hasil = a ^ b
print(a,' XOR',b,'=',hasil)
a = True
b = True
hasil = a ^ b
print(a,' XOR',b,' =',hasil)