class Hazard:
    def __init__(self, x, y, tile_hazard):
        """
        Creates a single hazard
        args:
            x - x value of hazard - int
            y - y value of hazard - int
            tile_hazard - type of hazard - string
        """
        self.x = x
        self.y = y
        if tile_hazard == "fire":
            self.tile = "f"
        elif tile_hazard == "water":
            self.tile = "w"
        elif tile_hazard == "earth":
            self.tile = "e"
        elif tile_hazard == "tree":
            self.tile = "t"
        elif tile_hazard == "pillar":
            self.tile = "p"

    def get_hazard_type(self):
        """
        get the hazard type
        returns:
            tile type
        """
        return self.tile

    def get_hazard_x(self):
        """
        get the hazard x value
        returns:
            tile x value
        """
        return self.x

    def get_hazard_y(self):
        """
        get the hazard y value
        returns:
            tile y value
        """
        return self.y


class Hazards:
    def __init__(self, hazards):
        """
        create an array of all the hazards
        args:
            hazards - array of hazards - array of objects
        """
        self.hazards = hazards

    def clear_hazard(self, hazard):
        """
        If the hazard exists we remove it
        args:
            hazrard - hazard to be removed - hazard object
        """
        for cur_hazard in (self.hazards):
            if hazard in self.hazards:
                self.hazards.remove(hazard)

    def add_hazard(self, hazard):
        """
        Add a new hazard to the room
        args:
            hazrard - hazard to be added - hazard object
        """
        self.hazards.append(hazard)
