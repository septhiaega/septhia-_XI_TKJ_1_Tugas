# Nama: septhia salfa egaputri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu. Rumus: Bilangan^Eksponen

def hitung_pangkat(bilangan, eksponen):
    return bilangan ** eksponen

# Meminta input dari pengguna
bilangan_input = float(input("Masukkan bilangan: "))
eksponen_input = int(input("Masukkan eksponen: "))

# Memanggil fungsi dan menampilkan hasilnya
print(f"Hasil dari {bilangan_input}^{eksponen_input} adalah: {hitung_pangkat(bilangan_input, eksponen_input)}")