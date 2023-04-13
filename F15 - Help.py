def help(role):
    if role == "new player":
        print("=========== HELP ===========")
        print("1. login\n   Untuk masuk menggunakan akun")
        print("2. exit\n   Untuk keluar dari program dan kembali ke terminal")
    elif role == "bandung_bondowoso":
        print("=========== HELP ===========")
        print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin\n   Untuk memanggil jin")
        # tambahkan command yang bisa diakses oleh Bandung Bondowoso
    elif role == "roro_jonggrang":
        print("=========== HELP ===========")
        print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia")
        # tambahkan command yang bisa diakses oleh Roro Jonggrang
    elif role == "jin_pengumpul":
        print("=========== HELP ===========")
        print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul\n   Untuk mengumpulkan resource candi")
        # tambahkan command yang bisa diakses oleh Jin Pengumpul
    elif role == "jin_pembangun":
        print("=========== HELP ===========")
        print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun\n   Untuk membangun candi")
        # tambahkan command yang bisa diakses oleh Jin Pembangun
    else:
        print("Role tidak valid")