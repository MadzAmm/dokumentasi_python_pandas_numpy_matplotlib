# Object-oriented progarming
# merupakan paradigma programing yang mengorganisir code berdasarkan objects dan class
# oop itu ibarat cara berpikir kita dalam dunia nyata dimana setiap benda memiliki karakteristik  (properties) dan kemampuan (behaviors).
# contoh sederhana:
# - mobil memiliki karakteristik : warna, merek, dan tahun.
# - mobil memliki kemampuan : maju, mundur, belok, dan klakson.
# Dalam oop :
# kerakteristik = atributes (variabel dalam objects)
# kemampuan = Methods (functions dalam objects)


# Keuntungan oop

# Data dan behavior tergabung dalam satu unit
# lebih mudah dipahami dan dimaintain
# REusable - bisa buat multiple instances
# Data protecttion - tidak mudah corrupt
# Scalable utuk sistem yang kompleks

# 4 pilar oop

# Encapsulation (pembungkusan), menggabungkan data  dan method dalam satu unit (class), dan menyembuyikan detail implementasi.
# Inheritance (Pewarisan), child class mewarisi properties dan methdod dari parent class
# Polymorphisme (Banyak bentuk), objek yang berbeda bisa merespon method call yang sama dengan cara yang berbeda.
# Abstraction (Abstraksi), menyembunyikan complexity dan hanya menamilkan interface yang penting.

# Real-World Analogies

# Class = Blueprint/Cetakan mobil
# Objects = MObil yang dproduksi dari blueprint
# Attributes = Warna, mesin, roda
# Methods = Maju,mundur, klakson.


# Apa itu class dan object

# CLass adalah blueprint atau template unntuk membuat objects. bayangkan class seperti cetakan kue - dengan satu cetakan, kita bisa membuat banyak kue dengan bentuk yang sama
# Object adalah instance dari class -hasil "produksi" dari blueprint class. setiap object memiliki data dan behavior yang sama strukturnya, tapi valuenya bisa berbeda.


# contoh blueprint


from unittest import result


class Kampus:
    pass


class Mahasiswa:
    pass


# dan berikut merupakan cara membuat objectya
# dua objek dari satu blueprint yang sama Kampus()
kampus1 = Kampus()
kampus2 = Kampus()

print(type(kampus1))  # <class '__main__.Kampus'>
print(type(kampus2))  # <class '__main__.Kampus'>


# dua objek dari satu blueprint yang sama yaitu Mahasiswa()
mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()
print(type(mahasiswa1))  # <class '__main__.Mahasiswa'>
print(type(mahasiswa2))  # <class '__main__.Mahasiswa'>


# Class dan attributes
# ==================================

# Attributes adalah variable menyimpan data dalam object
# Attributes itu ada beberapa diantaranya ada instance attributes, Class attributes


# Instance attributes

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "Maman"

print(mahasiswa1.nim)  # 12345
print(mahasiswa1.nama)  # Maman

mahasiswa2.nim = 234565
mahasiswa2.nama = "Syaiful"

print(mahasiswa2.nim)  # 234565
print(mahasiswa2.nama)  # Syaiful


# Class attributes
# =================================

# Instance attributes hanya akan ada di object hasil dari instasiasi dari class, dan tidak akan ada di object lain walaupunn dari class yang sama.
# Jika kita ingin membuat atribut yang secara default (bawaan) ada di semua object hasil instansiasi, maka kita perlu membuat class attributes, yaitu attributes yang didefinisikan di dalam classnya.


# Buat blueprint
class Kampus:
    nama = ""  # attributes class
    kota = ""  # attributes clas


class Mahasiswa:
    nama = ""  # attributes class
    nim = ""  # attributes class


# buat objek
kampus1 = Kampus()
kampus2 = Kampus()

# rubah value dari attributes class lewat objek
kampus1.nama = "UINJKT"
kampus1.kota = "Jakarta"
# rubah value dari attributes class lewat objek
kampus2.nama = "UI"
kampus2.kota = "Depok"

print(kampus1.nama)  # UINJKT
print(kampus1.kota)  # Jakarta

print(kampus2.nama)  # UI
print(kampus2.kota)  # Depok

# buat objek
mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()

# rubah value dari attributes class lewat objek
mahasiswa1.nama = "Maman"
mahasiswa1.nim = 12345
# rubah value dari attributes class lewat objek
mahasiswa2.nama = "Syaiful"
mahasiswa2.nim = 2345

print(mahasiswa1.nama)  # Maman
print(mahasiswa1.nim)  # 12345

print(mahasiswa2.nama)  # Syaiful
print(mahasiswa2.nim)  # 2345


# Class dengan Methods
# ==========================================

