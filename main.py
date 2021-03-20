import random
level = 1
boss = 100
player = 100
def bosat():
    global player
    player = player - 10

def attack():
    global boss
    atpow = 40
    atacdmg = level*atpow*random.uniform(0, 2)
    boss = boss - atacdmg

def heal():
    global player
    hpow = 40
    heal = level*hpow*random.uniform(0, 2)
    player = player + heal
    if player > 100:
        player = 100