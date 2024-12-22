# tipe data angka / angka satuan ( Integer | int )

# ini tipe data integer
data_integer = 5 
print("data = ", data_integer, ", bertipe :", type(data_integer))

# ini tipe data float
data_coba = 34.5
print("data ini = ", data_coba, ", bertipe : ", type(data_coba))

# tipe data int memiliki angka yang pasti / tidak mengandung koma ataupun yang lain


# tipe data desimal / angka bertanda koma atau titik ( Float | float ) 
data_float = 34.65
print("Data ini = ", data_float, ", bertipe : ", type(data_float))


# tipe data dengan karakter / tipe data string ( String | str )
a = "3.5"
b = 4
c = a * b 
print(c)
print("Data ini = ", a, ", bertipe : ", type(a))
print("Data ini = ", c, ", bertipe : ", type(c))


# tipe data biner True atau False ( Boolean | bool )
data_bool1 = True # harus menggunakan kapital kalao engga akan terhitung biasa
data_bool2 = False # harus menggunakan kapital kalao engga akan terhitung biasa
print("Kedua data ini = ", data_bool1,data_bool2, ", bertipe : ", type(data_bool1), type(data_bool2))


# tipe data khusus

# 1. tipe data complex atau tipe data dengan bilangan imajiner
data_complex = complex(5,6)
print("Data ini = ", data_complex, ", bertipe : ", type(data_complex))
# a = 5 yang artinya bilangan real
# b = 6 yang artinya bilangan imajiner
# rumus nya kalo di matematika z = a + bi




data_complex_2 = complex(7,8)
print("Data ini = ", data_complex_2, ", bertipe : ", type(data_complex_2))


# 2. tipe data dari bahasa C 
# python bisa make bahasa C karena python diciptakan dengan bahasa C

from ctypes import c_double 
data_c_double = c_double(10.5)
print("Data ini = ", data_c_double, ", bertipe : ", type(data_c_double))