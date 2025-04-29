import random

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

opcionJudagor = input('Ingrese las 3 opciones separadas por espacio (piedra, papel o tijera): ')

opcionJudagor = opcionJudagor.strip().lower()
jugadasHumano = opcionJudagor.split()

if len(jugadasHumano) != 3:
    print('Por favor ingrese 3 opciones.')
    exit()

opcionesJuego = ['piedra', 'papel', 'tijera']
for jugada in jugadasHumano:
    if jugada not in opcionesJuego:
        print('*Opción inválida*', jugada)
        exit()

jugadasPrograma = []
contador = 3
while contador > 0:
    numRandom = random.randrange(0,3)
    jugadasPrograma.append(opcionesJuego[numRandom])
    contador -=1

print('El programa elige:',(jugadasPrograma))

puntosHuman = 0
puntosProgram = 0

while contador <3:
    resultadoRetorn = compararOpciones(jugadasHumano[contador],jugadasPrograma[contador])
    if resultadoRetorn == -1:
        puntosProgram +=1
    elif resultadoRetorn == 1:
        puntosHuman += 1
    contador +=1

print('------- H - P')
print('Punteo:', puntosHuman, '-', puntosProgram)

if puntosHuman > puntosProgram:
    print('Ganador: Humano')
elif puntosProgram > puntosHuman:
    print('Ganador: Programa')
else:
    print('Resultado: Empate')