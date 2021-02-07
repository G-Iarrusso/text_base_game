from dragon import Dragon, Dragons
from player import Player
from combat import quick_attack, check_deaths
print("UT11_dragon_can_die: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(5, 5, 1, 1)
dragon = Dragon(0, 1, "water", 1, 1)
dragons = Dragons([dragon])

print("Step 1: Player is alive")
assert dragons.num_dragons() == 1

print("Step 2: Player dies")
quick_attack(test_player, dragon, 1)
check_deaths(test_player, dragon, dragons)
assert dragons.num_dragons() == 0

print("UT11_dragon_can_die: PASSED")
