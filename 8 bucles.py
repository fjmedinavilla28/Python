contador = 0
#print('2 elevedo a la ' + str(contador) + ' es igual a: ' + str(2**contador))
def run():
    LIMITE = 10000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevedo a la ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
             

if __name__ == '__main__':
    run()
