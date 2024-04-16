lista = []
for i in range(10):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

lista.reverse()
print(lista)