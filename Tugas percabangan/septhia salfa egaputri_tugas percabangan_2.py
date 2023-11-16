# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Buatlah program Python yang membantu seorang manajer proyek menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat. Program ini akan meminta input berupa estimasi waktu pengerjaan proyek dan waktu aktual pengerjaan proyek, kemudian memberikan informasi apakah proyek tersebut akan selesai tepat waktu atau terlambat.

def cek_status_proyek(estimasi_waktu, waktu_aktual):

    # Jika waktu aktual lebih kecil atau sama dengan estimasi waktu, proyek selesai tepat waktu
    if waktu_aktual <= estimasi_waktu:
        print("Proyek selesai tepat waktu.")

    # Jika waktu aktual lebih besar dari estimasi waktu, proyek terlambat
    else:
        print("Proyek terlambat.")

# Meminta input dari pengguna
estimasi_waktu_proyek = float(input("Masukkan estimasi waktu pengerjaan proyek (dalam satuan waktu): "))
waktu_aktual_proyek = float(input("Masukkan waktu aktual pengerjaan proyek (dalam satuan waktu): "))

# Memanggil fungsi untuk menentukan status proyek
cek_status_proyek(estimasi_waktu_proyek, waktu_aktual_proyek)





#INPUT 
#   Masukkan estimasi waktu pengerjaan proyek (dalam satuan waktu): "12.00"   
#   Masukkan waktu aktual pengerjaan proyek (dalam satuan waktu): "13.00"     
#OUTPUT = "Proyek terlambat"

#INPUT 
#   Masukkan estimasi waktu pengerjaan proyek (dalam satuan waktu): "12.00"
#   Masukkan waktu aktual pengerjaan proyek (dalam satuan waktu): "09.00"
#OUTPUT = "Proyek selesai tepat waktu"
