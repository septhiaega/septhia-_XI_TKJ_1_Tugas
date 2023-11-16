# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.Soal: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

def cek_status_persiapan(status_persiapan):
    # Jika status persiapan "Siap", proyek diluncurkan
    if status_persiapan.lower() == "siap":
        print("Proyek diluncurkan.")
    # Jika status persiapan "Tunda", proyek ditunda
    elif status_persiapan.lower() == "tunda":
        print("Proyek ditunda.")
    # Jika status persiapan tidak dikenali, tampilkan pesan kesalahan
    else:
        print("Status persiapan tidak dikenali. Harap masukkan 'Siap' atau 'Tunda'.")

# Meminta input status persiapan proyek dari pengguna
status_persiapan_proyek = input("Masukkan status persiapan proyek (Siap/Tunda): ")

# Memanggil fungsi untuk menentukan apakah proyek dapat diluncurkan
cek_status_persiapan(status_persiapan_proyek)



# INPUT : Masukkan status persiapan proyek (Siap/Tunda): 
# OUTPUT : Siap Proyek diluncurkan.

# INPUT : Masukkan status persiapan proyek (Siap/Tunda): 
# OUTPUT : Tunda Proyek ditunda.