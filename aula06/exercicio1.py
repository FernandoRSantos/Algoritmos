x = int(input("Digite um número inteiro: "))

if not(x % 5) == 0:
    print("Este número não é divisível por 5!")

else:
    if not(x % 3) == 0:
        print("Este número não é divisível por 3!")

    else:
        print("Este número é divisível por 5 e 3!")