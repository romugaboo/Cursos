#comando append insere valores
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

#comando extend junta listas

linguagens = ["python", "js", "c"]
print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])
print(linguagens)  # ["python", "js", "c", "java", "csharp"]