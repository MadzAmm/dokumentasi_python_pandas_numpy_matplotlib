# TUPLE
# ===============================
# Mirip denga list bisa diakses dengan index tapi tidak bisa diubah.
# Tuple bisa ditulis dengan kurung biasa ()
# Bisa mengetahui  panjang tuple dengan method len(tuple)
# Bisa diiterasi dengan loop


tanggal_lahir = (17, 8, 1945)
print(tanggal_lahir[0])  # 17
print(tanggal_lahir[1])  # 8
print(tanggal_lahir[-1])  # 1945
print(tanggal_lahir[:])  # (17, 8, 1945)

for i in tanggal_lahir:
    print(i)
# 17
# 8
# 1945

for i in range(0, len(tanggal_lahir)):
    print(tanggal_lahir[i])

# 17
# 8
# 1945
