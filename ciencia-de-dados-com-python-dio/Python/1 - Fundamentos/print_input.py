nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
# end = "\n" por padrão
print(nome, idade, end = "... \n")

# sep = " " por padrão
print(nome, idade, sep = "-")

#pode usar ambos ao mesmo tempo
print(nome, idade, sep = "-", end = "... \n")