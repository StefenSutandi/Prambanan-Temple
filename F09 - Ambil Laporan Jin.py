import csv

with open('laporan_jin.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    laporanjin = {}
    for row in reader:
        laporanjin['Total Jin'] = int(row['Total Jin'])
        laporanjin['Total Jin Pengumpul'] = int(row['Total Jin Pengumpul'])
        laporanjin['Total Jin Pembangun'] = int(row['Total Jin Pembangun'])
        laporanjin['Jin Terajin'] = row['Jin Terajin']
        laporanjin['Jin Termalas'] = row['Jin Termalas']
        laporanjin['Jumlah Pasir'] = int(row['Jumlah Pasir'])
        laporanjin['Jumlah Air'] = int(row['Jumlah Air'])
        laporanjin['Jumlah Batu'] = int(row['Jumlah Batu'])

# Fungsi untuk mencari jin terajin dan jin termalas
def find_top_and_bottom_jins(jins):
    top_jin = None
    bottom_jin = None
    for username, pengumpul, pembangun in jins:
        # Mengabaikan jin tanpa membuat candi
        if int(pembangun) > 0:
            if top_jin is None or int(pembangun) > int(jins[top_jin][2]):
                top_jin = username
            elif int(pembangun) == int(jins[top_jin][2]):
                top_jin = min(top_jin, username)
            if bottom_jin is None or int(pembangun) < int(jins[bottom_jin][2]):
                bottom_jin = username
            elif int(pembangun) == int(jins[bottom_jin][2]):
                bottom_jin = max(bottom_jin, username)
    return top_jin, bottom_jin

# Fungsi untuk menjumlahkan material
def sum_materials(jins):
    pasir = 0
    air = 0
    batu = 0
    for username, pengumpul, pembangun in jins:
        pasir += int(pengumpul.split()[0])
        air += int(pengumpul.split()[1])
        batu += int(pengumpul.split()[2])
    return pasir, air, batu

# Fungsi utama
def main():
    # Memuat data dari file CSV
    with open('laporan_jin.csv', newline='') as csvfile:
        rows = csv.DictReader(csvfile)

    # Menghitung jumlah jin per tipe dan jumlah jin total
    jin_pengumpul = 0
    jin_pembangun = 0
    jins = []
    for row in rows:
        username = row[0]
        pengumpul = row[1]
        pembangun = row[2]
        jins.append([username, pengumpul, pembangun])
        jin_pengumpul += int(pengumpul)
        jin_pembangun += int(pembangun)
    total_jin = jin_pengumpul + jin_pembangun

    # Mencari jin terajin dan jin termalas
    top_jin, bottom_jin = find_top_and_bottom_jins(jins)

    # Menjumlahkan material
    pasir, air, batu = sum_materials(jins)

    # Menampilkan hasil
    print(f'Total Jin: {total_jin}')
    print(f'Total Jin Pengumpul: {jin_pengumpul}')
    print(f'Total Jin Pembangun: {jin_pembangun}')
    print(f'Jin Terajin: {top_jin if top_jin else "-"}')
    print(f'Jin Termalas: {bottom_jin if bottom_jin else "-"}')
    print(f'Jumlah Pasir: {pasir}')
    print(f'Jumlah Air: {air}')
    print(f'Jumlah Batu: {batu}')


# # Menampilkan syarat untuk jin
# if total_jin == 0 or total_jin_pengumpul == 0 or total_jin_pembangun == 0:
#     print("Jin Terajin: -")
#     print("Jin Termalas: -")
# # Menampilkan syarat untuk jin terajin
# diligent_jin = laporanjin["jin_terajin"]
# if diligent_jin[0] > diligent_jin[1]:
#     diligent_jin[0], diligent_jin[1] = diligent_jin[1], diligent_jin[0]
# print("Jin Terajin: " + diligent_jin[0])

# # Menampilkan syarat untuk jin termalas
# lazy_jin = laporanjin["jin_termalas"]
# if lazy_jin[0] < lazy_jin[1]:
#     lazy_jin[0], lazy_jin[1] = lazy_jin[1], lazy_jin[0]
# print("Jin Termalas: " + lazy_jin[0])