import random
import matplotlib.pyplot as plt


def piedra_papel_tijeras():
    # Seteamos los valores a tomar de manera aleatoria por la pc
    set = ["piedra", "papel", "tijera"]
    # Le decimos a la pc que tome un valor aleatorio entre los 3
    pc_pick = random.choice(set)
    # Le pedimos al jugador que seleccione entre las 3 opciones
    pick = int(input("Ingrese 1 para piedra \nIngrese 2 para papel \nIngrese 3 para tijera \nSu opción: "))
    # Verificamos que el jugador haya respondido correctamente y le asignamos el valor a la variable pick
    while pick != 1 and pick != 2 and pick != 3:
        pick = int(input("Por favor seleccione un valor válido! \n", "Ingrese 1 para piedra \n", "Ingrese 2 para papel \n", "Ingrese 3 para tijera"))
    if pick == 1:
        pick = "piedra"
    elif pick == 2:
        pick = "papel"
    elif pick == 3:
        pick = "tijera"
    # Seteamos los enfrentamientos para cuando la PC elija piedra
    if pc_pick == "piedra":
        if pick == "piedra":
            print("Oh oh! Empate!")
        elif pick == "papel":
            print("¡¡¡Jugador Gana!!!")
        elif pick == "tijera":
            print("La Computadora ha ganado! :(")
    # Seteamos los enfrentamientos para cuando la PC elija papel
    elif pc_pick == "papel":
        if pick == "piedra":
            print("La Computadora ha ganado! :(")
        elif pick == "papel":
            print("Oh oh! Empate!")
        elif pick == "tijera":
            print("¡¡¡Jugador Gana!!!")
    # Seteamos los enfrentamientos para cuando la PC elija tijera
    elif pc_pick == "tijera":
        if pick == "piedra":
            print("¡¡¡Jugador Gana!!!")
        elif pick == "papel":
            print("La Computadora ha ganado! :(")
        elif pick == "tijera":
            print("Oh oh! Empate!")
    # Le preguntamos al usuario si desea volver a jugar
    otra_vez = input("Deseas volver a jugar? (si/no): ")
    while otra_vez != "si" and otra_vez != "no":
        otra_vez = input("Por favor ingrese un valor válido! \nDeseas volver a jugar? (si/no): ")
    if otra_vez == "si":
        piedra_papel_tijeras()
    else:
        principal()


def dado():
    # Le damos la bienvenida al usuario
    input("Bienvenido al dado loco! Presiona enter para continuar...")
    # Seteamos la cara del dado
    cara = random.randint(1,6)
    # Imprimimos el resultado
    print("El dado ha dado la cara ", cara, " !!!")
    # Le preguntamos al usuario si desea volver a jugar
    otra_vez = input("Deseas volver a jugar? (si/no): ")
    while otra_vez != "si" and otra_vez != "no":
        otra_vez = input("Por favor ingrese un valor válido! \nDeseas volver a jugar? (si/no): ")
    if otra_vez == "si":
        dado()
    else:
        principal()


