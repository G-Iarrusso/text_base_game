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
                self.print_hazards()

    def add_hazard(self, hazard):
        """
        Add a new hazard to the room
        """
        self.hazards.append(hazard)
