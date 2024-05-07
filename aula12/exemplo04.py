from math import pow

def potencia (numero, expoente = 2):
    
    resultado = pow(numero, expoente)
    return resultado

n = float(input("Digite o número: "))
e = int(input("Expoente: "))

print(f"Valor com expoente: {potencia(n,e)}")

print(potencia(expoente = e, numero = n))

print(f"Valor sem o expoente: {potencia(n)}")