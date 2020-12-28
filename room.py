"""
Room class for the TBG
"""


class Room:

    def __init__(self, x, y, player, dragons, hazards):
        """
        creates the room
        """
        self.room = [[0]*x for i in range(y)]
        self.room[player.player_x][player.player_y] = 1
        for hazard in hazards.hazards:
            h_x, h_y = hazard.x, hazard.y
            self.room[h_x][h_y] = hazard.tile
        for dragon in dragons.dragons:
            d_x, d_y = dragon.drag_x, dragon.drag_y
            self.room[d_x][d_y] = dragon.species

    def update_room(self, player, hazards, dragons):
        """
        This will updaqte the room whenever we add or remove an entity we should call this function
        """
        self.room = [[0]*len(self.room[0]) for i in range(len(self.room))]
        for hazard in hazards.hazards:
            h_x, h_y = hazard.x, hazard.y
            self.room[h_x][h_y] = hazard.tile
        for dragon in dragons.dragons:
            d_x, d_y = dragon.drag_x, dragon.drag_y
            self.room[d_x][d_y] = dragon.species
        self.room[player.player_x][player.player_y] = 1

    def print_room(self):
        """
        This prints the room for the user, this isnt like other prints this is for actual game
        """
        dungeon_room = ""
        for x in range(len(self.room)):
            dungeon_line = ""
            for y in range(len(self.room[x])):
                if self.room[x][y] == 1:
                    dungeon_line += "[X]"

                elif self.room[x][y] == "e":
                    dungeon_line += "[E]"
                elif self.room[x][y] == "w":
                    dungeon_line += "[W]"
                elif self.room[x][y] == "f":
                    dungeon_line += "[F]"

                elif self.room[x][y] == "fire":
                    dungeon_line += "[D]"
                elif self.room[x][y] == "earth":
                    dungeon_line += "[D]"
                elif self.room[x][y] == "water":
                    dungeon_line += "[D]"

                else:
                    dungeon_line += "[ ]"
            dungeon_line += "\n"
            dungeon_room += dungeon_line
        print(dungeon_room)

    def player_movement(self, direction, player):
        """
        Player uses the cardinal directions to move on the map 
        """
        if direction == "north" and player.player_x != 0:
            if self.room[player.player_x-1][player.player_y] == 0:
                player.player_x = player.player_x - 1
            else:
                print("object is in your path")

        elif direction == "south" and player.player_x != len(self.room)-1:
            if self.room[player.player_x+1][player.player_y] == 0:
                player.player_x = player.player_x + 1
            else:
                print("object is in your path")

        elif direction == "east" and player.player_y != len(self.room[0])-1:
            if self.room[player.player_x][player.player_y+1] == 0:
                player.player_y = player.player_y + 1
            else:
                print("object is in your path")

        elif direction == "west" and player.player_y != 0:
            if self.room[player.player_x][player.player_y-1] == 0:
                player.player_y = player.player_y - 1
            else:
                print("object is in your path")

        else:
            print("invalid input please try again")

    def dragon_movement(self, dragon, player):
        """
        Dragons will auto move towards the player
        can go over the hazard tiles
        """
        dif_x = dragon.drag_x - player.player_x
        dif_y = dragon.drag_y - player.player_y
        if dif_x < 0 and self.room[dragon.drag_x+1][dragon.drag_y] != 1:
            dragon.drag_x = dragon.drag_x + 1
        elif dif_x > 0 and self.room[dragon.drag_x-1][dragon.drag_y] != 1:
            dragon.drag_x = dragon.drag_x - 1
        if dif_y < 0 and self.room[dragon.drag_x][dragon.drag_y+1] != 1:
            dragon.drag_y = dragon.drag_y + 1
        elif dif_y > 0 and self.room[dragon.drag_x][dragon.drag_y-1] != 1:
            dragon.drag_y = dragon.drag_y - 1
