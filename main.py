from os import system, name
from time import sleep
player = 100
boss = 100

def clear():
    if name == 'nt': 
        _ = system('cls') 

def attack():
    print('From attack')
    # global boss
    # atpow = 20
    # damage = level*atpow*random.randint(0, 1)
    # boss -= damage


def heal():
    print('From heal')
    # hpow = 20
    # level*hpow*random.randint(0, 1)


def main():
    while True:
        global player
        print("Salut! Misiunea ta este sa bati Boss-ul. Amandoi aveti 100HP.",
        "\nTu ai doua abilitati pe care le poti folosi, adica Heal si Attack")

        while( boss > 0 or player > 0):
            print(f'Ai {player} HP. ')
            alegimare = input("Ce alegi? Heal, Attack sau Quit (H / A / Q) ")
            alegi = alegimare.lower()

            if alegi == "h":
                heal()
                sleep(2)
                clear()
            elif alegi == "a":
                attack()
                sleep(2)
                clear()
            elif alegi == 'q':
                print('Game Over')
                return
            else:
                print("Trebuie sa alegi intre H si A")
                sleep(2)
                clear()
                

        if player <= 0:
            print("Ai murit, incearca din nou")
            break
        elif boss <= 0:
            print("Ai invins boss-ul, felicitari! ")
            break


if __name__ == '__main__':
    main()
