Px = float(input("Digite aqui a primeira coordenada X: "))
Py = float(input("Digite aqui a primeira coordenada Y: "))

Qx = float(input("Digite aqui a segunda coordenada X: "))
Qy = float(input("Digite aqui a segunda coordenada Y: "))

#eu pensei em usar listas mas o input ficaria meio complexo para o usuário(ter q colocar x, y) 
#e o código ficaria meio chatinho de fazer tendo q pegar a primeira posição as duas listas e dps pegar a segunda posição delas tb

print("a distância entre os pontos é de:", ((Px - Qx)**2 + (Py - Qy)**2)**(1/2))