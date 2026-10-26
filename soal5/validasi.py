"""Validasi log debit air dan perhitungan galat rata-rata terhadap acuan."""
import csv


def baca_log(nama_file):
    """Membaca log_debit.csv dan memeriksa tiap baris data.

    Pemeriksaan: jumlah kolom harus 2, debit harus angka,
    dan debit harus berada pada 5 sampai 25 (batas termasuk).

    Input : nama_file (str)
    Output: (data_valid, data_ditolak)
            data_valid   = list nilai debit (float)
            data_ditolak = list dict berisi nomor, isi, dan alasan
    """
    data_valid = []
    data_ditolak = []

    with open(nama_file, "r", newline="", encoding="utf-8-sig") as file:
        pembaca = csv.reader(file)
        next(pembaca)  # lewati judul kolom (baris 1)

        for nomor, kolom in enumerate(pembaca, start=2):
            baris = ",".join(kolom)
            alasan = []
            debit = None

            if len(kolom) != 2:
                alasan.append("jumlah kolom bukan 2")
            else:
                try:
                    debit = float(kolom[1].strip())
                except ValueError:
                    alasan.append("debit bukan angka")
                else:
                    if not 5 <= debit <= 25:
                        alasan.append("di luar rentang 5-25")

            if alasan:
                data_ditolak.append({
                    "nomor": nomor,
                    "isi": baris,
                    "alasan": alasan,
                })
            else:
                data_valid.append(debit)

    return data_valid, data_ditolak


def galat_absolut(hasil, acuan):
    """Selisih mutlak antara hasil program dan nilai acuan."""
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    """Galat relatif dalam persen. Acuan 0 memunculkan ValueError."""
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh nol")
    return abs((hasil - acuan) / acuan) * 100


ACUAN = 13.5714
TOLERANSI = 0.5  # persen

data_valid, data_ditolak = baca_log("soal5/log_debit.csv")

print("Jumlah data valid  :", len(data_valid))
print("Jumlah data ditolak:", len(data_ditolak))

for item in data_ditolak:
    print(f"Baris {item['nomor']}: {item['isi']} - {', '.join(item['alasan'])}")

if data_valid:
    rata_rata = sum(data_valid) / len(data_valid)
    print(f"Rata-rata data valid: {rata_rata:.2f}")

    ga = galat_absolut(rata_rata, ACUAN)
    gr = galat_relatif(rata_rata, ACUAN)
    print(f"Galat absolut      : {ga:.4f}")
    print(f"Galat relatif (%)  : {gr:.4f}")

    if gr <= TOLERANSI:
        print("Status             : LULUS")
    else:
        print("Status             : TIDAK LULUS")
else:
    print("Tidak ada data valid.")