# Methods adalah function yang berada di dalam class dan bisa dipanggil oleh objects
# Perbedaan method atau function dalam class dengan function biasa adalah adanya parameter self.
# parameter self sangat penting karena parameter ini adalaha parameter khusus yang merujuk pada instance /object yang sedang memanggil method. misal jika object  yang memanggil adalah mahasiswa1 maka self itu adalah class yang menjadi objek dari mahasiswa1, jika object yang memanggil adalah mahasiswa2 maka self itu adalah class yang menjadi objek mahasiswa2. jadi tergantung si object yang memanggilnya.


class Mahasiswa:
    nim = ""
    nama = ""

    def perkenalan(
        self,
    ):  # perbedaan dengan function biasa, method yang ada di dalam class memiliki parameter self
        print(f"Hello nama saya {self.nama}, dan nim saya adalah {self.nim}")


mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "Maman"
mahasiswa1.perkenalan()  # Hello nama saya Maman, dan nim saya adalah 12345


mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 2345
mahasiswa2.nama = "Syaiful"
mahasiswa2.perkenalan()  # Hello nama saya Syaiful, dan nim saya adalah 2345


# Methode dengan parameters selain self
# ======================================================

# Parameter di method tidak hanya self, kita bisa menambahkan pparameter lain seperti function biasa.
# Semua yang bisa kita lakukan di function bisa kita lakukan juga di method.


class Mahasiswa:
    nim = ""
    nama = ""

    def perkenalan(self):
        print(f"Hello nama saya {self.nama}, dan nim saya adalah {self.nim}")

    def hello(self, nama):
        print(f"Hello {nama}, nama saya adalah {self.nama}")


mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "Arya"
mahasiswa1.nim = 12345
mahasiswa1.perkenalan()  # Hello nama saya Arya, dan nim saya adalah 12345
mahasiswa1.hello("Syaiful")  # Hello Syaiful, nama saya adalah Arya

# Naming Conventions
# ===========================================

# Class Name : PascalCase, misal Mahasiswa, MataPelajaran, KategoriBarang.
# Method Name : snake_case, misal perkenalan(), warna_mobil, dll.
# Attribute Name : snake_case, misal  nama, nama_depan, nama_belakang, dll.


# Constructor
# ========================================

# Constructor adalah method spesial yang otomatis dipanggil saat object dibuat.
# Dalam python, constructor adalah method __init__()
# Constructor digunakan untuk initialize (setup awal) oject dengan data yang diperlukan.

# contoh class yang memiliki method yang bukan constructor


class Mahasiswa:
    nim = ""
    nama = ""

    def perkenalan(self, nama, nim):
        self.nama = nama
        self.nim = nim


# ketika hendak membuat objek dan kemudian memanggilnya maka perlu panggil secara manual objek dan methodnya.

mhs = Mahasiswa()
mhs.perkenalan("Arya", 12345)
print(mhs.nama)  # Arya
print(mhs.nim)  # 12345

# contoh class dengan cunstructor


class Mahasiswa:
    nim = ""
    nama = ""

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


# maka ketika membuat dan memanggil objek bisa langsung tanpa memanggil method seperti sebelumnya.
mhs = Mahasiswa("Rian", 12345)
print(mhs.nama)  # Rian
print(mhs.nim)  # 12345

# Constructor dengan validasi

# Salah satu keuntungan menggunakan constructor adalah kita bisa menambahkan validasi saat object pertama kali dibuat secara otomatis.
# Contohnya misal kita bisa cek nilai dari parameter, jika tidak valid maka kita bisa me raise error.
# Materi tentang raise error akan dibahas di materi khusus


class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        self.no = no
        self.saldo = saldo
        # validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")


budi = BankAccount("10", 1000)
# eri = BankAccount("11", -1000)  # ValueError: Saldo tidak boleh negatif

print(budi.no)  # 10
print(budi.saldo)  # 1000


# Selain method __init__ ada method seperti :
# __str__() : menentukan bagaiamana object ditampilkan sebagai string
# __eq__() : Equality, untuk membandingkan object dengan object lainnya. jadi ketika kita menggunakan operator  perbandingan  ==, maka method __eq__() yang akan dipanggil.
# __lt__(self,other) untuk < (kurang dari)
# __gt__(self,other) untuk > (lebih dari)
# __le__(self,other) untuk <= (lebih kecil sama dengan)
# __ge__(self,other) untuk >= (lebih besar sama dengan)


