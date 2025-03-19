numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False if input() == "n" else True
    
    if ehVegano:
        tipoVegano = "Vegano"
    else:
        tipoVegano = "Nao-vegano"

    print(f'Pedido {i}: {prato} ({tipoVegano}) - {calorias} calorias')