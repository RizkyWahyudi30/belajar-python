#  Operasi dan memanipulasi string

#  1. Menyambung string (concatenate)
nama_awal       = "Wole"
nama_tengah     = "Des"
nama_akhir      = "Great"

nama_lengkap    = nama_awal + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)
#  string kosong digunakan untuk membuat spasi

#  2. Menghitung panjang string — menggunakan operasi length
panjang_nama = len(nama_lengkap)
print("nama lengkap dari " + nama_lengkap + " = " + str(panjang_nama)) #  ** menggunakan str karena panjang_nama disitu termasuk tipe data numbers
#  karena :
#  Hasil dari operasi len menghasilkan nilai bilangan bulat (integer), jika ingin digabungkan maka harus diubah dulu ke tipe string

#  3. Operator untuk string
#  -- mengecek apakah ada komponen char atau string di dalam string
s = "w"
status = s in nama_lengkap # case sensitive
print(s + " ada di " + nama_lengkap + " = " + str(status))
#  ini akan menghasilkan nilai false karena (W) tidak ada dalam variabel nama lengkap 
#  -- jika nilai true seperti ini :
s = "Des"
status = s in nama_lengkap # case sensitive
print(s + " ada di " + nama_lengkap + " = " + str(status))
#  -- jika ingin mengecek yang tidak ada, bisa memakai not
s = "f"
status = s not in nama_lengkap # case sensitive
print(s + " tidak ada di " + nama_lengkap + " = " + str(status))

# 
# 
#  -- jika ingin mengulang kata / kalimat bisa seperti ini :
print("ini"*10)
#  ataupun didepannya
print(3*"end")

#  4. Indexing 
print("index ke-0 : " + nama_lengkap[0]) # jika kita mulai ini, maka huruf awal dihitung sebagai 0, bukan satu, maka huruf yang ditampilkan merupakan huurf W
print("index ke-1 : " + nama_lengkap[1]) # ini akan mengeluarkan output huruf "e" karena huruf setelah w adalah e
print("index ke-7 : " + nama_lengkap[7]) # contoh lain nya 
#  -- bagaimana jika kita membuat nya menggunakan minus? apa yang terjadi?
print("index ke-(-2) : " + nama_lengkap[-2]) # jika kita menggunakan minus, maka akan dihitung dari belakang
print("index ke-(-5) : " + nama_lengkap[-5]) # ini juga sama 
#  ** bagaimana jika -0? hasilnya bagaimana ?
print("index ke-(-0) : " + nama_lengkap[-0]) # ** hasilnya akan tetap sama dengan 0 biasa
# 
#  -- bagaimana jika kita inign menghitung range nya ? Kita bisa menggunakan ini :
print("index ke-[0:6] : " + nama_lengkap[0:7]) # ketika kita ingin menghitung huruf dari 0 sampai 6, maka diakhir fungsi
                                                # kita perlu menambahkan angka nya 1, agar sampai ke huruf 6
print("index ke-[5:12] : " + nama_lengkap[5:13]) # ini contoh lainnya
#  ========================================================================================
#  -- bagaimana jika kita ingin menghitung genap nya saja ? bisa menggunakan ini
print("index ke-[0,2,4,5,6,8,10,12] :" + nama_lengkap[0:13:2]) # kita perlu menambahkan angka 2 dibelakang nya
# 
#  =======================================
#  -- jika kita ingin menghitung item kecil dan item terbesar dalam string :
#  menggunakan min-max, ascii_code, ord, str dan chr
#  ** item paling kecil **
print("item terkecil : " + min(nama_lengkap))
#  ** item paling besar **
print("item terbesar : " + max(nama_lengkap)) # ini akan menghasilkan output huruf t, yang seharusnya item terbesar adalah huruf w jika dari urutan alfabet
                                                # ini karena huruf W kita memakai CAPSLOCK, dan mungkin python tidak bisa membacanya

#  ascii_code, ord, str, chr
ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah : " + str(ascii_code))
data = 215
print("char untuk ASCII CODE adalah : " + chr(data))


#  5. Operator dalam bentuk method 
data = "camiel defgris the Haquel s'lif"
jumlah = data.count("e")
print("Jumlah huruf e pada = " + data + " adalah : " + str(jumlah))
