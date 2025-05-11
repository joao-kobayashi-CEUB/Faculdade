isOver = "não"
soma = 0
M20 = 0
qnt = 0

while isOver == "não":
    N = int(input("Digite o valor aqui: "))
    qnt += 1
    soma += N

    if N > 20:
        M20 += 1



    isOver = input("Já acabou? digite sim ou não: ")
print("Você inseriu", qnt, "números")
print("A soma deles foi:", soma)
print("A média deles foi de:", soma/qnt)
print("A quantidade de números maiores que 20 foram:", M20)
#Dava pra ter feito com lista mas como não precisa guardar os valores inseridos, seria mt trampo pra algo desnecessário