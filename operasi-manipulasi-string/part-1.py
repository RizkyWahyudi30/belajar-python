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


