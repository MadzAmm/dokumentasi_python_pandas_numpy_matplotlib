# DICTIONARY
# ===================================
# Di struktur data seperti list dan tuple, elemen atau datanya bisa diakses dengan index. sedangkan dalam dictionary, data bisaa diakses dengan key.
# Berguna untuk menyimpan data dalam pasangan key-value (kunci-nilai).
# Dictionary ditulis dengan kurung kurawal {}
# Perlu menentukan key dan value
# Key bisa tipe data str, int, float, bool, namun biasanya pakau str
# Untuk mengakses dan mengubah value, bisa gunakan key dengan kurung kotak [key] seperti di list
# del dict[key] untuk menghapus value
# len(dict) untuk mengetahui panjang dict
# Bisa diiterasi


siswa = {"nama": "Yuri", "umur": 26, "kelas": "7b"}

print(siswa)  # {'nama': 'Yuri', 'umur': 26, 'kelas': '7b'}

print(siswa["nama"])  # Yuri
print(siswa["umur"])  # 26
print(siswa["kelas"])  # 7b

# Ubah nilai
siswa["umur"] = 20
print(siswa)  # {'nama': 'Yuri', 'umur': 20, 'kelas': '7b'}

# Menghapus key-value
del siswa["kelas"]
print(siswa)  # {'nama': 'Yuri', 'umur': 20}

# Iterasi keys
for key in siswa:
    print(
        key, ":", siswa[key]
    )  # ! untuk mendapatkan valuenya maka harus memakai siswa[key]
# nama : Yuri
# umur : 20

# Iterasi key-value pairs
for (
    key,
    value,
) in siswa.items():  # gunakan .items() supaya langsung mendapatkan key dan valuenya.
    print(key, "=", value)

# nama = Yuri
# umur = 20
