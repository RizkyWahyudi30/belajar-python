#  OPERATOR DALAM BENTUK METHOD

## Mengubah case dari string
#  ** merubah ke upper **
cara1 = "Halo Ini Saya WahYuuu, Seorang Cyber Security dan Fullstack"
print("ini cara 1 : " + cara1.upper())

# ** merubah ke lower **
cara2 = "Halo Ini Saya WahYuuu, Seorang Cyber Security dan Fullstack"
print("ini cara 2 : " + cara2.lower())

## Pengecekan dengan isX method
# ** pengecekan lower case **
text = "halo ini apakah benar?"
print(text + ". Apakah Lower? : " + str(text.islower())) # karena jika tanpa str() ini akan terhitung sebagai bool
# ** pengecekan upper case **
text = "Halo ini apakah benar?"
print(text + ". Apakah Upper : " + str(text.isupper())) # karena jika tanpa str() ini akan terhitung sebagai bool

'''
Ada tambahan lagi :
1. isalpha() <-- untuk mengecek apakah semuanya huruf atau alphabet saja 
2. isalnum() <-- untuk mengecek apakah didalam variabel ada angka dan huruf
3. isdecimal() <-- untuk mengecek apakah semuanya angka saja
4. isspace() <-- untuk mengecek apakah didalam ada spasi, tab, newline
5. istitle() <-- untuk mengecek apakah awal kata dimulai dari huruf besar
'''

# praktek
# ** yang ke 1 **
text = "ini bernilai apa ?"
print("1. bernilai = " + str(text.isalpha())) # false karna ada tanda tanya (?)
# ** yang ke 2 **
text = "2a"
print("2. bernilai = " + str(text.isalnum())) # bernilai true karena ada angka dan huruf (huruf, bukan kata apalagi kalimat)
# ** yang ke 3 **
text = "1234S6"
print("3. bernilai = " + str(text.isdecimal())) # false karena ada huruf S
# ** yang ke 4 **
text = "    "
print("4. bernilai = " + str(text.isspace())) # true karena berisi spasi dan tab
# ** yang ke 5 **
text = "Apakah Rill banh"
print("5. bernilai = " + str(text.istitle())) # false karena kata "banh" dari huruf kecil

## pengecekan komponan
# ** menggunakan startswith **
text = "Ini bwenilai apa"
print("Ini bernilai = " + str(text.startswith("Ini")))
# ** menggunakan endwidth **
print("Ini bernilai = " + str(text.endswith("apa")))

## penggabungan dan pemisahan komponen
# ** menggunakan .join() **
data = ["ini", "menggunakan", "data", "list"]
print(" ".join(data))
# ** menggunakan .split() **
data = "Saya suka seseorang yang saya cintai"
print(data.split()) 

## alokasi karakter
# ** menggunakan rjust() **
text = "kanan"
print("'" + text.rjust(10) + "'") 
# ** menggunakan ljust() **
text = "kiri"
print("'" + text.ljust(10) + "'") 
# ** menggunakan center() **
text = "tengah"
print("'" + text.center(10) + "'") 

# bagaimana jika kita ingin memberikan tanda di kanan kiri nya, bisa menambhkan argument, seperti ini :
text = "tengah"
print("'" + text.center(10,"-") + "'") 
text = "kiri"
print("'" + text.ljust(10,"+") + "'") 
text = "kanan"
print("'" + text.rjust(10,"#") + "'") 
