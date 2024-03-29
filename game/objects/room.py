"""
Room class for the TBG
"""


class Room:

    def __init__(self, x, y, goals=None, player=None, dragons=None, hazards=None):
        """
        creates the room
        args:
            x - how wide the map is - int
            y - how tall the map is - int
            goals - the goals for when the room is cleared - array of goal object
            player - the player object
            dragons - all the dragons - array of dragon objects
            hazards - all the hazards - array of hazard objects
        """
        self.room = [[0]*y for i in range(x)]
        self.goals = goals
        if player is not None:
            self.room[player.get_player_x()][player.get_player_y()] = 1

        if hazards is not None:
            for hazard in hazards.hazards:
                h_x, h_y = hazard.get_hazard_x(), hazard.get_hazard_y()
                self.room[h_x][h_y] = hazard.get_hazard_type()

        if dragons is not None:
            for dragon in dragons.dragons:
                d_x, d_y = dragon.get_drag_x(), dragon.get_drag_y()
                self.room[d_x][d_y] = dragon.get_drag_species()

    def update_room(self, player=None, dragons=None, hazards=None):
        """
        This will updaqte the room whenever we add or remove an entity we should call this function
        args:
            player - the player in the room
            dragons - the dragons -  list of dragon objects
            hazards - the hazard - list of hazard objects

        """
        self.room = [[0]*len(self.room[0]) for i in range(len(self.room))]
        if player is not None:
            self.room[player.get_player_x()][player.get_player_y()] = 1

        if hazards is not None:
            for hazard in hazards.hazards:
                h_x, h_y = hazard.get_hazard_x(), hazard.get_hazard_y()
                self.room[h_x][h_y] = hazard.get_hazard_type()

        if dragons is not None:
            for dragon in dragons.dragons:
                d_x, d_y = dragon.get_drag_x(), dragon.get_drag_y()
                self.room[d_x][d_y] = dragon.get_drag_species()

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
        """
        print the cleared room afetr all enemies are dead
        args:
            player - player object
        """
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
                elif self.room[x][y] == "d":
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
        args
            direcrtion - the direction the player is moving
            player - the player object
        returns
            1 - if succesful
            0 - if fails
        """
        VALID_TILES = ["g","d"]
        if direction == "north" and player.get_player_x() != 0:
            if self.room[player.get_player_x()-1][player.get_player_y()] == 0:
                player.set_player_x(player.get_player_x() - 1)
                return 1
            elif self.room[player.get_player_x()-1][player.get_player_y()] in VALID_TILES:
                player.set_player_x(player.get_player_x() - 1)
                return 1

        elif direction == "south" and player.get_player_x() != len(self.room)-1:
            if self.room[player.get_player_x()+1][player.get_player_y()] == 0:
                player.set_player_x(player.get_player_x() + 1)
                return 1
            elif self.room[player.get_player_x()+1][player.get_player_y()] in VALID_TILES:
                player.set_player_x(player.get_player_x() + 1)
                return 1

        elif direction == "east" and player.get_player_y() != len(self.room[0])-1:
            if self.room[player.get_player_x()][player.get_player_y()+1] == 0:
                player.set_player_y(player.get_player_y() + 1)
                return 1
            elif self.room[player.get_player_x()][player.get_player_y()+1] in VALID_TILES:
                player.set_player_y(player.get_player_y() + 1)
                return 1

        elif direction == "west" and player.get_player_y() != 0:
            if self.room[player.get_player_x()][player.get_player_y()-1] == 0:
                player.set_player_y(player.get_player_y() - 1)
                return 1
            if self.room[player.get_player_x()][player.get_player_y()-1] in VALID_TILES:
                player.set_player_y(player.get_player_y() - 1)
                return 1

        return 0

    def dragon_movement(self, dragon, player):
        """
        Dragons will auto move towards the player can go over the hazard tiles
        args
            dragon - dragon moving
            player - player getting moved to
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

    def is_clear(self):
        """
        check if the room is clear
        """
        for line in self.room:
            for tile in line:
                if tile not in [0, 1, "g", "f", "e", "w","d"]:
                    return 0
        return 1

    def on_goal(self, player):
        """
        check if the player is on goal tile
        args
            player - player in the game
        returns
            0 - if player dies
            1 - if dragon dies
        """
        if self.is_clear():
            for goal in self.goals.goals:
                outcome = player.get_player_x() == goal.get_goal_x(
                ) and player.get_player_y() == goal.get_goal_y()
                print(outcome)
                if outcome:
                    return True
        return False
