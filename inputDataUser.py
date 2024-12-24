# Mengambil input data dari user

print("====== Cara Dasar ======")
data = input("masukkan data : ") # apapun kata, kalimat, angka yang kita masukkan, akan berakhir menjadi tipe data string
print("data : ", data, ", type : ", type(data))

# jika ingin mengubah tipe data nya menjadi integer, maka dengan cara
print("====== Mengubah data ke integer ======")
data_int = int(input("masukkan data : "))
print("data : ", data_int, ", type : ", type(data_int))

# biar gampang bisa diubah dengan cara mengganti variabel menjadi angka
print("====== Lebih Ringkas ======")
angka = float(input("masukkan data float : "))
angka =  int(input("masukkan data integer : "))
print("data : ", angka, ", type : ", type(angka))
print("data : ", angka, ", type : ", type(angka))

# jika ingin dengan boolean
print("====== Data Boolean ======")

biner = bool(input("masukkan data biner : ")) # akan selalu menghasilkkan nilai true walaupun data biner nya nol
print("data : ", biner, ", type : ", type(biner))

# jika ingin nilai false harus di casting ke integer dulu
biner = bool(int(input("masukkan data biner : ")))
print("data : ", biner, ", type : ", type(biner))

