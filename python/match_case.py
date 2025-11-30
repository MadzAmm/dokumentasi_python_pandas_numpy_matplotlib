#  PERNYATAAN MATCH CASE
# ==============================================
# fitur alternatif yang lebih bersih untuk elif yang banyak


hari = input("Masukan hari:").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari Kerja")
    case "sabtu" | "minggu":
        print("Hari Libur")
    case _:
        print("bukan hari")


# kalau pakai if-elif

hari = input("Masukan hari:").lower()

if hari == "senin" or "selasa" or "rabu" or "kamis" or "jumat":
    print("Hari Kerja")
elif hari == "sabtu" or "minggu":
    print("Hari Libur")
else:
    print("Bukan hari")
