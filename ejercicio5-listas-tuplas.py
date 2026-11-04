cantidad = int(input("¿Cuántas letras? "))

letras = []

for i in range(cantidad):
    letra = input("Letra: ").lower()
    letras.append(letra)

print("a:", letras.count('a'))
print("e:", letras.count('e'))
print("i:", letras.count('i'))
print("o:", letras.count('o'))
print("u:", letras.count('u'))
