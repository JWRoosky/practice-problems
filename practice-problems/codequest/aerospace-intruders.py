class Ship:
    def __init__(self, name, clss, x, y):
        self.name = name
        self.clss = clss
        self.x = x
        self.y = y
        self.destroyed = False

    def move(self):
        if self.clss == 'A':
            self.x -= 10
        elif self.clss == 'B':
            self.x -= 20
        else:
            self.x -= 30


def destroy(Ship):
    Ship.destroyed = True


cases = int(input())
for i in range(cases):
    num_ships = int(input())
    for j in range(num_ships):
        ship_lst = []
        str_ship = input()
        ship = Ship(str_ship[0:str_ship.index('_')], str_ship[str_ship.index('_'):str_ship.index(':')],
                    int(str_ship[str_ship.index(':'):str_ship.index(',')]), int(str_ship[str_ship.index(','):]))
        ship_lst.append(ship)
