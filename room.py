"""
Room class for the TBG
"""


class Room:

    def __init__(self, x, y, player, dragons, hazards):
        self.room = [[0]*x for i in range(y)]
        self.room[player.player_x][player.player_y] = 1
        for hazard in hazards.hazards:
            h_x, h_y = hazard.x, hazard.y
            self.room[h_x][h_y] = hazard.tile
        for dragon in dragons.dragons:
            d_x,d_y = dragon.drag_x, dragon.drag_y
            self.room[d_x][d_y] = dragon.species
        self.location_x = player.player_x
        self.location_y = player.player_y

    def update_room(self, hazards):
        self.room = [[0]*len(self.room) for i in range(len(self.room[0]))]
        for hazard in hazards.hazards:
            h_x, h_y = hazard.x, hazard.y
            self.room[h_x][h_y] = hazard.tile
        self.room[self.location_x][self.location_y] = 1

    def print_room(self):
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
                elif self.room[x][y] == "fire":
                    dungeon_line += "[FD]"
                elif self.room[x][y] == "earth":
                    dungeon_line += "[ED]"
                elif self.room[x][y] == "water":
                    dungeon_line += "[WD]"
                elif self.room[x][y] == "f":
                    dungeon_line += "[F]"
                else:
                    dungeon_line += "[]"
            dungeon_line += "\n"
            dungeon_room += dungeon_line
        print(dungeon_room)

    def player_movement(self, direction, player):
        if direction == "north" and self.location_x != 0:
            if self.room[self.location_x-1][self.location_y] == 0:
                self.room[self.location_x][self.location_y] = 0
                new_x = self.location_x - 1
                player.player_x = new_x
                self.location_x = new_x
                self.room[self.location_x][self.location_y] = 1
            else:
                print("object is in your path")

        elif direction == "south" and self.location_x != len(self.room)-1:
            if self.room[self.location_x+1][self.location_y] == 0:
                self.room[self.location_x][self.location_y] = 0
                new_x = self.location_x + 1
                player.player_x = new_x
                self.location_x = new_x
                self.room[self.location_x][self.location_y] = 1
            else:
                print("object is in your path")

        elif direction == "east" and self.location_y != len(self.room[0])-1:
            if self.room[self.location_x+1][self.location_y+1] == 0:
                self.room[self.location_x][self.location_y] = 0
                new_y = self.location_y + 1
                player.player_y = new_y
                self.location_y = new_y
                self.room[self.location_x][self.location_y] = 1
            else:
                print("object is in your path")

        elif direction == "west" and self.location_y != 0:
            if self.room[self.location_x+1][self.location_y-1] == 0:
                self.room[self.location_x][self.location_y] = 0
                new_y = self.location_y - 1
                player.player_y = new_y
                self.location_y = new_y
                self.room[self.location_x][self.location_y] = 1
            else:
                print("object is in your path")

        else:
            print("invalid input please try again")
        self.print_room()
