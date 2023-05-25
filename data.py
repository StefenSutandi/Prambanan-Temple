# Kumpulan F01 sampai F16
import random
import argparse
import os
import sys

# F01
def login():
    global role, username, sudahLogin
    sudahLogin = False
    usernameAda = False
    passwordBenar = False
    role = ""
    username = input('Username: ')
    password = input("Password: ")
    for barisUsername in range(NeffUser):   #pengulangan username 
        if username == listUser[barisUsername][0]: #cari si baris username
            usernameAda = True
            break
    print()
    if usernameAda:
        if password == listUser[barisUsername][1]: # cek password
            passwordBenar = True
            role = listUser[barisUsername][2]
            sudahLogin = True
            print(f"Selamat datang, {username}!")
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")

# F02
def logout():
    global sudahLogin, role
    if sudahLogin: # Sudah login
        print()
        role = ""
        sudahLogin = False
        usernameAda = False
    else: # Belum login
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")

# F03
def summonjin():
    global listUser,NeffUser
    i = 1
    formulaudahpenuhjin = True
    while formulaudahpenuhjin and i < 102:
        if listUser[i] == ["","",""] :
            formulaudahpenuhjin = False
        i += 1
    if formulaudahpenuhjin:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else :
        print('Jenis jin yang dapat dipanggil:\n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi\n')
        formulajenisjin = True
        formulausernamejin = False
        formulapasswordjin = False
        while formulajenisjin :             #menu jenis jin
            jenisjin = int(input('Masukkan nomer jenis jin yang ingin dipanggil: '))
            print()
            if jenisjin == 1 : #jenis jin 1
                print('Memilih jin "Pengumpul".')
                print()
                formulajenisjin = False
                formulausernamejin = True
                formulapasswordjin = False
                rolesijin = 'pengumpul'
                
                while formulausernamejin: #menu username summonjin
                    usernamejin = input('Masukkan username jin: ')
                    formulaudahkepakeuser = False
                    for q in range(2,NeffUser) :
                        if usernamejin == listUser[q][0] :
                            formulaudahkepakeuser = True
                            break
                    
                    if not formulaudahkepakeuser: #kalo belum kepake username, lanjoot
                        bariskosong = i-1
                        listUser[bariskosong][0] = usernamejin  #ngeganti yang kosong sama username
                        listUser[bariskosong][2] = rolesijin
                        NeffUser += 1
                        formulausernamejin = False
                        formulapasswordjin = True
                        formulajenisjin = False
                        
                    elif formulaudahkepakeuser: #kalo udah kepake user. ngulang lagu
                        formulausernamejin = True
                        formulapasswordjin = False
                        formulajenisjin = False
                        print()
                        print(f'Username "{usernamejin}" sudah diambil!')
                        print()
                                
                    while formulapasswordjin : #menu password summonjin
                        passwordjin = input('Masukkan password jin: ')
                        print()
                        if 5 < len(passwordjin) < 25 : # cek memenuhi passwordnya 
                            listUser[bariskosong][1] = passwordjin  #ngeganti yang kosong sama username
                            formulausernamejin = False
                            formulapasswordjin = False
                            formulajenisjin = False
                            print("Mengumpulkan sesajen...")
                            print("Menyerahkan sesajen...")
                            print("Membacakan mantra...")
                            print()
                            print(f"Jin {usernamejin} berhasil dipanggil!")
                        else :
                            formulausernamejin = False
                            formulapasswordjin = True
                            formulajenisjin = False
                            print('Password panjangnya harus 5-25 karakter!')
                            print()
                                                                                                                                                                                                                                                        
            elif jenisjin == 2 : #jenis jin 2
                print('Memilih jin "Pembangun".')
                print()
                formulajenisjin = False
                formulausernamejin = True
                formulapasswordjin = False
                rolesijin = 'pembangun'
                while formulausernamejin: #menu username summonjin
                    usernamejin = input('Masukkan username jin: ')
                    formulaudahkepakeuser = False
                    for q in range(2,NeffUser) :
                        if usernamejin == listUser[q][0] :
                            formulaudahkepakeuser = True
                            break
                    
                    if not formulaudahkepakeuser : #kalo belum kepake username, lanjoot
                        bariskosong = i-1
                        listUser[bariskosong][0] = usernamejin  #ngeganti yang kosong sama username
                        listUser[bariskosong][2] = rolesijin
                        NeffUser += 1
                        formulausernamejin = False
                        formulapasswordjin = True
                        formulajenisjin = False
                    
                    elif formulaudahkepakeuser : #kalo udah kepake user. ngulang lagu
                        formulausernamejin = True
                        formulapasswordjin = False
                        formulajenisjin = False
                        print()
                        print(f'Username "{usernamejin}" sudah diambil!')
                        print()
                                                                                                                          
                    while formulapasswordjin : #menu password summonjin
                        passwordjin = input('Masukkan password jin: ')
                        print()
                        if 5 < len(passwordjin) < 25 : # cek memenuhi passwordnya
                            listUser[bariskosong][1] = passwordjin  #ngeganti yang kosong sama username
                            formulausernamejin = False
                            formulapasswordjin = False
                            formulajenisjin = False
                            print("Mengumpulkan sesajen...")
                            print("Menyerahkan sesajen...")
                            print("Membacakan mantra...")
                            print()
                            print(f"Jin {usernamejin} berhasil dipanggil!")
                            
                        else :
                            formulausernamejin = False
                            formulapasswordjin = True
                            formulajenisjin = False
                            print('Password panjangnya harus 5-25 karakter!')
                            print()
                                                                                                                
            else :
                print(f'Tidak ada jenis jin bernomor {jenisjin}!')
                print()
                formulajenisjin = True
                formulausernamejin = False
                formulapasswordjin = False

