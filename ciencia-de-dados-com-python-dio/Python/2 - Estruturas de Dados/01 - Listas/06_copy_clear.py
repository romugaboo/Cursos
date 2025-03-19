#duplica a lista para que seja passado uma apenas cópia dela para função
lista = [1, "Python", [40, 30, 20]]
lista2 = lista.copy()

print(lista)
print(lista2)
print(id(lista2), id(lista))

lista.clear()
print(lista)  # []