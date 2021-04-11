import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from objects.room import Room  # noqa: E402
from objects.player import Player  # noqa: E402
print("UT2_wall_collisions: STARTING")
print("Step 0: Starting room is printed")
test_player = Player(1, 1, 0, 1)
test_room = Room(2, 2, player=test_player)
test_room.print_room()

print("Step 1: Moving north")
test_room.player_movement("north", test_player)
test_room.update_room(player=test_player)
control_player = Player(1, 1, 0, 1)
control_room = Room(2, 2, player=control_player)
assert test_room.print_room() == control_room.print_room(
), "UT2_wall_collisions: FAILED - Test fails on moving north"

print("Step 2: Moving east")
test_room.player_movement("east", test_player)
test_room.update_room(player=test_player)
control_player = Player(1, 1, 0, 1)
control_room = Room(2, 2, player=control_player)
assert test_room.print_room() == control_room.print_room(
), "UT2_wall_collisions: FAILED - Test fails on moving east"

print("Step 2: Moving south")
test_room.player_movement("south", test_player)
test_room.player_movement("south", test_player)
test_room.update_room(player=test_player)
control_player = Player(1, 1, 1, 1)
control_room = Room(2, 2, player=control_player)
assert test_room.print_room() == control_room.print_room(
), "UT2_wall_collisions: FAILED - Test fails on moving south"

print("Step 4: Moving west")
test_room.player_movement("west", test_player)
test_room.player_movement("west", test_player)
test_room.update_room(player=test_player)
control_player = Player(1, 1, 1, 0)
control_room = Room(2, 2, player=control_player)
assert test_room.print_room() == control_room.print_room(
), "UT2_wall_collisions: FAILED - Test fails on moving south"

print("UT2_wall_collisions: PASSED")
