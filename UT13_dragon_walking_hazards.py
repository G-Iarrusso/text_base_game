from room import Room
from dragon import Dragon, Dragons
from player import Player
from hazards import Hazard, Hazards
print("UT13_dragon_walking_hazards: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(1, 1, 0, 0)
fire_tile = Hazard(2, 0, "fire")
room_hazards = Hazards([fire_tile])
dragon = Dragon(3, 0, "water", 10, 10)
room_dragons = Dragons([dragon])
test_room = Room(1, 4, player=test_player, dragons=room_dragons, hazards=room_hazards)
test_room.print_room()

print("Step 1: First move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons, hazards=room_hazards)
control_dragon = Dragon(2, 0, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(1, 4, player=test_player, dragons=control_dragons, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(), "UT6_dragon_chasing: FAILED - Test fails on first movement"

print("Step 2: Second move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons, hazards=room_hazards)
control_dragon = Dragon(1, 0, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(1, 4, player=test_player, dragons=control_dragons, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(), "UT6_dragon_chasing: FAILED - Test fails on second movement"

print("UT6_dragon_chasing: PASSED")
