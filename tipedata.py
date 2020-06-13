print('tipe data skalar => tipe data sederhana')
anak1 = 'anak pertama'
anak2 = 'anak kedua'
anak3 = 'anak ketiga'
anak4 = 'anak keempat'
anak5 = 'anak kelima'

print(anak1)

print('\ntipe data list/daftar/array')
buah = ['mangga','anggur','jeruk','apel']
print(buah)
buah.append('durian')
print(buah)

print('\nsalah satu buah kesukaanku')
print("aku suka buah", buah[4])

print('\nsemua buah kesukaanku')
for a in buah:
    print(f'aku suka buah {a}')

print('\nbuah kesukaanku dengan cara ribet')
for a in range(0, len(buah)):
    print(f'{a+1}. aku suka buah {buah[a]}')