# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

def cek_file_di_server(nama_file, daftar_file):
    # Jika nama file ada dalam daftar file di server, file sudah ada
    if nama_file in daftar_file:
        print("File sudah ada.")
    # Jika nama file tidak ada dalam daftar file di server, file belum ada
    else:
        print("File belum ada.")

# Nama file yang akan diperiksa
nama_file_target = "data.txt"

# Daftar file di server
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

# Memanggil fungsi untuk memeriksa keberadaan file
cek_file_di_server(nama_file_target, daftar_file_di_server)

