x = input("Digite uma frase: ")

qtd = 0

for letra in x:
    if letra == 'a' or letra == 'A' or letra == 'ã':
        qtd = qtd + 1

print("Existem ", qtd, "letras 'a' na sua frase!")