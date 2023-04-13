import random

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