# F04
def hilangkanjin():
    global listUser,NeffUser,listCandi,NeffCandi,sisaCandi
    formulaadajin = False
    hilanginyangmana = input("Masukkan username jin: ")
    for barisjin in range(2,NeffUser):
        if listUser[barisjin][0] == hilanginyangmana :     
            formulaadajin = True
            barisyangdiilangin = barisjin
            break
    if formulaadajin:
        yakin = input(f'Apakah anda yakin ingin menghapus jin dengan username {hilanginyangmana} (Y/N)? ')
        if yakin == 'Y' or yakin == 'y':
            if listUser[barisyangdiilangin][2] == 'pembangun' and NeffCandi > 0:
                for i in range (NeffCandi):
                    if listCandi[i][1] == hilanginyangmana:
                        listCandi[i] = ["","","","",""]
                        sisaCandi -= 1
                NeffCandi = CekNeffCandi(listCandi,NeffCandi)
            listUser[barisyangdiilangin][0] = ''
            listUser[barisyangdiilangin][1] = ''
            listUser[barisyangdiilangin][2] = ''
            if barisyangdiilangin != NeffUser-1:
                listUser[barisyangdiilangin] = listUser[NeffUser-1]
                listUser[NeffUser-1] = ["","",""]
            NeffUser -= 1
            print()
            print("Jin telah berhasil dihapus dari alam gaib.")
        elif yakin == 'N' or yakin == 'n': 
            print(f'Membatalkan penghapusan jin {hilanginyangmana}')
    else : 
        print('Tidak ada jin dengan username tersebut.')

# Fungsi mengecek ulang Nilai Efektif list candi
def CekNeffCandi(listCandi,NeffCandi):
    Temp = NeffCandi
    NeffCandi = 0
    for i in range (Temp):
        if listCandi[i] != ["","","","",""]:
            NeffCandi = (listCandi[i][0])+1
    return NeffCandi

# F05
def ubahJin():
    global listUser,NeffUser
    uname_jin = input("Masukkan username jin: " )
    jinAda = False
    i = 1
    while i < 102 and not jinAda:
        if listUser[i][0] == uname_jin:
            jinAda = True
        i += 1
    if jinAda:
        index_jin = i-1
        role = listUser[index_jin][2]
        if role == "pengumpul":
            cek = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            role = "pembangun"
            listUser = berhasil(cek, index_jin, role,listUser)
        else: # role == "pembangun"
            cek = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            role = "pengumpul"
            listUser = berhasil(cek,index_jin,role,listUser)
    else:
        print("Tidak ada jin dengan username tersebut.")

