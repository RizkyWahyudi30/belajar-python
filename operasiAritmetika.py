#  operasi artimetika

a = 20 
b = 30
#  ===== operasi dasar ====== 
# pertambahan
hasil = a + b
print(a, "+", b, "=", hasil)

#  pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#  perkalian 
hasil = a * b
print(a, "*", b, "=", hasil)

#  pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

#  ===== operasi eksponen (pangkat) => pakai ** 
a = 12
b = 3
hasil = a ** b
print(a, "**", b, "=", hasil)

#  ===== operasi modulus (sisa bagi) => pakai %
a = 11
b = 2
hasil = a % b
print(a, "%", b, "=", hasil)

#  ===== operasi floor division (mirip dengan modulus, tapi ini pembulatannya) => pakai //
hasil = a // b
print (a, "//", b, "=", hasil)



#  ====== PRIOTITAS OPERATION ======
x = 4 
y = 5
z = 2

#  kategeri yang diutamakan => () , eksponen, perkalian-pembagian-modulus-floorDivision , perjumlahan dan pengurangan
#  perhitungan simpelnya
#  tanpa tanda kurung
hasil = x - z * y + x
print(x, "-", z, "*", y, "+", x, "=", hasil)

#  dengan tanda kurung
hasil = x - z * (y + x)
print(x, "-", z, "*", "(", y, "+", x, ")", "=", hasil)



#  perhitunagn hard
#  perhitungan akan berbeda 
print("===== TANPA TANDA KURUNG =====")

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

#  gambarannya
#  x ** y * z + x / y - y % z // x
#  4 ** 5 * 2 + 4 / 5 - 5 % 2 // 4
#   1024  * 2 +  0,8  -  1 //  4
#      2048  +  0, 8 - 0
#            2048,8    

#  ==============================================
print("===== DENGAN TANDA KURUNG =====")


#  jika salah satu kita tambahkan tanda kurung, maka akan dikerjakakan duluan
hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", "(", z, "+", x, ")", "/", y, "-", y, "%", z, "//", x, "=", hasil)
