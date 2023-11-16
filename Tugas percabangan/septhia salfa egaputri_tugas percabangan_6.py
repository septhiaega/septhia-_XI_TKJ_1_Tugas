# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

def kategorikan_produk(penjualan):
    # Kategorikan produk berdasarkan penjualan
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif 500 <= penjualan <= 1000:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"

    return kategori

# Meminta input data penjualan bulanan dari pengguna
penjualan_produk = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Memanggil fungsi untuk mengkategorikan produk
kategori_produk = kategorikan_produk(penjualan_produk)

# Menampilkan hasil kategori produk
print(f"Kategori produk: {kategori_produk}")



#INPUT : "Masukkan jumlah penjualan bulanan produk" = 12000
#OUTPUT :Kategori produk: Produk Terlaris

#INPUT : "Masukkan jumlah penjualan bulanan produk": 700
#OUTPUT : Kategori produk: Produk Populer

#IMPUT : "Masukkan jumlah penjualan bulanan produk": 80
#OUTPUT : Kategori produk: Produk Biasa
