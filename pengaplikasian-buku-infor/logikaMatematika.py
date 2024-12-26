#  Buku Informatika Kelas 10

#  Ada di halaman 14 sampai 17
'''
Materi yang akan dibahas :
    1. Negasi
    2. Konjungsi
    3. Disjungsi
    4. Implikasi
    5. Biimplikasi
'''
print("=============== OPERASI MATEMATIKA ===============")
#  variabel 
p = True
q = False


#  1. Negasi
print("1. NEGASI, negasi adalah metode membalikkan nilai sebelumnya, yang semula nya bernilai TRUE menjadi false dan sebaliknya.")
print("   Operasi logika matematika ini menggunakan logika boolean, yaitu NOT")
print("\n   NEGASI dapat dinyatakan dengan tanda : ~")
#  contoh pengaplikasiannya
def negasi(p):
    # Fungsi ini untuk operasi negasi (NOT)
    return not p
print("Hasil operasi logika matematika NEGASI : ")
print(f"• Negasi (~p) : {negasi(p)}")
print(f"• Negasi (~q) : {negasi(q)} \n")

#  2. Konjungsi
print("2. KONJUNGSI, konjungsi merupakan teknik pneggabungan beberapa pertanyaan")
print("   Operasi logika matematika ini menggunakan logika boolean, yaitu AND")
print("\n   NEGASI dapat dinyatakan dengan tanda : ∧")
#  contoh pengaplikasiannya 
def konjungsi(p, q):
    return p and q 
print("Hasil operasi logika matematika KONJUNGSI : ")
print(f"• Konjungsi (p ∧ q): {konjungsi(p, q)}\n")

#  3. Disjungsi
print("3. DISJUNGSI, disjungsi merupakan teknik perbandingan antara dua pernyataan(penyataan majemuk)")
print("   Operasi logika matematika ini menggunakan logika boolean, yaitu OR")
print("\n   NEGASI dapat dinyatakan dengan tanda : ∨")
#  contoh pengaplikasiannya
def disjungsi(p, q):
    return p or q
print("Hasil operasi logika matematika KONJUNGSI : ")
print(f"• Konjungsi (p ∨ q): {disjungsi(p, q)}\n")

#  4. Implikasi
print("4. IMPLIKASI, implikasi merupakan penerapan pertanyaan majemuk yang menggunakan kata penghubung")
print("   Operasi logika matematika ini menggunakan kata, yaitu IF-THEN")
print("\n   IMPLIKASI dapat dinyatakan dengan tanda : →")
#  contoh pengaplikasiannya
def implikasi(p, q):
    return not p or q
print("Hasil operasi logika matematika IMPLIKASI : ")
print(f"• Konjungsi (p → q): {implikasi(p, q)}\n")

#  5. Bimplikasi
print("5. BIIMPLIKASI, biimplikasi merupakan jenis pernyataan majemuk yang dibentuk dengan kata penghubung")
print("   Operasi logika matematika ini menggunakan kata, yaitu IF AND ONLY IF")
print("\n   BIIMPLIKASI dapat dinyatakan dengan tanda : ↔")
#  contoh pengaplikasiannya
def biimplikasi(p, q):
    return p == q
print("Hasil operasi logika matematika BIIMPLIKASI : ")
print(f"• Konjungsi (p → q): {biimplikasi(p, q)}\n")


print("=============== SELESAI ===============")


