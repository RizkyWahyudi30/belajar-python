# perubahan tipe data dari tipe data satu ke tipe data yang lain

# operating casting
# tipe data = int, float, bool, str

# integer
print("========= INTEGER =========")
data_int = -10;
print("tipe = ", data_int, ", type = ", type(data_int))

# ===========================================
# casting tipe data
data_float = float(data_int);
print("data = ", data_float, ", type = ", type(data_float))
# casting tipe data
# ===========================================

data_float   = float(data_int);
data_bool    = bool(data_int);
data_str     = str(data_int)
print("data = ", data_float, ", type = ", type(data_float));
print("data = ", data_bool, ", type = ", type(data_bool)); # akan bernilai false jika data_int nya diberikan nilai 0
print("data = ", data_str, ", type = ", type(data_str));

# float
print("========= FLOAT =========")
data_float = 9.9;
print("tipe = ", data_float, ", type = ", type(data_float))

data_int       = int(data_float);
data_bool      = bool(data_float);
data_str       = str(data_float);
print("data = ", data_int, ", type = ", type(data_int)) # akan dibulatkan ke bawah 
print("data = ", data_bool, ", type = ", type(data_bool))
print("data = ", data_str, ", type = ", type(data_str))

# boolean
print("============ BOOLEAN =========")
print("===== True =====")
data_bool_true = True; # True
print("tipe = ", data_bool_true, ", type ", type(data_bool_true))

data_float      = float(data_bool_true);
data_int        = int(data_bool_true);
data_str        = str(data_bool_true);
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))

print("===== FALSE =====")
data_bool_false = False; # False
print("tipe = ", data_bool, ", type ", type(data_bool_true))

data_float      = float(data_bool_false);
data_int        = int(data_bool_false);
data_str        = str(data_bool_false);
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))

# string
print("========== STRING ==========")
data_str = "10"; # string harus berupa angka, tidak bisa berupa huruf / kalimat
print("tipe = ", data_str, ", type = ", type(data_str))

data_bool       = bool(data_str); # kalo mau ngubah string ke bool dengan nilai false dengan cara dibawah ini
data_int        = int(data_str);
data_float      = float(data_str);
print("data = ", data_bool, ", type = ", type(data_bool))
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))

print("=== false string to boolean ===")
data_str = ""; # ini cara nya agar bisa menjadi false
print("tipe = ", data_str, ", type = ", type(data_str))

data_bool       = bool(data_str); # data string harus kosong agar menghasilkan nilai false
# data_int        = int(data_str);
# data_float      = float(data_str);
print("data = ", data_bool, ", type = ", type(data_bool))
# print("data = ", data_int, ", type = ", type(data_int))
# print("data = ", data_float, ", type = ", type(data_float))