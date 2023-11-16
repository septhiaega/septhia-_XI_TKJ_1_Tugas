# Nama: septhia salfa egaputri
# Kelas: XI - Tkj 1
# No. abs : 24
# Soal: Peternakan Ayam

jumlah_ayam = 100
persentase_pertumbuhan = 0.05
target_ayam = 200
bulan = 0

while jumlah_ayam <= target_ayam:
    jumlah_ayam += jumlah_ayam * persentase_pertumbuhan
    bulan += 1

print(f"Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_ayam} ekor.")



#OUTPUT : Dibutuhkan 15 bulan agar jumlah ayam melebihi 200 ekor.