alunos = []
while True:
    nome = str(input("Digite o nome do Aluno: ")).strip().upper()
    nota1 = float(input("1 Nota: "))
    nota2 = float(input("2 Nota: "))
    print("=" * 20)
    media = (nota1 + nota2) / 2
    alunos.append((nome, nota1, nota2,media))

    resposta = str(input("Quer continuar ? [S/N]: ")).upper().strip()[0]
    if resposta not in "SN":
        resposta = str(input("Digite [S/N]: "))
    else:
        if resposta == "N":
            break
print("-=" * 50)
print("No.  NOME     MEDIA")
print("_"* 25)
for i, aluno in enumerate(alunos):
    print("{:>2} {:>10} {:>5.1f}".format(i + 1, aluno[0],aluno[3]))
print("=" * 70)
while True:
    notas = int(input("Gostaria de ver as notas de qual aluno? (Digite 999 para cancelar): "))
    if notas == 999:
        print("\033[031mEncerrando Programa")
        break
    elif notas > 0 and notas <= len(alunos):
        aluno = alunos[notas - 1]
        print("=" * 50)
        print("As notas do aluno {} são [{:.1f}],[{:.1f}] e sua media é [{:.1f}]".format(aluno[0], aluno[1],aluno[2],aluno[3]))
        if media >= 7:
            print("\033[32mO aluno {} esta aprovado\033[m".format(aluno[0]))
        elif media < 7:
            print("\033[31mO aluno {} esta reprovado\033[m".format(aluno[0]))
        print("=" * 50)
    else:
        print("Aluno não encontrado.Tente novamente")


