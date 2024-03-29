def print_player(player):
    """
    TODO
    change to the get/set functions
    """
    """
    prints the players info
    """
    print("Starting health: " + str(player.starting_health) +
          " Current Health: " + str(player.current_health))
    print("X: " + str(player.player_x + 1) + " Y: " + str(player.player_y + 1))


def print_hazard(hazard):
    """
    TODO
    change to the get/set functions
    """
    """
    Hazards info
    """
    print("X: " + str(hazard.x + 1) + " Y: " +
          str(hazard.y + 1) + " Tile type: " + hazard.tile)


def print_hazards(hazards):
    """
    TODO
    change to the get/set functions
    """
    """
    prints all the hazards
    """
    for hazard in hazards.hazards:
        print_hazard(hazard)


def print_dragon(dragon):
    """
    TODO
    change to the get/set functions
    """
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

def print_goal(goal):
    """
    Prints the goal
    """
    print("X:" + str(goal.x + 1) + " Y:" +str(goal.y+1))
    print("Type:" + str(goal.tile))