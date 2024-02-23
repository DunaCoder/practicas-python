import random

opciones = ("piedra", "papel", "tijera")

print("¡Bienvenido al juego de piedra, papel o tijera!")

rondas = 0
puntuacion_jugador = 0
puntuacion_maquina = 0

while rondas < 5:
    opciones_jugador = input("Escoge (piedra, papel, tijera): ").lower()
    maquina = random.choice(opciones)
    print(f"Elegiste: {opciones_jugador}")
    print(f"La máquina eligió: {maquina}")

    # if opciones_jugador != opciones:
    #     print("opcion no validad")
    #     puntuacion_jugador = 0
    #     puntuacion_maquina = 0
    if opciones_jugador == maquina:
        print("Empate.")

    elif opciones_jugador == "tijeras" and (maquina == "piedra" or maquina == "tijera"):
        print("¡Ganaste!")
        puntuacion_jugador += 1

    elif opciones_jugador == "papel" and (maquina == "piedra" or maquina == "tijera"):
        print("¡Ganaste!")
        puntuacion_jugador += 1

    elif opciones_jugador == "piedra" and (maquina == "papel" or maquina == "tijera"):
        print("¡Ganaste!")
        puntuacion_jugador += 1

    else:
        print("¡Perdiste!")
        puntuacion_maquina += 1

    rondas += 1

print(f"Rondas jugadas: {rondas}")
print(f"Tu puntuación: {puntuacion_jugador}")
print(f"Puntuación de la máquina: {puntuacion_maquina}")

if puntuacion_jugador > puntuacion_maquina:
    print("¡Felicidades, ganaste el juego!")
elif puntuacion_jugador < puntuacion_maquina:
    print("Lo siento, la máquina ganó el juego.")
else:
    print("¡Empate! Ambos jugadores tienen la misma puntuación.")
