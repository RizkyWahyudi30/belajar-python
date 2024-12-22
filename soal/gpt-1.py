# mengecek bilangan prima
def cek_bilangan(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka**.5)+ 1):
        if angka % 1 == 0:
            return False
    return True

# meminta input dari pengguna
try: 
    prima = int(input("Memasukkan bilangan bulat: "))
    if cek_bilangan(prima):
        print(f"Bilangan {prima} adalah bilangan prima")
    else:
        print(f"Bilangan {prima} bukan bilangan prima")
except ValueError:
    print("Input tidak valid! Harap masukkan bilangan bulat")