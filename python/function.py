# FUNCTION
# ===================================
# Function dibuat dengan menggunakan kata kunci def
# lalu diikuti dengan nama function dan diakhiri dengan kurung buka dan tutup lalu titik dua :. contoh, def nama_function():
# Biasanya nama function dibuat seperti nama variable, snake_case dan huruf kecil semua
# Isi function harus terdapat indentasi untuk menandakan bahwa itu adalah isi dari functionnya
# Untuk memanggil function, bisa langsung panggil dengan nama_function diikuti dengan kurung buka dan tutup. contoh, nama_function()


def fungsi():
    # kode yang akan dieksekusi sebagai function fungsi
    print("Hai, ini fungsi dari function fungsi")


# Panggil
fungsi()  # Hai, ini fungsi dari function fungsi
fungsi()  # Hai, ini fungsi dari function fungsi
fungsi()  # Hai, ini fungsi dari function fungsi


def cetak():
    print("Hasil cetak dari function cetak")


cetak()  # Hasil cetak dari function cetak


# FUNCTION DENGAN PARAMETER
# ===============================================
# Parameter memungkinkan kita untuk mengirim data ke function
# Caranya dengan tambahkan nama parameter ke dalam tanda kurung. contoh def nama_fungsi(nama): -------> nama itu parameter.
# Jika ingin menambahkan lebih dari satu parameter maka bisa gunakan karakter koma (,) sebagai pemisah parameter tsb. def nama_fungsi(nama, umur): -----------> nama dan umur itu parameter
# Lalu saat memanggil function tersebut maka wajib mengisi data pada parameter functionnya. atau bisa disebut sebagai argumen, yaitu data yang dikirim ke parameter function. nama_fungsi("Rey", 25) --------------> Rey dan 25 itu argumen, data yang dikirim ke parameter nama dan umur.


def bio(nama, umur):
    print(f"nama = {nama}, umur = {umur}")


# panggil fungsi bio dengan isi argumennya
bio("Rey", 20)  # nama = Rey, umur = 20
bio("Amanda", 28)  # nama = Amanda, umur = 28


def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjangnya adalah {} m2".format(luas))


# Panggil function luas_persegi_panjang dengan mengisi argumen panjang dan lebarnya
luas_persegi_panjang(20, 8)  # luas persegi panjangnya adalah 160 m2
luas_persegi_panjang(23, 5)  # luas persegi panjangnya adalah 115 m2
luas_persegi_panjang(50, 3)  # luas persegi panjangnya adalah 150 m2


# FUNCTION DENGAN RETURN VALUE
# ================================================
# Function melakukan sesuatu dan kita ingin mendapatkan hasil dari kegiatan function tersebut.
# Function bisa mengembalikan value (nilai) dari kegiatan yang dilakukan di dalam function
# Function bisa mengembalikan nilai dengan menggunakan kata kunci return yang kemudian diikuti value yang akan dikembalikan.


def luas_lingkaran(rad):
    pi = 3.14159
    luas = pi * rad**2
    return luas


luas1 = luas_lingkaran(10)
luas2 = luas_lingkaran(8)
print(luas1, luas2)  # 314.159 201.06176

# dengan adanya return, kita bisa gunakan value dari kegiatan sebelumnya
luas_double = luas1 * 2
print(luas_double)  # 628.318 (dua kali lipat dari value luas1 : 314.159)


# kalau tanpa return maka function tidak bisa jadi nilai dari variabel dan tidak bisa menggunakan value dari kegiatan sebelumnya
def sapa_dunia():
    print("Halo Dunia!")  # Hanya mencetak ke layar


# Kita coba simpan hasilnya ke variabel
hasil = sapa_dunia()

# Kalau kita cek isi variabel 'hasil'
print(hasil)
# Output: None (Karena fungsi tidak mengembalikan apa-apa)


# DEFAULT PARAMETER
# ================================================
# Sebelumnya kita tahu bahwa harus mengisi data pada saat panggil function jika pada function ada parameter.
# Tapi kita bisa menambahkan default parameter, yaitu nilai awal untuk parameter tersebut.
# Sehingga ketika kita tidak mengisi data pada saat memanggil function maka parameter dari function tersebut akan menggunakan nilai/data awal.
# Posisi default parameter tidak boleh di depan parameter biasa, harus di belakang parameter biasa.
# Untuk membuat default parameter, cukup tambahkan = diikuti denga nilai awalnya.


