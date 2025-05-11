N = int(input("Digite o número aqui: "))

Par = 0
Impar = 0
qntPar = 0
qntImpar = 0

while N != 0:

    if N % 2 == 0:
        Par += N
        qntPar += 1
    else:
        Impar += N
        qntImpar += 1
    N = int(input("Digite o número aqui: "))

print("Média dos pares:", Par/qntPar)
print("Média dos ímpares:", Impar/qntImpar)

