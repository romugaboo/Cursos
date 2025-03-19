texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#for
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
print()

#for e range (começo inclusivo, fim exclusivo, iteração opcional 1 por padrão)
print(list(range(0, 5)))
for numero in range (0, 51, 5):
    print(numero, end = " ")
print()

#while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
print("Obrigado por usar nosso sistema bancário!")

#interrompe laço no break
for numero in range(20):
    if numero == 12:
        break
    print(numero, end = " ")
print()

#pula o número 12 e continua pulando o restante do for
for numero in range(20):
    if numero == 12:
        continue
    print(numero, end = " ")
print()

#pula o número 12 e continua após o if
for numero in range(20):
    if numero != 12:
        print(numero, end = " ")
print()