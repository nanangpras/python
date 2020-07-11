from oopgeometri.bangun_ruang import BangunRuang

class Segitiga(BangunRuang):

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'modul menghitung luas segitiga\n' \
               f'dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi /2
