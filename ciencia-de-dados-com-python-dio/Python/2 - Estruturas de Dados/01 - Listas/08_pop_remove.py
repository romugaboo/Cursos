#pop elimina o último elemento ou elemento especificado via index
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
print(linguagens) # js

#remove elimina a primeira instância do elemento
linguagens = ["python", "js", "c", "java", "csharp", "c"]

linguagens.remove("c")
print(linguagens)  # ["python", "js", "java", "csharp", "c"]