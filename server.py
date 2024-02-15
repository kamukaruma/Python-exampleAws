from flask import Flask
import os
import random
PORT = 8080

#Minijuego de adivinar números --> AKINATOR

#Generar un número aleatorio entre 0 y 100
numero_secreto = random.randint(1, 100)

#Bienvenida al juego
print("Bienvenido al jugo de adivinar números")

#Establecemos el número de intentos a 0 al inicio del juego
intentos = 0

#Lógica del juego
while True:
    eleccion = int(input("Adivina el número entre 0 y 100: \n"))
    intentos += 1

    if eleccion == numero_secreto:
        print(f"Has adivinado el número secreto, el número secreto es {numero_secreto}, y lo has adivinado en {intentos} intentos")
        break #salimos del bucle 

    elif eleccion < numero_secreto:
        print("El número secreto es más alto")
    
    else:
        print("el número secreto es más bajo")
