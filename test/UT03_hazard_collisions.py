import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from game.objects.room import Room  # noqa: E402
from game.objects.player import Player  # noqa: E402
from game.objects.hazards import Hazard, Hazards  # noqa: E402
print("UT3_hazard_collisions: STARTING")
print("Step 0: Starting room is printed")
test_player = Player(1, 1, 1, 1)
fire_tile_s = Hazard(2, 1, "fire")
fire_tile_n = Hazard(0, 1, "fire")
fire_tile_w = Hazard(1, 0, "fire")
fire_tile_e = Hazard(1, 2, "fire")
room_hazards = Hazards([fire_tile_e, fire_tile_w, fire_tile_n, fire_tile_s])
test_room = Room(3, 3, player=test_player, hazards=room_hazards)
test_room.print_room()

print("Step 1: Moving north")
test_room.player_movement("north", test_player)
test_room.update_room(player=test_player, hazards=room_hazards)
control_player = Player(1, 1, 1, 1)
control_room = Room(3, 3, player=control_player, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT3_hazard_collisions: FAILED - Test fails on moving north"

print("Step 2: Moving east")
test_room.player_movement("east", test_player)
test_room.update_room(player=test_player, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT3_hazard_collisions: FAILED - Test fails on moving east"

print("Step 2: Moving south")
test_room.player_movement("south", test_player)
test_room.update_room(player=test_player, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT3_hazard_collisions: FAILED - Test fails on moving south"

print("Step 4: Moving west")
test_room.player_movement("west", test_player)
test_room.update_room(player=test_player, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT3_hazard_collisions: FAILED - Test fails on moving south"

print("UT3_hazard_collisions: PASSED")
