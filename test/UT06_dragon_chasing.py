import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from objects.room import Room   # noqa: E402
from objects.dragon import Dragon, Dragons  # noqa: E402
from objects.player import Player  # noqa: E402
print("UT6_dragon_chasing: STARTING")
print("Step 0: Starting room is printed")
test_player = Player(1, 1, 1, 1)
dragon = Dragon(5, 5, "water", 10, 10)
room_dragons = Dragons([dragon])
test_room = Room(10, 10, player=test_player, dragons=room_dragons)
test_room.print_room()

print("Step 1: First move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons)
control_dragon = Dragon(4, 4, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(10, 10, player=test_player, dragons=control_dragons)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on first movement"

print("Step 2: Second move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons)
control_dragon = Dragon(3, 3, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(10, 10, player=test_player, dragons=control_dragons)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on second movement"

print("Step 3: Third move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons)
control_dragon = Dragon(2, 2, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(10, 10, player=test_player, dragons=control_dragons)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on third movement"

print("Step 4: Fourth move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons)
control_dragon = Dragon(1, 2, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(10, 10, player=test_player, dragons=control_dragons)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on fourth movement"

print("Step 4: Fourth move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player, dragons=room_dragons)
control_dragon = Dragon(1, 2, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(10, 10, player=test_player, dragons=control_dragons)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on final movement"

print("UT6_dragon_chasing: PASSED")
