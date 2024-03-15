import random


computador = random.randrange(0, 3)
opcion_computador = ''

opcion_usuario = (input('Ingresa tu opcion (Piedra / Papel / Tijera): ').title())

if (opcion_usuario != 'Piedra' and opcion_usuario != 'Papel' and opcion_usuario != 'Tijera'):
    print('Argumento inválido: Debe ser Piedra, Papel o Tijera')
    
else:
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
    else :
        print('Empate')