# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

def hitung_diskon(total_belanja, status_anggota):
    # Inisialisasi nilai diskon
    diskon = 0

    # Cek status anggota
    if status_anggota.lower() == "premium":
        # Jika anggota premium dan total belanjaan lebih dari 500.000, berikan diskon 15%
        if total_belanja > 500000:
            diskon = 0.15
        # Jika anggota premium dan total belanjaan tidak lebih dari 500.000, berikan diskon 10%
        else:
            diskon = 0.10
    elif status_anggota.lower() == "biasa":
        # Jika anggota biasa dan total belanjaan lebih dari 300.000, berikan diskon 7%
        if total_belanja > 300000:
            diskon = 0.07
        # Jika anggota biasa dan total belanjaan tidak lebih dari 300.000, diskon tetap 0%
        else:
            diskon = 0

    # Hitung nilai diskon
    nilai_diskon = total_belanja * diskon

    # Hitung total pembayaran setelah diskon
    total_pembayaran = total_belanja - nilai_diskon

    # Tampilkan hasil
    print(f"Total Belanja: Rp {total_belanja:,}")
    print(f"Diskon: Rp {nilai_diskon:,}")
    print(f"Total Pembayaran Setelah Diskon: Rp {total_pembayaran:,}")

# Contoh penggunaan program
total_belanja_pelanggan = float(input("Masukkan total belanja pelanggan: "))
status_anggota_pelanggan = input("Masukkan status anggota (biasa/premium): ")

hitung_diskon(total_belanja_pelanggan, status_anggota_pelanggan)





#INPUT : 
#   Masukkan total belanja pelanggan: 600000
#   Masukkan status anggota (biasa/premium): premium
#OUTPUT:
#   Total Belanja: Rp 600,000.0
#   Diskon: Rp 90,000.0
#   Total Pembayaran Setelah Diskon: Rp 510,000.0

# INPUT : 
#   Masukkan total belanja pelanggan: 600000
#   Masukkan status anggota (biasa/premium): biasa
#OUTPUT :
#   Total Belanja: Rp 600,000.0
#   Diskon: Rp 42,000.0
#   Total Pembayaran Setelah Diskon: Rp 558,000.0