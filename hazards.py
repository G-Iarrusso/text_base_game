class Hazard:

    def __init__(self, x, y, tile_hazard):
        self.x = x
        self.y = y
        if tile_hazard == "fire":
            self.tile = "f"
        elif tile_hazard == "water":
            self.tile = "w"
        elif tile_hazard == "earth":
            self.tile = "e"

    def print_hazard(self):
        print("X: " + str(self.x) + " Y: " + str(self.y) + " Tile type: " + self.tile)


class Hazards:
    def __init__(self, hazards):
        self.hazards = hazards

    def clear_hazard(self, hazard):
        for i in range(len(self.hazards)):
            if self.hazards[i] == hazard:
                self.hazards.pop(i)

    def add_hazard(self, hazard):
        self.hazards.append(hazard)

    def print_hazards(self):
        for i in range(len(self.hazards)):
            self.hazards[i].print_hazard()
