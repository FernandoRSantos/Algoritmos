l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))
q = float(input("Digite a quantidade em litros da lata de tinta: "))

a = l * c
pd = 2.80
p = 0.80 * 2.10
cldtp = q / 3
quanti_latas = round(a / cldtp)

medi_area_pint = (((a / cldtp) - pd) - p)

print("A área pintada será ", medi_area_pint, "!")
print("O que levará", quanti_latas, "latas de tinta!")