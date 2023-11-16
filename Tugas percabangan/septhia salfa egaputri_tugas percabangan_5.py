# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24 
# soal : Deskripsi Pekerjaan: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

def tentukan_hasil_nilai(tugas, ujian):
    # Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa lulus
    if tugas > 70 and ujian > 60:
        hasil = "Lulus"
    # Jika tidak memenuhi syarat, siswa gagal
    else:
        hasil = "Gagal"
    
    return hasil

# Meminta input nilai tugas dan ujian dari pengguna
nilai_tugas = float(input("Masukkan nilai tugas siswa (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian siswa (skala 0-100): "))

# Memanggil fungsi untuk menentukan hasil nilai akhir
hasil_nilai = tentukan_hasil_nilai(nilai_tugas, nilai_ujian)

# Menampilkan hasil nilai akhir
print(f"Hasil nilai akhir: {hasil_nilai}")




#INPUT :
#   Masukkan nilai tugas siswa (skala 0-100): 90
#   Masukkan nilai ujian siswa (skala 0-100): 80
#OUTPUT : 
#   Hasil nilai akhir: Lulus

#INPUT : 
#   Masukkan nilai tugas siswa (skala 0-100): 20
#   Masukkan nilai ujian siswa (skala 0-100): 40
#OUTPUT :
#   Hasil nilai akhir: Gagal