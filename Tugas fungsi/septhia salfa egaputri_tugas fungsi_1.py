# Nama: septhia salfa egaputri
# Kelas: XI-Tkj 1
# Nomor Absen: 24
# Soal: Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna. Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)

def total_deret_bilangan_ganjil(batas):
    total = 0
    for i in range(1, 2 * batas, 2):
        total += i
    return total

# Meminta input dari pengguna
batas_deret = int(input("Masukkan batas deret bilangan ganjil: "))

# Memanggil fungsi dan menampilkan hasilnya
print(f"Total deret bilangan ganjil hingga batas {batas_deret} adalah: {total_deret_bilangan_ganjil(batas_deret)}")




#INPUT : Masukkan batas deret bilangan ganjil: 9 
#OUTPUT : Total deret bilangan ganjil hingga batas 9 adalah: 81