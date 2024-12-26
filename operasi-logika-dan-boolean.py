#  OPERASI LOGIKA ATAY BOOLEAN

#  ada beberapa yaitu : not, or, and, xor

#  menggunakan NOT
print("========== NOT ==========")
x = True
y = not x
print("nilai x : ", x)
print("--- menggunakan not ---")
print("nilai y : ", y )
#  operasi logika menggunakan not adalah mengembalikan nilai dengan sebaliknya
#  jika nilai x = True maka, not x / y = false || begitupun sebaliknya

#  menggunakan OR
print("========== OR ==========")   ### kita hrus mempunyai 2 nilai
#  Didalam logika OR, jika salah satu nilai terdapat TRUE maka output nya akan menghasilkan nilai TRUE
#  1.
x = False
y = False
z = x or y
#  2. 
print(x, "OR", y, "=", z)
x = False
y = True
z = x or y
#  3.
print(x, "OR", y, "=", z)
x = True
y = False
z = x or y
#  4.
print(x, "OR", y, "=", z)
x = True
y = True
z = x or y
print(x, "OR", y, "=", z)

#  menggunakan AND 
print("========== AND ==========")   ### kita hrus mempunyai 2 nilai
#  Didalam logika AND, jika salah satu nilai terdapat FALSE maka output nya akan menghasilkan nilai FALSE
#  /// kebalikan dari OR ///
#  1.
x = False
y = False
z = x and y
#  2. 
print(x, "AND", y, "=", z)
x = False
y = True
z = x and y
#  3.
print(x, "AND", y, "=", z)
x = True
y = False
z = x and y
#  4.
print(x, "AND", y, "=", z)
x = True
y = True
z = x and y
print(x, "AND", y, "=", z)

#  menggunakan XOR
print("========== XOR ==========")   ### kita hrus mempunyai 2 nilai 
#  Didalam operasi logika, nilai nya akan TRUE jika salah satu nya saja, TETAPI jika 2 variabel bernilai TRUE, maka akan 
#  menghasilkan nilai FALSE
#  ///XOR menggunakan tanda = ^  ///
#  1.
x = False
y = False
z = x ^ y
#  2. 
print(x, "XOR", y, "=", z)
x = False
y = True
z = x ^ y
#  3.
print(x, "XOR", y, "=", z)
x = True
y = False
z = x ^ y
#  4.
print(x, "XOR", y, "=", z)
x = True
y = True
z = x ^ y
print(x, "XOR", y, "=", z)
