################
# Sebastian Scheel - @sebastianscheel
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from soporte import minimo,maximo 
lista=[]
cantidad_valores=int(input("cantidad de valores de la lista: "))
for i in range (cantidad_valores):
    lista.append(input("ingresar valor:"))
print(f"esta es la lista: ",lista)
maximo(lista)
minimo(lista)