import random


computador = random.randrange(0, 3)
opcion_computador = ''

opcion_usuario = (input('Ingresa tu opcion (Piedra / Papel / Tijera): ').title())

# Ingreso de usuario

if opcion_usuario == 'Piedra':
    opcion_usuario = 'Piedra'
elif opcion_usuario =='Papel':
    opcion_usuario = 'Papel'
elif opcion_usuario == 'Tijera':
    opcion_usuario = 'Tijera'
else :
    print('Argumento inválido: Debe ser Piedra, Papel o Tijera')
    

# Seleccion pc

if computador == 0:
    opcion_computador = 'Piedra'
elif computador == 1:
    opcion_computador = 'Papel'
elif computador == 2:
    opcion_computador = 'Tijera'


print('Tu jugaste: ', opcion_usuario)
print('Computador jugó: ', opcion_computador)

if opcion_usuario == 'Piedra' and opcion_computador == 'Papel':
    print('Perdiste!!!')
elif opcion_usuario == 'Piedra' and opcion_computador == 'Tijera':
    print('Ganaste!!!')
elif opcion_usuario == 'Papel' and opcion_computador == 'Piedra':
    print('Ganaste!!!')
elif opcion_usuario == 'Papel' and opcion_computador == 'Tijera':
    print('Perdiste!!!')
elif opcion_usuario == 'Tijera' and opcion_computador == 'Piedra':
    print('Perdiste!!!')
elif opcion_usuario == 'Tijera' and opcion_computador == 'Papel':
    print('Ganaste!!!')
elif opcion_usuario == 'Tijera' and opcion_computador == 'Tijera':
    print('Empate')
elif opcion_usuario == 'Papel' and opcion_computador == 'Papel':
    print('Empate')
elif opcion_usuario == 'Piedra' and opcion_computador == 'Piedra':
    print('Empate')
else:
    print('Argumento inválido: Debe ser Piedra, Papel o Tijera')
    
# PD no supe como hacer que solo muestre el mensaje de error al ingresar cualquier dato erroneo,
# Estuve leyendo sobre el break pero no me funciono :(