# Fungsi mengubah role jin
def berhasil(cek, index_jin, role,user):
    if(cek == 'Y' or cek == 'y'):
        user[index_jin][2] = role
        print("Jin telah berhasil diubah.")
    elif(cek == 'N' or cek == 'n'):
        print("Jin tidak jadi diubah.")
    return user

# F06
def pembangun(username):
    global listCandi,NeffCandi,sisaCandi,listBahan
# random_number = random.randint(1,5)
# output random_number akan ditampilkan random number dari 1 sampai 5
    butuh_pasir = random.randint(1,5) 
    butuh_batu = random.randint(1,5)  
    butuh_air = random.randint(1,5)
# Kondisi ketika jumlah bahan bangunan lebih banyak dibandingkan bahan bangunan yang dibutuhkan.
    if (butuh_pasir <= listBahan[0][2]) and (butuh_batu <= listBahan[1][2]) and (butuh_air <= listBahan[2][2]): 
        listBahan[0][2] -= butuh_pasir
        listBahan[1][2] -= butuh_batu
        listBahan[2][2] -= butuh_air
        Candi = ["",username,butuh_pasir,butuh_batu,butuh_air]
        if sisaCandi > 0:
            sisaCandi -= 1
            app = appendCandi(listCandi,NeffCandi,Candi)
            listCandi = app[0]
            NeffCandi = app[1]
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {sisaCandi}.")
        print 
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

def appendCandi(listCandi,NeffCandi,Candi):
    x = 10
    for i in range (NeffCandi):
        if listCandi[i] == ["","","","",""]:
            Candi[0] = i
            listCandi[i] = Candi
            x = 0
            break
    if x == 10:
        Candi[0] = NeffCandi
        listCandi[NeffCandi] = Candi
        NeffCandi += 1
    return (listCandi,NeffCandi)