def sapa(nama, sapaan="Hai"):
    print(sapaan, nama)


sapa(
    "Yuji"
)  # Hai Yuji (Hai -----> default parameter yang otomatis muncul jika kita tidak mengisi data pada saat panggil function)
sapa("Aca", "Hallo")  # Hallo Aca
sapa("Manan", "Hey")  # Hey Manan


# KEYWORD ARGUMENT
# ===================================================
# Argument adalah nilai yang kita kirim ke parameter function ketika kita memanggil function
# Saat panggil function, posisi argument harus sama dengan posisi parameter di  function.
# Tapi jika kita ingin mengacak posisi argument segingga berbeda dengan posisi parameter maka harus menyebutkan parameternnya saat memanggil function.
# Fitur ini disebut Keyword Argument
# Saat menggunakan keyword argument, kit juga bisa mengkombinasikan dengan argument biasa.


def perkenalan(nama, umur, kota):
    print(f"nama {nama}, {umur} tahun, tinggal di kota {kota}")


# Positional Arguments
perkenalan("Ran", 15, "Sumedang")  # nama Ran, 15 tahun, tinggal di kota Sumedang

# Keyword Arguments
perkenalan(
    kota="Cirebon", nama="Sari", umur=25
)  # nama Sari, 25 tahun, tinggal di kota Cirebon


# gabung keyword, positional arguments, dan default parameter
def profil(nama, umur, kota="Jakarta", pekerjaan="Belum bekerja"):
    print(
        "Nama {}, umur {} tahun, tinggal di kota {}, {}".format(
            nama, umur, kota, pekerjaan
        )
    )


profil(
    "Reza",
    23,
)  # Nama Reza, umur 23 tahun, tinggal di kota Jakarta, Belum bekerja
profil(
    "Jeje", 15, "Padang", "Petani"
)  # Nama Jeje, umur 15 tahun, tinggal di kota Padang, Petani
profil(
    kota="Garut", nama="Dadang", umur=40, pekerjaan="Pengusaha"
)  # Nama Dadang, umur 40 tahun, tinggal di kota Garut, Pengusaha
profil(
    pekerjaan="Data Analyst",
    nama="Mad",
    umur=25,
    kota="Tangerang",
)  # Nama Mad, umur 25 tahun, tinggal di kota Tangerang, Data Analyst


# LOCAL VARIABLE
# ======================================
# Saat membuat variabel di dalam function maka varibel tersebut bersifat lokal di  function itu, sehingga tidak bisa digunakan di luar function.


def test():
    x = 100
    print("Nilai x di dalam fungsi :", x)


test()  # Nilai x di dalam fungsi : 100

# disini tidak bisa panggil variabel x
print(x)  # Error


# GLOBAL VARIABEL
# ===========================================
# Variabel yang kita buat di luar functionn, maka bisa digunakan di dalam function.
# Namun kita tidak bisa mengubah nilai  dari global variabel di dalam function. Jika kita hendak mengubah nilai global variabel maka kita harus mmenggunakan kata kunci "global"  di dalam functionnya.

nama_global = "Tejo"


def cetak_nama():
    print(nama_global)


# Tidak bisa merubah nilai dari variabel global, tapi hanya sekedar membuat variabel lokal baru.
def ubah_nama1():
    nama_global = (
        "Hari"  # -----variabel lokal baru bukan pengubah nilai dari variabel global
    )
    print(ubah_nama1)  # "Hari"


# Nah yang ini bisa merubah nilai dari variabel global nama_global
def ubah_nama2():
    global nama_global
    nama_global = "Rena"


cetak_nama()  # "Tejo"
ubah_nama1()
cetak_nama()  # "Tejo"
ubah_nama2()
cetak_nama()  # "Rena"


# PARAMETER DINAMIS
# ====================================
# Bisa dengan menambahkan tanda * sebelum parameter untuk  memberi tahu bahwa itu adalah parameter dinamis berupa list
# Bisa juga dengan menambahkan tanda ** sebelum nama parameter unntuk memberi tahu bahwa itu adalah parameter dinamis berupa dictionary


# buat function
def cetak_list(*list):  # *list parameter dinamis berupa  list
    for i in list:
        print(i)


# lalu gunakan function
cetak_list(1, 2, 3, 4, 5)
# 1
# 2
# 3
# 4
# 5


def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")


cetak_dict(nama="Dea", umur="25", kota="Jakarta")
# nama: Dea
# umur: 25
# kota: Jakarta
