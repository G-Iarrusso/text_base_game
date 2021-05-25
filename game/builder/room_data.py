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

"""
hazards = {
            "hazard" : {
                "x" : 2,
                "y" : 2,
                "tile_hazard" : "fire"
            },
            "hazard_1" : {
                "x" : 3,
                "y" : 4,
                "tile_hazard" : "water"
            },
        }
print(hazards)
for each in hazards:
    print(hazards[each]["x"])
print(ROOM.get("first_room"))

print(ROOMS)
print(ROOMS.get("first_room"))
print(ROOMS.get("first_room").get("hazards"))
hazards = ROOMS.get("first_room").get("hazards")
for each in hazards:
    print(hazards.get(each).get("x"))
    print(hazards.get(each).get("y"))
    print(hazards.get(each).get("tile_hazard"))
    print()
"""
