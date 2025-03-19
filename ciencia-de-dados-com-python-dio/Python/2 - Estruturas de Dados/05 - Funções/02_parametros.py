#obrigatório definir argumentos por posição antes da /
def criar_carro1(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro1("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")

#obrigatório definir argumentos por nome após o *
def criar_carro2(modelo, ano, placa, marca, * , motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#híbrido: * e /
def criar_carro3(modelo, ano, placa, / , marca, * , motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro3("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")