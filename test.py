from room import Room
from hazards import Hazard, Hazards
from player import Player
from dragon import Dragon, Dragons
from debugging import print_dragons, print_player, print_hazards
"""
UT1
TC-1 player can move NESW - DONE

UT2
TC-2 player cannot move through walls - DONE

UT3
TC-3 player cannot move through hazards - DONE

UT4
TC-4 adding a hazard updates properly - DONE
TC-s removing a hazard updates properly - DONE

UT5
TC-6 adding a dragon updates properly - DONE

UT6
TC-8 dragons will chase the player - DONE

UT7
TC-9 when player within 1 square of dragon combat starts - DONE

UT8
TC-10 player can die in combat - DONE

UT9
TC-11 player can use quick attack
TC-12 player can use Heavy attack
TC-13 player can use dodge
TC-14 player can use block

UT10
TC-15 dragon will use claw
TC-16 dragon will use tail
TC-17 dragon will use breath

UT11
TC-18 dead dragon will be removed

UT12
TC-19 player heal all works
TC-20 Player heal amount works
TC-21 player get armour works

UT13
TC-7 dragons can move through the hazards
"""


"""
#room.print_room()
#room.movement("west")
earth_tile = Hazard(1,1,"earth")
water_tile = Hazard(2,2,"water")
fire_tile = Hazard(3,3,"fire")

#earth_tile.print_hazard()
#water_tile.print_hazard()
#fire_tile.print_hazard()
room_Hazards = Hazards([earth_tile, water_tile, fire_tile])
room = Room(11, 10, 4, 3, room_Hazards)
room.print_room()
room_Hazards.clear_hazard(earth_tile)
room.update_room(room_Hazards)
room.print_room()


# testing movement
guy = Player(50,50,4,6)
guy = Player(50,50,2,4)

earth_tile = Hazard(1,1,"earth")
water_tile = Hazard(2,2,"water")
fire_tile = Hazard(3,3,"fire")
room_Hazards = Hazards([earth_tile, water_tile, fire_tile])

earth_drag = Dragon(8,8,"earth",50,50)
fire_drag = Dragon(8,8,"fire",50,50)

dragons = Dragons([earth_drag])
dragons.add_dragon(fire_drag)
dragons.print_dragons()
dragons.clear_dragon(fire_drag)


room = Room(11, 10, guy, dragons, room_Hazards)
room.print_room()
#guy.print_player()
room.player_movement("west", guy)
#guy.print_player()
room.update_room(guy, room_Hazards, dragons)
room.print_room()
for i in range(5):
    room.dragon_movement(earth_drag, guy)
    room.update_room(guy, room_Hazards, dragons)
    room.print_room()


# testing combat

guy = Player(50, 50, 0, 0)
print_player(guy)
earth_tile = Hazard(1, 1, "earth")
water_tile = Hazard(2, 2, "water")
fire_tile = Hazard(3, 3, "fire")
room_Hazards = Hazards([earth_tile, water_tile, fire_tile])
print_hazards(room_Hazards)
earth_drag = Dragon(8, 8, "earth", 50, 50)
dragons = Dragons([earth_drag])
print_dragons(dragons)
room = Room(11, 10, guy, dragons, room_Hazards)
room.print_room()
while True:
    print("Enter MOVE and either north, east, south, or west.")
    dir = input('')

    tokens = dir.split(' ')
    if tokens[0] == "MOVE":

        room.player_movement(tokens[1], guy)
        # if player moves to dragon
        if guy.is_in_combat(room):
            print("\nENTER COMBAT!!!!!")
            val = guy.combat(earth_drag, dragons)
            room.update_room(guy, room_Hazards, dragons)
            room.print_room()
            continue

        room.dragon_movement(earth_drag, guy)
        room.update_room(guy, room_Hazards, dragons)
        room.print_room()

        # if dragon moves to player
        if guy.is_in_combat(room):
            print("\nENTER COMBAT!!!!!")
            val = guy.combat(earth_drag, dragons)
            room.update_room(guy, room_Hazards, dragons)
            room.print_room()
            continue
    elif dir == 'no':
        break
    else:
        print('Invalid try again')
"""
print("Welcome to the Quest")
token = input("what is your name?")