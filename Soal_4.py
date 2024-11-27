berat = int(input('masukan berat badan (Kg): '))
tinggi = float(input('masukan tinggii badan (M): '))

print()

BMI = berat/(tinggi**2)
print(f'Berat_Badan: {berat}')
print(f'Tinggi_Badan: {tinggi}')
print(f'Nilai_BMI_Anda: {BMI}')

if BMI<18.5:
    print(f'kategori BMI : Berat Badan Kurang ')
elif (BMI>= 18.5 and BMI<24.9):
    print(f'kategori BMI : Berat Badan Normal')
elif (BMI>= 25 and BMI<29.9):
    print(f'kategori BMI : Kelebihan Berat Badan ')
elif BMI>=30:
    print(f'Kategori BMI : Obesitas')