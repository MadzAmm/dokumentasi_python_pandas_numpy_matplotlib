# MENGGABUNGKAN STR
# bisa menggunakan +
# str tidak bisa digabungkan dengan tipe data lain. solusi harus konversi dengan str()

nama = "aisy"  # str
umur = 25  # int

# Penggabungan yang salah
# pesan = "nama saya"+ nama + ", umur saya" + umur

# Penggabungan yang benar
pesan = "nama saya " + nama + ", umur saya " + str(umur)

print(pesan)


# PANJANG STR
# pakai function len() untuk mengetahui panjang str
# tipe data dari hasil len() adalah int

# bisa taruh di value dalam variabel
panjang_nama = len(nama)
print(panjang_nama)  # 4 (int)
# atau langsung dalam print
print(len(pesan))  # 28 (int)
print(type(len(nama)))  # <class 'int'>


# AKSES KARAKTER DALAM STR (INDEXING)
# Setiap karakter dalam str memiliki posisi (index) yang dimulai dari 0
# Untuk akses posisi bisa gunakan square brackets (kurug kotak)
# Gunakan index negatif jika hendak mulai dari karakter paling belakang.


nama = "Linux"
print(nama[0])  # L (karakter peratama)
print(nama[1])  # i (karakter kedua)
print(nama[3])  # u (karakter keempat)
print(nama[-1])  # x (karakter terakhir)
print(nama[-2])  # u (karakter kedua dari belakang)


# STR SLICING (tidak hanya satu karater yang diambil tapi bisa lebih)
# Gunakan kurung kotak juga tapi ada posisi awal dan posisi akhir yang dipisahkan oleh titik dua (:) > [..:..]
# Jika posisi awal tidak disebutkan maka defaut index adalah 0. > [:3] (index ke 0 sampai ke 3)
# Jika posisi akhir tidak disebutkan maka default index adalah index terakhir. > [:] (index ke 0 sampai index terakhir).


print(nama[0:3])  # Lin (index 0,1,2)
print(nama[2:4])  # nu  (index 2,3)
print(nama[:2])  # Li   (dari awal sampai index 1)
print(nama[3:])  # ux   (index 3 sampai index terakhir yaitu index 4)
print(nama[:])  # Linux (dari index awal sampai index terakhir / seluruh str)


# STR METHODS (FUNGSI STR)
# upper() mengubah jadi  huruf besar
# lower() mengubah jadi huruf kecil
# title() mengubah huruf awal setiap kata jadi besar
# capitalize() mengubah huruf awal jadi besar
# strip() menghilangkan karakter kosong (seperti spasi) di  awal  dan di akhir
# replace(dari,menjadi) mengganti bagian tertentu dalam str
# count(text) menghitung berapa kali teks muncul
# find() mencari posisi/iindex teks muncul

nama = "Tissa"

upper = nama.upper()
print(upper)  # TISSA

lower = nama.lower()
print(lower)  # tissa


nama_panjang = " tissa  anggraine"
title = nama_panjang.title()
print(title)  # Tissa  Anggraine

capitalize = nama_panjang.capitalize()
print(capitalize)  # Tissa  anggraine

print(nama_panjang.strip())  # tissa anggraine

print(nama_panjang.replace("tissa", "sari"))  # sarianggraine

print(nama_panjang.count("s"))  # 2

teks = "Ubuntu Linux"
posisi = teks.find("Linux")
print(posisi)  # 7
# atau bisa langsung pakai di print juga
print(teks.find("Linux"))  # 7


# ESCAPE CHARACTERS
# \n baris baru/enter
# \t tab
# \ backslash
# mau " atau ' , atau karakter lainnya dalam kalimat maka dahului \ dulu

teks = "teks pertama \nteks kedua"
print(teks)
# teks pertama
# teks  kedua

biodata = "nama:\taisy\numur:\t25"
print(biodata)
# nama:  aisy
# umur:  25

path = "D:\\Users\\Aisy\\Directory"
print(path)  # D:\Users\Aisy\Directory

teks2 = 'katakan "hay" pada orang itu setiap hari jum\'at.'
print(teks2)  # katakan "hay" pada orang itu setiap hari jum'at.


# STR INTERPOLATION / F-STR
# Cara menggabungkan varibel dengan teks
# lebih mudah dibaca dan efisien daripada concatenation (+)
# f-str = cara terbaru dan direkomendasikan untuk interpolasi str di python
# pakai kurung kurawal  untuk akses variabel

nama = "Wahyu"
kelas = 12
kota = "Semarang"

# pakai concatenation (+)
print(
    "Halo, nama saya "
    + nama
    + ", saya kelas "
    + str(kelas)
    + ", saya tinggal di kota "
    + kota
)

#  pakai interpolasi str atau f-str
print(f"Halo, nama saya {nama}, saya kelas {kelas}, saya tinggal di kota {kota}")
# atau
profil = f"Halo, nama saya {nama}, saya kelas {kelas}, saya tinggal di kota {kota}"
print(profil)
# atau str.format biasa
print(
    "Halo, nama saya {}, saya kelas {}, saya tinggal di kota {}".format(
        nama, kelas, kota
    )
)
# atau str.format dengan index
print(
    "Halo, nama saya {0}, saya kelas {1}, saya tinggal di kota {2}".format(
        nama, kelas, kota
    )
)
# atau str.format dengan nama parameter
print(
    "Halo, nama saya {n}, saya kelas {k}, saya tinggal di kota {ko}".format(
        n=nama, k=kelas, ko=kota
    )
)

# hasilnya akan sama yaitu 'Halo, nama saya Wahyu, saya kelas 12, saya tinggal di kota Semarang'


# f-str dengan expressions
# f-str bisa  eksekusi ekspresi langsung di dalamnya.

harga = 30000
jumlah = 5

total = f"harga satu apel adalah {harga}, sedangkan saya membeli {jumlah} buah apel maka harga totalnya adalah {harga*jumlah}"
print(
    total
)  # harga satu  apel adalah 30000, sedangkan saya membeli 5 buah apel maka harga totalnya adalah 150000

nama = "wina"
salam = f"Halo {nama.upper()}"
print(salam)  # Halo WINA
