import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from game.objects.room import Room
from game.objects.goal import Goal, Goals
from game.objects.player import Player
from game.objects.debugging import print_dragon, print_hazards, print_hazard, print_goal, print_player
from game.objects.dragon import Dragon, Dragons
from game.objects.hazards import Hazard, Hazards
from game.builder.room_data import (_get_room_info, _get_dragon_names, _get_dragon_info_by_name, 
_get_hazard_names,_get_hazard_info_by_name, _get_goal_names,_get_goal_info_by_name, _get_player_info)


class Builder:
    def __init__(self, room_name):
        """
        builds the stage
        args:
            room_name - name coresponding to room dictionary - string
        """
        self.room_name = room_name
        self.x,self.y = _get_room_info(self.room_name)
        names = _get_dragon_names(self.room_name)
        self.dragons = []
        for name in names:
            dragon = _get_dragon_info_by_name(self.room_name, name)
            self.dragons.append(dragon)

        names = _get_hazard_names(self.room_name)
        self.hazards = []
        for name in names:
            hazard = _get_hazard_info_by_name(self.room_name, name)
            self.hazards.append(hazard)

        names = _get_goal_names(self.room_name)
        self.goals = []
        for name in names:
            goal = _get_goal_info_by_name(self.room_name, name)
            self.goals.append(goal)
        
        self.player = _get_player_info(self.room_name)

    def build_dragons(self, dragons):
        drag_object=[]
        for dragon in dragons:
            drag = Dragon(dragon[0], dragon[1], dragon[2], dragon[3], dragon[4])
            drag_object.append(drag)
        return Dragons(drag_object)
    
    def build_hazards(self, hazards):
        hazard_object=[]
        for hazard in hazards:
            haz = Hazard(hazard[0], hazard[1], hazard[2])
            hazard_object.append(haz)
        return Hazards(hazard_object)
    
    def build_goals(self, goals):
        goals_object= []
        for goal in goals:
            g = Goal(goal[0], goal[1], goal[2])
            goals_object.append(g)
        return Goals(goals_object)

    def build_player(self, player):
        return Player(player[2], player[3], player[0], player[1])
    
            
def build_game(builder):
    builder.dragons = builder.build_dragons(builder.dragons)
    builder.hazards = builder.build_hazards(builder.hazards)
    builder.goals = builder.build_goals(builder.goals)
    builder.player = builder.build_player(builder.player)
    builder.room = Room(builder.x, builder.y, builder.goals, builder.player, builder.dragons, builder.hazards)
    builder.room.print_room()
