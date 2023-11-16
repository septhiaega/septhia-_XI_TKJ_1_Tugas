# nama : septhia salfa egaputri
# kelas : XI TKJ 1
# no. abs : 24
# soal : Deskripsi Pekerjaan: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

def cek_perlu_restart(pembaruan_perangkat):
    # Jika pembaruan perangkat lunak mengharuskan restart, sistem perlu di-restart
    if pembaruan_perangkat.lower() == "ya":
        print("Sistem perlu di-restart.")
    # Jika pembaruan perangkat lunak tidak mengharuskan restart, sistem tidak perlu di-restart
    else:
        print("Sistem tidak perlu di-restart.")

# Meminta input informasi pembaruan perangkat lunak dari pengguna
pembaruan_perangkat_lunak = input("Apakah pembaruan perangkat lunak mengharuskan restart? (ya/tidak): ")

# Memanggil fungsi untuk menentukan apakah sistem perlu di-restart
cek_perlu_restart(pembaruan_perangkat_lunak)




#INPUT : Apakah pembaruan perangkat lunak mengharuskan restart? (ya/tidak): ya   
#OUTPUT : Sistem perlu di-restart.

#INPUT : Apakah pembaruan perangkat lunak mengharuskan restart? (ya/tidak): tidak
#OUTPUT : Sistem tidak perlu di-restart.