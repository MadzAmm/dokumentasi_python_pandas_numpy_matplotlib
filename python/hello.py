# print("hello pyhton")
# print("hello world")

# cek angka genap atau ganjil
# angka = int(input("Masukan angka favorit anda:"))

# if angka % 2 == 0:
#     print("Angka yang anda masukan yaitu angka {} adalah angka genap".format(angka))
# else:
#     print(f"Angka yang anda masukan yaitu angka {angka} adalah angka ganjil")


# tebak tingkat pendidikan dari umur dengan ternary
tebak = 0
max = 5

while tebak < max:
    umur = int(input("Masukan umur:"))
    tebak += 1

    if umur >= 6 and umur <= 12:
        print("Karena umur kamu {} tahun, maka kamu adalah siswa SD".format(umur))
        print(f"Sisa tebak tinggal {max-tebak}")
    elif umur >= 13 and umur <= 15:
        print("Karena umur kamu {} tahun, maka kamu adalah siswa SMP".format(umur))
        print(f"Sisa tebak tinggal {max-tebak}")
    elif umur >= 16 and umur <= 18:
        print(f"Karena umur kamu {umur} tahun, maka kamu adalah siswa SMA")
        print(f"Sisa tebak tinggal {max-tebak}")
    elif umur >= 0 and umur <= 5:
        print(f"Karena umur kamu {umur} tahun, maka kamu belum masuk sekolah")
        print(f"Sisa tebak tinggal {max-tebak}")
    else:
        print(
            "Karena umur kamu {u} tahun, maka kamu adalah seorang Mahasiswa".format(
                u=umur
            )
        )
        print(f"Sisa tebak tinggal {max-tebak}")
    break
else:
    ("Sisa tebak {}. Sesi selesai".format(max - tebak))
