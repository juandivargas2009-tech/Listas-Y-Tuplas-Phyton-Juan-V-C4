cantidad = int(input("Cantidad: "))

numeros = []

for i in range(cantidad):
    numero = int(input())
    numeros.append(numero)

buscar = int(input("Número a buscar: "))

posicion = -1

for i in range(len(numeros)):
    if numeros[i] == buscar:
        posicion = i
        break

if posicion != -1:
    print("El", buscar, "está en la posición", posicion)
else:
    print("El", buscar, "no está en la lista")
 