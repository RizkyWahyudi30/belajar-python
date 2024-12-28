#  Operasi bitwise
#  operasi biner 

#  Bitwise ==> operasi pada masing masing bit

#  Operasi bitwise ada yang mennggunakan OR, AND, XOR, NOT

#  Variable
x = 8
y = 5

#  Menggunakan bitwise OR : |
z = x | y
print("\n========== MENGGUNAKAN OR ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("nilai :", y, ", binary :", format(y,"08b"))
print("--------------------------------------- ( tanda OR | )")
print("nilai :", z, ", binary :", format(z,"08b"))

#  Menggunakan bitwise AND : &
z = x & y
print("\n========== MENGGUNAKAN AND ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("nilai :", y, ", binary :", format(y,"08b"))
print("--------------------------------------- ( tanda AND & )")
print("nilai :", z, ", binary :", format(z,"08b"))


#  Menggunakan bitwise XOR : ^
z = x ^ y
print("\n========== MENGGUNAKAN XOR ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("nilai :", y, ", binary :", format(y,"08b"))
print("--------------------------------------- ( tanda XOR ^ )")
print("nilai :", z, ", binary :", format(z,"08b"))

#  Menggunakan bitwise NOT : ~
z = ~x
print("\n========== MENGGUNAKAN NOT ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("--------------------------------------- ( tanda NOT ~ )")
print("nilai :", z, ", binary :", format(z,"08b"))
#  jika ingin di flip bisa menggunakan cari ini 
print("--------------------------------------- ( tanda XOR ^ )")
p = 0b0000001000
q = 0b1111111111
print("nilai :", p^q, ", binary :", format(p^q,"08b"))




#  =========================
#  Shifting 
#  menggeser

#  Shifting right  : >>
z = x >> 3
print("\n========== MENGGUNAKAN SHIFTING RIGHT ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("--------------------------------------- ( tanda right >> )")
print("nilai :", z, ", binary :", format(z,"08b"))

#  Shifting left  : <<
z = x << 3
print("\n========== MENGGUNAKAN SHIFTING LEFT ==========")
print("nilai :", x, ", binary :", format(x,"08b"))
print("--------------------------------------- ( tanda left << )")
print("nilai :", z, ", binary :", format(z,"08b"))