#  Operasi Komperasi
#  Membandingkan nilai
#  Setiap hasil dari komperasi adalah boolean

#  Biasanya menggunakan
#  > , < , >= , <= , == , != , is . is not

#  ============== Bahas ====================
#  variabel
a = 6
b = 4

#  Lebih besar dari >
print("\n=============== Lebih dari > =============== ")

hasil = b > a 
print(a, ">", b, "=", hasil)
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = a > 6 # jika kita menyatakan seperti ini, maka nilai nya akn false
print(a, ">", 6, "=", hasil) # karena nilai yang sama tidak dapat dinyatakan sebagai lebih dari

#  Kurang dari < 
print("\n=============== Kurang dari < =============== ")

hasil = a < 3 
print(a, "<", 3, "=", hasil)
hasil = a < 9
print(a, "<", 9, "=", hasil)
hasil = a < 6
print(a, "<", 6, "=", hasil)

#  Lebih dari sama dengan >= 
print("\n===============  Lebih dari sama dengan >=  =============== ")

hasil = a >= 5
print(a, ">=", 5, "=", hasil)
hasil = b >= 5
print(b, ">=", 5, "=", hasil)
# yang membedakan dari sebelumnya
hasil = a >= 6
print(a, ">=", 6, "=", hasil)  # hasilnya akan bernilai true, karena sistem lebih dari sama dengan, berbeda dari sebelumnya
                                # karena, sistem ini, memulai dari angka yang ditargetkan, beda dengan yang diaatsnya, mulai lebih sedikit
                                # dari angka yang ditargetkan

#  Kurang dari sama dengan <=
print("\n===============  Kurang dari sama dengan <=  =============== ")
#  ssama seperti sebelum nya untuk hitungan yang ketiga
hasil = a <= 5
print(a, "<=", 5, "=", hasil)
hasil = b <= 5
print(b, "<=", 5, "=", hasil)
# yang membedakan dari sebelumnya
hasil = a <= 6
print(a, "<=", 6, "=", hasil)

#  Sama dengan ==
print("\n===============  Sama dengan ==  =============== ")
hasil = a == 6 # beda antara sama dengannya satu (=) dan sama dengan dua (==)  
print(a, "==", 6, "=", hasil) # sama dengan satu disebutnya dengan : assigment
                                # kalo sama dengan dua (==) itu artinya membandingkan dua buah nilai
hasil = a == 5
print(a, "==", 5, "=", hasil)

#  Tidak sama dengan !=
print("\n===============  Tidak sama dengan !=  =============== ")
hasil = a != 6
print(a, "!=", 6, "=", hasil)
hasil = a != 3
print(a, "!=", 3, "=", hasil)


#  Selanjut nya ini agak berbeda, kita akan membahasa is dan is not
#  ==== Mundur dulu ====

#  Operasi komperasi yang dijalankan diaatas :
#  seperti > , < , >=, <= , == , !=
#  hanya dapat dijalankan pada syntax literal

#  Maksudnya seperti ini : 
#  a == 4

#  // a merupakan sebuah variabel dan a memiliki nilai nya dan dapat disimpan di komputer, atau memakan memori / masuk memori
#  // sedangkan 4 merupakan literal, dia hanya bisa dijalankan sekali saja, karena dia bukan variabel dan hanya langsung nilai
    # maka ketika dipanggil kembali, itu akan tidak bisa, karena 4 bukanlah, variabel

#  Maka dari itu
#  Fungsi is disini guna nya untuk membandingkan objek atau memori

#  Contohnya :
#  a is b  // ini tidak akan bisa

#  Yang bener :
#  a = 4
#  b = 4
#  a is b  // ini akan berjalan, karena is membandingkan dua variabel

print("\n===============  Object Identity 'is'  =============== ")
#  'is' sebagai komparasi object identity
x = 5  # ini adalah assingment membuat objek
y = 5 
print("nilai x = ", x, "id = ", hex(id(x)))  
print("nilai y = ", y, "id = ", hex(id(y)))  
#  nilai id nya akan sama, karena python ketika mendeteksi ada hal yang memilki kesamaan, biasanya disimpan di memori yang saam
hasil = x is y
print("x is y = ", hasil)
#  Jika 'y' diubah menjadi nilai, contohnya 5, maka akan terjadi warning seperti dibawah 
#  ///   SyntaxWarning: "is" with 'int' literal. Did you mean "=="?   hasil = x is 5   ///

#  Bagaimana jika nilai dari variabelnya diubah ?
x = 6
y = 5 
print("nilai x = ", x, "id = ", hex(id(x)))  
print("nilai y = ", y, "id = ", hex(id(y))) 
hasil = x is y
print("x is y = ", hasil)
#  Maka nilai id akan disimpan di memori yang berbeda dan nilai perbandingkan is akan menghasilkan nilai = false

#  Kalo yang is not
#  Sistem sama kayak tidak sama dengan, mencari yang berbeda
print("\n===============  Object Identity 'is not'  =============== ")
x = 5  # ini adalah assingment membuat objek
y = 5 
print("nilai x = ", x, "id = ", hex(id(x)))  
print("nilai y = ", y, "id = ", hex(id(y)))  
#  nilai id nya akan sama, karena python ketika mendeteksi ada hal yang memilki kesamaan, biasanya disimpan di memori yang saam
hasil = x is not y  ### ini akan menghasilkan nilai false, berbanding terbalik
print("x is y = ", hasil)
#  Jika 'y' diubah menjadi nilai, contohnya 5, maka akan terjadi warning seperti dibawah 
#  ///   SyntaxWarning: "is" with 'int' literal. Did you mean "=="?   hasil = x is 5   ///

#  Bagaimana jika nilai dari variabelnya diubah ?
x = 6
y = 5 
print("nilai x = ", x, "id = ", hex(id(x)))  
print("nilai y = ", y, "id = ", hex(id(y))) 
hasil = x is not y   ### ini akan menghasilkan nilai true,  berbanding terbalik
print("x is y = ", hasil)