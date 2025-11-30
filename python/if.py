# PERNYATAAN IF
# =====================================
# Berguna untuk menjalankan kode hanya jika kondisi tertentu bernilai True
# Setelah if harus ada : (titik dua)
# Kode yang akan dijalankan jika kondisi True harus diindentasi (diberi spasi di awal).


nilai = int(input("Masukan nilai 1-10: "))

if nilai < 1 or nilai > 10:
    print(
        "Salah input nilai"
    )  # masih akan lanjut ke kode selanjutnya meskipun logika ini telah dieksekusi dan True karena mungkin ada logika yang True pada kode selanjutnya, sehingga kalau pakai if terus menerus dan selama kondisi itu True maka akan dieksekusi.

if nilai > 8:
    print("Sangat baik")

if nilai == 8:
    print("Baik")

if nilai <= 6:
    print("Kurang")

if nilai == 7:
    print("Cukup")


# PERNYATAAN IF-ELSE
# ======================================
# Digunakan ketika ingin menjalankan kode yang berbeda untuk kondisi True dan False

nilai = int(input("Masukan nilai:"))

if nilai >= 6:
    print("Lulus")
else:
    print("Belum lulus")


# PERNYATAAN ELIF
# =====================================
# elif (else if) berguna untuk mengecek beberapa kondisi "secara berurutan" (sulosi dari masalah penggunaan if berulang yang tidak menghentikan eksekusi kode ketika sudah ada yang bernilai True)

nilai = int(input("Masukan nilai 1-10: "))

if nilai < 1 or nilai > 10:
    print(
        "Salah input nilai"
    )  # jika True pada baris kode ini maka kode akan berhenti dan selesai tidak lanjut ke kode selanjutnya seperti kode diatas yang tanpa elif (hanya if if if dan if).

elif nilai > 8:
    print("Sangat baik")

elif nilai == 8:
    print("Baik")

elif nilai <= 6:
    print("Kurang")

else:
    print("Cukup")


# KONDISI DENGAN OPERATOR LOGIKA
# ======================================================
# Karena kondisi harus bernilai boolean maka bisa menggunakan operator logika seperti and, or, not.

usia = int(input("Masukan usia:"))
ktp = input("Punya KTP? (y/n):")


if usia >= 18 and ktp == "y":
    print("Boleh nyoblos")
else:
    print("Belum bisa nyoblos")

# and = harus True pada kondisi usia >= 18 dan ktp == y untuk bisa eksekusi "boleh nyoblos", kalau salah satunya False maka masuk ke else. beda dengan or yang hanya mensyaratkan satu True saja.


# NESTED IF (if Bersarang)
# ===================================
# Bisa menempatkan if di dalam if


username = input("Username:")
password = input("Password:")

if username == "mad":
    if password == "123":
        print("Login Berhasil")
        print("Selamat datang {}".format(username))
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan")
