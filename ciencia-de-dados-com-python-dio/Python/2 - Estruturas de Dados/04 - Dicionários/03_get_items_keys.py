contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

resultado = contatos.items()
print(resultado) # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

resultado = contatos.keys()
print(resultado)  # dict_keys(['guilherme@gmail.com'])
