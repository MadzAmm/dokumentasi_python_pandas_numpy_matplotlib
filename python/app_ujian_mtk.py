def buka_soal():
    soal_jawab = []
    with open("../data/bank_soal.txt", "r") as file:
        for line in file:
            soal_jawab.append(line.strip())
            # print(line.strip())
    return soal_jawab


def buat_soal():
    soal_jawab = buka_soal()
    import random

    random.shuffle(soal_jawab)  # acak soal yang  mmuncul
    soal_ujian = []
    for i in range(10):
        soal = soal_jawab[i]  # "pertanyaan"| "Jawaban_benar, salah, salah, salah"
        data = soal.split("|")  # ["pertanyaan", "Jawaban_benar, salah, salah, salah"]
        pertanyaan = data[0]  # "pertanyaan"
        opsi_jawaban = data[1]  # "Jawaban_benar, salah, salah, salah"
        jawaban = opsi_jawaban.split(
            ","
        )  # ["Jawaban_benar", "salah", "salah", "salah"]
        jawaban_benar = jawaban[0]  # jawaban benar
        random.shuffle(jawaban)  # acak jawabah

        soal_ujian.append(
            {
                "pertanyaan": pertanyaan,
                "jawaban": jawaban,
                "jawaban_benar": jawaban_benar,
            }
        )

    return soal_ujian


def app_ujian():
    ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    jawaban_benar = 0
    jawaban_salah = 0

    for i in range(len(ujian)):
        soal = ujian[i]
        print("===========================================")
        print("Pertanyaan", i + 1, ":", soal["pertanyaan"])
        print("jawaban:")

        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(f"{opsi[j]}. {jawaban}")

        jawaban_user = input("Pilih Jawaban (A/B/C/D):").upper()
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban benar")
            jawaban_benar += 1
        else:
            print(f"Jawaban salah, yang benar adalah {soal["jawaban_benar"]}")
            jawaban_salah += 1

    print("=============================")
    print("======== HASIL UJIAN ========")
    print("=============================")
    print("Total jawaban benar:", jawaban_benar)
    print("Total jawaban salah", jawaban_salah)
    print(f"Hasil ujian: {jawaban_benar/ (jawaban_benar + jawaban_salah) * 100}%")


app_ujian()
