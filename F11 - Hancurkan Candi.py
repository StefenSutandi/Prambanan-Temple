import csv

def hancurkancandi():
    id_candi = input("Masukkan ID candi: ")

    # membuka file CSV untuk dibaca
    with open('candi.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        candi = None
        for row in reader:
            if row['ID'] == id_candi:
                candi = row
                break

    if candi is None:
        print("Tidak ada candi dengan ID tersebut.")
        return

    confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
    if confirm.lower() == 'y':
        # membuka file CSV untuk ditulis
        with open('candi.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()

            # menulis baris-baris selain yang dihapus
            with open('candi.csv', mode='r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['ID'] != id_candi:
                        writer.writerow(row)

        print("Candi telah berhasil dihancurkan.")