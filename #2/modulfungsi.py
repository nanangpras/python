"""
perhitungan luas segitiga
rumus luas alas * tinggi / 2
"""

print('\nMenghitung segitiga biasa')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'luas segitanya adalah {luas_segitiga}')

print('\nMenghitung segitiga copy paste')
alas = 15
tinggi = 3
luas_segitiga = alas * tinggi / 2
print(f'luas segitanya adalah {luas_segitiga}')

print('\nMenghitung luas segitiga dengan fungsi')
def hitung_luas_segitiga (alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga
alas = 12
tinggi = 4
print(f'Dengan fungsi luas segitiga adalah {hitung_luas_segitiga(20,2)}')
print(f'Dengan fungsi, alas = {alas}, tinggi = {tinggi} maka luas segitiga adalah {hitung_luas_segitiga(alas,tinggi)}')