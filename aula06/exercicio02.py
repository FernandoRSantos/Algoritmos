x = float(input("Digite o valor da compra: "))

if x <= 1000:
    d = x * 0.10
    D = 10

elif x <= 5000:
    d = x * 0.20
    D = 20

else:
    d = x * 0.30
    D = 30

v = x - d

print("A sua compra tem ", D, "% de desconto!")
print("E com o desconto aplicado, sua compra está agora no valor de R$", v, "!")