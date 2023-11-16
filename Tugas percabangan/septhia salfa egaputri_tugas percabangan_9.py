# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman. Soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut: • Peminjaman 7 hari atau kurang: "Peminjaman Pendek" • Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah" • Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

def tentukan_jenis_pinjaman(durasi_peminjaman):
    # Tentukan jenis pinjaman berdasarkan durasi peminjaman
    if durasi_peminjaman <= 7:
        jenis_pinjaman = "Peminjaman Pendek"
    elif 7 < durasi_peminjaman <= 30:
        jenis_pinjaman = "Peminjaman Menengah"
    else:
        jenis_pinjaman = "Peminjaman Panjang"

    return jenis_pinjaman

# Meminta input durasi peminjaman buku dari pengguna
durasi_peminjaman_buku = int(input("Masukkan durasi peminjaman buku dalam hari: "))

# Memanggil fungsi untuk menentukan jenis pinjaman
jenis_pinjaman_buku = tentukan_jenis_pinjaman(durasi_peminjaman_buku)

# Menampilkan hasil jenis pinjaman
print(f"Jenis Pinjaman: {jenis_pinjaman_buku}")




#INPUT : Masukkan durasi peminjaman buku dalam hari: 5
#OUTPUT : Jenis Pinjaman: Peminjaman Pendek

#INPUT : Masukkan durasi peminjaman buku dalam hari: 20
#OUTPUT : Jenis Pinjaman: Peminjaman Menengah

#INPUT : Masukkan durasi peminjaman buku dalam hari: 40
#OUTPUT : Jenis Pinjaman: Peminjaman Panjang