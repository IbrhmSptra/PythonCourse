#latihan logical operator
#range angka

# - = false
# + = true
#--------5++++++10------
angka = float(input("Masukin Nilai dong : "))
proses = angka>5 and angka<10 #true
print("Hasilnya adalah :", proses)

#+++++++5------10+++++++
angka = float(input("Masukin Nilai dong : "))
proses = angka<5 or angka>10 #true
print("Hasilnya adalah :", proses)