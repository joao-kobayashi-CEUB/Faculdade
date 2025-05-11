n1 = float(input("primeiro número: "))
n2 = float(input("segundo número: "))
op = input("qual operação deseja realizar entre eles? \n [+, -, *, /]")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)