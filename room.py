"""
Room class for the TBG
"""


class Room:

    def __init__(self, x, y, goals=None, player=None, dragons=None, hazards=None):
        """
        creates the room
        """
        self.room = [[0]*y for i in range(x)]
        self.goals = goals
        if player is not None:
            self.room[player.player_x][player.player_y] = 1

        if hazards is not None:
            for hazard in hazards.hazards:
                h_x, h_y = hazard.x, hazard.y
                self.room[h_x][h_y] = hazard.tile

        if dragons is not None:
            for dragon in dragons.dragons:
                d_x, d_y = dragon.drag_x, dragon.drag_y
                self.room[d_x][d_y] = dragon.species

    def update_room(self, player=None, dragons=None, hazards=None):
        """
        This will updaqte the room whenever we add or remove an entity we should call this function
        """
        self.room = [[0]*len(self.room[0]) for i in range(len(self.room))]
        if player is not None:
            self.room[player.player_x][player.player_y] = 1

        if hazards is not None:
            for hazard in hazards.hazards:
                h_x, h_y = hazard.x, hazard.y
                self.room[h_x][h_y] = hazard.tile

        if dragons is not None:
            for dragon in dragons.dragons:
                d_x, d_y = dragon.drag_x, dragon.drag_y
                self.room[d_x][d_y] = dragon.species

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
        return dungeon_room

    def print_cleared_room(self, player):

        self.update_room(player=player)
        for goal in self.goals.goals:
            g_x, g_y = goal.get_goal_x(), goal.get_goal_y()
            self.room[g_x][g_y] = goal.get_goal_type()

        dungeon_room = ""
        for x in range(len(self.room)):
            dungeon_line = ""
            for y in range(len(self.room[x])):
                if self.room[x][y] == 1:
                    dungeon_line += "[X]"
                elif self.room[x][y] == "g":
                    dungeon_line += "[G]"
                elif self.room[x][y] == "s":
                    dungeon_line += "[S]"
                else:
                    dungeon_line += "[ ]"
            dungeon_line += "\n"
            dungeon_room += dungeon_line
        print(dungeon_room)
        return dungeon_room

    def player_movement(self, direction, player):
        """
        Player uses the cardinal directions to move on the map
        """
        if direction == "north" and player.get_player_x() != 0:
            if self.room[player.get_player_x()-1][player.get_player_y()] == 0:
                player.set_player_x(player.get_player_x() - 1)
                return 1
            elif self.room[player.get_player_x()-1][player.get_player_y()] == "g":
                player.set_player_x(player.get_player_x() - 1)
                return 1

        elif direction == "south" and player.get_player_x() != len(self.room)-1:
            if self.room[player.get_player_x()+1][player.get_player_y()] == 0:
                player.set_player_x(player.get_player_x() + 1)
                return 1
            elif self.room[player.get_player_x()+1][player.get_player_y()] == "g":
                player.set_player_x(player.get_player_x() + 1)
                return 1

        elif direction == "east" and player.get_player_y() != len(self.room[0])-1:
            if self.room[player.get_player_x()][player.get_player_y()+1] == 0:
                player.set_player_y(player.get_player_y() + 1)
                return 1
            elif self.room[player.get_player_x()][player.get_player_y()+1] == "g":
                player.set_player_y(player.get_player_y() + 1)
                return 1

        elif direction == "west" and player.get_player_y() != 0:
            if self.room[player.get_player_x()][player.get_player_y()-1] == 0:
                player.set_player_y(player.get_player_y() - 1)
                return 1
            if self.room[player.get_player_x()][player.get_player_y()-1] == "g":
                player.set_player_y(player.get_player_y() - 1)
                return 1

        return 0

    def dragon_movement(self, dragon, player):
        """
        Dragons will auto move towards the player
        can go over the hazard tiles
        """
        dif_x = dragon.get_drag_x() - player.get_player_x()
        dif_y = dragon.get_drag_y() - player.get_player_y()
        if dif_x < 0 and self.room[dragon.get_drag_x() + 1][dragon.get_drag_y()] != 1:
            dragon.set_drag_x(dragon.get_drag_x() + 1)
        elif dif_x > 0 and self.room[dragon.get_drag_x() - 1][dragon.get_drag_y()] != 1:
            dragon.set_drag_x(dragon.get_drag_x() - 1)
        if dif_y < 0 and self.room[dragon.get_drag_x()][dragon.get_drag_y()+1] != 1:
            dragon.set_drag_y(dragon.get_drag_y() + 1)
        elif dif_y > 0 and self.room[dragon.get_drag_x()][dragon.get_drag_y() - 1] != 1:
            dragon.set_drag_y(dragon.get_drag_y() - 1)

    def is_clear(self, player):
        for line in self.room:
            for tile in line:
                if tile not in [0, 1, "g"]:
                    print(tile)
                    return 0
        return 1

    def on_goal(self, player):
        if self.is_clear(player):
            for goal in self.goals.goals:
                outcome = player.get_player_x() == goal.get_goal_x(
                ) and player.get_player_y() == goal.get_goal_y()
                print(outcome)
                if outcome:
                    return 1
        return 0
