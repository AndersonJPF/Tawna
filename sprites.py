import time
import random

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

def attack(user, target):
    target.hp -= user.strength
    print(user.name + ' attacks!')
    time.sleep(2)
    print(user.name + ' deals ' + str(user.strength) + ' damage on ' + target.name + '!')

def fight(player, foe):
    print(player.name + ' will fight ' + foe.name + '!')
    time.sleep(1)
    while player.hp > 0 and foe.hp > 0:
        print('O que {} irá fazer?'.format(player.name))
        time.sleep(1)

        print ("""      A. Attack
        B. Attack
        C. Attack""")
        time.sleep(1)

        choice = input('>>> ')

        if choice in answer_A:
            attack(player, foe)
        elif choice in answer_B:
            pass
        else:
            pass

        attack(foe, player)
    print('The fight is over!')


class Player():
    def __init__(self):
        self.name = "Tawna"
        self.hp = 30
        self.strength = 10

class Enemy():
    def __init__(self):
        self.name = "Sarah"
        self.hp = 25
        self.strength = 8

Tawna = Player()
Sarah = Enemy()