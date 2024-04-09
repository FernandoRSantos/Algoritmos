ano = input("Digite uma data <DD/MM/AAAA>: ")
data = ano.split('/')

print(f"O ano que digitou foi {data[2]}/{data[1]}/{data[0]}")