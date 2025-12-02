def penjumlahan():
    print("===== Program penjumlahan =====")
    try:
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua:"))
        hasil = a + b
        print(
            "====> hasil dari penjumlahan angka {} dan {} adalah {}".format(a, b, hasil)
        )
        print("===== Program penjumlahan Selesai =====")

    except ValueError:
        print("Tolong input dengan angka bukan str karakter")
    finally:  # error ataupun tidak error tetap akan muncul
        lanjut = input(
            "Enter = lanjut ke menu, 5 = berhenti/keluar dari program: "
        )  # tentukan pilihan untuk lanjut dan berhenti
        if (
            lanjut == "5"
        ):  # logika agar menghasilan nilai False (berfungsi untuk sinyal menghentikan program)
            return False  # kembalikan value false pada fungsi ini jika lanjut == "5", memberi sinyal kepada fungsi menu bahwa program harus berhenti.
        return True  # kembalikan value True pada fungsi ini jika lanjut tidak sama dengan "5"


def pengurangan():
    print("===== Program pengurangan =====")
    try:
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua:"))
        hasil = a - b
        print(
            "====> hasil dari pengurangan angka {} dan {} adalah {}".format(a, b, hasil)
        )
        print("===== Program pengurangan Selesai =====")

    except ValueError:
        print("Tolong input dengan angka bukan str karakter")
    finally:
        lanjut = input("Enter = lanjut ke menu, 5 = berhenti/keluar dari program: ")
        if lanjut == "5":
            return False
        return True


def perkalian():
    print("===== Program perkalian =====")
    try:
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua:"))
        hasil = a * b
        print(
            "=====> hasil dari perkalian angka {} dan {} adalah {}".format(a, b, hasil)
        )
        print("===== Program perkalian Selesai =====")
    except ValueError:
        print("Tolong input dengan angka bukan str karakter")
    finally:
        lanjut = input("Enter = lanjut ke menu, 5 = berhenti/keluar dari program: ")
        if lanjut == "5":
            return False  # Mengembalikan False untuk sinyal berhenti
        return True  # Mengembalikan True untuk sinyal lanjut


def pembagian():
    print("===== Program pemabagian =====")
    try:
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua:"))
        hasil = a / b
        print(
            "=====> hasil dari pembagian angka {} dan {} adalah {}".format(a, b, hasil)
        )
        print("===== Program pemabagian Selesai =====")

    except ZeroDivisionError:
        print("Tidak bisa dibagi nol")
    except ValueError:
        print("Tolong input dengan angka bukan str karakter")
    finally:
        lanjut = input("Enter = lanjut ke menu, 5 = berhenti/keluar dari program: ")
        if lanjut == "5":
            return False
        return True


# Fungsi menu() harus menangkap nilai kembalian dari fungsi operasi
def menu():
    while True:
        print("===== Kalkulator Sederhana =====")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih nomor:"))

            # Variabel untuk menampung sinyal apakah harus berhenti
            lanjut_program = True

            if pilih == 1:
                lanjut_program = (
                    penjumlahan()
                )  # ingat! fungsi operasi mengembalikan nilai bool. True akan lanjut, kalau False maka akan eksekusi kode if not lanjut_program (kode berada di bawah)
            elif pilih == 2:
                lanjut_program = pengurangan()
            elif pilih == 3:
                lanjut_program = perkalian()
            elif pilih == 4:
                lanjut_program = pembagian()
            elif pilih < 1 or pilih > 5:
                print("Opsi {} tidak ada dalam daftar".format(pilih))
                input("Enter untuk memilih kembali operasi kalkulator")
                continue
            else:
                print("===== TERIMA KASIH SUDAH MENCOBA =====")
                break

            # Cek sinyal dari fungsi operasi
            if not lanjut_program:  # jika tidak True (False) maka : ....
                print("===== TERIMA KASIH SUDAH MENCOBA =====")
                break

        except ValueError:
            print("Tolong masukan angka sesuai opsi operasi yang dipilih")
            input("Enter untuk memilih kembali operasi kalkulator")


menu()
