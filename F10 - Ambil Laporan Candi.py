def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rows = []
        for line in lines:
            row = line.replace('\n', '').split(',')
            rows.append(row)
        return rows

def main():
    # Memuat data dari file CSV
    file_path = 'laporan_candi.csv'
    rows = read_csv(file_path)

    # Menghitung jumlah candi dan material yang digunakan
    total_candi = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    id_termahal = ''
    harga_termahal = 0
    id_termurah = ''
    harga_termurah = float('inf')
    for row in rows:
        id_candi = row[0]
        pasir = int(row[1])
        batu = int(row[2])
        air = int(row[3])
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

# import csv

# laporancandi = []
# print("laporancandi")
# total_candi = int(input("Total Candi: "))
# total_pasir = int(input("Total Pasir yang digunakan: "))
# total_batu = int(input("Total Batu yang digunakan: "))
# total_air = int(input("Total Air yang digunakan: "))

# harga_candi = 10000 * total_pasir + 15000 * total_batu + 7500 * total_air

# candi = laporancandi[harga_candi]
# expensive_candi = candi[0]
# cheap_candi = candi[0]
# for c in candi:
#     if c[harga_candi] > expensive_candi[harga_candi]:
#         candi_termahal = c
#     if c[harga_candi] < cheap_candi[harga_candi]:
#         candi_termurah = c

# # menampilkan informasi candi termahal dan termurah
# print(" ID Candi Termahal: " + expensive_candi["nama"] + str(expensive_candi[harga_candi]))
# print(" ID Candi Termurah: " + cheap_candi["nama"] + str(cheap_candi[harga_candi]))