class Mahasiswa:
    nim = ""
    nama = ""

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __str__(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"  # returnnya harus string

    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama


mhs1 = Mahasiswa("Arya", 12345)
mhs2 = Mahasiswa("Arya", 12345)
# ketika ada operator == maka memanggil method __eq__
print(mhs1 == mhs2)  # True

# ketika dicetaknya itu dalam bentuk atau format string seperti ini
mhs = Mahasiswa("Dimas", 12345)
print(f"{mhs}")  # Nama: Dimas, NIM: 12345
# maka akan mengekseskusi method __str__()


# Decorator
# =====================================================

# Decorator adalah cara untuk "membungkus" atau memodifikasi behavior dari function atau method.
# Decorator ditandai dengan simbol @ diikuti nama decorator, dan ditulis di atas function/method.
# Python menyediakan beberapa built-in decorators untuk oop:
# @staticmethod - membuat method yang tidak perlu self atau cls.
# @classmethod - membuat method yang menerima cls dan parameter self.
# @property - membuat method yang bisa diakses seperti attribute


# @staticmethod = Independent Funcctions
# ======================================

# Static method adalah method yang berdiri sendiri secara independen
# untuk mengakses static method, kita tidak perlu menggunakan object, kita bisa langsung menggunakan classnya.
# Static method tidak bisa mengakes  class attribute ataupun instance attribute
# Untuk membuat static method, kita bisa menambahkan decorator @staticmethod pada method di class.


class Math:
    @staticmethod
    def add(a, b):
        return a + b


# bisa buat objectnya terlebih dahulu
result = Math.add(1, 2)
print(result)  # 3
# atau bisa juga tanpa membuat objectnya terlebih dahulu
print(Math.add(1, 2))  # 3


# @classmethod
# ============================

# class method adalah method yang menerima class sebagai parameter pertama (biasanya dinamakan cls), bukan instance.
# Berguna untuk factory methods atau operasi yang berhubungan dengan class itu sendiri.
# class method bisa  mengakses class attribute, namun tidak bisa mengakses instance attribute.


class BankAccount:
    no = ""
    balance = 0
    active = True

    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    @classmethod
    def disabled(
        cls, no, balance
    ):  # menerima parameter class di parameter pertama yang berfungsi untuk merubah value active dari True ke False.  class method juga bisa mengakses class attribute dari class
        account = cls(
            no, balance
        )  # ini adalah mirip dengan class BankAccount diatas yang memiliki method init yang memiliki parameter no dan balance. dimana class yang disini menjadi parameter pertama dari @classmethod
        account.active = False
        return account


bank_account1 = BankAccount("1", 1000)
# daripada merubah secara manual seperti ini
BankAccount.active = False

# mending setup di class dengan classmethod lalu panggil classmethodnya
bank_account2 = BankAccount.disabled("2", 2000)

print(
    f"Akun bank {bank_account1.no} memiliki saldo {bank_account1.balance} dan statusnya adalah {bank_account1.active}"
)
# Akun bank 1 memiliki saldo 1000 dan statusnya adalah True
print(
    f"Akun bank {bank_account2.no} memiliki saldo {bank_account2.balance} dan statusnya adalah {bank_account2.active}"
)
# Akun bank 2 memiliki saldo 2000 dan statusnya adalah False


# Kapan menggunakan masing-masing Instance method, staticmethod dan classmethod
# Instance method: ketika butuh akses ke instance (object) data
# class method: Untuk factory methods (method  untuk pembuatan instance object), atau operasi ada class level.
# staticmethod: untuk utility functions yang berhubungan dengan class tapi tidak butuh instance/class data.


# Property Methods untuk megontrol akses
# ==============================================

# Salah datu kekurangan menggunakan attribute adalah kita  tidak bisa mengontrol nilai yang dimasukkan atau didapatkan.
# Jika menggunakan function, maka hal ini bisa dilakukan, karena kita bisa memvalidasi nilai terlebih dahulu di function
# Banyak yang menggunakan method setter dan getter untuk mengontrol akses ke attribunte.


# CARA MANUAL DENGAN SETTER DAN GETTER
class Category:
    _nama = ""

    def set_nama(self, nama):
        if nama == "":
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama

    def get_nama(self):
        return self._nama


# jika kosong atau tidak diisi maka akan error
category1 = Category()
# category1.set_nama("")  # ValueError: Nama tidak boleh kosong

# jika di set namanya kemudian di get returnnya maka tidak akan error
category2 = Category()
category2.set_nama("Makanan")  # perlu memanggil method set_nama yang ada di class
print(category2.get_nama())  # Makanan

# CARA BARU DENGAN PROPERTY DECORATOR
# Property Decorator

# Di python baru, terdapat fitur bernama property decorator, dimana kita bisa menandai function sebagai setter dan getter menggunakan decorator @property
# selanjutnya, kita bisa menggunakan method tersebut layaknya menggunakan attribute


class Category:
    _nama = ""

    @property  # ----> ini sebagai getter yang akan mereturn value dari setter dibawah
    def nama(self):
        return self._nama

    @nama.setter  # -----> ini adalah setter, nama setter disesuaikan dengan nama method di getter atau property di atas
    def nama(self, nama):
        if nama == "":
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama


category1 = Category()
category1.nama = "Hamdan"  # cara panggilnya mirip seperti attribute, tapi kali ini bisa mengontrol nilai. meskipun terlihat seperti attribute tapi sebenarnya memanggil @nama.setter
print(category1.nama)  # Hamdan
