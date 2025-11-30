# CONDITIONANL EXPRESSION (TERNARY OPERATOR)
# ===================================================
# memungkinkan kita untuk menulis kondisi sederhana dalam satu baris

nilai = int(input("Masukan nilai:"))

# if-elif
if nilai >= 7:
    ket = "Lulus"
else:
    ket = "Belum lulus, coba tahun depan"


# ternary (lebih singkat)

ket = "Lulus" if nilai >= 7 else "Belum lulus, coba tahun depan"

print(f"Keterangan nilai: {ket}.")
