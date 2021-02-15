from dragon import Dragon
from player import Player
from combat import claw
print("UT8_player_can_die: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(5, 5, 1, 1)
dragon = Dragon(0, 1, "water", 10, 10)

print("Step 1: Player is alive")
assert not test_player.is_dead()

print("Step 2: Player dies")
claw(test_player, dragon, False, False)
assert test_player.is_dead()

print("UT8_player_can_die: PASSED")
