from room import Room
from dragon import Dragon, Dragons
from player import Player
from combat import is_in_combat
print("UT7_is_in_combat: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(1, 1, 1, 1)
dragon = Dragon(0, 1, "water", 10, 10)
room_dragons = Dragons([dragon])
test_room = Room(3, 3, player=test_player, dragons=room_dragons)
test_room.print_room()

print("Step 1: north tile")
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 2: north west tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(0, 0, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 3: west tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(1, 0, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 4: south west tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(2, 0, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 5: south tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(2, 1, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 6: south east tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(2, 2, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 7: east tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(1, 2, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 8: north east tile")
room_dragons.clear_dragon(dragon)
dragon = Dragon(0, 2, "water", 10, 10)
room_dragons.add_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert is_in_combat(test_player, test_room), "Player should be in combat"

print("Step 9: not in combat")
room_dragons.clear_dragon(dragon)
test_room.update_room(player=test_player, dragons=room_dragons)
test_room.print_room()
assert not is_in_combat(
    test_player, test_room), "Player should not be in combat"

print("UT7_is_in_combat: PASSED")
