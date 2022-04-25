#!/usr/bin/python3

# menerima input dari user:
# angka 1
angka1 = int(input("Masukkan angka pertama: "))

#angka 2
angka2 = int(input("Masukkan angka kedua: "))

# operasi yang dilakukan
	# 1 penjumlahan
	# 2 pengurangan	
	# 3 pembagian
	# 4 perkalian

print("""Masukkan operasi:
	1 : penjumlahan
	2 : pengurangan
	3 : pembagian
	4 : perkalian""")

operasi = int(input("Masukkan operasi"))

# melakukan operasi terhadap angkanya
if operasi == 1:
    print(angka1 + angka2)
elif operasi == 2:
    print(angka1 - angka2)
elif operasi == 3:
    print(angka1/angka2)
elif operasi == 4:
    print(angka1 * angka2)
