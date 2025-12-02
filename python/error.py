# ERROR
# =====================================
# Error adalah kesalahan yang terjadi saat program berjalan
# Ketika error terjadi, program akan berhenti dan menampilkan pesan error


# SyntaxError (Kesalahan syntax)
# misal lupa ditutup
# print("Hai Python"  # ---------> SyntaxError: '(' was never closed

# NameError (Variabel tidak ditemukan)
# Variabel 'nama' belum didefinisikan
# print(nama)  # -------> NameError: name 'nama' is not defined

# TypeError (Kesalahan tipe data)
# Tidak bisa menambah str dengan angka
# print("10" + 10)  # -----> TypeError: can only concatenate str (not "int") to str


# ValueError (Nilai tidak valid)
# Tidak bisa convert "abc" ke integer
# angka = int("abc") # ------> ValueError: invalid literal for int() with base 10: 'abc'


# IndexError  (Index tidak valid / tidak ditemukan)
# list = [1, 2, 3]
# print(list[5])  # -----> IndexError: list index out of range


# KeyError (Key tidak valid / tidak ditemukan)
# dict = {"nama": "Wayu"}
# print(dict["kota"])  # -----> KeyError: 'kota'


# ZeroDivisionError (Pembagian dengan nol)
# print(10 / 0)  # -----> ZeroDivisionError: division by zero


# PENANGANAN ERROR
# =========================================
# Memungkinkan program untuk menangani erro dengan baik tanpa berhenti secara tiba-tiba

# Try-Except
# Berguna untuk menangani error yang mungkin terjadi

# Program pembagian pertama akan langung berhenti jika terjadi error, entah karena input str  atau dibagi dengan 0

# print("===== PEMBAGIAN PERTAMA =====")


# angka1 = int(input("Masukan angka pertama:"))
# angka2 = int(input("Masukan angka kedua:"))
# hasil = angka1 / angka2
# print(
#     "Hasil pembagian antara {} dengan angka {} adalah {}".format(
#         angka1, angka2, int(hasil)
#     )
# )
# print("Terjadi kesalahan pada input pengguna")

# print("===== BERAKHIR =====")

# ==============================================================
# Berbeda jika kita menggunakan try-except
print("===== PEMBAGIAN KEDUA =====")

try:
    angka1 = int(input("Masukan angka pertama:"))
    angka2 = int(input("Masukan angka kedua:"))
    hasil = angka1 / angka2
    print(
        "Hasil pembagian antara {} dengan angka {} adalah {}".format(
            angka1, angka2, hasil
        )
    )
except:
    print("Terjadi kesalahan pada input pengguna")

print(
    "===== BERAKHIR ====="
)  # <------ kode ini  akan tereksekusi jika dari awal terjadi error entah input dengan str atau dibagi dengan 0


# MENANGANI ERROR SPESIFIK
# =====================================================
# Kita  bisa melakukan tindakkan yang berbeda untuk jenis error yang berbeda.
# Bisa menyebutkan tipe error setelah kata kunci except, sehingga ketika terjadi error jenis  tersebut, maka bagian except tersebut yang akan dieksekusi.
# Artinya kita bisa menambahkan lebih dari satu except.

try:
    a = float(input("Masukan angka pertama:"))
    b = float(input("Masukan angka kedua:"))
    hasil = a / b
    print("Hasil pembagian antara angka {} dan angka {} adalah {}".format(a, b, hasil))

except ValueError:
    print("Tolong masukan angka jangan karakter str")

except ZeroDivisionError:
    print("Jangan jadikan angka 0 sebagai pembagi")

except:
    print("Terjadi kesalahan lain")


# Try-Except-Else
# ============================================================
# Bisa gunakan else sepert if dan for
# Bagian else dijalankan ketika tidak ada error pada try except
# Jika terjadi error maka bagian error tidak akan dieksekusi

try:
    angka = int(input("Masukan angka yang ingin dicek:"))
except ValueError:
    print("Tolong input dengan angka jangan karakter str")
else:
    print("Angka yang anda masukan:", angka)
    if angka > 0:
        print("positif")
    elif angka < 0:
        print("negatif")
    else:
        print("Nol")


# Try Except Finally
# ==============================================
# else di try-except hanya aakan dieksekusi ketika tidak ada error
# Finally  berguna jika kita ingin melakukan sesuatu, baik itu jika terjadi error ataupun tidak
# artinya finally selalu dijalankan baik ada error atau tidak

try:
    angka = int(input("Masukan angka:"))
    print("Angka anda:", angka)
except ValueError:
    print("Input anda bukan angka")
finally:
    print("Program selesai dijalankan")
