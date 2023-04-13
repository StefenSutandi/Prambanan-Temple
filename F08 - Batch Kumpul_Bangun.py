import random

class JinPembangun:
    def __init__(self):
        self.sisa_candi = 0
        self.bahan_bangunan = {'pasir': 0, 'batu': 0, 'air': 0}
        
    def generate_bahan_bangunan(self):
        self.bahan_bangunan = {k: random.randint(1, 5) for k in self.bahan_bangunan}
        print('Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air)'.format(**self.bahan_bangunan))
        
    def build_candi(self):
        if self.sisa_candi > 0:
            print('Masih ada {0} candi yang perlu dibangun.'.format(self.sisa_candi))
            return
        
        if self.bahan_bangunan['pasir'] >= 2 and self.bahan_bangunan['batu'] >= 2 and self.bahan_bangunan['air'] >= 2:
            self.bahan_bangunan['pasir'] -= 2
            self.bahan_bangunan['batu'] -= 2
            self.bahan_bangunan['air'] -= 2
            self.sisa_candi = 100
            print('Candi berhasil dibangun.')
            print('Sisa candi yang perlu dibangun: {0}.'.format(self.sisa_candi))
        else:
            print('Bahan bangunan tidak mencukupi.')
            print('Candi tidak bisa dibangun!')

class JinPengumpul:
    def __init__(self):
        self.pasir = 0
        self.batu = 0
        self.air = 0
        
    def kumpul(self):
        self.pasir += random.randint(0, 5)
        self.batu += random.randint(0, 5)
        self.air += random.randint(0, 5)
        print("Jin menemukan {} pasir, {} batu, dan {} air.".format(self.pasir, self.batu, self.air))

jin_list = []

def summon_jin():
    pilihan = input("Pilih jin yang ingin Anda summon (pembangun/pengumpul): ")
    if pilihan == 'pembangun':
        jin_list.append(JinPembangun())
        print("Jin pembangun berhasil di-summon!")
    elif pilihan == 'pengumpul':
        jin_list.append(JinPengumpul())
        print("Jin pengumpul berhasil di-summon!")
    else:
        print("Pilihan tidak tersedia.")

def batchkumpul():
    total_pasir = 0
    total_batu = 0
    total_air = 0
    count_pengumpul = 0
    for jin in jin_list:
        if isinstance(jin, JinPengumpul):
            count_pengumpul += 1
            jin_kumpul = jin.kumpul()
            total_pasir += jin_kumpul[0]
            total_batu += jin_kumpul[1]
            total_air += jin_kumpul[2]
    if count_pengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {count_pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")

def batchbangun(jin_list):
    count_pembangun = 0
    for jin in jin_list:
        if isinstance(jin, JinPembangun):
            count_pembangun += 1
            jin.build_candi()
    if count_pembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")