def funcion_matematica():
    cant_puntos = int(input("Seleccione cuantos puntos desee tener (Máximo 4): "))
    while cant_puntos != 1 and cant_puntos != 2 and cant_puntos != 3 and cant_puntos != 4:
        cant_puntos = int(input("Valor inválido!!! \nSeleccione cuantos puntos desee tener (Máximo 4): "))
    # Para cuando sea 1 punto
    if cant_puntos == 1:
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Pedir los puntos
        punto_1_x = float(input("Seleccione el valor para el primer punto x: "))
        punto_1_y = float(input("Seleccione el valor para el primer punto y: "))
        # Dibujar puntos
        ax.scatter([punto_1_x], [punto_1_y])
        # Mostrar el gráfico
        plt.show()
        
        guardar_grafico = input("¿Desea guardar el gráfico? (si/no): ")
        while guardar_grafico != "si" and guardar_grafico != "no":
            guardar_grafico = input("Su respuesta ha sido inválida. ¿Desea guardar el gráfico? (si/no): ")
        if guardar_grafico == "si":
            # Guardar el gráfico en formato png
            plt.savefig("diagrama-dibujado.png")
            principal()
        else:
            principal()
    # Para cuando sean 2 puntos
    if cant_puntos == 2:
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Pedir los puntos
        punto_1_x = float(input("Seleccione el valor para el primer punto x: "))
        punto_1_y = float(input("Seleccione el valor para el primer punto y: "))
        punto_2_x = float(input("Seleccione el valor para el segundo punto x: "))
        punto_2_y = float(input("Seleccione el valor para el segundo punto y: "))
        # Dibujar puntos
        ax.plot([punto_1_x, punto_2_x], [punto_1_y, punto_2_y])
        # Mostrar el gráfico
        plt.show()
        
        guardar_grafico = input("¿Desea guardar el gráfico? (si/no): ")
        while guardar_grafico != "si" and guardar_grafico != "no":
            guardar_grafico = input("Su respuesta ha sido inválida. ¿Desea guardar el gráfico? (si/no): ")
        if guardar_grafico == "si":
            # Guardar el gráfico en formato png
            plt.savefig("diagrama-dibujado.png")
            principal()
        else:
            principal()
    # Para cuando sean 3 puntos
    if cant_puntos == 3:
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Pedir los puntos
        punto_1_x = float(input("Seleccione el valor para el primer punto x: "))
        punto_1_y = float(input("Seleccione el valor para el primer punto y: "))
        punto_2_x = float(input("Seleccione el valor para el segundo punto x: "))
        punto_2_y = float(input("Seleccione el valor para el segundo punto y: "))
        punto_3_x = float(input("Seleccione el valor para el tercer punto x: "))
        punto_3_y = float(input("Seleccione el valor para el tercer punto y: "))
        # Dibujar puntos
        ax.plot([punto_1_x, punto_2_x, punto_3_x], [punto_1_y, punto_2_y, punto_3_y])
        # Mostrar el gráfico
        plt.show()
        
        guardar_grafico = input("¿Desea guardar el gráfico? (si/no): ")
        while guardar_grafico != "si" and guardar_grafico != "no":
            guardar_grafico = input("Su respuesta ha sido inválida. ¿Desea guardar el gráfico? (si/no): ")
        if guardar_grafico == "si":
            # Guardar el gráfico en formato png
            plt.savefig("diagrama-dibujado.png")
            principal()
        else:
            principal()
    # Para cuando sean 4 puntos
    if cant_puntos == 4:
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Pedir los puntos
        punto_1_x = float(input("Seleccione el valor para el primer punto x: "))
        punto_1_y = float(input("Seleccione el valor para el primer punto y: "))
        punto_2_x = float(input("Seleccione el valor para el segundo punto x: "))
        punto_2_y = float(input("Seleccione el valor para el segundo punto y: "))
        punto_3_x = float(input("Seleccione el valor para el tercer punto x: "))
        punto_3_y = float(input("Seleccione el valor para el tercer punto y: "))
        punto_4_x = float(input("Seleccione el valor para el cuarto punto x: "))
        punto_4_y = float(input("Seleccione el valor para el cuarto punto y: "))
        # Dibujar puntos
        ax.plot([punto_1_x, punto_2_x, punto_3_x, punto_4_x], [punto_1_y, punto_2_y, punto_3_y, punto_4_y])
        # Mostrar el gráfico
        plt.show()
        
        guardar_grafico = input("¿Desea guardar el gráfico? (si/no): ")
        while guardar_grafico != "si" and guardar_grafico != "no":
            guardar_grafico = input("Su respuesta ha sido inválida. ¿Desea guardar el gráfico? (si/no): ")
        if guardar_grafico == "si":
            # Guardar el gráfico en formato png
            plt.savefig("diagrama-dibujado.png")
            principal()
        else:
            principal()

def principal():
    print("¡¡¡Bienvenido a la ruleta de los juegos!!!\n")
    juego = int(input("Seleccione a que juego desea jugar! \n1- Piedra/Papel/Tijera \n2- Tirar un dado \n3- Graficar una función matemática " +
    "\n4- Salir \nElija su opción (1/2/3/4): "))
    while juego != 1 and juego != 2 and juego != 3 and juego != 4:
        juego = int(input("\n\n\nPor favor, seleccione un juego válido \nSeleccione a que juego desea jugar! \n1- Piedra/Papel/Tijera " +
        "\n2- Tirar un dado \n3- Graficar una función matemática \n4- Salir \nElija su opción (1/2/3/4): "))
    if juego == 1:
        piedra_papel_tijeras()
    elif juego == 2:
        dado()
    elif juego == 3:
        funcion_matematica()
    elif juego == 4:
        print("¡¡¡Gracias por jugar con nosotros!!! :D")
        exit


principal()
