def eprimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Digite um número inteiro positivo: "))

l = []
o = []

for i in range(x):
    if eprimo(i):
        l.append(i)
    else:
        o.append(i)

print(f"A quantidade de números primos em {x} é: {len(l)}")

print(f"O valor da soma de todo os números primos em {x} é: {sum(l)}")