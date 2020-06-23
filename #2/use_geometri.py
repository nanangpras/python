from geometri.persegipanjang import hitung_luas_persegipanjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
alas = 4
tinggi = 2
print(f'hitung luas segitiga dengan packages {hitung_luas_segitiga(alas,tinggi)}')
print(f'hitung luas segitiga dengan packages {hitung_luas_segitiga(5,2)}')

print(f'\n{info_persegipanjang()}')
print(f'luas persegi panjang {hitung_luas_persegipanjang(3,2)}')
