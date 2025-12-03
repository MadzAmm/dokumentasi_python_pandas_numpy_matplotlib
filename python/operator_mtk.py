# OPERATOR DASAR : (+) tambah, (-) kurang, (/) pembagian
# OPERATOR PEMBAGIAN : (//) pembagian bulat, (%) modulo/sisa pembagian.
# OPERATOR PANGKAT : (**) pangkat
# ===============================================


x = 20
y = 2

print(x + y)  # 22
print(x - y)  # 18
print(x * y)  # 40
print(x / y)  # 10.0
print(x // y)  # 10
print(x % y)  # 0 (sisa pembagian dari 20/2)
print(21 % y)  # 1 (sisa pembagian dari 21/2)
print(x**y)  # 400

print(type(x + y))  # <class 'int'>
print(type(x - y))  # <class 'int'>
print(type(x * y))  # <class 'int'>
print(type(x / y))  # <class 'float'>
print(type(x // y))  # <class 'int'>
print(type(x % y))  # <class 'int'>


# OPERATOR ASSIGNMENT (PENUGASAN)
# =========================================================
# berguna untuk memberikan nilai pada variabel dengan menggunakan tanda =
# Compound Assignment : operator yang menggabungkan operasi aritmatika dengan assignment.

a = 5
print("a awal: ", a)  # 5

a += 5  # artinya a = a + 5
print("a setelah += 5 adalah", a)  # 10

a -= 2  # artinya a = a -2
print("a setelah -= 2 adalah", a)  # 8

a *= 3  # artinya a = a * 3
print("a setelah *= 3 adalah", a)  # 24

a /= 6  # artinya a = a / 6
print("a setelah /= 6 adalah", a)  # 4.0


# OPERATOR PERBADINGAN
# ==========================================
# Berguna untuk membandingkan dua nilai. hasil  dari operasi ini adalah bool (True atau False)

x = 5
y = 4

print(x > y)  # True (x lebih besar daripada y)
print(x < y)  # False (x lebih kecil  daripada y)
print(x >= y)  # True (x lebih besar sama  dengan y)
print(x <= y)  # False (x lebih kecil sama dengan y)
print(x == y)  # False (x sama dengan y)
print(x != y)  # True (x tidak sama dengan y)

# bisa juga digunakan pada str tapi hanya == dan !=

c = "rama"
d = "Rama"
e = "Ira"
f = "Ira"

print(c == d)  # False (karena rama tidak sama dengan Rama)
print(c != e)  # True (karena rama dan Ira tidak sama)
print(e == f)  # True (karena Ira sama dengan Ira)


# OPERATOR LOGIKA
# ============================================
# berguna untuk menggabungkan atau memodifikasi nilai boolean
# and (dan), mengahsilkan True jika 'kedua kondisi' True
# or (atau), menghasilkan True jika 'salah satu kondisi' True
# not (tidak), membalik boolean

kelas = 12
print(kelas > 6 and kelas < 13)  # True
# tapi kalau
print(
    kelas > 13 and kelas < 14
)  # False (karena kedua kondisi tidak semuanya True yaitu 12 > 13 (False))

nama = "Reza"
print(
    nama == "Reza" or nama == "reza"
)  # True (karena ada salah satu  kondisi yang True yaitu Reza == Reza )
# tapi kalau
print(
    nama != "Reza" or nama == "reza"
)  # False (karena kedua konsisi tidak ada yang True)

hidup = True
print(not hidup)  # False


# OPERATOR STR
# ==================================
# berfungsi pada str
# Concatenation (+) untuk menambah str
# Repetition (*) untuk  mengulang str sejumlah angka yang ditentukan
# Membership (in) untuk mengecek apakah text ada dalam str

# +
nama_depan = "Anna"
nama_belakang = "Huwaish"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Anna Huwaish

# *
print(nama_depan * 10)  # AnnaAnnaAnnaAnnaAnnaAnnaAnnaAnnaAnnaAnna

# in
teks = "Linux adalah Operating System"
print("Linux" in teks)  # True (karena kata Linux ada di teks)
print("Windows" in teks)  # False
print("System" in teks)  # True


# PRIORITAS OPERATOR
# ====================================================
# Operator mempunyai urutan (precedence). operator dengan prioritas lebih tinggi akan dieksekusi terlebih dahulu
# Urutan prioritas
# 1. ** (pangkat)
# 2. *,/,//,% (perkalian, pembagian)
# 3. +,- (penjumlahan, pengurangan)
# 4. ==,!=, <,>, <=,>= (perbandingan)
# 5. not
# 6. and
# 7. or
