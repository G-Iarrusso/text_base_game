from room import Room
from hazards import Hazard, Hazards
from player import Player
from dragon import Dragon, Dragons
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
"""
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

"""
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
"""