# Tipe data dasar python
# -integer (int) = bilangan bulat
# -Float = Bilangan Desimal
# -String (str) = Teks
# -Boolean (bool) = True/False


# 1. int
# bilangan bulat positif dan negatif

umur = 24
tahun_lahir = 2002
saldo = -100000
nol = 0

# bilangan besar (python bisa handle angka sangat besar)
populasi_dunia = 8000000000
angka_besar = 1234567891234567891234577890

# untuk  mengecek type data bisa tambahka type()
print(type(umur))  # <class 'int'>
print(type(angka_besar))  # <class 'int'>


# 2. float
# bilangan dengan koma/titik

tinggi = 160.9
berat = 70.5
pi = 3.14159
suhu = -3.6

# notasi scientific
speed_of_light = 3e8  # 3 x 10^8 = 300000000
very_small = 1e-6  # 0.000001

print(type(tinggi))  # <class 'float'>
print(type(speed_of_light))  # <class 'float'>


# 3. str
nama = "aisy"  # single quotes (')
kota = "jakarta"  # double quotes (")
kalimat = """ 
hai nama saya adalah iman, 
silahkan panggil saja i atau man 
"""  # triple quotes  (multi-line)
empty_str = ""  # str kosong

print(type(kalimat))  # <class 'str'>
print(empty_str)


# 4. bool
is_student = True
is_married = False
has_license = True

print(type(is_student))  # <class 'bool'>


# VARIABEL
# =============================================

# assignment dasar
nama = "mad"
umur = 15
tinggi = 167.8
is_active = True

print(nama)  # mad
print(type(nama))

# multiple assignment
a = b = c = 0  # semua variabel bernilai 0
d, e, f = 1, 2, 3  # d = 1, e = 2, e = 3
nama, umur = "rey", 26  # nama="rey", umur=26

# mengubah nilai variabel
nilai = 90
print(nilai)  # 90
nilai = 100  # mengubah nilai
print(nilai)  # 100


# menggunakan variabel dalam operasi
nama_depan = "rey"
nama_belakang = "qwen"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # rey qwen

panjang = 20
lebar = 4
luas = panjang * lebar
print(luas)  # 80


# menggunakan variabel dalam print
print("nama lengkap:", nama_lengkap)  # nama lengkap: rey qwen
print("luas persegi panjang:", luas)  # luas persegi panjang: 80


# input dari pengguna dengan menggunakan function input() yang selalu menghasilkan str.
nama = input("masukan nama:")
print("hello", nama)

umur = input(
    "masukan umur kamu:"
)  # input disini pasti memiliki tipe data str bukan int atau float meskipun diinput berupa angka.
print("umur anda", umur)
print(type(umur))  # <class 'str'>

# function konversi tipe data
# int() = mengubah ke int
# str() = mengubah ke str
# float() = mengubah ke float
# bool() = mengubah ke bool (True/False)

umur = int(input("masukan umur kamu:"))
berat = float(input("masukan berat badan kamu:"))

print("umur kamu adalah", umur, "berat badan kamu adalah", berat)
print(type(umur))  # <class 'int'>
print(type(berat))  # <class 'float'>
