import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from game.objects.room import Room  # noqa: E402
from game.objects.hazards import Hazard, Hazards  # noqa: E402
print("UT4_hazard_addition_and_deletion: STARTING")
print("Step 0: Starting room is printed")
room_hazards = Hazards([])
hazard = Hazard(0, 0, "water")
test_room = Room(1, 1, hazards=room_hazards)
test_room.print_room()

print("Step 1: Adding hazard")
room_hazards.add_hazard(hazard)
test_room.update_room(hazards=room_hazards)
control_room = Room(1, 1, hazards=room_hazards)
assert test_room.print_room() == control_room.print_room(
), "UT4_hazard_addition_and_deletion: FAILED - Test fails on moving north"

print("Step 2: Removing hazard")
room_hazards.clear_hazard(hazard)
test_room.update_room(hazards=room_hazards)
control_room = Room(1, 1)
assert test_room.print_room() == control_room.print_room(
), "UT4_hazard_addition_and_deletion: FAILED - Test fails on moving east"

print("UT4_hazard_addition_and_deletion: PASSED")
