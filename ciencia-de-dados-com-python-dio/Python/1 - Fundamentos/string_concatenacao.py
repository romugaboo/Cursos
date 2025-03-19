nome = "Lari"
idade = 20
profissao = "programadora"
linguagem = "Python"
saldo = 198.75

dicionario = {"nome": "Lari", "idade": 20}

#estilo %: antigo, herdado do C
print("Nome: %s Idade: %d" % (nome, idade))

#estilo .format(): menos legível
print("Nome: {} Idade: {}". format(nome, idade))
print("Nome: {1} Idade: {0}". format(idade, nome))
print("Nome: {name} Idade: {age}". format(name = nome, age = idade))
print("Nome: {nome} Idade: {idade}". format(**dicionario))

# estilo f: recomendado
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")