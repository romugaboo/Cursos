saldo = 1000
saque = 250
limite = 200
conta_especial = True

#difícil visualização
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

#fácil visualização
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

# is ou is not para igualdade de referências
print(saldo is limite)
print(saldo is not limite)

# = ou != para igualdade de valores
print(saldo == limite)
print(saldo != limite)

# in ou not in para verificar se o elemento existe
frutas = ["limão", "uva"]
print("maçã" in frutas)
print("limão" not in frutas)

# funciona mesmo se for apenas parte do todo
curso = "curso de python"
print("python" in curso)