lista = []
lista2 = []

for i in range(5):
    v1 = int(input(f"Digite o valor de {1+i} da 1° lista: "))
    lista.append(v1)

for u in range(5):
    v2 = int(input(f"Digite o valor de {1+u} da 2° lista: "))
    lista2.append(v2)

lista3 = lista + lista2

print(f"{lista3} é a combinação das duas listas!")