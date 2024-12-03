nome = input("Qual nome do Aluno: ")


simulado = float(input(f"Digite a nota do simulado do {nome}: "))
prova = float(input(f"Digite a nota da prova do {nome}: "))
comportamento = float(input(f"Qual será a nota de comportamento do {nome}: "))


nota = simulado + prova + comportamento


if nota >= 6:
    print(f"A nota final do {nome} é: {nota}")
    print(f"{nome} está Aprovado(a)")
else:
    print(f"A nota final do {nome} é: {nota}")
    print(f"{nome} está de Recuperação")