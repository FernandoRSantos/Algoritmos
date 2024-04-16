lista = []
for i in range(5):
    v = int(input(f"Digite o valor de {1+i}: "))
    lista.append(v)

print(max(lista))

m = max(lista)

print(lista.index(m))