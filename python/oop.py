class RekneningBank:

    def __init__(self, tabungan):
        self.tabungan = tabungan

    def cek_saldo(self):
        print("Saldo anda sebesar = Rp. {}".format(self.tabungan))

    def menabung(self):
        tambah = int(input("Silahkan masukan nominal yang akan ditabungkan: "))
        self.tabungan += tambah

    def tarik(self):
        kurang = int(input("Silahkan masukan nominal yang akan ditarik:"))
        if self.tabungan < kurang:
            print(
                "Maaf saldo anda tidak mencukupi \nSaldo anda saat ini adalah sebesar = Rp {}".format(
                    self.tabungan
                )
            )
        else:
            self.tabungan -= kurang


tabunganku = RekneningBank(100000)
tabunganku.cek_saldo()
tabunganku.menabung()
tabunganku.cek_saldo()
tabunganku.tarik()
tabunganku.cek_saldo()
tabunganku.tarik()
tabunganku.cek_saldo()
