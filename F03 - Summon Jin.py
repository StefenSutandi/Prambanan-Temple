def summon_jin():
    # Cek apakah jumlah jin sudah maksimal
    file = open('jin.txt', mode='r')
    jin_count = 0
    while True:
        line = file.readline()
        if not line:
            break
        if line.strip() != "":
            jin_count += 1
    file.close()
    
    if jin_count >= 100:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung Bondowoso tidak dapat men-summon lebih dari itu.")
        return
    
    # Meminta input dari pengguna untuk jenis jin dan username
    jin_type = None
    while jin_type not in ["1", "2"]:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        jin_type = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        
        if jin_type not in ["1", "2"]:
            print("Tidak ada jenis jin bernomor “{}”!".format(jin_type))
    
    if jin_type == "1":
        jin_name = "Pengumpul"
    else:
        jin_name = "Pembangun"
        
   # Meminta input dari pengguna untuk username dan password jin
    username = None
    while username is None or username == "" or is_username_taken(username):
        username = input("Masukkan username jin: ")
        username = username.rstrip()  # Menghapus whitespace di akhir string
    if is_username_taken(username):
        print("Username “{}” sudah diambil!".format(username))
    
    # Mengecek panjang password
    password = None
    while password is None or password == "" or not (password[4:] == "" or password[24:] == ""):
        password = input("Masukkan password jin: ")
        password = password.rstrip()  # Menghapus whitespace di akhir string
    if password == "":
        print("Password tidak boleh kosong!")
    elif not (password[4:] == "" or password[24:] == ""):
        print("Password harus terdiri dari 5 sampai 25 karakter!")

    # Menyimpan data jin ke dalam file
    with open('jin.txt', mode='a') as file:
        file.write(f"{jin_type},{username},{password}\n")
    
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print(f"Jin {jin_name} berhasil dipanggil!")
    
    
def is_username_taken(username):
    file = open('jin.txt', mode='r')
    line = file.readline()
    while line != "":
        comma_indexes = []
        for i in range(len(line)):
            if line[i] == ',':
                comma_indexes.append(i)
        if len(comma_indexes) >= 2:
            if line[comma_indexes[0]+1:comma_indexes[1]] == username:
                file.close()
                return True
        line = file.readline()
    file.close()
    return False