import random
import sys

def compararOpciones(Op1, Op2):
    if Op1 == Op2:
        return 0
    if Op1 == 'piedra' and Op2 == 'tijera':
        return 1
    if Op1 == 'papel' and Op2 == 'piedra':
        return 1
    if Op1 == 'tijera' and Op2 == 'papel':
        return 1
    return -1

if __name__=="__main__":
    
    jugadasHumano = sys.argv[1:]

    if len(jugadasHumano) != 3:
        print('Por favor ingrese 3 opciones (piedra, papel o tijera).')
        sys.exit()

    jugadasLimpias = []
    for jugada in jugadasHumano:
        jugadaLimpia = jugada.strip().lower()
        jugadasLimpias.append(jugadaLimpia)
    jugadasHumano = jugadasLimpias

    opcionesJuego = ['piedra', 'papel', 'tijera']
    for jugada in jugadasHumano:
        if jugada not in opcionesJuego:
            print('Opción inválida:', jugada)
            sys.exit()

    jugadasPrograma = []
    contador = 3
    while contador > 0:
        numRandom = random.randrange(0, 3)
        jugadasPrograma.append(opcionesJuego[numRandom])
        contador -= 1

    print('El programa elige:', jugadasPrograma)

    contador = 0
    puntosHuman = 0
    puntosProgram = 0

    while contador < 3:
        resultadoRetorn = compararOpciones(jugadasHumano[contador], jugadasPrograma[contador])
        if resultadoRetorn == -1:
            puntosProgram += 1
        elif resultadoRetorn == 1:
            puntosHuman += 1
        contador += 1
    print('------- H - P')
    print('Punteo:', puntosHuman, '-', puntosProgram)

    if puntosHuman > puntosProgram:
        print('Ganador: Humano')
    elif puntosProgram > puntosHuman:
        print('Ganador: Programa')
    else:
        print('Resultado: Empate')