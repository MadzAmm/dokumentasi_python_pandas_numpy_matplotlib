# FILE I/O (Input / Output)
# =======================================
# File I/O adalah kemampuan program untuk mambaca data dari file dan menulis data ke file
# Dengan file i/o kita bisa :
# Menyimpan data secara permanen
# Membaca data yang sudah tersimpan
# Membuat laporan dalam bentuk file
# Memproses data dari file eksternal
# Backup dan restore data aplikasi

# MEMBUKA DAN MENUTUP FILE
# ============================
# Gunakan function open(file,mode) untuk membuka file
# Setelah membuka file maka jangan lupa untuk menutupnya dengan menggunakan function close() pada variabelnya
# Saat membuka file, kita harus tentukan mode nya.

# Mode
# r =read (baca) : Membaca file yang sudah ada.
# w =Write (tulis) : Menulis file baru  atau menimpa file lama
# a =Append (tambah): Menambah data di akhir  file
# x =Create (buat): Membuat file baru, error jika file sudah ada, tida menimpa seperti w (write)

# Menulis ke file
# Bisa gunakan function write(str)
# Perlu diperhatikan, yang sudah di close() tidak bisa ditulis lagi.


# file = open("nilai_siswa.csv", "w")

# while True:
#     nama = input("Nama siswa (enter untuk selesai):")
#     if nama == "":
#         break

#     nilai = int(input("Nilai Siswa:"))

#     file.write(f"{nama}, {nilai}, \n")
#     print("Data {} berhasil disimpan".format(nama))

# file.close()
# print("Program Selesai")


# # MEMBACA DARI  FILE
# # Bisa gunakan function read(), function ini akan mengembalikan seluruh isi file
# # Kalau hanya ingin membaca file per baris, maka kita harus menggunakan iterasi for untuk membaca per baris

# file = open("nilai_siswa.csv", "r")

# for line in file:
#     data = line.strip().split(
#         ","
#     )  # akan jadi list sehingga data di dalam file  bisa diakses  dengan index, strip (hilangkan jika sisi-sisinya ada spasi), split (dipotong/dipecah menggunakan koma)
#     print(data[0], ":", data[1])  # tampilan cetak -----> hadi : 7

# file.close()
# print("SELESAI")


# # With STATEMENT *direkomendasikan
# # =======================================
# # Saat membaca/menulis file, kita harus berhati-hati karena jika terjadi error, dan kita lupa melakukan close() maka aplikasi kita bisa terjadi Memory Leak (kondisi dimana informasi file masih di memori aplikasi, padahal kita sudah tidak menggunakan file tersebut)
# # Hal ini sangat berbahaya karena penggunaan memori aplikasi kita akan semakin besar tanpa kita sadari
# # with statement memastikan file otomatis tertutup, bahkan jika terjadi error
# # Dengan menggunakan with statement. kita tidak perlu khawatir lupa close() file.

# with open("nilai_siswa.csv", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         print(data[0], ":", data[1])

# print("SELESAI")


# ERROR HNADLING untuk file
# ================================================
# Walaupun selalu menutup file menggunakan with statement, tapi jika terjadi error maka aplikasi tetap akan berhenti
# Oleh karena itu, kiita tetap perlu menggunakan try-except
# Misal, bagaimana jika file yang kita baca itu tidak ada, maka akan terjadi eror FileNotFoundError.

# with open(
#     "nilai_siswa2.csv", "r"
# ) as file:  # taruhlah file yang memang belum ada untuk membuktikan adanya error filenotound...
#     for line in file:
#         data = line.strip().split(",")
#         print(data[0], ":", data[1])

# print("SELESAI")
# -----------------> FileNotFoundError: [Errno 2] No such file or directory: 'nilai_siswa2.csv'

# maka solusinya tambahkan try-except agar tidak crash
try:
    with open("nilai_siswa2.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ",", data[1])
except FileNotFoundError:
    print("File tidak ditemukan")
print("SELESAI")
