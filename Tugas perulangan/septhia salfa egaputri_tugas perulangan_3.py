# Nama: septhia salfa egaputri
# Kelas: XI - Tkj 1
# Nomor Absen: 24
# Soal: Investasi

nilai_investasi_awal = 10000
persentase_pertumbuhan = 0.06
target_investasi = 20000
tahun = 0

while nilai_investasi_awal <= target_investasi:
    nilai_investasi_awal += nilai_investasi_awal * persentase_pertumbuhan
    tahun += 1

print(f"Dibutuhkan {tahun} tahun agar nilai investasi melebihi {target_investasi} dollar.")



#OUTPUT : Dibutuhkan 12 tahun agar nilai investasi melebihi 20000 dollar.