from oopgeometri.bangun_ruang import BangunRuang

class PersegiPanjang(BangunRuang):
    def __init__(self,p, l):
        #fungsi pertamakali yang dipanggil saat object diciptakan dlm hal ini p1 di main.py
        self.p = p
        self.l = l

    def info(self):
        return f'modul menghitung persegipanjang dengan OOP\n' \
               f'dengan panjang = {self.p} lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
