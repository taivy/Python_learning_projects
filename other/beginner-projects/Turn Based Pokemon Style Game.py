from random import randint
from operator import methodcaller

class pokemon():
    def __init__(self):
        self.health = 100
    def set_enemy(self, e):
        self.enemy = e

    def moderate(self):
        damage = randint(18, 25)
        self.enemy.health -= damage

    def big_range(self):
        damage = randint(10, 35)
        self.enemy.health -= damage

    def heal(self):
        h = randint(18, 25)
        self.health += h

moves = {1: methodcaller('moderate'), 2: methodcaller('big_range'), 3: methodcaller('heal'),}


user = pokemon()
comp = pokemon()

comp.set_enemy(user)
user.set_enemy(comp)


print("""
The first move do moderate damage and has a small range (such as 18-25).
The second move have a large range of damage and can deal high or low damage (such as 10-35).
The third move  heal whoever casts it a moderate amount, similar to the first move.
""")
print('Choose move (1-3): ')


while comp.health > 0 and user.health > 0:
    u_move = int(input())
    c_move = randint(1, 3)
    moves[u_move](user)
    moves[c_move](comp)
    print('User move: ' + str(u_move) + '. Computer move: '+ str(c_move))
    print('User health: ' + str(user.health) + '. Computer health: ' + str(comp.health))

if comp.health < 0 and user.health > 0:
    print('User wins')
elif comp.health > 0 and user.health < 0:
    print('Computer wins')
elif comp.health < 0 and user.health < 0:
    print('Draw')