from oopgeometri.persegipanjang import PersegiPanjang
from oopgeometri.segitiga import Segitiga
from oopgeometri.bangun_ruang import BangunRuang

print('Menggunakan OOP')

p1 = PersegiPanjang(10,4)
print(p1.info())
print(f'maka luasnya adalah {p1.hitung_luas()}')
print('-------------------------------------------------------')

s1 = Segitiga(4,2)
print(s1.info())
print(f'luas segitiga = {s1.hitung_luas()}')

print('\nMencoba membuat objek dari kelas Bangun Ruang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

print('\nPolymorphism')
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
