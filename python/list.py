# LIST (DAFTAR)
# =====================================
# Kumpulan data yang bisa menyimpan banyak nilai dalam satu variabel.
# List ditulis dengan menggunakan kurung siku []

# List kosong

list = []

# List dengan angka

angka = [1, 2, 3, 4, 5]

#  List dengan str

nama = ["Rey", "Awah", "Amah"]

# List campuran

mix = ["Rey", 20, "Amah", 27]

print(list, angka, nama, mix)

# [] [1, 2, 3, 4, 5] ['Rey', 'Awah', 'Amah'] ['Rey', 20, 'Amah', 27]


# MANIPULASI LIST
# ===============================================
# Akses list sama serperti str yang menggunakan index
# Ubah elemen lisst bisa menggunakan index dan ubah seperti mengubah variabel.
# append(data), menambah elemen ke list di bagian akhir
# insert(index,data), menambah data pada index yang ditentukan
# remove(data), menghapus elemen dari list
# del list[index], sama seperti remove() hanya saja pakai index. del hari[0].
# pop(), menghapus elemen terakhir
# len(list), menghitung panjang list
# list bisa digabungkan dengan list lain menggunakan operator +.
# list bisa di iterasi menggunakan for loop  sama seperti str


# Mengakses elemen dalam list

data = ["Sai", 20, "Pisang", "Bandung", 12]
print(data[0])  # Sai
print(data[1])  # 20
print(data[2])  # Pisang
print(data[3])  # Bandung
print(data[-1])  # 12
print(data[:])  # ['Sai', 20, 'Pisang', 'Bandung', 12]
print(data[2:])  # ['Pisang', 'Bandung', 12]

# Mengubah elemen

hari = ["Senin", "Selasa", "Rabu", "Kamis"]
print(hari)  # ['Senin', 'Selasa', 'Rabu', 'Kamis']

hari[0] = "Minggu"
print(hari)  # ['Minggu', 'Selasa', 'Rabu', 'Kamis']

hari.append("Jumat")
print(hari)  # ['Minggu', 'Selasa', 'Rabu', 'Kamis', 'Jumat']

hari.insert(0, "Senin")
print(hari)  # ['Senin', 'Minggu', 'Selasa', 'Rabu', 'Kamis', 'Jumat']

print(hari.pop())  # Jumat

print(hari)  # ['Senin', 'Minggu', 'Selasa', 'Rabu', 'Kamis']

hari.remove("Kamis")
print(hari)  # ['Senin', 'Minggu', 'Selasa', 'Rabu']

del hari[1]
print(hari)  # ['Senin', 'Selasa', 'Rabu']

print(len(hari))  # 3


data_satu = [1, 2, 3, 4, 5]
data_dua = [6, 7, 8, 9, 0]
gabung = data_satu + data_dua
print(gabung)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in hari:
    print(i)
# Senin
# Selasa
# Rabu

#  atau
for i in range(0, len(hari)):
    print(hari[i])
# hasilnya sama

# Senin
# Selasa
# Rabu

cek_hari = input("Masukan hari:")
if cek_hari in hari:
    print(f"hari {cek_hari} ada di list")
else:
    print("hari {} tidak ada di dalam list".format(cek_hari))
