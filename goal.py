class Goal:
    def __init__(self, x, y, goal_type):
        """
        Creates a single hazard
        """
        self.x = x
        self.y = y
        if goal_type == "goal":
            self.tile = "g"
        elif goal_type == "door":
            self.tile = "d"

    def get_goal_type(self):
        return self.tile

    def get_goal_x(self):
        return self.x

    def get_goal_y(self):
        return self.y


class Goals:
    def __init__(self, goals):
        self.goals = goals

    def clear_goal(self, goal):
        """
        If the hazard exists we remove it
        """
        for cur_goal in (self.goals):
            if goal in self.goals:
                self.hazards.remove(cur_goal)

    def add_goal(self, hazard):
        """
        Add a new hazard to the room
        """
        self.hazards.append(hazard)
