def print_player(player):
    """
    prints the players info
    """
    print("Starting health: " + str(player.starting_health) +
          " Current Health: " + str(player.current_health))
    print("X: " + str(player.player_x + 1) + " Y: " + str(player.player_y + 1))


def print_hazard(hazard):
    """
    Hazards info
    """
    print("X: " + str(hazard.x + 1) + " Y: " +
          str(hazard.y + 1) + " Tile type: " + hazard.tile)


def print_hazards(hazards):
    """
    prints all the hazards
    """
    for hazard in hazards.hazards:
        print_hazard(hazard)


def print_dragon(dragon):
    """
    Dragon info
    """
    print("x:" + str(dragon.drag_x + 1) + " Y: " + str(dragon.drag_y + 1))
    print("Species: " + dragon.species + ", Current health: " +
          str(dragon.current_health) + ", Total health: " + str(dragon.starting_health))


def print_dragons(dragons):
    """
    prints all dragons
    """
    for dragon in dragons.dragons:
        print_dragon(dragon)
