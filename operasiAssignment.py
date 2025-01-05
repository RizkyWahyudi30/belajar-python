#  Operasi Assignment
#  operasi yang dapat dilakukan dengan penyingkatan

#  operasi + dengan assignment

a = 3 # ini adalah assignment
print("nilai a : ", a)


print("========== OPERASI ARTIMETIKA ==========")
# a = a + 1  ===> ini dapat lebih dipersingkat lagi, menjadi 
a += 1
print("nilai a += 1 menjadi : ", a)
#  versi kurang
a -= 2
print("nilai a -= 2 menjadi : ", a)
#  versi kali
a *= 9
print("nilai a *= 2 menjadi : ", a)
#  versi bagi
a /= 3
print("nilai a /= 2 menjadi : ", a)
#  versi modulus
b = 7
print("\nnilai b : ", b)
b %= 3
print("nilai b %= 3 menjadi : ", b)
#  versi floor devision
b = 7
print("nilai b : ", b)
b //= 3
print("nilai b //= 3 menjadi : ", b)
#  versi pangkat
b = 7
print("nilai b : ", b)
b **= 3
print("nilai b **= 3 menjadi : ", b)

print("\n========== OPERASI BITWISE ==========")
print("==> OR")
#  OR
c = True # ver 1
print("Nilai c : ", c)
c |= False
print("nilai c |= false menjadi : ", c)
c = False # ver 2
print("Nilai c : ", c)
c |= False
print("nilai c |= false menjadi : ", c)

#  AND
print("==> AND")
c = True # ver 1
print("Nilai c : ", c)
c &= False
print("nilai c &= false menjadi : ", c)
c = True # ver 2
print("Nilai c : ", c)
c &= True
print("nilai c &= true menjadi : ", c)

#  XOR
print("==> XOR")
c = True # ver 1
print("Nilai c : ", c)
c ^= False
print("nilai c ^= false menjadi : ", c)
c = True # ver 2
print("Nilai c : ", c)
c ^= True
print("nilai c ^= true menjadi : ", c)

#  Shifting Right
print("==> Shifting Right")
d = 0b0100
print("nilai d : ", format(d,"04b"))
d >>= 2
print("nilai d >>= menjadi : ", format(d,"04b"))
#  Shifting Left
print("==> Shifting Left")
d <<= 2
print("nilai d <<= menjadi : ", format(d,"04b"))



