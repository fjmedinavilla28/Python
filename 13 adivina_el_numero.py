import random

def run():

    print("""
    Bienvenido a este fabuloso juego
    Debe esconger un número y de acuerdo
    a las indicaciones del computador, lo
    vas cambiando para adivinar
    ¡Mucha suerte!
    """)

    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100:'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
        
    print('¡ Ganaste Alejito!')

if __name__ == '__main__':
    run()