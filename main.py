from data import *
import data

load()
login()

while True:
    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
    command = input(">>> ")
    if command == "login":
        if (not (data.sudahLogin)): # Belum login
            login() 
        else: # Sudah login
            print("Login gagal!")
            print(f'Anda telah login dengan username {data.username}, silahkan lakukan “logout”') 
            print("sebelum melakukan login kembali.")
    elif command == "logout":
        logout()
    elif command == "summonjin":
        if (data.role) == 'bandung_bondowoso':
            summonjin()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "hapusjin":
        if (data.role) == 'bandung_bondowoso':
            hilangkanjin()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "ubahjin":
        if (data.role) == 'bandung_bondowoso':
            ubahJin()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "bangun":
        if (data.role) == "pembangun":
            pembangun(data.username)
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "kumpul":
        if (data.role) == "pengumpul":
            pengumpul()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "batchkumpul":
        if (data.role) == "bandung_bondowoso":
            batch_kumpul()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "batchbangun":
        if (data.role) == "bandung_bondowoso":
            batch_bangun()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "laporanjin":
        if (data.role) == "bandung_bondowoso":
            laporanjin(data.listUser,data.NeffUser,data.listBahan,data.listCandi,data.NeffCandi)
        else:
            print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso")
    elif command == "laporancandi":
        if (data.role) == "bandung_bondowoso":
            laporancandi(data.listCandi,data.NeffCandi)
        else:
            print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
    elif command == "hancurkancandi":
        if (data.role) == "roro_jonggrang":
            hancurkancandi()
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "ayamberkokok":
        if (data.role) == "roro_jonggrang":
            ayam_berkokok(100-(data.sisaCandi))
        else:
            print(f"Anda tidak bisa menggunakan command tersebut untuk {data.role}")
    elif command == "save":
        save(data.listUser,data.NeffUser,data.listCandi,data.NeffCandi,data.listBahan)
    elif command == "exit":
        exit(data.listUser,data.NeffUser,data.listCandi,data.NeffCandi,data.listBahan)
    elif command == "help":
        help(data.role)
    else:
        print("Tidak ada command tersebut.")