# SET (HIMPUNAN)
# ===================================
# Set, kumpula data yang tidak berurutan dan tidak memiliki elemen duplikat
# Karena tidak berurutan dan tidak duplikat maka tidak bisa diakses dengan menggunakan index
# Set ditulis dengan kurung kurawal {} atau fungsi set()
# add(value), untuk menambahkan data ke set
# remove(value), untuk menghapus data di set
# untuk akses data di set biasannya menggunakan for loop

hari = {"Senin", "Selasa", "Rabu"}
print(
    hari
)  # {'Selasa', 'Rabu', 'Senin'} tidak urut, begitu juga di print selanjutnya akan berubah lagi urutannya.

# Tambah elemen
hari.add("Kamis")
print(hari)  # {'Kamis', 'Senin', 'Rabu', 'Selasa'}
hari.add("Kamis")
print(
    hari
)  # {'Kamis', 'Senin', 'Rabu', 'Selasa'} hasilnya sama karena value yang di add sudah ada dan sama. inilah set.

# Hapus elemen
hari.remove("Kamis")
print(hari)  # {'Rabu', 'Selasa', 'Senin'} urutan berubah

# Menampilkan elemen
for e in hari:
    print(e)
# hasil cetak dengan urutan baru, cetak lagi urutannya beda lagi
# Selasa
# Rabu
# Senin
