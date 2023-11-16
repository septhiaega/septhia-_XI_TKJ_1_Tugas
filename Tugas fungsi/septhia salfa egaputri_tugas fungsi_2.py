# Nama: septhia salfa egaputri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan. Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1

def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

# Meminta input dari pengguna
bilangan = int(input("Masukkan bilangan untuk menghitung faktorial: "))

# Memanggil fungsi dan menampilkan hasilnya
print(f"Faktorial dari {bilangan} adalah: {hitung_faktorial(bilangan)}")




# INPUT : Masukkan bilangan untuk menghitung faktorial: 6
# OUTPUT : Faktorial dari 6 adalah: 720