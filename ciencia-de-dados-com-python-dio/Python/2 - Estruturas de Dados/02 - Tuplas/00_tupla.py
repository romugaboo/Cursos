#tuplas são imutáveis, coloca-se vírgula no final
frutas = ("laranja", "pera", "uva",)
print(frutas)
print(frutas[0])  # laranja
print(frutas[2])  # uva
print(frutas[-1])  # uva
print(frutas[-2])  # pera

#tuple: comando antigo pouco usado
letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

#modo sem tuple, vírgula no final obrigatória para um único elemento
pais = ("Brasil",)
print(pais)


