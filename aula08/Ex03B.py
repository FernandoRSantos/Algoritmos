v = 0
frase = input("Digite uma frase: ")

for vogal in "AEIOUaeiouãâÃÂõôÕÔÉéêÊ":
    v = v + frase.count(vogal)

print(f"Sua frase tem {v} vogal(is)!")