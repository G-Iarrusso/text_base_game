from dragon import Dragon, Dragons
from player import Player
from combat import quick_attack, check_deaths
from goal import Goal, Goals
from room import Room
print("UT14_goal_room: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(1, 1, 0, 0)
goal = Goal(0, 3, "goal")
goals = Goals([goal])
dragon = Dragon(0, 1, "water", 10, 10)
dragons = Dragons([dragon])
test_room = Room(1, 4, player=test_player, dragons=dragons, goals=goals)
test_room.print_room()

print("Step 1: Clear room")
assert dragons.num_dragons() == 1
quick_attack(test_player, dragon, 1)
check_deaths(test_player, dragon, dragons)

print("Step 2: Print clean room")
assert dragons.num_dragons() == 0
test_room.update_room(player=test_player, dragons=dragons)
assert test_room.is_clear(test_player)
room_print = test_room.print_cleared_room(test_player)
assert "G" in room_print


assert test_room.player_movement("east", test_player)
test_room.update_room(player=test_player, dragons=dragons)
test_room.print_cleared_room(test_player)

assert test_room.player_movement("east", test_player)
test_room.update_room(player=test_player, dragons=dragons)
test_room.print_cleared_room(test_player)

assert test_room.player_movement("east", test_player)
test_room.update_room(player=test_player, dragons=dragons)
test_room.print_cleared_room(test_player)

assert test_room.on_goal(test_player)

print("UT14_goal_room: PASSED")
