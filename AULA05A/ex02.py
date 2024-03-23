n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

ma = (n1 + n2) / 2

print("Sua média foi: ", ma)

if ma >= 6.0:
    print("Aprovado!")

else:
    print("Reprovado!")