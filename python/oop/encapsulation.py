# Encapsulation
# =========================================

# Merupakan prinsip oop yang menggabungkan data dan methods dalam satu unit (class) dan mengontrol akses ke data tersebut.
# Bayangkan encapsulation seperti kotak aman - data penting disimpan di dalam, dan hanya bisa diakses melalui cara yang terkontrol.

# Mengapa encapsulation itu penting?

# Data protection - mencegah data diubah sembarangan
# Data validation - memastikan data selalu dalam kondisi valid
# Interface Control - mudah mengubah internal implementation
# Maintenance - mudah mengubah internal implementation
# Security - menyembunyikan detail sensitive.

# Access Modifiers dalam python

# Python menggunakan naming conventions untuk menandai level akses:
# 1. public attributes (default): bisa diakses dimana saja-tidak ada protection,
# 2. protected attributes (single underscore "_") : convention bahwa attribut ini untuk internal use class dan subclass,
# 3. privat attributes (double undersccore "__"): Python akan melakukan name mangling (pengubahan nama attribute dari luar) sehingga attribute sulit untuk diakses  dari luar.


class BankAccount:
    no = ""  # -------> public attribute (default)
    _balance = 0  # protected attribute (single underscore)
    __active = True  # private attribute (double underscore)

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
# BankAccount.active = False

# mending setup di class dengan classmethod lalu panggil classmethodnya
bank_account2 = BankAccount.disabled("2", 2000)

print(
    f"Akun bank {bank_account1.no} memiliki saldo {bank_account1._balance} dan statusnya adalah {bank_account1.__active}"
)
# error karena tidak bisa mengakses attribut active, kenapa karena active adalah private attribute (yang bisa akses hanya yang ada di dalam class dan subclass, tidak bisa diluar class seperti mencoba mencetak ini). sedangkan untuk attribute balance masih bisa diakses tapi secara convensi tnda "_" ini berarti tidak direkomendasikan untuk bisa diakses di luar (uji coba, silahkan hapus {bank_account1.__active}, maka akan tidak error dan mencetak hasilnya. )
print(
    f"Akun bank {bank_account2.no} memiliki saldo {bank_account2._balance} dan statusnya adalah {bank_account2.__active}"
)
# sama error karena mengakses private attribute


class BankAccount:
    __nama = ""
    __balance = 0

    def __init__(self, nama):
        self.__nama = nama

    # bisa pakai decorator property
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # bisa juga menggunakan getter dan sette manual
    # def get_balance(self):
    #     return self.__balance

    # def set_balance(self, balance):
    #     self.__balance = balance

    def cash_out(self, amount):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount


# dengan decorator property
mu_account = BankAccount("Muhammad")
mu_account.balance = 1000
print(mu_account.balance)  # 1000
mu_account.cash_out(500)
print(mu_account.balance)  # 500

# dengan setter dan getter manual
# mad_account = BankAccount("Madina")
# mad_account.set_balance(2000)
# print(mad_account.get_balance())  # 2000
# mad_account.cash_out(750)
# print(mad_account.get_balance())  # 1250
