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

jin = JinPembangun()
while True:
    jin.generate_bahan_bangunan()
    jin.build_candi()