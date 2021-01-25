class Hazard:
    def __init__(self, x, y, tile_hazard):
        """
        Creates a single hazard
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
        return self.tile

    def get_hazard_x(self):
        return self.x

    def get_hazard_y(self):
        return self.y


class Hazards:
    def __init__(self, hazards):
        self.hazards = hazards

    def clear_hazard(self, hazard):
        """
        If the hazard exists we remove it
        """
        for cur_hazard in (self.hazards):
            if hazard in self.hazards:
                self.hazards.remove(hazard)

    def add_hazard(self, hazard):
        """
        Add a new hazard to the room
        """
        self.hazards.append(hazard)
