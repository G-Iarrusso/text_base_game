ROOMS = {
    "first_room": {
        "room": {
            "x": 5,
            "y": 5,
        },
        "hazards": {
            "hazard_1": {
                "x": 2,
                "y": 2,
                "tile_hazard": "fire"
            },
            "hazard_2": {
                "x": 1,
                "y": 1,
                "tile_hazard": "earth"
            },
        },
        "dragons": {
            "dragon_1": {
                "x": 3,
                "y": 3,
                "species": "fire",
                "starting_health": 10,
                "current_health": 10
            },
            "dragon_2": {
                "x": 4,
                "y": 4,
                "species": "earth",
                "starting_health": 10,
                "current_health": 10
            }
        },
        "goals": {
            "door": {
                "x": 2,
                "y": 4,
                "type": "door",
            },
            "goal": {
                "x": 2,
                "y": 4,
                "type": "goal",
            }
        },
        "player": {
            "x": 0,
            "y": 2,
            "starting_health": 100,
            "current_health": 100
        }
    }
}


def _get_room(room_name):
    """
    get the room in the dictionary entry
    Args:
        room_name - the name of the dictionary entry
    Returns:
        the room sub dictionary of exists, else None
    """
    room = ROOMS.get(room_name).get("room")
    return room


def _get_dragons(room_name):
    """
    get all the dragons in the dictionary entry
    Args:
        room_name - the name of the dictionary entry
    Returns:
        the dragons sub dictionary if exists, else None
    """
    dragons = ROOMS.get(room_name).get("dragons")
    return dragons


def _get_hazards(room_name):
    """
    get all the hazards in the dictionary entry
    Args:
        room_name - the name of the dictionary entry
    Returns:
        the hazards sub dictionary if exists, else None
    """
    hazards = ROOMS.get(room_name).get("hazards")
    return hazards


def _get_goals(room_name):
    """
    get all the goals in the dictionary entry
    Args:
        room_name - the name of the dictionary entry
    Returns:
        the goals sub dictionary if exists, else None
    """
    goals = ROOMS.get(room_name).get("goals")
    return goals


def _get_player(room_name):
    """
    get all the hazards in the dictionary entry
    Args:
        room_name - the name of the dictionary entry
    Returns:
        the player sub dictionary if exists, else None
    """
    player = ROOMS.get(room_name).get("player")
    return player


def _get_dragon_names(room_name):
    """
    get the names of each dragon entry in the dragons sub dictionary
    args:
        room_name - the name of the dictionary entry
    returns:
        an array of dragon names
    """
    name = []
    for each_drag in _get_dragons(room_name):
        name.append(each_drag)
    return name


def _get_dragon_info_by_name(room_name, dragon_name):
    """
    Given a dragons name return its info
    args
        room_name - the name of the dictionary entry
        dragon_name - the specific dragon within the dictionary entry
    returns:
        x - the dragon's x - int
        y - the dragon's y - int
        species - the dragon's species - string
        starting_health - the dragon's starting health - int
        current_health - the dragon's current health - int
    """
    dragons = _get_dragons(room_name)
    x = dragons.get(dragon_name).get("x")
    y = dragons.get(dragon_name).get("y")
    species = dragons.get(dragon_name).get("species")
    starting_health = dragons.get(dragon_name).get("starting_health")
    current_health = dragons.get(dragon_name).get("current_health")

    return x, y, species, starting_health, current_health


def _get_hazard_names(room_name):
    """
    get the names of each hazard entry in the hazards sub dictionary
    args:
        room_name - the name of the dictionary entry
    returns:
        an array of hazard names
    """
    name = []
    for each_hazard in _get_hazards(room_name):
        name.append(each_hazard)
    return name


def _get_hazard_info_by_name(room_name, hazard_name):
    """
    Given a hazard's name return its info
    args
        room_name - the name of the dictionary entry
        hazard_name - the specific hazard within the dictionary entry
    returns:
        x - the hazard's x - int
        y - the hazard's y - int
        tile_hazard - the hazard's type - string
    """
    hazards = _get_hazards(room_name)
    x = hazards.get(hazard_name).get("x")
    y = hazards.get(hazard_name).get("y")
    tile_hazard = hazards.get(hazard_name).get("tile_hazard")

    return x, y, tile_hazard


def _get_goal_names(room_name):
    """
    get the names of each goal entry in the goals sub dictionary
    args:
        room_name - the name of the dictionary entry
    returns:
        an array of goal names
    """
    name = []
    for each_goal in _get_goals(room_name):
        name.append(each_goal)
    return name


def _get_goal_info_by_name(room_name, goal_name):
    """
    Given a goal's name return its info
    args
        room_name - the name of the dictionary entry
        goal_name - the specific goal within the dictionary entry
    returns:
        x - the goal's x - int
        y - the goal's y - int
        type - the goal's type - string
    """
    goal = _get_goals(room_name)
    x = goal.get(goal_name).get("x")
    y = goal.get(goal_name).get("y")
    type = goal.get(goal_name).get("type")

    return x, y, type


def _get_player_info(room_name):
    """
    Given a room name return its player's info
    args
        room_name - the name of the dictionary entry
    returns:
        x - the player's x - int
        y - the player's y - int
        starting_health - the player's starting health - int
        current_health - the player's current health - int
    """
    player = _get_player(room_name)
    x = player.get("x")
    y = player.get("y")
    starting_health = player.get("starting_health")
    current_health = player.get("current_health")

    return x, y, starting_health, current_health


def _get_room_info(room_name):
    """
    Given a room name return its info
    args
        room_name - the name of the dictionary entry
    returns:
        x - the room's x size- int
        y - the room's y size - int
    """
    room = ROOMS.get(room_name).get("room")
    x = room.get("x")
    y = room.get("y")

    return x, y
