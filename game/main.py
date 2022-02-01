import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from game.builder.builder import Builder, build_game
from game.input.handler import get_input

first_room = Builder("first_room")
build_game(first_room)
print(first_room.player.is_dead())
print(first_room.room.on_goal(first_room.player))

while(not(first_room.player.is_dead() and first_room.room.on_goal(first_room.player))):
    parsed_input = get_input(first_room)
    if parsed_input == -1:
        break