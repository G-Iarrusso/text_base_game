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
guy = Player(50,50,4,6)

earth_tile = Hazard(1,1,"earth")
water_tile = Hazard(2,2,"water")
fire_tile = Hazard(3,3,"fire")
room_Hazards = Hazards([earth_tile, water_tile, fire_tile])

earth_drag = Dragon(8,8,"earth",50,50)
fire_drag = Dragon(7,7,"fire",50,50)
water_drag = Dragon(9,9,"water",50,50)
dragons = Dragons([earth_drag, fire_drag, water_drag])

room = Room(11, 10, guy, dragons, room_Hazards)
room.print_room()
