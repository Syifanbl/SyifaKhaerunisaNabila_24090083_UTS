jumlah_barang = int(input('masukan jumlah_bang: '))
total_harga = 0

for i in range(1,jumlah_barang +1 ):
    harga = float(input(f'masukan harga barang ke-{x} : '))
    total_harga+= harga

print(f'Total harga belanjaan: {total_harga}')