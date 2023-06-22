import math

def op1():
    print("Calcular el perimetro de un circulo de radio : ...")
    rad=input()
    rad= float(rad)
    resultado= 2 * (math.pi * rad)
    print("")
    print("")
    print ("el resultado del perimetro es : " , resultado)
    print("")
    print("")

def op2():
    print("Calcular el area de un circulo de radio : ...")
    rad=input()
    rad= float(rad)
    resultado=(math.pi * (rad * rad))
    print("")
    print("")
    print ("el resultado del area es : " , resultado)
    print("")
    print("")

def op3():
    print("Calcular el diametro de un circulo de radio : ...")
    rad=input()
    rad= float(rad)
    resultado=(rad * 2)
    print("")
    print("")
    #print ("el resultado del diametro es : " , resultado)
    print (f"El resultado del diametro es: {resultado}")
    print("")
    print("")

while True:
    print("selecciona una opcion: ")
    print("1 - calcula el perimetro")
    print("2 - calcula el area")
    print("3 - calcula el diametro")
    print("4 - salir")

    x = input()
    print(x)

    if x == "1":
        print("opcion 1")
        op1()
    elif x == "2":
        print ("opcion 2")
        op2()
    elif x == "3":
        print ("opcion 3")
        op3()
    elif x == "4":
        break
    else:
        print ("")
        print ("No has pulsado nada válido")
        print ("")