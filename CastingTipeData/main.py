#casting tipe data
"""Integer"""
a = -1
hasilfloat = float(a) #5.0
hasilstr = str(a) #"5" dan ini tidak bisa di hitung aritmatika kaya +,-, x ,:
hasilbool = bool(a) # 0 bakalan false selain dari 0 itu true
print(hasilfloat)
print(hasilstr)
print(hasilbool)

print()
print("==============================================================================================")

"""Float"""
a = 3.5
hasilint = int(a) #dia bakalan hilang titiknya , bakalan dibulatkan kebawah jika decimal outputnya 3
hasilstr = str(a) #"3.5" dan ini tidak bisa di hitung aritmatika kaya +,-, x ,:
hasilbool = bool(a) # 0 bakalan false selain dari 0 itu true
print(hasilint)
print(hasilstr)
print(hasilbool)

print()
print("==============================================================================================")

"""Boolean"""
a = False
hasilint = int(a) #isinya true itu bakal 1 , isinya false itu bakal 0
hasilstr = str(a) #"false", "True" 
hasilfloat = float(a) #isinya true itu bakal 1.0 , isinya false itu bakal 0.0
print(hasilint)
print(hasilstr)
print(hasilfloat)

print()
print("==============================================================================================")

"""String"""
a = "70"
hasilbool = bool(a) #true, akan false jika isi stringnya kosong
hasilint = int(a) #error jika bukan angka , tidak akan eror jika stringnya itu angka
hasilfloat = float(a) #error jika bukan angka, tidak akan eror jika stringnya itu angka
print(hasilint)
print(hasilbool)
print(hasilfloat)
