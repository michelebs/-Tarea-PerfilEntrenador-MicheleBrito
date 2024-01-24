#sexo del jugador
print("----------------------------------------------------------------")
x=input("¿Eres chico o chica?: ")
w="Bienvenid"
if x=="chico":
    w+= "o"
else:
    w+= "a"
print("----------------------------------------------------------------")
print(w,"al mundo de los pokemon")
print("----------------------------------------------------------------")

# edad del jugador (limite)
y=input("¿Qué edad tienes?: ")
if int(y)<10:
    if x=="chico":
        print("No tienes edad para ser entrenador")
    else:
        print("No tienes edad para ser entrenadora")
print("----------------------------------------------------------------")

#compañero de viaje
reg=input("Necesitarás un compañero de viaje. ¿En que región  te encuentras?: ")
if reg=="Kanto"and x=="chico":
    print("Tu compañera de viaje es Misty!")
else:
    print("Tu compañero de viaje es Brook!")
print("----------------------------------------------------------------")

# escogencia del pokemon del jugador
tipo=input("¿Qué tipo de pokemon quieres para empezar?: ")
if tipo=="agua":
    print("Tu starter es Oshawott")
elif tipo=="fuego":
    print("Tu starter es Cyndaquil")
else:
    print("Tu starter es Rowlet")
print("----------------------------------------------------------------")