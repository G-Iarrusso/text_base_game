class Goal:
    def __init__(self, x, y, goal_type):
        """
        Creates a single hazard
        args:
            x - the x value - int
            y - the y value - int
            goal_type - the type of goal - string
        """
        self.x = x
        self.y = y
        if goal_type == "goal":
            self.tile = "g"
        elif goal_type == "door":
            self.tile = "d"

    def get_goal_type(self):
        """
        get the goal type
        returns:
            the type of tile
        """
        return self.tile

    def get_goal_x(self):
        """
        get the goal x value
        returns:
            the x value of tile
        """
        return self.x

    def get_goal_y(self):
        """
        get the goal y value
        returns:
            the y value of tile
        """
        return self.y


class Goals:
    def __init__(self, goals):
        """
        create the array of goals
        args:
            goals - array of goal objects - objects array
        """
        self.goals = goals

    def clear_goal(self, goal):
        """
        If the hazard exists we remove it
        args:
            goal - the goal to be removed - goal object
        """
        for cur_goal in (self.goals):
            if goal in self.goals:
                self.hazards.remove(cur_goal)

    def add_goal(self, hazard):
        """
        Add a new hazard to the room
        args:
            goal - the goal to be added - goal object
        """
        self.hazards.append(hazard)
