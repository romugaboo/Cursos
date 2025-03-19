#dict: {chave, valor} chave precisa ser imutável
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  
print(pessoa) # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(pessoa["nome"])  # "Guilherme"
print(pessoa["idade"])  # 28
print(pessoa["telefone"])  # "3333-1234"

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-1781"

print(pessoa)

#dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)