# soal 1
print("===== 1. Menampilkan tipe data masing - masing ======")
var1 = 123
var2 = "Hello, World!"
var3 = 3.14
var4 = True
var5 = [1, 2, 3, 4, 5]
var6 = {"name": "Alice", "age": 25}

print("Tipe dari tadi var1 = ", type(var1))
print("Tipe dari tadi var2 = ", type(var2))
print("Tipe dari tadi var3 = ", type(var3))
print("Tipe dari tadi var4 = ", type(var4))
print("Tipe dari tadi var5 = ", type(var5))
print("Tipe dari tadi var6 = ", type(var6))

# soal 2 
print("====== 2. Konversi tipe data =====")
num_str     = "456"
pi          = 3.14
is_active   = True 

# konversi num_str
num_int     = int(num_str)
num_float   = float(num_str)
# konversi pi
pi_int      = int(pi)
# konversi is_active
is_active_int = int(is_active)
is_active_str = str(is_active)

print("num_int = ", num_int)
print("num_float = ", num_float)
print("pi_int = ", pi_int)
print("is_active_int = ", is_active_int)
print("is_active_str = ", is_active_str)

# soal 3
print("====== 3. Konversi string ke integer ======")
a = 10 # integer
b = "30" # string

# komversi variable b ke tipe data integer
b_int = int(b)
result = a + b_int

print("hasil penjumlahan nya yaitu = ", result)

# soal 4 
print("===== 4. Validasi input dengan tipe data =====")

user_input = input("masukkan angka = ")

if user_input.isdigit():
    print("anda memasukkan ankga = ", int(user_input))
else: 
    print("input tidak valid, harus berupa angka")

# soal 5
print("===== 5. 45List, tuple dan dictionary ======")

data_list           = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data_tuple          = (11, 12, 13, 14, 15)
data_dictionary     = {"name" : "Wahyu", "age" : 16}

# tambah elemen ke data_list
data_list.append(9)
print("data_list setelah ditambah: ", data_list)

# Tidak bisa menambah elemen ke data_tuple
# data_tuple.append(9) -> AttributeError
# Tuples bersifat immutable

# tambah pasangan kunci nilai ke data_dictonary
data_dictionary["city"] = "Jakarta"
print("data_dictonary setelah ditambah: ", data_dictionary)