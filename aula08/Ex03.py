v = 0
frase = input("Digite uma frase: ")

for letra in frase:
    if letra.upper() in "AEIOU":
        v = v+1

print(f"Sua frase tem {v} vogal(is)!")
