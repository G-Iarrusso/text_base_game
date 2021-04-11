import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from objects.dragon import Dragon   # noqa: E402
from objects.player import Player   # noqa: E402
from objects.combat import claw, breath, tail  # noqa: E402
print("UT10_dragon_combat: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(5, 5, 100, 100)
dragon = Dragon(0, 1, "water", 100, 100)

print("Step 1: claw passes")
assert 1 == claw(test_player, dragon, False, False)
print("Step 2: claw dodge")
assert 0 == claw(test_player, dragon, True, False)
print("Step 3: claw block")
assert -1 == claw(test_player, dragon, False, True)
print("Step 4: breath passes")
assert 1 == breath(test_player, dragon, False, False)
print("Step 5: breath dodge")
assert 0 == breath(test_player, dragon, True, False)
print("Step 6: breath block")
assert -1 == breath(test_player, dragon, False, True)
print("Step 7: tail passes")
assert 1 == tail(test_player, dragon, False, False)
print("Step 8: tail dodge")
assert 0 == tail(test_player, dragon, True, False)
print("Step 9: tail block")
assert -1 == tail(test_player, dragon, False, True)
print("UT10_dragon_combat: PASSED")
