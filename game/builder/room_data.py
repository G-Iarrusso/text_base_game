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


def _get_dragons(room_name):
    dragons = ROOMS.get(room_name).get("dragons")
    return dragons


def _get_hazards(room_name):
    hazards = ROOMS.get(room_name).get("hazards")
    return hazards


def _get_goals(room_name):
    goals = ROOMS.get(room_name).get("goals")
    return goals


def _get_player(room_name):
    player = ROOMS.get(room_name).get("player")
    return player


def _get_dragon_names(room_name):
    name = []
    for each_drag in _get_dragons(room_name):
        name.append(each_drag)
    return name


def _get_dragon_info_by_name(room_name, dragon_name):
    dragons = _get_dragons(room_name)
    x = dragons.get(dragon_name).get("x")
    y = dragons.get(dragon_name).get("y")
    species = dragons.get(dragon_name).get("species")
    starting_health = dragons.get(dragon_name).get("starting_health")
    current_health = dragons.get(dragon_name).get("current_health")

    return x, y, species, starting_health, current_health


def _get_hazard_names(room_name):
    name = []
    for each_hazard in _get_hazards(room_name):
        name.append(each_hazard)
    return name


def _get_hazard_info_by_name(room_name, hazard_name):
    hazards = _get_hazards(room_name)
    x = hazards.get(hazard_name).get("x")
    y = hazards.get(hazard_name).get("y")
    tile_hazard = hazards.get(hazard_name).get("tile_hazard")

    return x, y, tile_hazard


def _get_goal_names(room_name):
    name = []
    for each_goal in _get_goals(room_name):
        name.append(each_goal)
    return name


def _get_goal_info_by_name(room_name, goal_name):
    goal = _get_goals(room_name)
    x = goal.get(goal_name).get("x")
    y = goal.get(goal_name).get("y")
    type = goal.get(goal_name).get("type")

    return x, y, type
