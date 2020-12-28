class Dragon:
    def __init__(self, x, y, species, current_health, starting_health):
        """
        Creates the Dragon Class
        """
        self.drag_x = x
        self.drag_y = y
        self.species = species
        self.current_health = current_health
        self.starting_health = starting_health


class Dragons:

    def __init__(self, dragons):
        self.dragons = dragons

    def clear_dragon(self, dragon):
        """
        If the dragon exists we remove it
        """
        for cur_dragon in (self.dragons):
            if dragon in self.dragons:
                self.dragons.remove(dragon)
                self.print_dragons()

    def add_dragon(self, dragon):
        """
        Add a new dragon to the room
        """
        self.dragons.append(dragon)
