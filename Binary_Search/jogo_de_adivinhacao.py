# http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

primeiro = 0
ultimo = 100
running = True
contador = 0

while running:

    chute = []
    for c in range(primeiro, ultimo+1):
        chute.append(c)

    chute_do_meio = (ultimo + primeiro)//2

    contador += 1

    resposta = int(input('''\n\nO número {} está correto?
    
    
        1) Sim
    
        2) Chutou alto
    
        3) Chutou baixo
    
        '''.format(chute_do_meio)))

    if resposta == 1:
        running = False
        print(f'\nAcertei depois de {contador} tentativa(s)! ')
    elif resposta == 2:
        ultimo = chute_do_meio - 1
    elif resposta == 3:
        primeiro = chute_do_meio + 1




"""import random
number=int(input("enter a number less than 9999 :"))
first=0
last=9999
flag=0
count=0
while flag==0:
    guess=random.randint(first,last)
    print(guess)
    count+=1
    if guess>number:
        print("too high")
        last=guess-1
    elif guess==number:
        print("you have guessed the correct number in "+str(count)+" turns.")
        break
    elif guess<number:
        print("too low")
first=guess+1"""
