class Dragon:
    def __init__(self, x, y, species, current_health, starting_health):
        self.drag_x = x
        self.drag_y = y
        self.species = species
        self.current_heath = current_health
        self.starting_health = starting_health

    def print_dragon(self):
        print("x:" + str(self.drag_x + 1) + " Y: " + str(self.drag_y + 1))
        print("Species: " + self.species + " Current health: " + str(self.current_heath) + " Total health: " + str(self.starting_health))


class Dragons:
    def __init__(self, dragons):
        self.dragons = dragons

    def print_dragons(self):
        for dragon in self.dragons:
            dragon.print_dragon()
