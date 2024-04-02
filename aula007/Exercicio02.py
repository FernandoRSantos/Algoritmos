maior_imc = 0
menor_imc = 100
sp = 0
sh = 0

for k in range(1,6):
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    sh = sh + altura
    sp = sp + peso
    pm = sp / 5
    hm = sh / 5
    k = k + 1
print("resultados:")
print(f"Média Altura: {hm:5.2f}")
print(f"Média Peso: {pm:5.2f}")

