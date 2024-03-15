peso_kg = input('Ingrese su peso (kg): ')
peso_kg = float(peso_kg)

talla_altura = input('Ingrese su altura (cm): ')
talla_altura = float(talla_altura)
talla_altura = talla_altura/100

imc = peso_kg / (talla_altura**2)
print(f'su IMC es de: ', round(imc,2))

if (imc > 0 and imc < 18.5):
    print('La clasificación OMS es Bajo Peso')
elif (imc >= 18.5 and imc < 25):
    print('La clasificación OMS es Adecuado')
elif (imc >= 25 and imc < 30):
    print('La clasificación OMS es Sobrepeso')
elif (imc >= 30 and imc < 35):
    print('La clasificación OMS es Obesidad Grado I')
elif (imc >= 35 and imc < 40):
    print('La clasificación OMS es Obesidad Grado II')
else:
    print('La clasificación OMS es Obesidad Grado III')