isOver = "não"

qntProva = 0
qntAprov = 0
qntReprov = 0

while isOver == "não":
    N = int(input("Digite o valor da nota do aluno aqui: "))
    qntProva += 1

    if N >= 5:
        qntAprov += 1
    else:
        qntReprov += 1



    isOver = input("Já acabou? digite sim ou não: ")
print(qntProva, "alunos fizeram a prova")
print(qntAprov, "alunos foram aprovados")
print(qntReprov, "alunos foram reprovados")
