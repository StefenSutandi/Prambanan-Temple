def hilangkanjin():
    username = input("Masukkan username jin: ")
    jin_dict = {}
    jin_exists = False
    with open('jin.txt', mode='r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line[:-1] # hapus karakter '\n'
            if line == "":
                continue
            line_username = ""
            line_jin_id = ""
            reading_username = True
            for i in range(len(line)):
                if line[i] == ",":
                    reading_username = False
                    continue
                if reading_username:
                    line_username += line[i]
                else:
                    line_jin_id += line[i]
            if line_username == username:
                jin_exists = True
                while True:
                    choice = input("Apakah anda yakin ingin menghapus jin dengan username " + username + " (Y/N)? ")
                    if choice == "Y":
                        jin_id = int(line_jin_id)
                        with open('candi.txt', mode='r+') as candi_file:
                            lines = candi_file.readlines()
                            candi_file.seek(0)
                            for candi_line in lines:
                                if not candi_line.startswith(str(jin_id) + ","):
                                    candi_file.write(candi_line)
                            candi_file.truncate()
                        print("Jin telah berhasil dihapus dari alam gaib.")
                        break
                    elif choice == "N":
                        break
                    else:
                        print("Input tidak valid. Masukkan Y atau N.")
                break

    if not jin_exists:
        print("Tidak ada jin dengan username tersebut.")