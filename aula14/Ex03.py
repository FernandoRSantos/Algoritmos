x = input("Digite um valor: ")

y = list(x)
z = []

for i in y:
    z.append(int(i))

soma = sum(z)
m = 1

for i in range(len(y)):
    m = z[i] * m

print(soma)
print(m)
