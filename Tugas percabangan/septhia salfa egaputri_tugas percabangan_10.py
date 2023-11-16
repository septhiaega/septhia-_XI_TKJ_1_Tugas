# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang pengembang perangkat lunak, Anda perlu membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka. Soal: Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut: • Performa 5: Bonus 20% dari gaji tahunan. • Performa 4: Bonus 10% dari gaji tahunan. • Performa 3: Bonus 5% dari gaji tahunan. • Performa 2: Bonus 2% dari gaji tahunan. • Performa 1: Tidak ada bonus. Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.


# Meminta input nilai performa karyawan dari pengguna
performa_karyawan = int(input("Masukkan nilai performa karyawan (1-5): "))

# Menentukan bonus tahunan berdasarkan performa menggunakan percabangan ternary
bonus_tahunan = 0.20 if performa_karyawan == 5 else (0.10 if performa_karyawan == 4 else (0.05 if performa_karyawan == 3 else (0.02 if performa_karyawan == 2 else 0)))

# Menampilkan hasil bonus tahunan
print(f"Bonus Tahunan: {bonus_tahunan * 100}% dari gaji tahunan.")




#Masukkan nilai performa karyawan (1-5): 2
#Bonus Tahunan: 2.0% dari gaji tahunan.

#Masukkan nilai performa karyawan (1-5): 3
#Bonus Tahunan: 5.0% dari gaji tahunan.

#Masukkan nilai performa karyawan (1-5): 5
#Bonus Tahunan: 20.0% dari gaji tahunan.