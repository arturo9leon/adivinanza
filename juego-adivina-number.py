import random


def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinando = False

    # primeras lineas del juego
    print("bienvenido al juego de adivinanza")
    print("debes adivinar el nnumero del 1 al 100")
    print("Intenta adivinanrlo")

    while not adivinando:
        # solicitar un numero del 1 al 100
        adivinanza = input("Introdusca un numero del 1 al 100: ")

        # "verificar la entrada sea un numero"
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # de string a number
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"el numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"el numero secreto es menos a {adivinanza}")
            else:
                print(
                    f"Felicitaciones has ganado el numero {adivinanza} es el numero secreto"
                )

        else:
            print("introdusca un numero")


juego_adivinanza()
