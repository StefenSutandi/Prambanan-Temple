def ubahjin():
    username = input("Masukkan username jin: ")
    jin_dict = {}
    with open('jin.txt', mode='r') as file:
        line = file.readline()
        while line:
            if line[-1] == '\n':
                line = line[:-1]
            if line != "":
                comma_idx = find_comma(line)
                jin_username = line[:comma_idx]
                jin_type = line[comma_idx+1:]
                jin_dict[jin_username] = line
            line = file.readline()
    
    if username in jin_dict:
        while True:
            choice = input(f"Jin ini bertipe \"{jin_type}\". Yakin ingin mengubah ke tipe \"{'Pembangun' if jin_type=='Pengumpul' else 'Pengumpul'}\" (Y/N)? ")
            if choice == "Y":
                new_jin_type = 'Pembangun' if jin_type=='Pengumpul' else 'Pengumpul'
                new_jin_data = jin_username + ',' + new_jin_type + '\n'
                jin_dict[jin_username] = new_jin_data
                with open('jin.txt', mode='w') as file:
                    for jin in jin_dict.values():
                        file.write(jin)
                print("Jin telah berhasil diubah.")
                break
            elif choice == "N":
                break
    else:
        print("Tidak ada jin dengan username tersebut.")

def find_comma(s):
    for i in range(len(s)):
        if s[i] == ',':
            return i
    return -1
