MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
tem_RG = False

idade = int(input("Informe sua idade: "))

#estruturas condicionais
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")

#estruturas condicionais aninhadas
if tem_RG:
    if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar a CNH.")
    elif idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
    else:
        print("Ainda não pode tirar CNH.")

#if ternário
status = "Sucesso" if idade >= MAIOR_IDADE else "Falha"
print(f"{status} ao retirar a CNH.")