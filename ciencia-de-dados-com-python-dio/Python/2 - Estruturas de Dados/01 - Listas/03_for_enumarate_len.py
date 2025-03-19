carros = ["gol", "celta", "palio"]

for carro in carros:
	print(carro)

for i in range(len(carros)):
	print(carros[i])

for i in range(0,len(carros),2):
	print(carros[i])

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")