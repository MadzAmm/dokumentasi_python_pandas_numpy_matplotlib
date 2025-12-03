def tebak_angka():

    import random

    angka_random = random.randint(1, 10)
    max_tebak = 3
    tebak = 0

    while tebak < max_tebak:

        tebak += 1

        tebakan = int(input("Coba tebak angka rahasianya:"))
        if tebakan > angka_random:
            print(
                f"Angka terlalu besar, percobaan tersisa tinggal {max_tebak - tebak} kali lagi"
            )
        elif tebakan < angka_random:
            print(
                f"Angka terlalu kecil, percobaan tersisa tinggal {max_tebak - tebak} kali lagi"
            )
        else:
            print("Tebakan anda benar!, Angka rahasianya adalah:", angka_random)
            break
    else:
        print("Anda telah mencapai batas maksimal tebakan")
        print("Angak rahasianya adalah angka {}".format(angka_random))

    input("Enter: Ulangi game")


def menu():

    while True:
        print("========================")
        print("GAME TEBAK ANGKA RAHASIA")
        print("========================")
        print("1. Tebak Angka")
        print("2. Keluar")

        pilih = int(input("Pilihan:"))

        if pilih == 1:
            tebak_angka()
        elif pilih == 2:
            print("Program Tebak angka rahasia selesai")
            break
        else:
            print("Error: Pilihan tidak  valid")


menu()
