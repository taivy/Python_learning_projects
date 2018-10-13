class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health -= unit_1.attack
        if unit_1.health > 0 and unit_2.health > 0:
            unit_1.health -= unit_2.attack
        else:
            break
    if unit_1.health > 0 and unit_2.health <= 0:
        unit_2.is_alive = False
        return True
    else:
        unit_1.is_alive = False
        return False


if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False