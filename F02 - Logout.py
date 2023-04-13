def logout():
    global current_user
    
    if current_user is None:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        print("Logout berhasil!")
        current_user = None