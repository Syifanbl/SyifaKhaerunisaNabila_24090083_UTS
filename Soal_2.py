tahun = int(input('Masukan_tahun: '))


kabisat = tahun%4

if kabisat==0:
    print(f'Tahun{tahun} adalah Tahun Kabisat')

else:
    print(f'Tahun{tahun} adalah bukan Tahun Kabisat')
    