# PERULANGAN (LOOP)
# =======================================
# Berguna untuk menjalankan kode yang sama berulang kali.
# Lebih efisien daripada menulis kode yang sama berkali-kali.

# FOR LOOP
# ==========================
# Berguna untuk  mengulang kode sejumlah tertentu atau mengiterasi melalui sekumpulan data
# Biasanya menggunakan function range() untuk membuat urutan angka untuk perulangannya

# mencetak angka 0-4
for i in range(5):
    print(i)

# mencetak angka 1-9
for i in range(1, 10):
    print(i)

# mencetak "python" sebanyak 5 kali
for i in range(5):
    print("python")

# menghintung mundur 5-1
for i in range(5, 0, -1):
    print(i)

# FOR LOOP DENGAN STR
# =======================
# Untuk mengiterasi setiap karakter dalam str

kata = "Linux"

for huruf in kata:
    print(huruf)


nama = input("Masukan nama:")

for karakter in nama:
    print(karakter)


# WHILE LOOP
# ================================================
# Mengulang kode selama kondisi tertentu masih True. jadi bukan berdasarkan range seperti for loop.

angka = 1

while (
    angka <= 5
):  # apakah angka 1 itu lebih besar sama dengan 5?, jika iya maka True dan lanjutkan ke baris selanjutanya
    print(angka)  # cetak angka yang lolos dari baris kode sebelumnya
    angka += 1  # penting agar setelah cetak lalu tambahkan dengan angka 1, kalau tidak maka angka tetap  sama dengan 1 dan kondisi akan selalu True karena 1 itu <= 5.
    # terus sampai kondisi while False yaitu angka > 5. kalau false maka perulangan berhenti.

# input sampai benar (kombinasi dengan if)

password = ""  # password kosong terlebih dahulu
while (
    password != "123"
):  # selama/ketika password tidak sama dengan 123 maka.....(lanjut ke baris kode selanjutnya)
    password = input("Masukan Password: ")  # password dari input
    if password != "123":  # jika input tidak sama dengan 123 maka...
        print("Password salah, coba lagi")  # cetak password salah....
        # misal inputnya salah maka False, kalau False maka looping dari awal lagi sampai True (input password yang tepat)

print(
    "Password Benar"
)  # jika True maka looping selesai dan lanjut eksekusi baris kode diluar while loop dalam hal ini adalah print("...").


# BREAK DAN CONTINUE
# ==========================================
# break berguna untuk keluar dari perulangan
# continue berguna untuk melanjutkan ke iterasi berikutnya

hari_rahasia = "senin"

while (
    True
):  # ini akan bernilai True selamanya sehingga melakukan perulangan terus menerus
    hari = input("Tebak hari:").lower()

    if hari == hari_rahasia:
        print("Benar! hari rahasianya adalah hari", hari_rahasia)
        break  # ini kunci untuk berhenti dan keluar dari loop yang sebenarnya masih True dan akan terus True.
    else:
        print("salah, coba lagi")


# continue
# mencetak hanya angka ganjil

for x in range(10):  # untuk x pada range 10
    if x % 2 == 0:  # jika x modulo 2 nya sama dengan 0 (genap)
        continue  # maka akan bertemu continue sehingga lanjut ke iterasi angka berikutnya tanpa eksekusi baris kode dibawahnya.
    print(
        x
    )  # cetak angka yang berhasil lolos dari kode diatasnya yaitu angka ganjil. kenapa angka ganjil yang lolos karena ketika angkanya genap maka perintah print tidak dieksekusi melainkan melanjutkan perulangan dengan angka berikutnya.

# cetak hanya angka genap

for i in range(10):
    if i % 2 == 1:
        continue
    else:
        print(i)


# LOOP DENGAN ELSE
# ======================================
# Fitur unik python, yang berguna jika loop selesai secara normal bisa eksekusi else (tidak dengan break)

# mencari huruf dalam kata
# for denga else

kata = input("Masukan kata:")
huruf = input("Cari huruf:")

for karakter in kata:
    if karakter == huruf:
        print(f"Huruf {huruf} ditemukan dalam kata {kata}")
        break  # akan bertemu dengan break dan mengabaikan else dibawahnya jika karakter == huruf, jika tidak maka perulangan sebenarnya berlanjut hanya saja ada else.
else:
    print(
        "huruf {h} tidak ditemukan dalam kata {k}".format(h=huruf, k=kata)
    )  # tidak bertemu dengan break sehingga perulangan berlanjut hanya saja ada else sehingga perulangan berhenti dengan mengeksekusi else.


# while dengan else
# Mencari password yang benar dengan batas percobaan

password_benar = "123p"
percobaan = 0
max_percobaan = 5

while (
    percobaan < max_percobaan
):  # selama percobaan itu kurang dari max_percobaan maka...
    password = input(
        "Masukan password:"
    )  # lakukan input password yang jadi value dari variabel password
    percobaan += 1  # tambahkan percobaan dengan angka 1 (penting agar percobaan bertambah dan membuat pengkondisian while jadi False)

    if (
        password == password_benar
    ):  # jika password yang diinput itu sama dengan password_benar
        print("login berhasil")  # maka cetak ""
        break  # dan break perulangan (menyelesaikan dan keluar dari loop sehingga kode berikutnya tidak di eksekusi)
    else:  # jika passwrod tidak sama dengan password_benar maka cetak "" dan lanjutkan perulangan sampai pengkondisian False atau bertemu dengan break pada perulangan berikutnya.
        print(f"Password salah. sisa percobaan anda adalah {max_percobaan-percobaan}")
else:  # jika percobaan > max_percobaan (False) dan tidak bertemu dengan break maka else ini dieksekusi. karena pengkondisian pada while bernilai False (karena percobaan lebih dari max_percobaan) maka perulangan berhenti.
    print("Terlalu banyak percobaan gagal, akses ditolak")


# NESTED LOOP
# ===================================
# loop di dalam loop (baik for di dalam while, while di dalam for, for di dalam for, while di dalam while, dst)


for i in range(1, 6):
    for j in range(
        1, 6
    ):  # selesaikan perulangan sebanyak range, setalah range terpenuhi maka loop naik ke loop diatasnya yaitu loop i dengan i yang baru. masuk ke loop disini lagi dan melakukan perulangan sebanyak range lagi, setalah range terpenuhi untuk kesekian kalinya maka loop naik ke loop diatasnya dengan i yang baru. terus seperti itu sampai i pada loop diatasnya mencapai range yang telah ditentukan.
        hasil = i * j
        print(i, "x", j, "=", hasil)
    print("==================")

# hasil
# i | j | hasil
# -------------------------
# 1 x 1 = 1         # i masih 1 dan j melakukan loop sebanyak range.
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# ==================
# 2 x 1 = 2         # i baru yaitu 2 setelah j mencapai loop sebanyak range pada loop sebelumnya
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# ==================
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# ==================
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# ==================
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# ==================
