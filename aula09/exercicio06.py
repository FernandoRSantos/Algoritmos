from random import randint

resultado = [0]*13
freq = [0]*13

for i in range(30000):
    lado = randint(1, 6)
    lado2 = randint(1,6)
    soma = lado + lado2
    resultado[soma] = resultado[soma] + 1

print(resultado)
print(freq)

for i in range(2, 13):
    freq[i] = (resultado[i] / 30000) * 100

for i in range(2, 13):
    print(f"{i} - {resultado[i]} - {freq[i]:6.2f}%")