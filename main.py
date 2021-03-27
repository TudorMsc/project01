from os import system, name
from time import sleep
import random
level = 1
boss = 10
player = 100


def bosat():
    global player
    player = player - 10

def attack():
    global boss
#    atpow = 40
    atacdmg = level * random.uniform(0, 2)
    boss = boss - atacdmg


def heal():
    global player
#    hpow = 40
    heal = level * random.uniform(0, 2)
    player = player + heal
    if player > 100:
        player = 100

def clear():
    if name == 'nt': 
        _ = system('cls') 

def main():
    while True:
        global player
        clear()
        print("Salut! Misiunea ta este sa bati Boss-ul. Amandoi aveti 100HP.",
        "\nTu ai doua abilitati pe care le poti folosi, adica Heal si Attack")

        while( boss > 0 or player > 0):
            print(f'Ai {player} HP. ')
            print(f'Boss-ul are {boss} HP. ')
            alegimare = input("Ce alegi? Heal, Attack sau Quit (H / A / Q) ")
            alegi = alegimare.lower()

            if alegi == "h":
                heal()
                clear()
            elif alegi == "a":
                attack()
                bosat()
                clear()
            elif alegi == 'q':
                print('Game Over')
                sleep(1)
                clear()
                return
            else:
                print("Trebuie sa alegi intre H si A")
                sleep(1)
                clear()
            
            if player <= 0 and boss <= 0:
                print("Ai omorat boss-ul, dar cu pretul vietii tale.")
                sleep(2)
                clear()
                return

            elif boss <= 0:
                print("Ai invins boss-ul, felicitari! ;) ")
                sleep(2)
                clear()
                return

            elif player <= 0:
                print("Ai fost invins, mai incearca. ")
                sleep(2)
                clear()
                return
                


if __name__ == '__main__':
    main()
