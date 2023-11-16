# Nama: Septhia salfa egaoutri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal: Pelari

jarak_awal = 5
persentase_kenaikan = 0.10
target_jarak = 10
minggu = 0

while jarak_awal <= target_jarak:
    jarak_awal += jarak_awal * persentase_kenaikan
    minggu += 1

print(f"Dibutuhkan {minggu} minggu agar pelari dapat berlari lebih dari {target_jarak} kilometer.")


#OUTPUT : Dibutuhkan 8 minggu agar pelari dapat berlari lebih dari 10 kilometer.