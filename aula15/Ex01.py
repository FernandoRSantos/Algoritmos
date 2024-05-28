from random import choice

x = input("Escolha 'pedra, papel ou tesoura': ").upper()

e = ('PEDRA', 'PAPEL', 'TESOURA')

r = choice(e)

if (x == 'PEDRA' and r == 'PAPEL') or (x == 'PAPEL' and r == 'TESOURA') or (x == 'TESOURA' and r == 'PEDRA'):
    print("Você acabou de perder!")


elif (x == 'PEDRA' and r == 'TESOURA') or (x == 'PAPEL' and r == 'PEDRA') or (x == 'TESOURA' and r == 'PAPEL'):
    print('Eu acabei de perder, parabéns!')


elif (x == 'PEDRA' and r == 'PEDRA') or (x == 'PAPEL' and r == 'PAPEL') or (x == 'TESOURA' and r == 'TESOURA'):
    print('Deu empate, vamos jogar denovo!')