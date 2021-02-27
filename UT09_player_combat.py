from dragon import Dragon
from player import Player
from combat import heavy_attack, quick_attack, dodge, block
print("UT9_player_combat: STARTING")

print("Step 0: Starting room is printed")
test_player = Player(5, 5, 1, 1)
dragon = Dragon(0, 1, "water", 100, 100)

print("Step 1: Quick attack passes")
assert quick_attack(test_player, dragon, 10)

print("Step 2: quick attack fails")
assert not quick_attack(test_player, dragon, 100)

print("Step 3: Heavy attack passes")
assert heavy_attack(test_player, dragon, 10)

print("Step 4: Heavy attack fails")
assert not heavy_attack(test_player, dragon, 100)

print("Step 5: dodge passes")
assert dodge(test_player, 10)

print("Step 6: dodge fails")
assert not dodge(test_player, 100)

print("Step 7: block passes")
assert block(test_player, 10)

print("Step 8: block fails")
assert not block(test_player, 100)

print("UT9_player_combat: PASSED")
