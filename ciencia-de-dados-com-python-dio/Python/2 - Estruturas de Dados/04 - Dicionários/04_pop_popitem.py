contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
            "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "Não encontrado")  # {}
print(resultado)

#popitem: remove o último elemento
contatos.popitem()
print(contatos)