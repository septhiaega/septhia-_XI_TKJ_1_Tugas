# Nama: septhia salfa egaputri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n. Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def hitung_fibonacci(n):
    if n <= 1:
        return n
    else:
        return hitung_fibonacci(n - 1) + hitung_fibonacci(n - 2)

# Meminta input dari pengguna
n_fibonacci = int(input("Masukkan nilai n untuk bilangan Fibonacci: "))

# Memanggil fungsi dan menampilkan hasilnya
print(f"Bilangan Fibonacci ke-{n_fibonacci} adalah: {hitung_fibonacci(n_fibonacci)}")


