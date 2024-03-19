l1 = int(input("Digite seu o lado A: "))
l2 = int(input("Digite seu o lado B: "))
l3 = int(input("Digite seu o lado C: "))
if ((l1+l2) < l3) or ((l2+l3) < l1) or ((l3+l1) < l2):
    input("Isso não é um triângulo!")
elif l1 == l2 == l3:
    input("Este é um triângulo retângulo!")
elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    input("Este é um triângulo isóceles!")
else:
    input("Este é um triângulo Escaleno")