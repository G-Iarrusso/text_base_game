import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from game.objects.room import Room  # noqa: E402
from game.objects.dragon import Dragon, Dragons  # noqa: E402
from game.objects.player import Player  # noqa: E402
from game.objects.hazards import Hazard, Hazards  # noqa: E402
print("UT13_dragon_walking_hazards: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(1, 1, 0, 0)
fire_tile = Hazard(0, 2, "fire")
room_hazards = Hazards([fire_tile])
dragon = Dragon(0, 3, "water", 10, 10)
room_dragons = Dragons([dragon])
test_room = Room(1, 4, player=test_player,
                 dragons=room_dragons, hazards=room_hazards)
test_room.print_room()

print("Step 1: First move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player,
                      dragons=room_dragons, hazards=room_hazards)
control_dragon = Dragon(0, 2, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(1, 4, player=test_player,
                    dragons=control_dragons, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on first movement"

print("Step 2: Second move")
test_room.dragon_movement(dragon, test_player)
test_room.update_room(player=test_player,
                      dragons=room_dragons, hazards=room_hazards)
control_dragon = Dragon(0, 1, "water", 10, 10)
control_dragons = Dragons([control_dragon])
control_room = Room(1, 4, player=test_player,
                    dragons=control_dragons, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT6_dragon_chasing: FAILED - Test fails on second movement"

print("UT6_dragon_chasing: PASSED")
