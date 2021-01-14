from room import Room
from dragon import Dragon, Dragons
print("UT5_dragon_addition_and_deletion: STARTING")
print("Step 0: Starting room is printed")
room_dragons = Dragons([])
dragon = Dragon(0, 0, "water", 10, 10)
test_room = Room(1, 1, dragons=room_dragons)
test_room.print_room()

print("Step 1: Adding dragon")
room_dragons.add_dragon(dragon)
test_room.update_room(dragons=room_dragons)
control_room = Room(1, 1, dragons=room_dragons)
assert test_room.print_room() == control_room.print_room(), "UT5_dragon_addition_and_deletion: FAILED - Test fails on moving north"

print("Step 2: Removing dragon")
room_dragons.clear_dragon(dragon)
test_room.update_room(dragons=room_dragons)
control_room = Room(1, 1)
assert test_room.print_room() == control_room.print_room(), "UT5_dragon_addition_and_deletion: FAILED - Test fails on moving east"

print("UT5_dragon_addition_and_deletion: PASSED")