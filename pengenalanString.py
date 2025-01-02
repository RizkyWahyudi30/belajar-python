#  Cara membuat string

#  dasar nya
print("=== Dasar ===")

data = "ini bentuk biasa dari string yang sering kita gunakan\n"
print(data)

'''

1. Menggunakan kutip satu dan kutip dua 
2. Menggunakan bantuan backslash 
3. Menggunakan \t (backslash tab) dan \b (backslash backspace) dan newline

'''

#  menggunakan kutip satu dan dua
#  -- kutip satu --
print("=== 1. Menggunakan kutip satu dan kutip dua ===")

data = 'ini adalah bentuk string dengan kutip satu'
print(data)
#  -- kutip dua --
data = "ini adalah bentuk string dengan kutip dua"
print(data)
#  jika kita ingin menggabungkan keduanya bisa seperti ini 
data = "'ini adalah gabungan dari kutip satu dan kutip dua'\n"
print(data) # untuk gabungan dua ini bisa kutip dua dluan ataupun kutip satu dluan


#  menggunakan bantuan backslash
print("=== 2. Menggunakan bantuan backslash ===")
#  -- jika kita ingin membuat kalimat yang ada kutip nya --
data = 'ini merupakan contoh dengan tanda ku\'tip'
print(data)
#  -- jika ingin membuat kalimat dengan backslash di dalam nya --
data = "C:\\User\\react\\program-web\n"
print(data)


#  menggunakan backslash tab dan backslash backspace
print("=== 3.. Menggunakan bantuan backslash ===")
#  -- menggunakan backslash tab akan membuat kata yang dipenggal akan berjauhan  
data = "ini kalimat yang menggunakan \tbackslash tab"
print(data)
#  -- menggunakan backslash backspace akan membuat angka yang dipenggal menjadi berdekatan/nempel
data = "ini kalimat yang menggunakan \bbackslash backspace"
print(data) 

#  -- newline ini memiliki beberapa contohnya : --
#  1. menggunakan \n || ini yang biasa kita gunakan
print("-- menggunakan backslash n --")
print("ini baris pertama. \nini baris kedua.") # ini nama nya || LF = Line Feed
#  2. menggunakan \r
print("-- menggunakan backslash r --")
print("ini baris pertama. \rini baris kedua.") # ini nama nya || CR = Carriage Return 
#  3. menggunakan \r\n
print("-- menggunakan keduanya --")
print("ini baris pertama. \r\nini baris kedua.") # Gabungan dari kedua diatas
