# Format String
# dengan format string, kita dapat mempersingkat penulisan

# contoh generic
# ** string **
data = "bahasa yang mudah dipahami."
print(f"Python adalah {data}")
# ** boolean **
data = True
print(f"nilai output = {data}")
# ===============
# ** angka **
data = 2334.5
print(f"angka nya = {data}")
# ** angka : bilangan bulat **
data = 16
print(f"angka bilangan bulat = {data:d}") # format :d untuk menyatakan bahwa angka ini adalah bilangan bulat desimal
# ** angka : bilangan ribuan / jutaan **
data = 2000 # ribuan
print(f"angka bilangan ribuan = {data:,}") # format :, untuk memisahkan dari 3 angka nol
data = 2000000 # jutaan
print(f"angka bilangan jutaan = {data:,}") # format :, untuk memisahkan dari 3 angka nol
# ** angka : bilangan desimal **
data = 20345.4321
print(f"angka bilangan desimal = {data:.2f}") # format :.2f adalah untuk menyingkat output nya
# ** angka : menampilkan leading zero
data = 20345.4321
print(f"angka / menampilkan leading zero (8) = {data:8.2f}") # dengan 8 === pada angka 8 tidak terlihat
data = 20345.4321
print(f"angka / menampilkan leading zero (9) = {data:9.2f}") # dengan 9 === akan ada spasi 1 di depan angka 
data = 20345.4321
print(f"angka / menampilkan leading zero (09) = {data:09.2f}") # dengan 09 === akan menampilkan 0 di depan
data = 20345.4321
print(f"angka / menampilkan leading zero (010) = {data:010.2f}") # dengan 010 === akan menampilkan 2 nol di depan
# ** angka : menampilkan tanda + dan -
data_plus = 20
data_minus = -20
print(f"output dari angka plus dan minus = {data_plus:+d} dan {data_minus:+d}") # format :+ untuk lebih memspesifisikan kalau angka itu positif
# ** angka : memformat persen / menampilkan persen **
data_persen = 00.6742
print(f"menampilkan angka persen = {data_persen:%}")  # cara 1
data_persen = 00.6742
print(f"menampilkan angka persen = {data_persen:.2%}")  # cara 2
# ** angka : menampilkan angka lain seperti binary, octal, hexadecimal
data_angka_lain = 30
print(f"angka binary = {bin(data_angka_lain)}")
print(f"angka octal = {oct(data_angka_lain)}")
print(f"angka hexadecimal = {hex(data_angka_lain)}")