# F07
def pengumpul():
    global listBahan
    jumlah_pasir = random.randint(0,5)
    jumlah_batu = random.randint(0,5)
    jumlah_air = random.randint(0,5)
    print(f"Jin menemukan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
    listBahan[0][2] += jumlah_pasir
    listBahan[1][2] += jumlah_batu
    listBahan[2][2] += jumlah_air

# F08
def jumlah_jin(role,user,N):
    jumlah_pengumpul = 0
    jumlah_pembangun = 0
    for i in range(2,N):
        if(user[i][2] == 'pengumpul'): #role = 'pengumpul'
            jumlah_pengumpul += 1
        else:#role = 'pembangun'
            jumlah_pembangun += 1
    if(role == 'pengumpul'): #peran = pengumpul
        return jumlah_pengumpul
    else:#peran = pembangun
        return jumlah_pembangun

def input_bahan (bahan_bangunan,pasir,batu,air,tipe):
    if(tipe == 'pengumpul'): #tipe pengumpul
        bahan_bangunan[0][2] += pasir
        bahan_bangunan[1][2] += batu
        bahan_bangunan[2][2] += air
    else:#tipe Pembangun
        bahan_bangunan[0][2] -= pasir
        bahan_bangunan[1][2] -= batu
        bahan_bangunan[2][2] -= air
    return (bahan_bangunan)

def random_bahan (bahan,role):
    if role == "pengumpul":
        if(bahan == 'pasir'):
            pasir = random.randint(0,5)
            return pasir
        elif(bahan == "batu"):
            batu = random.randint(0,5)
            return batu
        elif(bahan == 'air'):
            air = random.randint(0,5)
            return air
    elif role == "pembangun":
        if(bahan == 'pasir'):
            pasir = random.randint(1,5)
            return pasir
        elif(bahan == "batu"):
            batu = random.randint(1,5)
            return batu
        elif(bahan == 'air'):
            air = random.randint(1,5)
            return air

def batch_kumpul():
    global listBahan
    jumlah_pengumpul = jumlah_jin('pengumpul',listUser,NeffUser)
    pasir = 0
    batu = 0
    air = 0
    if(jumlah_pengumpul == 0):
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:#ada jin pengumpul
        for i in range(jumlah_pengumpul):
            pasirTemp = random_bahan("pasir","pengumpul")
            pasir += pasirTemp
            batuTemp = random_bahan('batu',"pengumpul")
            batu += batuTemp
            airTemp = random_bahan('air',"pengumpul")
            air += airTemp

        print("Mengerahkan "+str(jumlah_pengumpul)+" jin untuk mengumpulkan bahan.")
        print("Jin menemukan total "+str(pasir)+" pasir, "+str(batu)+" batu, "+str(air)+" air.")
        listBahan = input_bahan(listBahan,pasir,batu,air,'pengumpul')

def batch_bangun():
    global listBahan, listCandi, NeffCandi,listUser,NeffUser,sisaCandi
    jumlah_pembangun = jumlah_jin('pembangun',listUser,NeffUser)
    jin_pembangun = ["" for i in range (jumlah_pembangun)]
    k = 0
    if jumlah_pembangun > 0:
        for i in range (2,NeffUser):
            if listUser[i][2] == 'pembangun':
                jin_pembangun[k] = listUser[i][0]
                k += 1
    pasir = 0
    batu = 0
    air = 0
    if(jumlah_pembangun == 0):
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:#ada jin pembangun
        candiTemp = [["","",0,0,0] for i in range (jumlah_pembangun)]
        for i in range(jumlah_pembangun):
            pasirTemp = random_bahan("pasir","pembangun")
            pasir += pasirTemp
            batuTemp = random_bahan('batu',"pembangun")
            batu += batuTemp
            airTemp = random_bahan('air',"pembangun")
            air += airTemp
            candiTemp[i] = ["",jin_pembangun[i],pasirTemp,batuTemp,airTemp]
        print("Mengerahkan "+str(jumlah_pembangun)+" jin untuk membangun candi")
        print("dengan total bahan "+str(pasir)+" pasir, "+str(batu)+" batu, "+str(air)+" air.")
        if pasir <= listBahan[0][2] and batu <= listBahan [1][2] and air <= listBahan [2][2]:
            print(f"Jin berhasil membangun total {jumlah_pembangun} candi.")
            listBahan = input_bahan(listBahan,pasir,batu,air,'pembangun')
            for i in range (jumlah_pembangun):
                Temp = appendCandi(listCandi,NeffCandi,candiTemp[i])
                listCandi = Temp[0]
                NeffCandi = Temp[1]
            sisaCandi -= jumlah_pembangun
        else: # Jika bahan kurang
            print("Bangun gagal. Kurang",end="")
            if(pasir > listBahan[0][2]):
                if (batu+air > 0):
                    print(" "+str(pasir - listBahan[0][2])+" pasir",end=",")
                else:
                    print(" "+str(pasir - listBahan[0][2])+" pasir",end=",")
            if(batu > listBahan[1][2]):
                if (air > 0) or (pasir < 0):
                    print(" "+str(batu - listBahan[1][2])+" batu",end=",")
                else:
                    print(" dan "+str(batu - listBahan[1][2])+" batu",end="")
            if(air > listBahan[2][2]):
                if (pasir+batu > 0):
                    print(" dan "+str(air - listBahan[2][2])+" air",end="")
                else:
                    print(" "+str(air - listBahan[2][2])+" air",end="")
            print(".")

# F09
def find_top_and_bottom_jins(listUser,NeffUser,listCandi,NeffCandi,jumlahJin):
    top_jin = None
    bottom_jin = None
    jin = [[0,""] for i in range (jumlahJin)]
    # Mencari seluruh jin
    for i in range (jumlahJin):
        jin[i][1] = listUser[i+2][0]
    # Mencari jumlah candi untuk setiap jin pembangun
    for i in range (NeffCandi):
        if listCandi[i] != ["","","","",""]:
            j = 0
            tidakKetemu = True
            while tidakKetemu:
                if listCandi[i][1] == jin[j][1]:
                    jin[j][0] += 1
                    tidakKetemu = False
                j += 1
    jumlah_candi_max = 0
    jumlah_candi_min = 101
    for i in range (jumlahJin):
        # Mengabaikan jin tanpa membuat candi
        if jin[i][0] > 0:
            if (top_jin is None) or (jin[i][0] > jumlah_candi_max):
                top_jin = jin[i][1]
                jumlah_candi_max = jin[i][0]
            elif jin[i][0] == jumlah_candi_max:
                top_jin = min(top_jin, jin[i][1])
            if bottom_jin is None or (jin[i][0] < jumlah_candi_min):
                bottom_jin = jin[i][1]
                jumlah_candi_min = jin[i][0]
            elif jin[i][0] == jumlah_candi_min:
                bottom_jin = max(bottom_jin, jin[i][1])
    return top_jin, bottom_jin

# Fungsi utama
def laporanjin(listUser,NeffUser,listBahan,listCandi,NeffCandi):
    # Menghitung jumlah jin per tipe dan jumlah jin total
    jin_pengumpul = 0
    jin_pembangun = 0
    if NeffUser > 2:
        for i in range (2,NeffUser):
            if listUser[i][2] == "pengumpul":
                jin_pengumpul += 1
            elif listUser[i][2] == "pembangun":
                jin_pembangun += 1
    total_jin = jin_pengumpul + jin_pembangun

    # Mencari jin terajin dan jin termalas
    top_jin, bottom_jin = find_top_and_bottom_jins(listUser,NeffUser,listCandi,NeffCandi,total_jin)

    # Menampilkan hasil
    print()
    print(f'> Total Jin: {total_jin}')
    print(f'> Total Jin Pengumpul: {jin_pengumpul}')
    print(f'> Total Jin Pembangun: {jin_pembangun}')
    print(f'> Jin Terajin: {top_jin if top_jin else "-"}')
    print(f'> Jin Termalas: {bottom_jin if bottom_jin else "-"}')
    print(f'> Jumlah Pasir: {listBahan[0][2]}')
    print(f'> Jumlah Air: {listBahan[2][2]}')
    print(f'> Jumlah Batu: {listBahan[1][2]}')

# F10
def laporancandi(listCandi,NeffCandi):
    # Menghitung jumlah candi dan material yang digunakan
    total_candi = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    id_termahal = ''
    harga_termahal = 0
    id_termurah = ''
    harga_termurah = float('inf')
    for i in range (NeffCandi):
        if listCandi[i] != ["","","","",""]:
            id_candi = listCandi[i][0]
            pasir = listCandi[i][2]
            batu = listCandi[i][3]
            air = listCandi[i][4]
            harga_candi = 10000 * pasir + 15000 * batu + 7500 * air
            if harga_candi > harga_termahal:
                id_termahal = id_candi
                harga_termahal = harga_candi
            if harga_candi < harga_termurah and harga_candi > 0:
                id_termurah = id_candi
                harga_termurah = harga_candi
            total_candi += 1
            total_pasir += pasir
            total_batu += batu
            total_air += air

    # Menampilkan hasil
    print('> Total Candi:', total_candi)
    print('> Total Pasir yang digunakan:', total_pasir)
    print('> Total Batu yang digunakan:', total_batu)
    print('> Total Air yang digunakan:', total_air)
    print('> ID Candi Termahal:', id_termahal if id_termahal != '' else '-')
    print('> ID Candi Termurah:', id_termurah if id_termurah != '' else '-')

# F11
def hancurkancandi():
    global listCandi,NeffCandi,sisaCandi
    id_candi = int(input("Masukkan ID candi: "))
    candi = None
    if listCandi[id_candi] != ["","","","",""]:
        candi = listCandi[id_candi]

    if candi is None:
        print()
        print("Tidak ada candi dengan ID tersebut.")
    else:
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        if confirm.lower() == 'y':
            # menghancurkan candi
            listCandi [id_candi] = ["","","","",""]
            sisaCandi += 1
            # mengganti nilai efektif list candi
            if (id_candi == NeffCandi-1):
                Temp = NeffCandi
                NeffCandi = 0
                for i in range (Temp):
                    if listCandi[i] != ["","","","",""]:
                        NeffCandi = i+1
            print()
            print("Candi telah berhasil dihancurkan.")

# F12
def ayam_berkokok(jumlah_candi):
    if jumlah_candi >= 100:
        print("Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi:", jumlah_candi, "\n\nYah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi:", jumlah_candi, "\n\nSelamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
    
    # Keluar program
    sys.exit()

# F13
# Fungsi untuk membuang \n
def strip(string):
    newString = ""
    for i in range ((len(string))-1):
        newString += string[i] 
    return newString

def load():
    global listUser,NeffUser,listCandi,NeffCandi,listBahan,lenListBahan,sisaCandi,sisaJin
    sisaCandi = 100
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', nargs='?', default='*')
    args = parser.parse_args()
    if args.nama_folder == '*':
        print("Tidak ada nama folder yang diberikan!")
        print()
        print("Usage: python main.py <nama_folder>")
        sys.exit()
    else:
        folderName = args.nama_folder
        prevPath = os.getcwd()
        isFolderAda = os.path.exists(folderName)
        
        if isFolderAda:
            currentPath = os.path.realpath(folderName)
            os.chdir(currentPath)
            print("Loading...")
            print()
            listUser = [["","",""] for i in range (102)]
            NeffUser = 0
            with open ("user.csv") as fileUser:
                fileUser.readline()
                for line in fileUser:
                    currentString = strip(line)
                    stringUsername = ""
                    stringPassword = ""
                    stringRole = ""
                    delimiterCount = 0
                    for IdChar in range (len(currentString)):
                        if currentString[IdChar] != ';':
                            if delimiterCount == 0:
                                stringUsername += currentString[IdChar]
                            elif delimiterCount == 1:
                                stringPassword += currentString[IdChar]
                            else: # delimiterCount == 2
                                stringRole += currentString[IdChar]
                        else: #currentString[IdChar] == ';'
                            delimiterCount += 1
                    NeffUser += 1
                    listUser[NeffUser-1][0] = stringUsername
                    listUser[NeffUser-1][1] = stringPassword
                    listUser[NeffUser-1][2] = stringRole

            listCandi = [["","","","",""] for i in range (100)]
            NeffCandi = 0
            with open ("candi.csv") as fileCandi:
                fileCandi.readline()
                for line in fileCandi:
                    currentString = strip(line)
                    if currentString != ";;;;":
                        stringId = ""
                        stringPembuat = ""
                        stringPasir = ""
                        stringBatu = ""
                        stringAir = ""
                        delimiterCount = 0
                        for IdChar in range (len(currentString)):
                            if currentString[IdChar] != ';':
                                if delimiterCount == 0:
                                    stringId += currentString[IdChar]
                                elif delimiterCount == 1:
                                    stringPembuat += currentString[IdChar]
                                elif delimiterCount == 2:
                                    stringPasir += currentString[IdChar]
                                elif delimiterCount == 3:
                                    stringBatu += currentString[IdChar]
                                else: # delimiterCount == 4
                                    stringAir += currentString[IdChar]
                            else:
                                delimiterCount += 1
                        NeffCandi = (int(stringId))+1
                        sisaCandi -= 1
                        listCandi[NeffCandi-1][0] = int(stringId)
                        listCandi[NeffCandi-1][1] = stringPembuat
                        listCandi[NeffCandi-1][2] = int(stringPasir)
                        listCandi[NeffCandi-1][3] = int(stringBatu)
                        listCandi[NeffCandi-1][4] = int(stringAir)


            listBahan = [['pasir','10000/pasir',0],['batu',"15000/batu",0],["air","7500/air",0]]
            NeffBahan = 3
            with open ("bahan_bangunan.csv") as fileBahan:
                fileBahan.readline()
                for line in fileBahan:
                    currentString = strip(line)
                    stringNama = ""
                    stringDeskripsi = ""
                    stringJumlah = ""
                    delimiterCount = 0
                    for IdChar in range (len(currentString)):
                        if currentString[IdChar] != ';':
                            if delimiterCount == 0:
                                stringNama += currentString[IdChar]
                            elif delimiterCount == 1:
                                stringDeskripsi += currentString[IdChar]
                            else: # delimiterCount == 2
                                stringJumlah += currentString[IdChar]
                        else:
                            delimiterCount += 1
                    if stringNama == "pasir":
                        listBahan [0][2] = int(stringJumlah)
                    elif stringNama == "batu":
                        listBahan [1][2] = int(stringJumlah)
                    else: # stringNama == "air"
                        listBahan[2][2] = int(stringJumlah)
            print('Selamat datang di program "Manajerial Candi"')
            print("Silakan masukan username Anda")
            os.chdir(prevPath)
        else:
            print("Folder "+'"'+str(folderName)+'"'+" Tidak ditemukan")
            sys.exit()

# F14
def save(listUser,NeffUser,listCandi,NeffCandi,listBahan):
    folderName = input("Masukkan nama folder: ")
    print()
    print("Saving...")
    print()
    prevPath = os.getcwd()
    if not os.path.exists(folderName):
        os.mkdir(folderName)
        os.chdir(folderName)
        print("Membuat folder", os.getcwd())
        print()
    else:
        os.chdir(folderName)
    fileUser = open("user.csv",'w')
    fileUser.write("username;password;role\n")
    for i in range (NeffUser):
        if listUser[i] != ["","",""]:
            stringDitulis = listUser[i][0]+";"+listUser[i][1]+";"+listUser[i][2]
            fileUser.write(stringDitulis+"\n")

    fileCandi = open("candi.csv",'w')
    fileCandi.write("id;pembuat;pasir;batu;air\n")
    for i in range (NeffCandi):
        if listCandi[i] != ["","","","",""]:
            stringDitulis = str(listCandi[i][0])+';'+listCandi[i][1]+';'+str(listCandi[i][2])+';'+str(listCandi[i][3])+';'+str(listCandi[i][4])
            fileCandi.write(stringDitulis+"\n")

    fileBahan = open("bahan_bangunan.csv",'w')
    fileBahan.write("nama;deskripsi;jumlah\n")
    for i in range (3):
        if listBahan != ["","",""]:
            stringDitulis = listBahan[i][0]+';'+listBahan[i][1]+';'+str(listBahan[i][2])
            fileBahan.write(stringDitulis+"\n")

    fileUser.close()
    fileCandi.close()
    fileBahan.close()
    print("Berhasil menyimpan data di folder", os.getcwd())
    os.chdir(prevPath)

# F15
def help(role):
    print("=========== HELP ===========")
    if role == "":
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    else: # role bukan ""
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        if role == "bandung_bondowoso":
            print("2. summonjin")
            print("   Untuk memanggil jin")
            print("3. hapusjin")
            print("   Untuk menghilangkan jin yang sudah dipanggil")
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            print("5. batchkumpul")
            print("   Untuk menyuruh semua jin pengumpul mengumpulkan bahan")
            print("6. batchbangun")
            print("   Untuk menyuruh semua jin pembangun membangun candi")
            print("7. laporanjin")
            print("   Untuk melihat berapa banyak jin telah dipanggil dan kinerja jin")
            print("8. laporancandi")
            print("   Untuk melihat berapa banyak candi telah dibangun dan biaya candi termahal dan termurah")
            print("9. save")
            print("   Untuk menyimpan progress")
            print("10. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        elif role == "roro_jonggrang":
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi yang tersedia")
            print("3. ayamberkokok")
            print("   Untuk menyelesaikan permainan")
            print("4. save")
            print("   Untuk menyimpan progress")
            print("5. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        elif role == "pengumpul":
            print("2. kumpul")
            print("   Untuk mengumpulkan bahan")
            print("3. save")
            print("   Untuk menyimpan progress")
            print("4. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        else: # role == "pembangun"
            print("2. bangun")
            print("   Untuk membangun candi")
            print("3. save")
            print("   Untuk menyimpan progress")
            print("4. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")

# F16
def exit(listUser,NeffUser,listCandi,NeffCandi,listBahan):
    perluSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (perluSave != "y" and perluSave != "Y" and perluSave != "n" and perluSave != "N"):
        perluSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if perluSave == "y" or perluSave == "Y":
        save(listUser,NeffUser,listCandi,NeffCandi,listBahan)
    sys.exit()