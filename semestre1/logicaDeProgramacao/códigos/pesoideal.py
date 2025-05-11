sexo = input("Selecione seu sexo: M para masculino e F para feminino: ")
while(sexo not in ("M","F")):
    print("os valores só podem ser M ou F. Por favor escreva novamente")
    sexo = input("Selecione seu sexo: M para masculino e F para feminino: ")

h = float(input("Digite sua altura em metros:"))

if(sexo == "M"):
    print("Seu peso ideal é:", (72.7 * h)-58,"Kg")
else:
    print("Seu peso ideal é:", (62.1 * h)-44.7,"Kg")