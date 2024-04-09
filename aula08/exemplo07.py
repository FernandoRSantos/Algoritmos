nome = input("Digite seu nome completo: ")
nascimento = input("Digite sua data de nasc <DD/MM/AAAA>: ")
data = nascimento.split('/')
print(data)
palavra = nome.split()
pre_nome = palavra[0]
sobrenome = palavra[1]

print(f"Olá {pre_nome}... muito bonito seu sobrenome: {sobrenome}")
print(f"Você nasceu no {data[0]} do {data[1]} de {data[2]}")
