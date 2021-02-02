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
        self.claw = 5
        self.tail = 10
        self.breath = 15

    def get_drag_x(self):
        return self.drag_x

    def get_drag_y(self):
        return self.drag_y

    def get_drag_species(self):
        return self.species

    def get_drag_health(self):
        return self.current_health

    def get_drag_claw(self):
        return self.claw

    def get_drag_tail(self):
        return self.tail

    def get_drag_breath(self):
        return self.breath

    def set_drag_health(self, health):
        self.current_health = health

    def set_drag_x(self, x):
        self.drag_x = x

    def set_drag_y(self, y):
        self.drag_y = y


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

    def add_dragon(self, dragon):
        """
        Add a new dragon to the room
        """
        self.dragons.append(dragon)
