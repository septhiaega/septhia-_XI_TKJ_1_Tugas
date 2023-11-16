# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon berdasarkan aturan berikut: Jika total belanjaan lebih dari 500.000, berikan diskon 10%. Jika total belanjaan antara 300.000 dan 500.000, berikan diskon 5%. Jika total belanjaan kurang dari 300.000, tidak ada diskon.

def hitung_diskon(total_belanja):
    # Jika total belanjaan lebih dari 500.000, berikan diskon 10%
    if total_belanja > 500000:
        diskon = 0.1
    # Jika total belanjaan antara 300.000 dan 500.000, berikan diskon 5%
    elif 300000 <= total_belanja <= 500000:
        diskon = 0.05
    # Jika total belanjaan kurang dari 300.000, tidak ada diskon
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

# Contoh penggunaan
total_belanja_pelanggan = float(input("Masukkan total belanja pelanggan: "))
hitung_diskon(total_belanja_pelanggan)




#INPUT = Masukkan total belanja pelanggan: 600000
#OUTPUT :
# Total Belanja: Rp 600,000.0
# Diskon: Rp 60,000.0
# Total Pembayaran Setelah Diskon: Rp 540,000.0


#INPUT = Masukkan total belanja pelanggan: 200000
#OUTPUT : 
# Total Belanja: Rp 200,000.0
# Diskon: Rp 0.0
# Total Pembayaran Setelah Diskon: Rp 200,000.0

#INPUT = Masukkan total belanja pelanggan: 500000
#OUTPUT :
# Total Belanja: Rp 500,000.0
# Diskon: Rp 25,000.0
# Total Pembayaran Setelah Diskon: Rp 475,000.0