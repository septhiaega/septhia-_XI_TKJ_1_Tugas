# Nama: Spethia salfa egaputri
# Kelas: XI - Tkj 1
# Nomor Absen: 24
# Soal: Pedagang Apel

jumlah_apel = 100
persentase_penjualan = 0.10
target_sisa_apel = 20
hari = 0

while jumlah_apel > target_sisa_apel:
    jumlah_apel -= jumlah_apel * persentase_penjualan
    hari += 1

print(f"Dibutuhkan {hari} hari agar sisa apel kurang dari {target_sisa_apel} buah.")

#OUTPUT : Dibutuhkan 16 hari agar sisa apel kurang dari 20 buah.