def menu():
	menu = """
	Bem-Vinde ao Sistema Bancário!
	===========MENU===========
	1 - Depositar
	2 - Sacar
	3 - Exibir extrato
	4 - Novo Usuário
	5 - Criar Conta
	6 - Listar Contas
	0 - Sair
	==========================
	"""
	return input(menu)

def depositar(saldo, extrato, /):
	deposito = float(input("Digite o valor que deseja depositar: "))
	if deposito > 0:
		saldo += deposito
		extrato = f"Depósito = +R$: {deposito}\n"
		print("Depósito efetuado com sucesso.")
	else:
		print("Esse valor para depósito é inválido.")
	return saldo, extrato

def sacar(*, saldo, extrato, num_saques, limite_num_saques, limite_valor_saques):
	saque = float(input("Digite o valor que deseja sacar (até R$: 500.00): "))
	excedeu_saldo = saque > saldo
	excedeu_limite = saque > limite_valor_saques
	excedeu_saques = num_saques >= limite_num_saques

	if excedeu_saldo:
		print("Operação falhou. Você não tem saldo suficiente.")

	elif excedeu_limite:
		print("Operação falhou. O valor de saque é maior que R$: 500.00.")

	elif excedeu_saques:
		print("Operação falhou. Número de saques diários excedidos.")

	elif saque > 0:
		num_saques += 1
		saldo -= saque
		extrato += f"Saque = -R$: {saque}\n"
		print("Saque efetuado com sucesso.")

	else:
		print("Operação falhou. O valor informado é inválido.")	
	
	return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
	print("=========EXTRATO=========")
	print("Não foram realizadas movimentações." if not extrato else extrato)
	print(f"\nSaldo atual = R$: {saldo:.2f}")
	print("=========================")

def filtrar_usuario(cpf, usuarios):
	usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
	return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
	cpf = input("Informe o CPF (somente número): ")
	usuario = filtrar_usuario(cpf, usuarios)

	if usuario:
		print("\nJá existe usuário com esse CPF!")
		return

	nome = input("Informe o nome completo: ")
	data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
	endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

	usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

	print("Usuário criado com sucesso!")
	
def criar_conta(agencia, usuarios, contas):
	cpf = input("Informe o CPF do usuário: ")
	usuario = filtrar_usuario(cpf, usuarios)

	if usuario:
		print("\n=== Conta criada com sucesso! ===")
		numero_conta = len(contas) + 1
		conta =  {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
		contas.append(conta)

	else:
		print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
	for conta in contas:
		linha = f"""\
			Agência:\t{conta['agencia']}
			Conta:\t\t{conta['numero_conta']}
			Titular:\t{conta['usuario']['nome']}
		"""
		print("=" * 50)
		print(linha)

def main():
	saldo = 0
	extrato = ""
	num_saques = 0
	usuarios = []
	contas = []
	LIMITE_NUM_SAQUES = 3
	LIMITE_VALOR_SAQUES = 500
	AGENCIA = "0001"

	while True:
		opcao = menu()

		if opcao == "1":
			saldo, extrato = depositar(saldo, extrato)

		elif opcao == "2":
			saldo, extrato = sacar(
				saldo = saldo,
				extrato = extrato, 
				num_saques = num_saques,
				limite_num_saques = LIMITE_NUM_SAQUES,
				limite_valor_saques = LIMITE_VALOR_SAQUES
				)

		elif opcao == "3":
			exibir_extrato(saldo, extrato = extrato)

		elif opcao == "4":
			criar_usuario(usuarios)
			
		elif opcao == "5":
			criar_conta(AGENCIA, usuarios, contas)

		elif opcao == "6":
			listar_contas(contas)
			
		elif opcao == "0":
			print("Sistema bancário encerrado.")
			break

		else:
			print("Operação inválida, tente novamente.")

if __name__ == "__main__":
	main()