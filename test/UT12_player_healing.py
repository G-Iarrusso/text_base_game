import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from objects.dragon import Dragon  # noqa: E402
from objects.player import Player  # noqa: E402
from objects.combat import claw  # noqa: E402
print("UT12_player_healing: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(5, 5, 100, 100)
dragon = Dragon(0, 1, "water", 10, 10)

print("Step 1: Player is alive")
assert not test_player.is_dead()

print("Step 2: Player dies")
claw(test_player, dragon, False, False)
assert test_player.get_player_health() < test_player.get_player_starting_health()
test_player.bandage()
test_player.bandage()
test_player.bandage()
assert not test_player.bandage()
claw(test_player, dragon, False, False)
test_player.heal_all()
assert test_player.get_player_starting_health() == test_player.get_player_health()
base_health = test_player.get_player_starting_health()
test_player.gain_armour(10)
assert test_player.get_player_starting_health() > base_health
print("UT12_player_healing: PASSED")
