from game.objects.combat import is_in_combat, combat
from game.objects.debugging import print_dragon, print_dragons
from game.builder.builder import Builder
POSSIBLE_MOVE = [
    "north",
    "east",
    "west",
    "south",
]
POSSIBLE_COMBAT = [
    "qa",
    "hq",
    "bl",
    "dg",
]
POSSIBLE_ACTION = [
    "bandage"
]

def handle_input(builder:Builder, input:str):
    drag_in_combat = is_in_combat(builder.player, builder.dragons)
    if(input in POSSIBLE_COMBAT and drag_in_combat):
        output = combat(builder.player, drag_in_combat,builder.dragons, input)
        if output == 1:
            print("dragon died")
        elif output == 0:
            print("Player died")
        else:
            print("nothing died")


    elif(input in POSSIBLE_MOVE and not drag_in_combat):
        outcome = builder.room.player_movement(input,builder.player)
        if outcome == 1:
            for dragon in builder.dragons.dragons:
                builder.room.dragon_movement(dragon, builder.player)
        if outcome == 1 and builder.room.on_goal(builder.player):
            print("on goal")
            return -1
        else:
            print(builder.room.on_goal(builder.player))


    elif(input in POSSIBLE_ACTION):
        print(3)
    else:
        print(4)
        return -1
    builder.room.update_room(dragons = builder.dragons, hazards = builder.hazards,player = builder.player)
    if builder.room.is_clear():
        builder.room.print_cleared_room(builder.player)
    else:
        builder.room.print_room()
def get_input(builder:Builder):
    return handle_input(builder, input())