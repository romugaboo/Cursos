menu = """
Bem-Vinde ao Sistema Bancário!
===========MENU===========
1 - Depositar
2 - Sacar
3 - Ver extrato
0 - Sair
==========================
"""

saldo = 0
extrato = ""
num_saques = 0
LIMITE_NUM_SAQUES = 3
LIMITE_VALOR_SAQUES = 500

while True:
	opcao = input(menu)

	if opcao == "1":
		deposito = float(input("Digite o valor que deseja depositar: "))

		if deposito > 0:
			saldo += deposito
			extrato = f"Depósito = +R$: {deposito}\n"
			print("Depósito efetuado com sucesso.")
		else:
			print("Esse valor para depósito é inválido.")

	elif opcao == "2":
		saque = float(input("Digite o valor que deseja sacar (até R$: 500.00): "))
		excedeu_saldo = saque > saldo
		excedeu_limite = saque > LIMITE_VALOR_SAQUES
		excedeu_saques = num_saques >= LIMITE_NUM_SAQUES

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

	elif opcao == "3":
		print("=========EXTRATO=========")
		print("Não foram realizadas movimentações." if not extrato else extrato)
		print(f"\nSaldo atual = R$: {saldo:.2f}")
		print("=========================")

	elif opcao == "0":
		print("Sistema bancário encerrado.")
		break

	else:
		print("Operação inválida, tente novamente.")