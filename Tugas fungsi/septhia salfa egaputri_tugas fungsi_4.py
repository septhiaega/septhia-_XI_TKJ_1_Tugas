# Nama: septhia salfa egaputri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan. Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n


def hitung_jumlah_digit(bilangan):
    return sum(int(digit) for digit in str(abs(bilangan)))

# Meminta input dari pengguna
bilangan_input = int(input("Masukkan bilangan untuk menghitung jumlah digit: "))

# Memanggil fungsi dan menampilkan hasilnya
print(f"Jumlah digit dari {bilangan_input} adalah: {hitung_jumlah_digit(bilangan_input)}")


# INPUT : Masukkan bilangan untuk menghitung jumlah digit: 0836847687657648756083468756023846284365832465784567567834638768754  
# OUTPUT : Jumlah digit dari 836847687657648756083468756023846284365832465784567567834638768754 adalah: 361