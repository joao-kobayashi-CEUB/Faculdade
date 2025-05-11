a = float(input("lado um: "))
b = float(input("lado dois: "))
c = float(input("lado três: "))

if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("É um triângulo equilátero")
    elif a == b or b == c or c == a:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")
