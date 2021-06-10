################
# Sebastian Scheel - @sebastianscheel
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
        print("error", err)
    return entero

    
def suma_lenta(numero, otro_numero):
    i=0
    while i<otro_numero:
        numero=(numero+1)
        i=(i+1)
    print("la suma es:",numero)

#def convertir_a_fahrrenheit(centigrados):
#    fahrrenheit= float(centigrados+1)
    
#def convertir_a_centigrados(fahrenheit):
    
def compara(numero,otro_numero):
    if numero<otro_numero:
        print("-1")
    elif numero>otro_numero:
        print("1")
    else:
        print("0")


def signo(numero):
    if numero==0:
        print(f"El numero {numero} es CERO")
    elif (numero > 0):
        print(f"El numero {numero} es POSITIVO")
    else:
        print(f"El numero {numero} es NEGATIVO")

def maximo(lista):
    maximo=lista[0]
    x=0
    for x in cantidad_valores:
     if lista[x]>maximo:
        maximo=lista[x] 
    print(f"El mayor es : ",maximo)
    
def minimo(lista):
    minimo=lista[0]
    for x in range(0,cantidad_valores):
     if lista[x]<minimo:
        minimo=lista[x] 
    print(f"El mayor es : ",minimo)

def division_lenta(dividendo,divisor):
    contador=0
    while dividendo >= divisor:
        dividendo=dividendo-divisor
        contador=contador+1
    print(f"el cociente es: ",contador, " y el resto es:",dividendo)


