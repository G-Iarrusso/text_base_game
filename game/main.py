import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from game.builder.builder import Builder, build_game

first_room = Builder("first_room")
build_game(first_room)