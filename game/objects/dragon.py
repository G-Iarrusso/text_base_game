class Dragon:
    """
    TODO
    add docstrings to each function/flush it out
    """

    def __init__(self, x, y, species, current_health, starting_health):
        """
        Creates the Dragon Class
        Args:
            x - dragons x location - int
            y - dragons y location - int
            species - the type of dragon - string
            current_health - the current health of the dragon - int
            starting health - the health the dragon starts with -int
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
        """
        get the dragons x value
        returns:
            the value for the dragons x
        """
        return self.drag_x

    def get_drag_y(self):
        """
        get the dragons y value
        returns:
            the value for the dragons y
        """
        return self.drag_y

    def get_drag_species(self):
        """
        get the dragons species value
        returns:
            the value for the dragons species
        """
        return self.species

    def get_drag_health(self):
        """
        get the dragons current healt value
        returns:
            the value for the dragons current health
        """
        return self.current_health

    def get_drag_claw(self):
        """
        get the dragons claw damage value
        returns:
            the value for the dragons claw damage
        """
        return self.claw

    def get_drag_tail(self):
        """
        get the dragons  tail value
        returns:
            the value for the dragons tail value
        """
        return self.tail

    def get_drag_breath(self):
        """
        get the dragons breat value
        returns:
            the value for the dragons breath
        """
        return self.breath

    def set_drag_health(self, health):
        """
        set the dragons current health
        args:
            health - the health of the dragon - int
        """
        self.current_health = health

    def set_drag_x(self, x):
        """
        set the dragons x value
        args:
            x - the new x value - int
        """
        self.drag_x = x

    def set_drag_y(self, y):
        """
        set the dragons y value
        args:
            y - the new y value - int
        """
        self.drag_y = y


class Dragons:

    def __init__(self, dragons):
        """
        create an array of all the dragons
        args:
            dragons - array of dragons - array of objects
        """
        self.dragons = dragons

    def clear_dragon(self, dragon):
        """
        If the dragon exists we remove it
        args:
            dragon - the dragon to be removed - dragon object
        """
        for cur_dragon in (self.dragons):
            if dragon in self.dragons:
                self.dragons.remove(dragon)

    def add_dragon(self, dragon):
        """
        Add a new dragon to the room
        args:
            dragon - the dragon to be added - dragon object
        """
        self.dragons.append(dragon)

    def num_dragons(self):
        """
        Add a new dragon to the room
        returns:
            the number of dragons left - int
        """
        return len(self.dragons)
