vh = float(input("Digite o valor da sua hora trabalhada: "))
ht = int(input("Digite a quantidade de horas trabalhadas no mês: "))

sb = vh * ht

if sb <= 900:
    ir = 0
    aliquota = 0

elif sb <= 1500:
    ir = (sb * 5) / 100
    aliquota = 5

elif sb <= 2500:
    ir = (sb * 10) / 100
    aliquota = 10

else:
    ir = (sb * 20) / 100
    aliquota = 20


inss = (sb * 10) / 100
fgts = (sb * 11) / 100
ip = (sb * 3) / 100
td = ir + inss
sl = sb - td

print("Salário Bruto: (", vh, "*", ht, ") : R$", sb)
print("(-) IR (", aliquota, "%)                : R$ ", ir)
print("(-) INSS (10%)               : R$ ", inss)
print("FGTS (11%)                   : R$ ", fgts)
print("Total de Descontos           : R$ ", td)
print("Salário Líquido              : R$ ", sl)
