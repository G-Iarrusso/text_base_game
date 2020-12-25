"""
Room class for the TBG
"""


class Room:

    def __init__(self, x, y, start_x, start_y):
        self.room = [[0]*x for i in range(y)]
        self.room[start_x][start_y] = 1
        self.location_x = start_x
        self.location_y = start_y

    def print_room(self):
        dungeon_room = ""
        for x in range(len(self.room)):
            dungeon_line = ""
            for y in range(len(self.room[x])):
                if self.room[x][y] == 1:
                    dungeon_line += "[X]"
                else:
                    dungeon_line += "[]"
            dungeon_line += "\n"
            dungeon_room += dungeon_line
        print(dungeon_room)

    def movement(self, direction):
        if direction == "north" and self.location_x != 0:
            self.room[self.location_x][self.location_y] = 0
            new_x = self.location_x - 1
            self.location_x = new_x
            self.room[self.location_x][self.location_y] = 1

        elif direction == "south" and self.location_x != len(self.room)-1:
            self.room[self.location_x][self.location_y] = 0
            new_x = self.location_x + 1
            self.location_x = new_x
            self.room[self.location_x][self.location_y] = 1

        elif direction == "east" and self.location_y != len(self.room[0])-1:
            print(len(self.room[0]))
            self.room[self.location_x][self.location_y] = 0
            new_y = self.location_y + 1
            self.location_y = new_y
            self.room[self.location_x][self.location_y] = 1

        elif direction == "west" and self.location_y != 0:
            self.room[self.location_x][self.location_y] = 0
            new_y = self.location_y - 1
            self.location_y = new_y
            self.room[self.location_x][self.location_y] = 1

        else:
            print("invalid input please try again")
        self.print_room()
