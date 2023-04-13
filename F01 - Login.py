# daftar user yang terdaftar di sistem
registered_users = ["Bandung", "Roro Jonggrang", "Jin Pekerja"]

# daftar password yang sesuai dengan setiap user
user_passwords = {
    "Bandung": "Bondowoso",
    "Roro Jonggrang": "Prambanan",
    "Jin Pekerja": "Batu Bara"
}

# status login pengguna saat ini
current_user = None

while True:
    # jika pengguna sudah login, tampilkan pesan sambutan
    if current_user:
        print(f"Selamat datang, {current_user}!")
        print("Masukkan perintah 'help' untuk daftar perintah yang tersedia.")
    else:
        print("Silakan login untuk mengakses sistem.")

    # minta pengguna untuk memasukkan username dan password
    username = input("Username: ")
    password = input("Password: ")

    # periksa apakah username terdaftar dan password cocok
    if username in registered_users:
        if user_passwords[username] == password:
            if current_user:
                print("Anda sudah login dengan username", current_user)
            else:
                current_user = username
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")