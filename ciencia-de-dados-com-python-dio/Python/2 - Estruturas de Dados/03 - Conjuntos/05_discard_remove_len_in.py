numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

#discard: retira o valor, caso ele não exista, não gera erro
numeros.discard(1)
numeros.discard(45)

#pop: retira o primeiro valor
numeros.pop()

#remove: retira o valor, porém da erro se ele não existir
numeros.remove(4)

print(numeros)

print(len(numeros))

print(1 in numeros)
print(6 in numeros)