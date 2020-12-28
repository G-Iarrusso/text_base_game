class Player:
    def __init__(self, starting_health, current_health, player_x, player_y):
        """
        single player
        """
        self.starting_health = starting_health
        self.current_health = current_health
        self.player_x = player_x
        self.player_y = player_y

    def take_damage(self, damage):
        """
        adjusts health based on damage taken
        """
        if self.current_health - damage <= 0:
            print("You've died")
        else:
            self.current_health = self.current_health - damage

    def heal_all(self):
        """
        heals the player to their startign health
        """
        self.current_health = self.starting_health

    def heal(self, amount):
        """
        heals player by the given amount
        """
        self.current_health = self.current_health + amount

    def gain_armour(self, armour):
        """
        gaining armor adds an amount to the players starting and current health
        """
        self.starting_health = self.starting_health + armour
        self.current_health = self.current_health + armour

    def print_player(self):
        """
        prints the players info
        """
        print("Starting health: " + str(self.starting_health) + " Current Health: " + str(self.current_health))
        print("X: " + str(self.player_x + 1) + " Y: " + str(self.player_y + 1))
