import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from game.objects.dragon import Dragon, Dragons  # noqa: E402
from game.objects.player import Player  # noqa: E402
from game.objects.combat import quick_attack, check_deaths  # noqa: E402
from game.objects.goal import Goal, Goals  # noqa: E402
from game.objects.room import Room  # noqa: E402
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
assert test_room.is_clear()
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
